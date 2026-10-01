#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

RULE_STATUS = {
    "RULE_LOCATED_UNTESTED",
    "CONSTITUTIONALLY_SUPPORTED",
    "CONSTITUTIONALITY_UNRESOLVED",
    "FACIALLY_SUSPECT",
    "AS_APPLIED_SUSPECT",
    "LIKELY_INVALID",
    "UPHELD_BINDING",
    "NONRESTRICTION_CONTEXT",
}
SOURCE_TYPES = {
    "STATUTE","REGULATION","ORDINANCE","AGENCY_POLICY","FACILITY_RULE",
    "CONTRACT_TERMS","HANDBOOK","PUBLIC_GUIDANCE","POSTED_SIGN","CASE_AUTHORITY"
}
PRIORITY = {"HIGH","MEDIUM","LOW"}

def fail(msg: str) -> None:
    raise ValueError(msg)

def main() -> int:
    root = Path(".").resolve()
    facilities = {}
    for p in (root/"registry/data/facilities").glob("*.json"):
        d=json.loads(p.read_text(encoding="utf-8"))
        facilities[d["slug"]]=d["facility_id"]

    files=sorted((root/"registry/data/restrictions").glob("*.json"))
    if not files:
        fail("no restriction corpus files found")

    total=0
    for p in files:
        d=json.loads(p.read_text(encoding="utf-8"))
        slug=d.get("slug")
        if slug not in facilities:
            fail(f"{p}: unknown facility slug {slug!r}")
        if d.get("facility_id") != facilities[slug]:
            fail(f"{p}: facility_id mismatch")
        if d.get("schema_version") != 1:
            fail(f"{p}: unsupported schema_version")
        ids=set()
        for r in d.get("rules",[]):
            rid=r.get("rule_id")
            if rid in ids:
                fail(f"{p}: duplicate rule_id {rid}")
            ids.add(rid)
            for key in ("title","source_type","source","applies_to","activities","project_status","summary"):
                if key not in r:
                    fail(f"{p}:{rid}: missing {key}")
            if r["source_type"] not in SOURCE_TYPES:
                fail(f"{p}:{rid}: invalid source_type {r['source_type']}")
            if r["project_status"] not in RULE_STATUS:
                fail(f"{p}:{rid}: invalid project_status {r['project_status']}")
            if r["project_status"] in {"CONSTITUTIONALLY_SUPPORTED","FACIALLY_SUSPECT","AS_APPLIED_SUSPECT","LIKELY_INVALID","UPHELD_BINDING"} and not r.get("authority_ids"):
                fail(f"{p}:{rid}: strong constitutional conclusion requires authority_ids")
            total += 1
        for t in d.get("cpra_targets",[]):
            if t.get("priority") not in PRIORITY:
                fail(f"{p}: invalid CPRA target priority")
            if not t.get("target") or not t.get("why"):
                fail(f"{p}: incomplete CPRA target")
        print(f"{slug}: {len(d.get('rules',[]))} rules, {len(d.get('cpra_targets',[]))} CPRA targets")

    print(f"Restriction corpus validated: {len(files)} facilities, {total} public-source rule records")
    return 0

if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except ValueError as exc:
        print(f"Restriction corpus validation error: {exc}", file=sys.stderr)
        raise SystemExit(2)
