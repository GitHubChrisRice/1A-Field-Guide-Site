# Facility Registry data

This directory is the source-of-truth layer for the public Facility Registry.

## Add or edit a facility

1. Create or update one record in `registry/data/facilities/`.
2. Preserve the immutable `facility_id`; names, slugs, addresses, and agencies may be corrected without changing it.
3. Add new reusable legal authorities to `registry/data/authorities.json` and reference them by ID.
4. Run:

```bash
python tools/registry/build_registry.py
python tools/registry/build_registry.py --check
python -m mkdocs build --clean
```

The generator validates classifications, confidence levels, authority references, subarea IDs, index-highlight references, and unresolved-result explanations before producing public pages.

## Design rule

The facility record is not a single forum label. Legal conclusions live at the **subarea** level, with federal and California classifications stored separately.

For public indoor common areas, add `indoor_common_space` only after researching the actual privacy/confidentiality context. Keep facility safeguard duties, visitor duties, recording posture, and claimed-restriction validity separate. Do not infer HIPAA applicability merely because a facility invokes the term.

Field verification is also separate. A pending sign/layout/boundary check does not automatically downgrade a legal classification unless the missing fact can change the legal result.

## Historical enforcement and rights-risk fields

Facility records may optionally include two top-level fields when research supports them:

### `rights_risk_signals`

A list of **scoped** signals. One event must not label an entire facility when only one area, activity, policy, or time period is implicated.

Required fields per signal:

- `signal_id`: stable facility-local identifier;
- `status`: `NONE`, `POSSIBLE`, `DOCUMENTED`, or `ADJUDICATED`;
- `activity`: canonical Registry activity value;
- `scope`: the exact area/activity/policy covered;
- `time_period`: the period actually reviewed;
- `summary`: concise evidence-based explanation;
- `current_legal_assessment`: the project's present legal characterization, with uncertainty stated where appropriate;
- `event_ids`: linked historical-event IDs;
- `last_reviewed`: date of the assessment.

Optional `subarea_ids` ties the signal to exact Registry subareas; omit or leave empty only for a genuinely facility/policy-wide scope. Optional `source_urls` may preserve direct supporting sources.

`DOCUMENTED` and `ADJUDICATED` signals must link at least one enforcement-history event. An `ADJUDICATED` signal must link an event assessed `ADJUDICATED_UNLAWFUL`.

`DOCUMENTED` means reliable evidence of a relevant adverse enforcement or chilling event exists. It does **not** mean a court held the action unconstitutional. `ADJUDICATED` is reserved for an actual adjudication on the represented issue.

### `enforcement_history`

A list of historical enforcement, chilling, litigation, or corrective events.

Required fields per event:

- `event_id`: stable facility-local identifier;
- `date`;
- `event_type`;
- `activity`;
- `scope`;
- `summary`;
- `legal_assessment`;
- `current_relevance`; and
- one or more `sources` as non-empty string references (direct URLs, evidence-manifest paths, or other stable source references).

Optional `subarea_ids` ties the event to exact Registry subareas. Public Registry output should expose those source references so the historical characterization remains auditable.

Historical assessments are date-sensitive and use:

- `ADJUDICATED_UNLAWFUL`
- `APPARENTLY_INCONSISTENT_WITH_THEN_CONTROLLING_LAW`
- `CONSTITUTIONALLY_SUSPECT_NEEDS_RECORDS`
- `LATER_LAW_CHANGED_OR_CLARIFIED`
- `LAWFUL_OR_DISTINGUISHABLE`
- `UNRESOLVED`

These fields are optional so an unresearched facility is not forced into a false `NONE` finding.

## Generated/public outputs

The generator emits the county index, individual facility pages, machine-readable `registry.json`, and flat `registry.csv`.

The next export layer is intended to generate XLSX and PDF facility/county/filter outputs from these same records.
