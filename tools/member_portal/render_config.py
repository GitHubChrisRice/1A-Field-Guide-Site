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
SESSION_DECL_RE = re.compile(r"(const SESSION_KEY='coalition-membership-session-v1';)")


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


SESSION_BRIDGE = r"""
const AUTH_CHANNEL_NAME='coalition-membership-auth-v1';
let authChannel=null;
try{authChannel=new BroadcastChannel(AUTH_CHANNEL_NAME)}catch{}
function storageRead(kind){try{return window[kind].getItem(SESSION_KEY)}catch{return null}}
function storageWrite(kind,value){try{window[kind].setItem(SESSION_KEY,value)}catch{}}
function storageRemove(kind){try{window[kind].removeItem(SESSION_KEY)}catch{}}
function validSession(s){return !!(s?.access_token&&s?.refresh_token)}
function persistSession(s){if(!validSession(s))return null;const raw=JSON.stringify(s);storageWrite('localStorage',raw);storageWrite('sessionStorage',raw);return s}
function loadSharedSession(){try{const s=JSON.parse(storageRead('localStorage')||storageRead('sessionStorage')||'null');return validSession(s)?persistSession(s):null}catch{return null}}
function requestPeerSession(timeout=450){
  const local=loadSharedSession();if(local)return Promise.resolve(local);
  if(!authChannel)return Promise.resolve(null);
  return new Promise(resolve=>{
    let done=false;
    const finish=s=>{if(done)return;done=true;clearTimeout(timer);authChannel.removeEventListener('message',onMessage);resolve(s?persistSession(s):null)};
    const onMessage=e=>{if(e.data?.type==='session-response'&&validSession(e.data.session))finish(e.data.session)};
    const timer=setTimeout(()=>finish(null),timeout);
    authChannel.addEventListener('message',onMessage);
    try{authChannel.postMessage({type:'session-request'})}catch{finish(null)}
  })
}
if(authChannel){authChannel.addEventListener('message',e=>{if(e.data?.type!=='session-request')return;const s=loadSharedSession();if(s){try{authChannel.postMessage({type:'session-response',session:s})}catch{}}})}
""".strip()

FORUM_DIAGNOSTIC_HTML = r"""
<section id="auth-diagnostics" class="panel" aria-labelledby="auth-diagnostics-title">
  <div class="section-heading"><div>
    <div class="eyebrow">Temporary troubleshooting</div>
    <h2 id="auth-diagnostics-title">Sign-in diagnostics</h2>
    <p class="muted">This reports only yes/no/error states. It does not display your email, user ID, access token, refresh token, or any secret.</p>
  </div><button id="run-auth-diagnostics" class="secondary" type="button">Run diagnostics</button></div>
  <pre id="auth-diagnostics-output" style="white-space:pre-wrap;overflow-wrap:anywhere;margin:0" aria-live="polite">Diagnostics have not run yet.</pre>
</section>
""".strip()

FORUM_DIAGNOSTIC_JS = r"""
function storageProbe(kind){
  try{
    const store=window[kind],probe='__coalition_auth_probe__';
    store.setItem(probe,'1');const roundTrip=store.getItem(probe)==='1';store.removeItem(probe);
    const raw=store.getItem(SESSION_KEY);
    let shaped=false;
    if(raw){try{shaped=validSession(JSON.parse(raw))}catch{}}
    return{available:true,roundTrip,sessionPresent:!!raw,sessionShaped:shaped,error:null};
  }catch(e){return{available:false,roundTrip:false,sessionPresent:false,sessionShaped:false,error:e?.name||'Error'}}
}
async function peerProbe(timeout=700){
  if(!authChannel)return{available:false,responded:false};
  const hadLocal=!!loadSharedSession();
  if(hadLocal)return{available:true,responded:false,skipped:'local session already present'};
  const peer=await requestPeerSession(timeout);
  return{available:true,responded:!!peer};
}
async function collectAuthDiagnostics(){
  const localBefore=storageProbe('localStorage'),tabBefore=storageProbe('sessionStorage');
  const peer=await peerProbe();
  const localAfter=storageProbe('localStorage'),tabAfter=storageProbe('sessionStorage');
  const s=loadSharedSession();
  let auth='not tested: no session',membership='not tested: no authenticated session';
  if(s){
    try{
      await req('/auth/v1/user',{token:s.access_token});auth='accepted';
      try{
        const rows=await req('/rest/v1/rpc/coalition_self_membership_status',{method:'POST',token:s.access_token,body:{}}),m=rows?.[0],roles=m?.role_codes||[];
        membership=(m?.membership_status==='approved'&&roles.includes('member'))?'approved member':'RPC succeeded, active Member gate not satisfied';
      }catch(e){membership='RPC failed'+(e?.status?' (HTTP '+e.status+')':'')}
    }catch(e){auth='rejected'+(e?.status?' (HTTP '+e.status+')':'')}
  }
  return{
    diagnosticVersion:'auth-diag-v1',
    secureContext:window.isSecureContext,
    broadcastChannelSupported:'BroadcastChannel' in window,
    localStorageBefore:localBefore,
    sessionStorageBefore:tabBefore,
    peerHandoff:peer,
    localStorageAfter:localAfter,
    sessionStorageAfter:tabAfter,
    sharedSessionAfterProbe:!!s,
    supabaseAuth:auth,
    membershipCheck:membership
  };
}
async function renderAuthDiagnostics(){
  const out=document.getElementById('auth-diagnostics-output');if(!out)return;
  out.textContent='Running diagnostics…';
  try{out.textContent=JSON.stringify(await collectAuthDiagnostics(),null,2)}catch(e){out.textContent='Diagnostics failed: '+(e?.name||'Error')}
}
const diagnosticsButton=document.getElementById('run-auth-diagnostics');
if(diagnosticsButton)diagnosticsButton.addEventListener('click',renderAuthDiagnostics);
""".strip()


def normalize_member_session(rendered: str) -> str:
    """Provide resilient same-origin member session sharing.

    Sessions persist to localStorage when available, retain sessionStorage as a
    compatibility fallback, and can be handed directly between open same-origin
    tabs through BroadcastChannel when persistent storage is blocked.
    """
    rendered, count = SESSION_DECL_RE.subn(r"\1\n" + SESSION_BRIDGE, rendered, count=1)
    if count != 1:
        fail("member page session declaration not found")

    replacements = {
        "function save(s){if(!s?.access_token||!s?.refresh_token)throw new Error('Incomplete session');sessionStorage.setItem(SESSION_KEY,JSON.stringify(s))}":
            "function save(s){if(!validSession(s))throw new Error('Incomplete session');persistSession(s)}",
        "function save(s){if(!s?.access_token||!s?.refresh_token)throw new Error('Incomplete session');const raw=JSON.stringify(s);localStorage.setItem(SESSION_KEY,raw);sessionStorage.setItem(SESSION_KEY,raw)}":
            "function save(s){if(!validSession(s))throw new Error('Incomplete session');persistSession(s)}",
        "function clear(){sessionStorage.removeItem(SESSION_KEY)}":
            "function clear(){storageRemove('localStorage');storageRemove('sessionStorage')}",
        "function clear(){localStorage.removeItem(SESSION_KEY);sessionStorage.removeItem(SESSION_KEY)}":
            "function clear(){storageRemove('localStorage');storageRemove('sessionStorage')}",
        "function clearSession(){sessionStorage.removeItem(SESSION_KEY)}":
            "function clearSession(){storageRemove('localStorage');storageRemove('sessionStorage')}",
        "function clearSession(){localStorage.removeItem(SESSION_KEY);sessionStorage.removeItem(SESSION_KEY)}":
            "function clearSession(){storageRemove('localStorage');storageRemove('sessionStorage')}",
        "function load(){try{const s=JSON.parse(sessionStorage.getItem(SESSION_KEY)||'null');return s?.access_token&&s?.refresh_token?s:null}catch{return null}}":
            "function load(){return loadSharedSession()}",
        "function load(){try{const raw=localStorage.getItem(SESSION_KEY)||sessionStorage.getItem(SESSION_KEY);const s=JSON.parse(raw||'null');if(s?.access_token&&s?.refresh_token){const normalized=JSON.stringify(s);localStorage.setItem(SESSION_KEY,normalized);sessionStorage.setItem(SESSION_KEY,normalized);return s}return null}catch{return null}}":
            "function load(){return loadSharedSession()}",
        "function loadSession(){try{const s=JSON.parse(sessionStorage.getItem(SESSION_KEY)||'null');return s?.access_token&&s?.refresh_token?s:null}catch{return null}}":
            "function loadSession(){return loadSharedSession()}",
        "function loadSession(){try{const raw=localStorage.getItem(SESSION_KEY)||sessionStorage.getItem(SESSION_KEY);const s=JSON.parse(raw||'null');if(s?.access_token&&s?.refresh_token){const normalized=JSON.stringify(s);localStorage.setItem(SESSION_KEY,normalized);sessionStorage.setItem(SESSION_KEY,normalized);return s}return null}catch{return null}}":
            "function loadSession(){return loadSharedSession()}",
        "function saveSession(s){sessionStorage.setItem(SESSION_KEY,JSON.stringify(s))}":
            "function saveSession(s){if(!validSession(s))throw new Error('Incomplete session');persistSession(s)}",
        "function saveSession(s){if(!s?.access_token||!s?.refresh_token)throw new Error('Incomplete session');const raw=JSON.stringify(s);localStorage.setItem(SESSION_KEY,raw);sessionStorage.setItem(SESSION_KEY,raw)}":
            "function saveSession(s){if(!validSession(s))throw new Error('Incomplete session');persistSession(s)}",
    }
    for old, new in replacements.items():
        rendered = rendered.replace(old, new)

    rendered = rendered.replace("let s=load();if(!s)return null;", "let s=load();if(!s)s=await requestPeerSession();if(!s)return null;")
    rendered = rendered.replace("let s=loadSession();if(!s)return null;", "let s=loadSession();if(!s)s=await requestPeerSession();if(!s)return null;")
    return rendered


def add_forum_auth_diagnostics(rendered: str) -> str:
    gate_end = '<div id="workspace" hidden>'
    if gate_end not in rendered:
        fail("member-forum-maps.html: workspace marker not found for diagnostics")
    rendered = rendered.replace(gate_end, FORUM_DIAGNOSTIC_HTML + "\n" + gate_end, 1)
    init_marker = "await init();</script>"
    if init_marker not in rendered:
        fail("member-forum-maps.html: init marker not found for diagnostics")
    rendered = rendered.replace(init_marker, FORUM_DIAGNOSTIC_JS + "\nawait init();await renderAuthDiagnostics();</script>", 1)
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
        if path.name == "member-forum-maps.html":
            rendered = add_forum_auth_diagnostics(rendered)
            if "auth-diag-v1" not in rendered or "auth-diagnostics-output" not in rendered:
                fail(f"{path}: privacy-safe authentication diagnostics were not injected")
        if "requestPeerSession" not in rendered or "BroadcastChannel" not in rendered:
            fail(f"{path}: member page is missing resilient cross-tab session handoff")
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
