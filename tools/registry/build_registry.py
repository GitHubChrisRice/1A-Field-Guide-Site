#!/usr/bin/env python3
"""Build the public Facility Registry from structured source records.

Registry JSON files under registry/data/facilities/ are the source of truth.
This script validates those records and generates:
  - docs/registry/index.md
  - docs/registry/<slug>.md
  - docs/registry/registry.json
  - docs/registry/registry.csv

Use --check after generation to verify deterministic outputs.
"""
from __future__ import annotations

import argparse
import csv
import io
import json
import sys
from pathlib import Path
from typing import Any

CLASSIFICATIONS = {"TPF", "LPF", "NPF", "NOT_PUBLIC", "UNRESOLVED"}
CONFIDENCE = {"HIGH", "MEDIUM", "LOW", "NONE"}
ACCESS = {"PUBLIC", "CONDITIONED_PUBLIC", "RESTRICTED", "UNKNOWN"}
FIELD_STATUS = {"PRE_FIELD", "PARTIAL_FIELD", "FIELD_VERIFIED"}
RECORDING_STATUS = {
    "NO_GENERAL_BAN_LOCATED",
    "STRONG_ACTIVITY_PROTECTION",
    "ACTIVITY_SPECIFIC_RULE",
    "SEPARATE_ANALYSIS",
    "UNRESOLVED",
    "NOT_APPLICABLE",
}
RESTRICTION_ACTIVITIES = {
    "GENERAL_EXPRESSION",
    "SPEECH_CONVERSATION",
    "SIGNS_DISPLAY",
    "LEAFLETS_LITERATURE",
    "PETITIONING",
    "ASSEMBLY_DEMONSTRATION",
    "SOLICITATION",
    "RECORDING",
    "PUBLIC_COMMENT",
    "TABLING_SETUP",
    "EXPRESSIVE_CLOTHING",
    "PRESS_INFORMATION_GATHERING",
    "ACCESS_REMOVAL",
}
RESTRICTION_STATUS = {
    "NO_MATERIAL_RESTRICTION_LOCATED",
    "RULE_LOCATED_UNTESTED",
    "CONSTITUTIONALLY_SUPPORTED",
    "CONSTITUTIONALITY_UNRESOLVED",
    "FACIALLY_SUSPECT",
    "AS_APPLIED_SUSPECT",
    "LIKELY_INVALID",
    "UPHELD_BINDING",
    "NOT_APPLICABLE",
}
RESTRICTION_STATUS_REQUIRING_RULE = RESTRICTION_STATUS - {
    "NO_MATERIAL_RESTRICTION_LOCATED",
    "NOT_APPLICABLE",
}
RESTRICTION_STATUS_REQUIRING_AUTHORITY = {
    "CONSTITUTIONALLY_SUPPORTED",
    "FACIALLY_SUSPECT",
    "AS_APPLIED_SUSPECT",
    "LIKELY_INVALID",
    "UPHELD_BINDING",
}
INDOOR_SPACE_TYPES = {
    "LOBBY",
    "FOYER",
    "WAITING_AREA",
    "PUBLIC_SERVICE_COUNTER",
    "GENERAL_SHARED_INTERIOR",
    "SHARED_CORRIDOR",
    "PURPOSE_LIMITED_INTERIOR",
}
PRIVACY_CONTEXT = {
    "NO_SPECIAL_RISK_IDENTIFIED",
    "ROUTINE_SENSITIVE_INFORMATION_POSSIBLE",
    "CONFIDENTIAL_INTERACTION_POSSIBLE",
    "CONFIDENTIAL_INTERACTION_LIKELY",
    "HIPAA_CONTEXT",
    "UNKNOWN",
}
HIPAA_POSTURE = {
    "NOT_INDICATED",
    "POTENTIALLY_APPLICABLE",
    "COVERED_ENTITY_CONTEXT",
    "UNKNOWN",
}
RIGHTS_RISK_STATUS = {"NONE", "POSSIBLE", "DOCUMENTED", "ADJUDICATED"}
ENFORCEMENT_EVENT_TYPE = {
    "WARNING",
    "CEASE_ORDER",
    "REMOVAL",
    "SUSPENSION",
    "TRESPASS_NOTICE",
    "POLICE_CALL",
    "DETENTION",
    "CITATION",
    "ARREST",
    "PROSECUTION",
    "CHILLING_COMPLIANCE",
    "CLAIM_LAWSUIT",
    "SETTLEMENT_INJUNCTION",
    "POLICY_CHANGE",
    "OTHER",
}
HISTORICAL_LEGAL_ASSESSMENT = {
    "ADJUDICATED_UNLAWFUL",
    "APPARENTLY_INCONSISTENT_WITH_THEN_CONTROLLING_LAW",
    "CONSTITUTIONALLY_SUSPECT_NEEDS_RECORDS",
    "LATER_LAW_CHANGED_OR_CLARIFIED",
    "LAWFUL_OR_DISTINGUISHABLE",
    "UNRESOLVED",
}


def die(message: str) -> None:
    raise ValueError(message)


def require(obj: dict[str, Any], key: str, context: str) -> Any:
    if key not in obj:
        die(f"{context}: missing required key {key!r}")
    return obj[key]


def validate_forum(result: dict[str, Any], context: str) -> None:
    classification = require(result, "classification", context)
    confidence = require(result, "confidence", context)
    require(result, "note", context)
    if classification not in CLASSIFICATIONS:
        die(f"{context}: invalid classification {classification!r}")
    if confidence not in CONFIDENCE:
        die(f"{context}: invalid confidence {confidence!r}")
    if classification == "UNRESOLVED" and confidence != "NONE":
        die(f"{context}: UNRESOLVED must use confidence NONE")
    if classification != "UNRESOLVED" and confidence == "NONE":
        die(f"{context}: classified forum may not use confidence NONE")


def validate_facility(
    f: dict[str, Any],
    authority_ids: set[str],
    seen_ids: set[str],
    seen_slugs: set[str],
) -> None:
    context = f.get("slug") or f.get("facility_id") or "facility"
    required = [
        "schema_version", "facility_id", "slug", "name", "state", "county", "city",
        "agency", "facility_type", "address", "last_verified", "field_status", "summary",
        "recording_summary", "research", "subareas", "index_highlights",
    ]
    for key in required:
        require(f, key, context)
    if f["schema_version"] != 1:
        die(f"{context}: unsupported schema_version {f['schema_version']!r}")
    if f["state"] != "California":
        die(f"{context}: v1 currently expects state=California")
    if f["facility_id"] in seen_ids:
        die(f"{context}: duplicate facility_id {f['facility_id']}")
    if f["slug"] in seen_slugs:
        die(f"{context}: duplicate slug {f['slug']}")
    seen_ids.add(f["facility_id"])
    seen_slugs.add(f["slug"])
    if f["field_status"] not in FIELD_STATUS:
        die(f"{context}: invalid field_status {f['field_status']!r}")

    signals = f.get("rights_risk_signals", [])
    if not isinstance(signals, list):
        die(f"{context}: rights_risk_signals must be a list")
    seen_signal_ids: set[str] = set()
    for idx, signal in enumerate(signals, start=1):
        signal_context = f"{context}.rights_risk_signals[{idx}]"
        signal_id = require(signal, "signal_id", signal_context)
        if signal_id in seen_signal_ids:
            die(f"{context}: duplicate rights-risk signal_id {signal_id!r}")
        seen_signal_ids.add(signal_id)
        status = require(signal, "status", signal_context)
        if status not in RIGHTS_RISK_STATUS:
            die(f"{signal_context}: invalid status {status!r}")
        activity = require(signal, "activity", signal_context)
        if activity not in RESTRICTION_ACTIVITIES:
            die(f"{signal_context}: invalid activity {activity!r}")
        for key in ("scope", "time_period", "summary", "current_legal_assessment", "last_reviewed", "event_ids"):
            require(signal, key, signal_context)
        if not isinstance(signal["event_ids"], list):
            die(f"{signal_context}: event_ids must be a list")
        if signal.get("subarea_ids") is not None and not isinstance(signal["subarea_ids"], list):
            die(f"{signal_context}: subarea_ids must be a list when supplied")
        if signal.get("source_urls") is not None and not isinstance(signal["source_urls"], list):
            die(f"{signal_context}: source_urls must be a list when supplied")

    history = f.get("enforcement_history", [])
    if not isinstance(history, list):
        die(f"{context}: enforcement_history must be a list")
    seen_event_ids: set[str] = set()
    for idx, event in enumerate(history, start=1):
        event_context = f"{context}.enforcement_history[{idx}]"
        event_id = require(event, "event_id", event_context)
        if event_id in seen_event_ids:
            die(f"{context}: duplicate enforcement event_id {event_id!r}")
        seen_event_ids.add(event_id)
        event_type = require(event, "event_type", event_context)
        if event_type not in ENFORCEMENT_EVENT_TYPE:
            die(f"{event_context}: invalid event_type {event_type!r}")
        activity = require(event, "activity", event_context)
        if activity not in RESTRICTION_ACTIVITIES:
            die(f"{event_context}: invalid activity {activity!r}")
        assessment = require(event, "legal_assessment", event_context)
        if assessment not in HISTORICAL_LEGAL_ASSESSMENT:
            die(f"{event_context}: invalid legal_assessment {assessment!r}")
        for key in ("date", "scope", "summary", "current_relevance", "sources"):
            require(event, key, event_context)
        if not isinstance(event["sources"], list) or not event["sources"]:
            die(f"{event_context}: sources must contain at least one source")
        if not all(isinstance(source, str) and source.strip() for source in event["sources"]):
            die(f"{event_context}: each source must be a non-empty string reference")
        if event.get("subarea_ids") is not None and not isinstance(event["subarea_ids"], list):
            die(f"{event_context}: subarea_ids must be a list when supplied")

    county = f["county"]
    if not county.get("name") or not county.get("fips"):
        die(f"{context}: county requires name and fips")
    address = f["address"]
    for key in ("street", "city", "state", "zip"):
        require(address, key, f"{context}.address")

    research = f["research"]
    for key in ("sweep_path", "evidence_path"):
        require(research, key, f"{context}.research")

    local_ids: set[str] = set()
    for sub in f["subareas"]:
        sid = require(sub, "subarea_id", f"{context}.subarea")
        if sid in local_ids:
            die(f"{context}: duplicate subarea_id {sid}")
        local_ids.add(sid)
        require(sub, "name", f"{context}.{sid}")
        access = require(sub, "access", f"{context}.{sid}")
        if access not in ACCESS:
            die(f"{context}.{sid}: invalid access {access!r}")
        validate_forum(require(sub, "federal", f"{context}.{sid}"), f"{context}.{sid}.federal")
        validate_forum(require(sub, "california", f"{context}.{sid}"), f"{context}.{sid}.california")
        recording = require(sub, "recording", f"{context}.{sid}")
        status = require(recording, "status", f"{context}.{sid}.recording")
        require(recording, "summary", f"{context}.{sid}.recording")
        if status not in RECORDING_STATUS:
            die(f"{context}.{sid}: invalid recording status {status!r}")

        audits = require(sub, "restriction_audits", f"{context}.{sid}")
        if not isinstance(audits, list) or not audits:
            die(f"{context}.{sid}: restriction_audits must contain at least one Constitution First audit")
        seen_activities: set[str] = set()
        for audit in audits:
            activity = require(audit, "activity", f"{context}.{sid}.restriction_audit")
            audit_status = require(audit, "status", f"{context}.{sid}.restriction_audit")
            require(audit, "summary", f"{context}.{sid}.restriction_audit")
            if activity not in RESTRICTION_ACTIVITIES:
                die(f"{context}.{sid}: invalid restriction activity {activity!r}")
            if activity in seen_activities:
                die(f"{context}.{sid}: duplicate restriction audit activity {activity!r}")
            seen_activities.add(activity)
            if audit_status not in RESTRICTION_STATUS:
                die(f"{context}.{sid}: invalid restriction status {audit_status!r}")
            if audit_status in RESTRICTION_STATUS_REQUIRING_RULE and not audit.get("rule_source"):
                die(f"{context}.{sid}: {audit_status} requires rule_source")
            if audit_status == "CONSTITUTIONALITY_UNRESOLVED" and not audit.get("unresolved_reason"):
                die(f"{context}.{sid}: CONSTITUTIONALITY_UNRESOLVED requires unresolved_reason")
            audit_authorities = audit.get("authority_ids", [])
            if audit_status in RESTRICTION_STATUS_REQUIRING_AUTHORITY and not audit_authorities:
                die(f"{context}.{sid}: {audit_status} requires supporting authority_ids")
            for aid in audit_authorities:
                if aid not in authority_ids:
                    die(f"{context}.{sid}: restriction audit references unknown authority id {aid!r}")

        indoor = sub.get("indoor_common_space")
        if indoor is not None:
            space_type = require(indoor, "space_type", f"{context}.{sid}.indoor_common_space")
            privacy_context = require(indoor, "privacy_context", f"{context}.{sid}.indoor_common_space")
            hipaa_posture = require(indoor, "hipaa_posture", f"{context}.{sid}.indoor_common_space")
            require(indoor, "facility_responsibility", f"{context}.{sid}.indoor_common_space")
            require(indoor, "visitor_responsibility", f"{context}.{sid}.indoor_common_space")
            require(indoor, "recording_effect", f"{context}.{sid}.indoor_common_space")
            if space_type not in INDOOR_SPACE_TYPES:
                die(f"{context}.{sid}: invalid indoor space_type {space_type!r}")
            if privacy_context not in PRIVACY_CONTEXT:
                die(f"{context}.{sid}: invalid privacy_context {privacy_context!r}")
            if hipaa_posture not in HIPAA_POSTURE:
                die(f"{context}.{sid}: invalid hipaa_posture {hipaa_posture!r}")
            for aid in indoor.get("authority_ids", []):
                if aid not in authority_ids:
                    die(f"{context}.{sid}: indoor analysis references unknown authority id {aid!r}")

        unresolved = (
            sub["federal"]["classification"] == "UNRESOLVED"
            or sub["california"]["classification"] == "UNRESOLVED"
            or status == "UNRESOLVED"
        )
        if unresolved and not sub.get("unresolved_reason"):
            die(f"{context}.{sid}: unresolved result requires unresolved_reason")
        for aid in sub.get("authority_ids", []):
            if aid not in authority_ids:
                die(f"{context}.{sid}: unknown authority id {aid!r}")

    event_ids = {event["event_id"] for event in history}
    for idx, event in enumerate(history, start=1):
        event_context = f"{context}.enforcement_history[{idx}]"
        for sid in event.get("subarea_ids", []):
            if sid not in local_ids:
                die(f"{event_context}: unknown subarea_id {sid!r}")

    for idx, signal in enumerate(signals, start=1):
        signal_context = f"{context}.rights_risk_signals[{idx}]"
        for sid in signal.get("subarea_ids", []):
            if sid not in local_ids:
                die(f"{signal_context}: unknown subarea_id {sid!r}")
        for event_id in signal["event_ids"]:
            if event_id not in event_ids:
                die(f"{signal_context}: unknown enforcement event_id {event_id!r}")
        if signal["status"] in {"DOCUMENTED", "ADJUDICATED"} and not signal["event_ids"]:
            die(f"{signal_context}: {signal['status']} requires at least one linked event_id")
        if signal["status"] == "ADJUDICATED":
            linked = [event for event in history if event["event_id"] in signal["event_ids"]]
            if not any(event["legal_assessment"] == "ADJUDICATED_UNLAWFUL" for event in linked):
                die(f"{signal_context}: ADJUDICATED requires a linked ADJUDICATED_UNLAWFUL event")
        if signal["status"] == "NONE" and signal["event_ids"]:
            die(f"{signal_context}: NONE may not link adverse enforcement events")

    for h in f["index_highlights"]:
        ids = require(h, "subarea_ids", f"{context}.index_highlight")
        require(h, "label", f"{context}.index_highlight")
        for sid in ids:
            if sid not in local_ids:
                die(f"{context}: index_highlight references unknown subarea {sid}")
        first = next(s for s in f["subareas"] if s["subarea_id"] == ids[0])
        first_pair = (first["federal"]["classification"], first["federal"]["confidence"])
        for sid in ids[1:]:
            other = next(s for s in f["subareas"] if s["subarea_id"] == sid)
            pair = (other["federal"]["classification"], other["federal"]["confidence"])
            if pair != first_pair:
                die(
                    f"{context}: highlight {h['label']!r} mixes "
                    f"federal classification/confidence {first_pair} and {pair}"
                )

    for aid in f.get("authorities", []):
        if aid not in authority_ids:
            die(f"{context}: unknown facility authority id {aid!r}")


def forum_label(result: dict[str, str]) -> str:
    c = result["classification"]
    if c == "NOT_PUBLIC":
        return "NOT PUBLIC"
    return c


def confidence_suffix(result: dict[str, str]) -> str:
    return "" if result["confidence"] == "NONE" else f" · {result['confidence']}"


def pill_class(classification: str) -> str:
    return {
        "TPF": "tpf",
        "LPF": "lpf",
        "NPF": "npf",
        "NOT_PUBLIC": "unresolved",
        "UNRESOLVED": "unresolved",
    }[classification]


def md_link_from_registry(target: str) -> str:
    if target.startswith("docs/"):
        target = target[len("docs/"):]
    return "../" + target


def generate_index(facilities: list[dict[str, Any]]) -> str:
    counties: dict[str, list[dict[str, Any]]] = {}
    for f in facilities:
        counties.setdefault(f["county"]["name"], []).append(f)

    out = [
        "---",
        "title: Facility Registry",
        "---",
        "",
        "# Facility Registry",
        "",
        '<div class="registry-hero" markdown>',
        "",
        "**Data-driven working Registry.** One compact row per facility. Forum classification, confidence, recording posture, and field verification are separate fields so a pending site visit does not make an otherwise answerable legal question look unresolved.",
        "",
        "Forum labels below are **project classifications**, not claims that a court has adjudicated that exact address.",
        "",
        "**Constitution First:** a government rule is recorded as a claimed restriction until its legal and constitutional support is analyzed. `RULE LOCATED` never means `lawful prohibition` by itself.",
        "",
        '<div class="registry-legend" markdown>',
        '<span class="registry-pill registry-pill--tpf">TPF</span> traditional public forum',
        '<span class="registry-pill registry-pill--lpf">LPF</span> limited public forum',
        '<span class="registry-pill registry-pill--npf">NPF</span> nonpublic forum',
        '<span class="registry-pill registry-pill--unresolved">UNRESOLVED</span> a real gap could change the answer',
        '<span class="registry-pill registry-pill--high">HIGH</span> strong classification confidence',
        '<span class="registry-pill registry-pill--medium">MEDIUM</span> defensible but more fact-sensitive',
        '<span class="registry-pill registry-pill--field">FIELD PENDING</span> verification only unless stated otherwise',
        "</div>",
        "",
        "[Constitution First](../constitution-first.md) · [How Registry classifications work](method.md) · [What can I actually do in each forum?](../california/forum-activity-guide.md) · [Registry data model](data-model.md) · [Machine-readable Registry JSON](registry.json) · [Flat subarea CSV](registry.csv)",
        "",
        "</div>",
        "",
    ]

    for county in sorted(counties):
        out += [f"## {county}", "", '<div class="registry-list" markdown>', ""]
        for f in sorted(counties[county], key=lambda x: (x["city"], x["name"])):
            out += [
                '<div class="registry-row" markdown>',
                "",
                '<div class="registry-row__identity" markdown>',
                "",
                f"### [{f['name']}]({f['slug']}.md)",
                "",
                f"{f['address']['street']}, {f['city']}  ",
                f"{f['facility_type'].replace('_', ' ').title()} · {f['agency']}",
                "",
                f"`{f['facility_id']}`",
                "",
                "</div>",
                "",
                '<div class="registry-row__classification" markdown>',
                "",
                "**Key classifications**",
                "",
            ]
            by_id = {s["subarea_id"]: s for s in f["subareas"]}
            for h in f["index_highlights"]:
                sub = by_id[h["subarea_ids"][0]]
                fed = sub["federal"]
                label = forum_label(fed) + confidence_suffix(fed)
                scope = f" **{h['scope_suffix']}**" if h.get("scope_suffix") else ""
                out.append(
                    f'<span class="registry-pill registry-pill--{pill_class(fed["classification"])}">'
                    f'{label}</span> {h["label"]}{scope}  '
                )
            out += [
                "",
                f"**Recording:** {f['recording_summary']}",
                "",
                "</div>",
                "",
                '<div class="registry-row__status" markdown>',
                "",
            ]
            if any(s["california"]["classification"] == "UNRESOLVED" for s in f["subareas"]):
                out.append('<span class="registry-pill registry-pill--unresolved">CA QUESTIONS REMAIN</span>')
            if any(s.get("indoor_common_space") for s in f["subareas"]):
                out.append('<span class="registry-pill registry-pill--high">INDOOR ANALYZED</span>')
            if f["field_status"] != "FIELD_VERIFIED":
                out.append('<span class="registry-pill registry-pill--field">FIELD PENDING</span>')
            field_items = f.get("field_items", [])[:3]
            if field_items:
                out += ["", "Main open field items: " + "; ".join(field_items) + "."]
            out += [
                "",
                f"[Detail]({f['slug']}.md) · "
                f"[Sweep]({md_link_from_registry(f['research']['sweep_path'])}) · "
                f"[Evidence]({md_link_from_registry(f['research']['evidence_path'])})",
                "",
                "</div>",
                "",
                "</div>",
                "",
            ]
        out += ["</div>", ""]

    out += [
        "## Scale model",
        "",
        "The compact index is designed to remain usable when the Registry grows from four facilities to counties and eventually statewide coverage. The structured records now also emit `registry.json` and a flat `registry.csv`, which are the foundation for later client-side search, filters, pagination, maps, and filtered downloads.",
        "",
        "The source of truth is `registry/data/facilities/*.json`; these Markdown pages are generated outputs.",
        "",
    ]
    return "\n".join(out).rstrip() + "\n"


def generate_detail(f: dict[str, Any], authorities: dict[str, Any]) -> str:
    out = [
        "---",
        f"title: {f['name']}",
        "---",
        "",
        f"# {f['name']}",
        "",
        f"**{f['address']['street']}, {f['city']}, CA {f['address']['zip']}**  ",
        f"{f['agency']} · `{f['facility_id']}`  ",
        f"**Last verified:** {f['last_verified']} · **Field status:** {f['field_status'].replace('_', ' ').title()}",
        "",
        '<div class="registry-bottom-line" markdown>',
        "",
        f"**Bottom line:** {f['summary']}",
        "",
        "</div>",
        "",
        "**Constitution First:** the Registry does not treat a posted or published government rule as lawful merely because it exists. [Read the governing project principle.](../constitution-first.md)",
        "",
        "[What do these forum labels mean for speech, signs, leaflets, recording, public comment, tabling, and other expression?](../california/forum-activity-guide.md)",
        "",
        "## Subarea classifications",
        "",
        "| Area | Federal classification | California classification | Confidence | Recording / practical note |",
        "| --- | --- | --- | --- | --- |",
    ]
    for s in f["subareas"]:
        fed = forum_label(s["federal"])
        ca = forum_label(s["california"])
        conf = s["federal"]["confidence"] if s["federal"]["confidence"] != "NONE" else "—"
        note = s["recording"]["summary"].replace("|", "\\|")
        area = s["name"].replace("|", "\\|")
        out.append(f"| {area} | **{fed}** | **{ca}** | **{conf}** | {note} |")

    out += [
        "",
        "## Constitution First — restriction audit",
        "",
        "A rule listed below is a **claimed restriction**, not a concession that the rule is constitutional. The status records how far the project has actually tested it.",
        "",
        "| Area | Activity | Restriction status | Current constitutional posture |",
        "| --- | --- | --- | --- |",
    ]
    for s in f["subareas"]:
        area = s["name"].replace("|", "\\|")
        for audit in s["restriction_audits"]:
            activity = audit["activity"].replace("_", " ").title()
            status_text = audit["status"].replace("_", " ")
            summary = audit["summary"].replace("|", "\\|")
            out.append(f"| {area} | {activity} | **{status_text}** | {summary} |")

    indoor_rows = [s for s in f["subareas"] if s.get("indoor_common_space")]
    if indoor_rows:
        out += [
            "",
            "## Indoor common-space / privacy responsibility",
            "",
            "These rows separate a facility's privacy/confidentiality duties from duties that actually apply to a visitor. A privacy interest can support a narrower restriction, but it does not become a blanket camera ban merely by being asserted.",
            "",
            "[Read the indoor common-space doctrine.](../california/indoor-public-common-spaces.md)",
            "",
            "| Area | Space type | Privacy context | HIPAA posture | Facility responsibility | Visitor responsibility | Recording consequence |",
            "| --- | --- | --- | --- | --- | --- | --- |",
        ]
        for s in indoor_rows:
            indoor = s["indoor_common_space"]
            area = s["name"].replace("|", "\\|")
            space_type = indoor["space_type"].replace("_", " ").title()
            privacy = indoor["privacy_context"].replace("_", " ").title()
            hipaa = indoor["hipaa_posture"].replace("_", " ").title()
            facility_resp = indoor["facility_responsibility"].replace("|", "\\|")
            visitor_resp = indoor["visitor_responsibility"].replace("|", "\\|")
            recording_effect = indoor["recording_effect"].replace("|", "\\|")
            out.append(
                f"| {area} | {space_type} | **{privacy}** | **{hipaa}** | "
                f"{facility_resp} | {visitor_resp} | {recording_effect} |"
            )

    out += ["", "## Recording posture", "", f["recording_summary"], ""]

    signals = f.get("rights_risk_signals", [])
    history = f.get("enforcement_history", [])
    if signals or history:
        out += [
            "## Enforcement history / rights-risk",
            "",
            "These are scoped evidence labels, not facility-wide guilt findings. **DOCUMENTED** means a relevant adverse enforcement or chilling event is reliably documented; it does not mean a court has adjudicated the action unlawful.",
            "",
        ]
    if signals:
        out += [
            "### Rights-Risk Signals",
            "",
            "| Signal | Activity | Subarea(s) | Scope | Period reviewed | Current legal assessment | Summary | Event links | Last reviewed |",
            "| --- | --- | --- | --- | --- | --- | --- | --- | --- |",
        ]
        subarea_names = {sub["subarea_id"]: sub["name"] for sub in f["subareas"]}
        for signal in signals:
            subareas = ", ".join(
                subarea_names.get(sid, sid) for sid in signal.get("subarea_ids", [])
            ) or "Facility/policy scope"
            events = ", ".join(signal["event_ids"]) or "—"
            out.append(
                f"| **{signal['status']}** | {signal['activity'].replace('_', ' ').title()} | "
                f"{esc(subareas)} | {esc(signal['scope'])} | {esc(signal['time_period'])} | "
                f"{esc(signal['current_legal_assessment'])} | {esc(signal['summary'])} | "
                f"{esc(events)} | {signal['last_reviewed']} |"
            )
        out.append("")
    if history:
        out += [
            "### Historical enforcement / chilling events",
            "",
            "| ID | Date | Event | Activity | Subarea(s) | Scope | Historical assessment | Summary | Current relevance | Sources |",
            "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
        ]
        subarea_names = {sub["subarea_id"]: sub["name"] for sub in f["subareas"]}
        for event in history:
            subareas = ", ".join(
                subarea_names.get(sid, sid) for sid in event.get("subarea_ids", [])
            ) or "Facility/policy scope"
            out.append(
                f"| {event['event_id']} | {event['date']} | {event['event_type'].replace('_', ' ').title()} | "
                f"{event['activity'].replace('_', ' ').title()} | {esc(subareas)} | {esc(event['scope'])} | "
                f"**{event['legal_assessment'].replace('_', ' ')}** | {esc(event['summary'])} | "
                f"{esc(event['current_relevance'])} | {esc('; '.join(event['sources']))} |"
            )
        out.append("")

    if f.get("field_items"):
        out += ["## What a field visit still adds", ""] + [f"- {x}" for x in f["field_items"]] + [""]
    if f.get("open_legal_items"):
        out += ["## What remains legally unresolved", ""] + [f"- {x}" for x in f["open_legal_items"]] + [""]

    out += ["## Research", ""]
    links = [
        f"[Sweep]({md_link_from_registry(f['research']['sweep_path'])})",
        f"[Evidence manifest]({md_link_from_registry(f['research']['evidence_path'])})",
    ]
    if f["research"].get("hardening_path"):
        links.append(
            f"[Classification hardening note]({md_link_from_registry(f['research']['hardening_path'])})"
        )
    if f["research"].get("indoor_hardening_path"):
        links.append(
            f"[Indoor common-space hardening note]({md_link_from_registry(f['research']['indoor_hardening_path'])})"
        )
    out += [" · ".join(links), ""]

    if f.get("authorities"):
        out += ["### Key authorities", ""]
        for aid in f["authorities"]:
            a = authorities[aid]
            out.append(f"- **{a['citation']}** — {a['topic']}")
        out.append("")

    out += [
        "## Data record",
        "",
        f"This page is generated from `registry/data/facilities/{f['slug']}.json`. "
        "The structured record is the source of truth for this Registry entry.",
        "",
    ]
    return "\n".join(out).rstrip() + "\n"


def generate_registry_json(
    facilities: list[dict[str, Any]], authorities: dict[str, Any]
) -> str:
    payload = {
        "schema_version": 1,
        "state": "California",
        "facility_count": len(facilities),
        "last_verified_max": max(f["last_verified"] for f in facilities),
        "facilities": facilities,
        "authorities": authorities,
    }
    return json.dumps(payload, indent=2, ensure_ascii=False, sort_keys=True) + "\n"


def generate_registry_csv(facilities: list[dict[str, Any]]) -> str:
    fields = [
        "facility_id", "slug", "facility_name", "county", "city", "agency", "facility_type",
        "street", "zip", "last_verified", "field_status", "subarea_id", "subarea_name", "access",
        "federal_classification", "federal_confidence", "california_classification",
        "california_confidence", "recording_status", "recording_summary",
        "restriction_activities", "restriction_statuses", "restriction_summaries",
        "indoor_space_type", "privacy_context", "hipaa_posture",
        "facility_privacy_responsibility", "visitor_privacy_responsibility",
        "privacy_recording_effect", "rights_risk_signals", "enforcement_event_count",
        "enforcement_assessments", "unresolved_reason",
    ]
    buf = io.StringIO(newline="")
    writer = csv.DictWriter(buf, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    for f in facilities:
        facility_signals = f.get("rights_risk_signals", [])
        facility_history = f.get("enforcement_history", [])
        for s in f["subareas"]:
            sid = s["subarea_id"]
            applicable_signals = [
                signal for signal in facility_signals
                if not signal.get("subarea_ids") or sid in signal.get("subarea_ids", [])
            ]
            applicable_history = [
                event for event in facility_history
                if not event.get("subarea_ids") or sid in event.get("subarea_ids", [])
            ]
            writer.writerow(
                {
                    "facility_id": f["facility_id"],
                    "slug": f["slug"],
                    "facility_name": f["name"],
                    "county": f["county"]["name"],
                    "city": f["city"],
                    "agency": f["agency"],
                    "facility_type": f["facility_type"],
                    "street": f["address"]["street"],
                    "zip": f["address"]["zip"],
                    "last_verified": f["last_verified"],
                    "field_status": f["field_status"],
                    "subarea_id": s["subarea_id"],
                    "subarea_name": s["name"],
                    "access": s["access"],
                    "federal_classification": s["federal"]["classification"],
                    "federal_confidence": s["federal"]["confidence"],
                    "california_classification": s["california"]["classification"],
                    "california_confidence": s["california"]["confidence"],
                    "recording_status": s["recording"]["status"],
                    "recording_summary": s["recording"]["summary"],
                    "restriction_activities": "; ".join(a["activity"] for a in s["restriction_audits"]),
                    "restriction_statuses": "; ".join(a["status"] for a in s["restriction_audits"]),
                    "restriction_summaries": " | ".join(a["summary"] for a in s["restriction_audits"]),
                    "indoor_space_type": s.get("indoor_common_space", {}).get("space_type", ""),
                    "privacy_context": s.get("indoor_common_space", {}).get("privacy_context", ""),
                    "hipaa_posture": s.get("indoor_common_space", {}).get("hipaa_posture", ""),
                    "facility_privacy_responsibility": s.get("indoor_common_space", {}).get("facility_responsibility", ""),
                    "visitor_privacy_responsibility": s.get("indoor_common_space", {}).get("visitor_responsibility", ""),
                    "privacy_recording_effect": s.get("indoor_common_space", {}).get("recording_effect", ""),
                    "rights_risk_signals": "; ".join(
                        f"{signal['signal_id']} {signal['status']} {signal['activity']}: "
                        f"{signal['scope']} [{signal['current_legal_assessment']}]"
                        for signal in applicable_signals
                    ),
                    "enforcement_event_count": len(applicable_history),
                    "enforcement_assessments": "; ".join(
                        sorted({event["legal_assessment"] for event in applicable_history})
                    ),
                    "unresolved_reason": s.get("unresolved_reason", ""),
                }
            )
    return buf.getvalue()


def load(root: Path) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    auth_doc = json.loads((root / "registry/data/authorities.json").read_text(encoding="utf-8"))
    authorities = auth_doc["authorities"]
    authority_ids = set(authorities)
    facilities: list[dict[str, Any]] = []
    seen_ids: set[str] = set()
    seen_slugs: set[str] = set()
    for path in sorted((root / "registry/data/facilities").glob("*.json")):
        f = json.loads(path.read_text(encoding="utf-8"))
        validate_facility(f, authority_ids, seen_ids, seen_slugs)
        facilities.append(f)
    if not facilities:
        die("No facility records found")
    return facilities, authorities


def outputs(
    root: Path,
    facilities: list[dict[str, Any]],
    authorities: dict[str, Any],
) -> dict[Path, str]:
    docs = root / "docs/registry"
    result: dict[Path, str] = {
        docs / "index.md": generate_index(facilities),
        docs / "registry.json": generate_registry_json(facilities, authorities),
        docs / "registry.csv": generate_registry_csv(facilities),
    }
    for f in facilities:
        result[docs / f"{f['slug']}.md"] = generate_detail(f, authorities)
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".", help="repository root")
    parser.add_argument(
        "--check",
        action="store_true",
        help="fail if generated files differ from files currently on disk",
    )
    args = parser.parse_args()
    root = Path(args.root).resolve()
    facilities, authorities = load(root)
    generated = outputs(root, facilities, authorities)

    stale: list[str] = []
    for path, text in generated.items():
        if args.check:
            if not path.exists() or path.read_text(encoding="utf-8") != text:
                stale.append(str(path.relative_to(root)))
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8", newline="")

    if stale:
        print("Registry generated outputs are stale:", file=sys.stderr)
        for path in stale:
            print(f"  - {path}", file=sys.stderr)
        return 1

    mode = "validated" if args.check else "generated"
    subareas = sum(len(f["subareas"]) for f in facilities)
    print(f"Registry {mode}: {len(facilities)} facilities, {subareas} subareas")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except ValueError as exc:
        print(f"Registry validation error: {exc}", file=sys.stderr)
        raise SystemExit(2)
