---
title: Registry data model
---

# Registry data model

The Facility Registry is designed around structured data rather than hand-authored facility pages.

## Source of truth

Each facility has one JSON record under:

`registry/data/facilities/<slug>.json`

The immutable `facility_id` is the durable machine identity. A human-readable slug, facility name, or address may change later without changing that ID.

For the current Contra Costa pilots the ID pattern is:

`CA-013-F####`

where `013` is the county namespace and the final number is a stable facility serial.

## Facility-level fields

A facility record stores identity and location, agency and facility type, property summary, last verification date, field-verification status, concise legal and recording summaries, field-check items, unresolved legal items, research/evidence links, authority references, index highlights, and subareas.

When historical research supports them, a facility record can also store:

- `rights_risk_signals` — scoped evidence signals for a defined area/activity/policy and review period; and
- `enforcement_history` — sourced warnings, removals, exclusions, police actions, prosecutions, chilling/compliance events, litigation, injunctions, policy changes, and related historical events.

These fields are optional. An unresearched facility is not assigned `NONE` merely because no history has been entered.

### Rights-Risk Signals

Current signal values are:

`NONE` · `POSSIBLE` · `DOCUMENTED` · `ADJUDICATED`

The signal is separate from forum classification, restriction-audit status, and field verification.

- `DOCUMENTED` means reliable evidence documents a relevant adverse enforcement or chilling event; it is **not** a judicial finding that the action was unlawful.
- `ADJUDICATED` is reserved for an actual court or competent-tribunal holding on the represented issue.

Signals must be scoped and include the period actually reviewed. Each signal has a stable `signal_id`, canonical `activity`, optional exact `subarea_ids`, a `current_legal_assessment`, and linked `event_ids`. A `DOCUMENTED` or `ADJUDICATED` signal cannot float free of the evidence history: it must point to at least one historical event.

### Enforcement-history assessments

Each historical event has a stable `event_id`, canonical activity, optional exact `subarea_ids`, one or more public/auditable source references, and a date-sensitive project assessment:

`ADJUDICATED_UNLAWFUL` · `APPARENTLY_INCONSISTENT_WITH_THEN_CONTROLLING_LAW` · `CONSTITUTIONALLY_SUSPECT_NEEDS_RECORDS` · `LATER_LAW_CHANGED_OR_CLARIFIED` · `LAWFUL_OR_DISTINGUISHABLE` · `UNRESOLVED`

This keeps historical evidence separate from modern law and prevents a later policy change from erasing what happened.

## Subareas are the legal unit

The building is not assigned one blanket forum label. Each `subarea` stores:

- stable `subarea_id`;
- public-access status;
- federal forum classification and confidence;
- California forum classification and confidence;
- recording posture;
- one or more **Constitution First restriction audits** identifying the activity, claimed restriction posture, and constitutional status;
- optional **indoor common-space analysis** for public lobbies, foyers, waiting areas, service counters, shared corridors, and similar interior areas;
- concise practical note;
- unresolved reason when one exists; and
- authority IDs supporting the result.

Current forum values are:

`TPF` · `LPF` · `NPF` · `NOT_PUBLIC` · `UNRESOLVED`

Current confidence values are:

`HIGH` · `MEDIUM` · `LOW` · `NONE`

`NONE` is reserved for an unresolved classification; a classified forum must carry an actual confidence level.

## Constitution First restriction audits

Each subarea must contain at least one `restriction_audits` entry. This prevents the Registry from treating a government rule as the legal conclusion.

Each audit stores:

- the expressive activity being analyzed;
- the current restriction status;
- a concise constitutional posture;
- the rule source when a rule has actually been located;
- the governing constitutional test where useful;
- supporting authority IDs for stronger conclusions; and
- an explicit unresolved reason when constitutionality is unresolved.

A located rule is never automatically serialized as `PROHIBITED`. The data model distinguishes rule existence from constitutional validity.

See [Constitution First](../constitution-first.md) and [Restriction Audit](../california/restriction-audit.md).

## Indoor common-space / privacy fields

When an indoor public/common subarea has been hardened, `indoor_common_space` stores:

- the type of shared interior space;
- the privacy/confidentiality context actually identified;
- whether HIPAA is indicated, potentially applicable, established as a covered-entity context, or unknown;
- the facility's own safeguard responsibility;
- any duty that actually applies to the visitor;
- the effect of the privacy facts on recording analysis; and
- supporting authority IDs.

This structure is intentionally separate from `recording` and `restriction_audits`.

A privacy interest does not automatically become a recording prohibition, and a facility's confidentiality duty does not automatically become a visitor duty.

The four pilot facilities currently use `HIPAA_POSTURE = NOT_INDICATED`; none has been established as a HIPAA covered-entity context in the Registry. Future health-related facilities must be researched before that status is promoted.

See [Indoor Public Common Spaces](../california/indoor-public-common-spaces.md).

## Validation rules

`tools/registry/build_registry.py` validates every record before generating public outputs. Among other checks, it rejects duplicate facility/subarea IDs, unknown classifications, invalid confidence combinations, unknown authority references, broken index-highlight references, and an unresolved result without an explicit `unresolved_reason`.

## Generated outputs

The site build generates:

- the county-scale Registry index;
- one detail page per facility;
- `registry.json` for future client-side search/filtering; and
- `registry.csv`, flattened to one row per facility subarea.

This is the base for later pagination, search, filter views, maps, XLSX workbooks, PDF field sheets, county packets, and statewide exports without rewriting the legal record in multiple formats.

## Export direction

The next export layer can consume these same records instead of scraping the website. A single-facility workbook/PDF, a county packet, and a filtered statewide view can therefore all be generated from the same validated source fields.
