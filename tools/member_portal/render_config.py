#!/usr/bin/env python3
"""Validate templated member pages and render deploy-only Supabase configuration."""

from __future__ import annotations

import argparse
import base64
import hashlib
import os
from pathlib import Path
import re

URL_PLACEHOLDER = "__COALITION_SUPABASE_URL__"
KEY_PLACEHOLDER = "__COALITION_SUPABASE_PUBLISHABLE_KEY__"
TARGETS = (
    "member-pilot.html",
    "member-community.html",
    "member-research.html",
    "member-research-submit.html",
    "member-research-import.html",
    "member-forum-maps.html",
)
SCRIPT_RE = re.compile(r'<script type="module">(?P<body>.*?)</script>', re.DOTALL)
SCRIPT_HASH_RE = re.compile(r"'sha256-[A-Za-z0-9+/=]+'");
SUPABASE_URL_RE = re.compile(r"https://[a-z0-9]+\.supabase\.co$")


def fail(message: str) -> None:
    raise SystemExit(message)


def target_paths(root: Path) -> list[Path]:
    paths = [root / name for name in TARGETS]
    missing = [str(path) for path in paths if not path.is_file()]
    if missing:
        fail("Missing member page(s): " + ", ".join(missing))
    return paths


def check_template(root: Path) -> None:
    for path in target_paths(root):
        text = path.read_text(encoding="utf-8")
        if text.count(URL_PLACEHOLDER) < 2:
            fail(f"{path}: expected Supabase URL placeholders in CSP and script")
        if text.count(KEY_PLACEHOLDER) != 1:
            fail(f"{path}: expected exactly one publishable-key placeholder")
        if re.search(r"https://[a-z0-9]+\.supabase\.co", text):
            fail(f"{path}: live Supabase project URL must not be committed")
        if re.search(r"sb_publishable__[A-Za-z0-9_-]+", text):
            fail(f"{path}: live Supabase publishable key must not be committed")
    print("Member portal source is safely templated.")


def normalize_member_session(rendered: str) -> str:
    """Upgrade legacy tab-only member-session helpers during deployment.

    Older member pages used sessionStorage, which made an authenticated portal
    look signed out when a member opened another member page in a new tab.
    Keep sessionStorage as a compatibility fallback while persisting the same
    Supabase session to same-origin localStorage so all member pages agree.
    """
    replacements = {
        "function save(s){if(!s?.access_token||!s?.refresh_token)throw new Error('Incomplete session');sessionStorage.setItem(SESSION_KEY,JSON.stringify(s))}":
            "function save(s){if(!s?.access_token||!s?.refresh_token)throw new Error('Incomplete session');const raw=JSON.stringify(s);localStorage.setItem(SESSION_KEY,raw);sessionStorage.setItem(SESSION_KEY,raw)}",
        "function clear(){sessionStorage.removeItem(SESSION_KEY)}":
            "function clear(){localStorage.removeItem(SESSION_KEY);sessionStorage.removeItem(SESSION_KEY)}",
        "function clearSession(){sessionStorage.removeItem(SESSION_KEY)}":
            "function clearSession(){localStorage.removeItem(SESSION_KEY);sessionStorage.removeItem(SESSION_KEY)}",
        "function load(){try{const s=JSON.parse(sessionStorage.getItem(SESSION_KEY)||'null');return s?.access_token&&s?.refresh_token?s:null}catch{return null}}":
            "function load(){try{const raw=localStorage.getItem(SESSION_KEY)||sessionStorage.getItem(SESSION_KEY);const s=JSON.parse(raw||'null');if(s?.access_token&&s?.refresh_token){const normalized=JSON.stringify(s);localStorage.setItem(SESSION_KEY,normalized);sessionStorage.setItem(SESSION_KEY,normalized);return s}return null}catch{return null}}",
        "function loadSession(){try{const s=JSON.parse(sessionStorage.getItem(SESSION_KEY)||'null');return s?.access_token&&s?.refresh_token?s:null}catch{return null}}":
            "function loadSession(){try{const raw=localStorage.getItem(SESSION_KEY)||sessionStorage.getItem(SESSION_KEY);const s=JSON.parse(raw||'null');if(s?.access_token&&s?.refresh_token){const normalized=JSON.stringify(s);localStorage.setItem(SESSION_KEY,normalized);sessionStorage.setItem(SESSION_KEY,normalized);return s}return null}catch{return null}}",
        "function saveSession(s){sessionStorage.setItem(SESSION_KEY,JSON.stringify(s))}":
            "function saveSession(s){if(!s?.access_token||!s?.refresh_token)throw new Error('Incomplete session');const raw=JSON.stringify(s);localStorage.setItem(SESSION_KEY,raw);sessionStorage.setItem(SESSION_KEY,raw)}",
    }
    for old, new in replacements.items():
        rendered = rendered.replace(old, new)
    return rendered


def render(root: Path) -> None:
    url = os.environ.get("COALITION_SUPABASE_URL", "").strip().rstrip("/")
    key = os.environ.get("COALITION_SUPABASE_PUBLISHABLE_KEY", "").strip()
    if not SUPABASE_URL_RE.fullmatch(url):
        fail("COALITION_SUPABASE_URL must be an https://<project>.supabase.co URL")
    if not key.startswith("sb_publishable__") or len(key) < 24:
        fail("COALITION_SUPABASE_PUBLISHABLE_KEY is missing or invalid")

    for path in target_paths(root):
        text = path.read_text(encoding="utf-8")
        if URL_PLACEHOLDER not in text or KEY_PLACEHOLDER not in text:
            fail(f"{path}: member backend placeholders are missing")
        rendered = text.replace(URL_PLACEHOLDER, url).replace(KEY_PLACEHOLDER, key)
        rendered = normalize_member_session(rendered)
        if "localStorage.getItem(SESSION_KEY)" not in rendered:
            fail(f"{path}: member page is not using the shared cross-tab session store")
        match = SCRIPT_RE.search(rendered)
        if not match:
            fail(f"{path}: inline module script not found")
        digest = base64.b64encode(hashlib.sha256(match.group("body").encode("utf-8")).digest()).decode("ascii")
        replacement = f"'sha256-{digest}'"
        rendered, count = SCRIPT_HASH_RE.subn(replacement, rendered, count=1)
        if count != 1:
            fail(f"{path}: CSP script hash declaration not found")
        if URL_PLACEHOLDER in rendered or KEY_PLACEHOLDER in rendered:
            fail(f"{path}: unresolved member backend placeholder after render")
        path.write_text(rendered, encoding="utf-8")
        print(f"Rendered {path} with deploy-only member backend configuration.")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=("check", "render"))
    parser.add_argument("root", type=Path)
    args = parser.parse_args()
    if args.mode == "check":
        check_template(args.root)
    else:
        render(args.root)


if __name__ == "__main__":
    main()
