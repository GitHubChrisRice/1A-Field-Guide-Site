# Facility Investigation Template

Use this template for a facility-specific research file or incident study. Separate verified law, official policy, observed facts, and legal analysis.

## Identification

~~~yaml
facility:
agency:
city:
county:
jurisdiction: California
investigation_id:
research_status:
research_started:
last_verified:
field_visit_date:
~~~

## Research question

State the specific proposition being investigated.

Examples:

- Does the public-lobby recording policy have identified legal authority?
- Does the facility require identification for ordinary public access?
- Has police previously treated a policy violation as criminal trespass?
- Are comparable favorable and unfavorable expressions treated differently?

## Specific area

Describe the exact area. Do not classify the entire facility if only one part is at issue.

- area:
- public hours:
- access status:
- screening:
- sign-in / badge / ID condition:
- physical boundaries:
- adjacent areas with different access:

## Property / boundary evidence

Complete the **baseline property pass for every facility where practical**, even when boundaries do not initially appear controversial. Escalate to the deeper boundary pass whenever ownership, control, right-of-way, easements, or the line between differently governed areas could affect access, forum, removal, or trespass analysis.

Do not infer legal boundaries from appearance alone.

### Baseline property pass

- [ ] search the official address in county assessor / parcel / GIS sources;
- [ ] record parcel / APN or equivalent identifier;
- [ ] record the current record owner if supported by an official source;
- [ ] identify the operational agency/controller if different from the owner;
- [ ] capture the official parcel/GIS source and retrieval date;
- [ ] identify immediately adjacent parcels when they affect approaches, parking, plazas, sidewalks, or shared campuses;
- [ ] record whether public right-of-way or easement questions are apparent;
- [ ] assign boundary confidence: VERIFIED / PARTIALLY-VERIFIED / UNRESOLVED.

### Deeper boundary pass when material

- [ ] obtain assessor parcel map / parcel-book reference;
- [ ] locate recorded parcel/subdivision maps, surveys, or corner records when available;
- [ ] identify street/right-of-way, dedication, or engineering records for relevant sidewalks and approaches;
- [ ] identify public-access easements, reciprocal-access agreements, or other recorded interests when relevant;
- [ ] identify leases, licenses, MOUs, joint-use, operating, maintenance, or parking agreements that may separate ownership from control;
- [ ] map the specific lot, plaza, forecourt, walkway, driveway, sidewalk, or other area being analyzed;
- [ ] preserve a reproducible GIS/export/PDF/screenshot when a dynamic map materially supports the analysis;
- [ ] identify what remains unresolved and whether a public-records request is needed.

### Property / boundary record

- boundary relevance:
- parcel / APN:
- assessor parcel map / map-book reference:
- recorded map / survey reference:
- record owner, if verified:
- operational controller, if different or separately established:
- public right-of-way / dedication information:
- easement / public-access information:
- parking / plaza / walkway control:
- adjacent parcel(s) relevant to access:
- boundary confidence: VERIFIED / PARTIALLY-VERIFIED / UNRESOLVED
- live source link(s):
- preserved map/export/screenshot:
- evidence manifest / facility evidence directory:
- retrieval / verification date:

| Source | Source type | Date/version | What it supports | Limits / unresolved issue | Preserved copy |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

Prefer official deeds, recorded parcel maps, assessor/parcel records, right-of-way or engineering maps, official GIS layers, and current leases/MOUs/operating agreements as appropriate to the question. A GIS or assessor map can be strong boundary evidence but does not automatically establish every easement, right-of-way, lease, operational-control arrangement, or constitutional forum classification.

When an interactive GIS map materially supports the analysis, preserve an export, PDF, or screenshot when practical in addition to linking the live source. Record enough identifying information to reproduce the view later, including parcel/APN, layer name, selected feature, and retrieval date.

## Forum / constitutional classification

- federal forum classification:
- California Speech Clause classification:
- activity analyzed:
- controlling authority:
- confidence:
- unresolved questions:

## Authority chain

| Layer | Source | Date/version | Narrow proposition | Status |
| --- | --- | --- | --- | --- |
| Constitution / case |  |  |  |  |
| Statute / regulation / ordinance |  |  |  |  |
| Agency policy |  |  |  |  |
| Facility sign / instruction |  |  |  |  |
| Enforcement practice |  |  |  |  |
| Exclusion / removal authority |  |  |  |  |
| Police / criminal authority |  |  |  |  |

## Current policy

- exact title/number:
- issuing body:
- adoption date:
- effective date:
- revision date:
- source URL / record:
- exact area covered:
- exact activity covered:
- exceptions:
- stated authority:
- superseded versions:

Do not treat a policy as law merely because it is written or posted.

## Signage and implementation

For each relevant sign:

- exact wording:
- exact location:
- date photographed/verified:
- photo/source:
- policy or authority referenced:
- whether sign predates/postdates relevant incidents:

## CPRA / public-record research

### Pre-visit requests

| Date | Request | Agency response | Records produced | Exemptions / issues | Follow-up |
| --- | --- | --- | --- | --- | --- |

Potential record categories:

- recording/photography policy;
- visitor and security policy;
- training materials;
- policy adoption/revision records;
- signage authorization;
- complaints and incident records;
- CAD/dispatch;
- body-camera/video;
- trespass/exclusion records;
- security contract/post orders;
- retention schedules;
- policy-change records;
- deeds, parcel maps, right-of-way maps, easement or dedication records, and operating/control agreements when boundary questions remain.

Requesting a category does not imply every responsive record is disclosable.

## Historical enforcement / prior incidents

Search beyond completed arrests or prosecutions. A warning, cease order, exclusion threat, or other official action can matter if it caused protected or potentially protected activity to stop or materially change.

Suggested search terms, tailored to the facility: `leafleting`, `handbill`, `petition`, `solicitation`, `filming`, `photography`, `recording`, `First Amendment`, `free speech`, `trespass`, `removal`, `suspension`, `patron conduct`, `disturbance`, `harassment`, `protest`, `demonstration`.

For each incident or chilling/compliance event:

- event_id:
- date / time period:
- event type:
- source(s):
- original/unedited source available:
- exact area:
- Registry subarea_id(s), if applicable:
- activity:
- visitor conduct:
- government conduct:
- policy / rule cited:
- police/security response:
- exclusion/removal authority cited:
- offense/detention/arrest authority cited:
- whether activity stopped or materially changed:
- disposition/outcome:
- records later obtained:
- law controlling at the time:
- later legal/policy change, if any:
- historical legal assessment:
- legal conclusion, if any, from a court:
- current relevance:
- unresolved factual disputes:

Historical legal assessment values:

- ADJUDICATED_UNLAWFUL
- APPARENTLY_INCONSISTENT_WITH_THEN_CONTROLLING_LAW
- CONSTITUTIONALLY_SUSPECT_NEEDS_RECORDS
- LATER_LAW_CHANGED_OR_CLARIFIED
- LAWFUL_OR_DISTINGUISHABLE
- UNRESOLVED

Keep incident evidence separate from legal authority. Except for an actual adjudication, do not describe a project historical assessment as a judicial finding.

### Rights-Risk Signal

If the record supports one, assign a scoped signal:

- NONE
- POSSIBLE
- DOCUMENTED
- ADJUDICATED

Record:

- signal_id:
- signal:
- activity:
- Registry subarea_id(s), if applicable:
- exact area/activity/policy scope:
- time period reviewed:
- linked event_id(s):
- evidence supporting signal:
- current legal assessment:
- last reviewed:

**DOCUMENTED** means reliable evidence of a relevant adverse enforcement or chilling event; it does **not** mean the government action has been adjudicated unlawful.

## Research flags

Check only those supported by the current record:

- [ ] SUPPORTED-BY-IDENTIFIED-AUTHORITY
- [ ] AUTHORITY-UNRESOLVED
- [ ] POTENTIAL-FACIAL-CONFLICT
- [ ] POTENTIAL-AS-APPLIED-CONFLICT
- [ ] POTENTIAL-VIEWPOINT-COMPARATOR
- [ ] POLICY-TO-CRIMINAL-AUTHORITY-GAP
- [ ] SUPERSEDED-OR-REVISED

Explain each selected flag.

## Field-verification plan

- specific question being tested:
- exact area:
- planned activity and asserted legal basis:
- expected policy:
- conduct deliberately excluded under the standing scenario:
- facts that would confirm/refute the hypothesis:
- records/evidence to preserve:
- stopping condition / closing time / access boundary:

## Field visit

### Timeline

| Time | Event | Exact statement/action | Source |
| --- | --- | --- | --- |

### Policy statements

Record the exact policy/rule identified by staff.

### Claimed legal authority

Record statutes, ordinances, regulations, cases, orders, signs, or policies actually cited.

### Comparator evidence

Document materially comparable conduct:

- favorable expression:
- unfavorable expression:
- recording/non-recording visitors:
- different visitors receiving different access treatment:
- warnings/removal:
- relevant differences that may explain the treatment:

Do not assume two situations are comparable merely because they look similar.

### Police/security encounter

- consensual contact or detention:
- time seizure/detention began:
- reason for stop stated:
- when the reason was stated relative to questioning:
- Vehicle Code § 2806.5 exception claimed, if any:
- offense articulated:
- facts articulated:
- removal authority articulated:
- policy treated as policy or as crime:
- warning:
- order:
- citation/arrest:
- final disposition:

## Post-visit records

| Date requested | Record | Result | Source | Notes |
| --- | --- | --- | --- | --- |

## Findings

Separate the following:

### Verified facts

### Official policy

### Controlling law

### Legal analysis

### Unresolved questions

### Corrections / later developments

## Publication note

If this investigation is published, link the primary records and original source material where lawful and appropriate, avoid unnecessary identification of uninvolved private individuals, and clearly distinguish allegations, observed facts, agency explanations, and adjudicated legal conclusions.
