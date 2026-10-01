---
title: California Public Facility 1A Registry Methodology
jurisdiction: California
last_verified: 2026-09-30
status: project-methodology
---

# California Public Facility 1A Registry

**Working methodology v0.6**  
**Status:** Working project methodology; initial pilot validation complete  
**Last revised:** September 30, 2026

## 1. Purpose

The California Public Facility 1A Registry is a research and accountability index for publicly accessible government facilities in California.

Its purpose is to document and organize:

- publicly available facility information;
- official agency policies, regulations, rules, and posted notices;
- applicable constitutional provisions, statutes, regulations, and case law;
- documented field observations made during peaceful First Amendment activity;
- public-records responses and other official follow-up materials;
- later corrections, policy changes, or agency responses.

The Registry is intended to help readers understand how government facilities state and apply rules affecting peaceful observation, photography, recording, speech, petitioning, access, and related First Amendment activity.

The Registry is **not a target list** and must not be used to direct, organize, or encourage harassment, confrontation, disruption, or coordinated pressure against a facility, public employee, or private person.

A facility listing is not an instruction or request for anyone to visit, contact, confront, or audit that facility.

### Relationship to the Field Guide and facility methodology

The project now separates three functions:

1. **Field Guide** — researches and explains generally applicable constitutional provisions, statutes, regulations, cases, and field rules.
2. **Facility Research and Field Verification** — defines the investigation workflow, authority chain, source collection, field verification, police-policy transition, and post-visit records process.
3. **Registry** — stores and publishes facility-specific facts, area-by-area access conditions, policies, signage, evidence history, research flags, and later corrections.

The canonical factual baseline is [NC-STANDING-01 v1](../../national-core/standing-scenario.md). California-specific legal mappings live in the [California Standing Scenario Overlay](../standing-scenario.md). The canonical facility-research workflow is [Facility Research and Field Verification](../facility-investigation-methodology.md).

Registry entries should consume those two documents rather than recreate them. A facility page should link to applicable Field Guide authorities and record only the facility-specific facts and analysis needed to apply those authorities.

## 2. Standing scenario

The Registry uses the project's canonical [NC-STANDING-01 v1](../../national-core/standing-scenario.md) factual baseline and then applies the [California Standing Scenario Overlay](../standing-scenario.md).

Do not maintain a second, shorter list of baseline assumptions here. If the national standing scenario changes, the Registry inherits the factual change through the canonical document; California-specific law remains in the overlay.

A facility entry may document an incident that materially departs from the standing scenario, but it must identify the changed fact rather than silently treating the incident as equivalent to the baseline.

The Registry also does not assume that an entire building, floor, or agency office has one access or forum status. Entries should identify the **specific area and activity** being analyzed.

## 3. Unit of evaluation

The Registry evaluates **government institutions, facilities, published rules, and documented government conduct**.

The Registry does not grade individual employees.

Individual public employees may be identified in factual source material when relevant to an official action, report, policy, or public proceeding, but the Registry should avoid unnecessary personal profiling and should not publish private contact information, home information, personal schedules, family information, or other nonpublic personal details.

The objective is institutional accountability, not personal humiliation.

## 4. Facility universe and inclusion

The long-term goal is to identify the broad population of California government facilities to which this work may apply, using public and official sources where practical.

The Registry should not be built only from controversial encounters, viral videos, or facilities thought likely to produce conflict. A statewide or category-based facility directory may include facilities before any policy research or field observation has occurred.

Potential directory sources may include:

- state-agency facility lists;
- county and municipal directories;
- court directories;
- public-school, college, and university directories;
- special-district directories;
- transit and airport authority directories;
- federal agency and USPS facility locators;
- official GIS and open-data sources.

A federal facility physically located in California may be catalogued in the statewide directory for location and cross-reference purposes, but its substantive legal analysis belongs in the project's federal-premises track. California statutes, CPRA, and California facility rules must not be assumed to govern merely because the property is geographically in California.

A neutral facility directory may therefore contain many Gray entries awaiting research alongside Green, Yellow, and Red entries. Inclusion in the directory does not imply concern, suspicion, or a recommendation that anyone visit the facility.

The project should document how facility populations were assembled so claims of directory completeness can be audited and improved over time.

## 5. Source-first research

Each facility page should begin with documentary research before any field observation is evaluated.

Relevant public information may include:

- official facility name and agency;
- official address and public hours;
- official facility or agency webpage;
- published visitor and security rules;
- published photography or recording policies;
- posted notices and signs visible to the public;
- public-meeting rules;
- agency administrative manuals or directives;
- applicable local ordinances;
- California statutes and regulations;
- federal statutes and regulations where applicable;
- controlling and relevant persuasive case law;
- public parcel, right-of-way, GIS, mapping, or other official geographic information when relevant to determining public property boundaries or access;
- CPRA, FOIA, or other official records obtained after research or a field observation.

### Property / boundary evidence

When a facility's constitutional or access analysis depends materially on where one property regime ends and another begins, the Registry entry should maintain a **Property / Boundary Evidence** record rather than rely on an unlabeled map image or visual impression.

The record should identify, when available:

- parcel/APN or equivalent identifier;
- record owner;
- operational controller if separately established;
- relevant public right-of-way, easement, lease, or joint-use information;
- the exact sidewalk, plaza, parking lot, approach, driveway, or other area affected;
- the official source and direct link;
- map/layer/document name and date or version;
- retrieval or verification date;
- what the source actually establishes;
- material limitations or unresolved conflicts; and
- boundary confidence: **VERIFIED**, **PARTIALLY-VERIFIED**, or **UNRESOLVED**.

A live official source should be linked when available. When the material source is an interactive GIS viewer or other dynamic map, preserve an export, PDF, or screenshot when practical so the project can later show the view actually relied upon. Record enough information to reproduce the result, such as layer name, parcel/APN, selected feature, and retrieval date.

When boundary evidence materially affects an entry, maintain a facility-specific evidence manifest. The current project convention is `docs/research/evidence/<facility-slug>/README.md`, with preserved exports/screenshots stored beside the manifest when practical. This keeps live-source links, preserved evidence, retrieval dates, and limitations tied to the specific facility rather than scattered through the handbook.

Do not collapse **ownership**, **operational control**, **public access**, **right-of-way status**, and **forum classification** into one fact. They can point in different directions and may require different sources. GIS and assessor maps are evidence, not automatic legal conclusions about every easement, lease, right-of-way, or constitutional classification.

### Anchor-case comparator

For a material forum classification, the Registry should identify the best **area-and-activity-specific anchor authority** available rather than infer a result from the facility category alone.

A useful comparison records:

- the exact area and expressive activity being analyzed;
- the anchor case or authority and whether it is binding or persuasive;
- the classification actually reached in that authority;
- the factual considerations that materially drove the classification;
- similarities and differences between the precedent and the local facility area;
- unresolved facts that could change the comparison;
- the resulting classification and confidence level; and
- any separate doctrine still required for the specific activity, such as recording, solicitation, leafleting, or removal/trespass.

Different areas at one address may require different anchors. The project should not turn an anchor case into a facility-wide categorical rule. If no sufficiently analogous case exists, apply general forum doctrine directly and state that no closer anchor authority was located.

Forum classification and activity-specific rights remain separate. For example, a leafleting case may strongly support the forum status of an exterior area without independently deciding whether a particular recording restriction there is lawful.

The canonical working method is maintained in `docs/research/FACILITY-PREP-SOP.md`.

Every substantive legal authority or facility policy relied on by the Registry should have a direct source link when a stable public source is available and a `last_verified` date.

Primary sources are preferred. Secondary sources may be used for explanation or research leads but should not replace primary authority when primary authority is available.

A statement such as `no supporting authority located as of [date]` means only that the project's documented research did not locate supporting authority by that date. Failure to locate supporting authority is not, by itself, proof that no such authority exists.

### Source preservation and link rot

Important facility-specific source material should be preserved well enough that later readers can determine what the project actually reviewed, even if an agency later changes or removes the online material.

Where practical and legally appropriate, an entry should record:

- source URL;
- retrieval or observation date;
- document title, version, revision date, or other identifying metadata;
- a preserved copy or archived reference when appropriate;
- a photograph of physical signage when signage is material;
- an optional SHA-256 hash for a preserved file when useful for later comparison.

The project should distinguish a preserved historical source from the agency's current policy. A later policy change should update the current record without erasing the historical evidence.

## 6. Registry status system

Color/status labels describe the state of the evidence. They are not judicial determinations. Public presentation must always display the text label and scope; color alone must never carry the status meaning.

### Status scope rule

A status is assigned to a **defined area, policy, activity, or incident**, not automatically to an entire street address, building, agency, or institution.

A single facility page may therefore contain multiple concurrent statuses. For example, one public lobby may have an unresolved recording-policy question while a separately controlled classroom, sidewalk, or meeting room has a different status.

Every non-Gray status should identify its scope clearly enough that a reader can tell **what was actually researched or tested**. A successful encounter in one area does not clear every policy or space at the facility, and an adverse encounter in one area does not establish that every operation at the facility is problematic.

### Gray — unresearched, incomplete, stale, or unresolved

Use Gray when:

- facility research has not yet been completed;
- available information is insufficient to evaluate a concern;
- a prior entry has become stale and requires reverification;
- material facts or governing law remain genuinely unresolved.

Gray does not imply either compliance or noncompliance.

### Green — no material concern identified or satisfactory documented response

Use Green when, based on the evidence reviewed:

- no material conflict between published policy and governing authority has been identified; or
- a field observation in the **identified area and activity** occurred without material adverse government action affecting the protected activity; or
- a previously identified concern was satisfactorily clarified or corrected.

Green does not mean a facility has been comprehensively tested for every possible constitutional issue, area, or activity.

Positive outcomes should receive meaningful visibility. The Registry may highlight facilities with clear policies, accurate legal guidance, professional handling of peaceful protected activity, transparent records practices, constructive corrections, or other exemplary performance under a future published rubric.

### Yellow — pre-field policy or legal concern

Use Yellow when public research identifies a specific, documented question that merits clarification or further verification.

Examples may include:

- an official rule or sign that appears broader than governing authority may permit;
- conflicting agency policies;
- a public-facing rule for which no supporting authority has yet been located;
- an unresolved distinction between statewide law and local/facility practice.

A Yellow status must identify:

1. the exact policy, sign, rule, or public information creating the concern;
2. the source for that material;
3. the legal authorities relevant to the concern;
4. the precise unresolved question.

Yellow must **not** be described as proof that a facility is violating the Constitution or law.

Yellow means: **a documented question exists.**

It does not mean: **go confront this facility.**

### Red — documented adverse government action

Use Red only when reliable evidence documents a material adverse government action **materially connected to the peaceful constitutional activity or facility-access issue being evaluated**.

Examples may include:

- removal from a public area;
- detention;
- arrest;
- search;
- seizure of a recording device or other property;
- an order to cease protected activity;
- a formal exclusion or trespass action;
- other official coercive action materially affecting the activity.

An unrelated event, such as a general evacuation that affects everyone equally and is not connected to the protected activity, should not create Red status merely because it interrupted an audit.

A Red status describes what the government **did**. It does not, by itself, declare that a court has determined the action unconstitutional or unlawful.

The legal-analysis section should use appropriately precise language such as:

- `appears inconsistent with [authority]`;
- `raises a substantial First Amendment question`;
- `raises a Fourth Amendment detention issue`;
- `agency has not identified supporting authority`;
- `legal status remains disputed`;
- `court later held the conduct unconstitutional`, when a court actually did so.

The Registry should reserve categorical statements such as `unconstitutional`, `unlawful`, or `violated the First Amendment` for situations where the underlying authority and procedural posture support that characterization.

### Current status and status history

Current status should not erase significant historical events.

A scoped issue may improve from Yellow or Red to Green after clarification or corrective action while retaining a visible status history, for example:

- `2026-09-16 — RED: documented removal during peaceful recording.`
- `2026-10-12 — agency reports outdated sign removed and policy corrected.`
- `2026-10-15 — GREEN: correction independently verified.`

Similarly, a currently stale issue may be Gray while retaining a historical Red or Yellow event. The project should distinguish each issue's **current scoped status** from its **status history**.

### Rights-Risk Signal — separate from Registry color/status

The Registry may maintain a second, explicitly scoped **Rights-Risk Signal** describing the evidentiary state of possible historical or current burdens on protected activity.

This signal is **not** a score, grade, blacklist, or substitute for the Gray/Green/Yellow/Red status system. It answers a different question:

> **How much reliable evidence currently exists that this area/activity has been subject to a potentially unlawful government restriction or enforcement practice?**

Allowed values:

- **NONE** — the completed review located no material rights-risk for the stated scope and period. This is not a guarantee that no historical event exists.
- **POSSIBLE** — a policy, historical report, or partial record raises a concrete issue, but the evidence is not yet sufficient to document the relevant adverse enforcement or chilling event.
- **DOCUMENTED** — reliable evidence documents a material warning, coercive action, enforcement event, or chilling/compliance event involving protected or potentially protected activity. This label **does not mean a court has found the action unlawful**.
- **ADJUDICATED** — a court or competent tribunal actually held the relevant challenged policy or enforcement unlawful on the issue represented by the signal.

Every signal must state:

- a stable facility-local signal ID;
- the canonical activity being evaluated;
- the exact area/activity or policy scope;
- exact subarea IDs when the signal is tied to defined Registry subareas;
- the time period reviewed;
- linked enforcement-history event IDs;
- the evidence on which the signal rests;
- the current legal assessment; and
- the date last reviewed.

A **DOCUMENTED** or **ADJUDICATED** signal must link to the underlying enforcement-history event(s). An **ADJUDICATED** signal must link to an event whose historical assessment is **ADJUDICATED_UNLAWFUL**.

A facility may have multiple scoped signals. Do not assign one facility-wide **DOCUMENTED** or **ADJUDICATED** label merely because one subarea or historical policy had a problem.

### Historical enforcement event assessment

Historical events should retain their own legal-assessment field rather than inherit the facility's current policy status.

Use:

- **ADJUDICATED_UNLAWFUL**
- **APPARENTLY_INCONSISTENT_WITH_THEN_CONTROLLING_LAW**
- **CONSTITUTIONALLY_SUSPECT_NEEDS_RECORDS**
- **LATER_LAW_CHANGED_OR_CLARIFIED**
- **LAWFUL_OR_DISTINGUISHABLE**
- **UNRESOLVED**

These classifications must be date-sensitive. A modern rule cannot silently be projected backward, and a later correction does not erase the historical event.

### Mature enforcement-history output

Where evidence exists, a mature Registry entry should make the following layers separately visible:

1. **Current law** — the presently governing constitutional/statutory/case framework.
2. **Current policy** — what the agency presently says.
3. **Policy gap** — any documented mismatch or unresolved authority question.
4. **Enforcement history** — warnings, removals, exclusions, police action, citations, arrests, prosecutions, or comparable official action.
5. **Chilling history** — documented cases where an official warning or threat caused activity to stop or materially change without an arrest or prosecution.
6. **Litigation history** — claims, suits, injunctions, adjudications, appeals, and relevant dispositions.
7. **Remedial history** — policy corrections, withdrawn signs, training changes, settlements, or other documented responses.
8. **Open rights-risk** — unresolved current or historical issue requiring more evidence or legal analysis.

This structure is intended to surface possible unknown rights violations without converting every historical dispute into a conclusion of illegality.

## 7. Status is evidence-based, not emotion-based

An area, policy, activity, or incident must not receive a Yellow or Red status because an encounter was unpleasant, rude, embarrassing, or unpopular.

The status should be traceable to source material and the published methodology.

Similarly, a scoped issue should not receive Green merely because an auditor personally liked the employees.

The Registry evaluates documented rules and conduct, not personalities.

## 8. No future-audit scheduling or targeting

The public Registry should not publish:

- planned audit dates or times;
- instructions to converge on a facility;
- calls for followers to contact or confront employees;
- predictions about which location is likely to generate conflict;
- rankings such as `best place to get arrested`, `easy target`, or similar language;
- employee work schedules for the purpose of timing an encounter;
- nonpublic security vulnerabilities or access-control information.

`Follow-up needed` should mean that additional documentary research, policy clarification, records responses, or independently obtained observations would improve the record.

It should not mean that people are being asked to descend on the facility.

## 9. Pre-field research and intent

Facility research follows [Facility Research and Field Verification](../facility-investigation-methodology.md).

A Registry entry may begin and remain **desk-research only**. Active field verification is not required merely because a policy question exists.

Pre-field work may establish:

- the agency and property-control structure;
- exact public-facing areas and ordinary access conditions;
- published hours and visitor procedures;
- written policies and posted signs;
- the authority the agency claims supports a restriction;
- relevant constitutional, statutory, regulatory, and case-law questions;
- prior enforcement history;
- CPRA/FOIA research targets;
- unresolved questions that require records or later verification.

The entry should distinguish a documented question from a legal conclusion. If a field visit would create an avoidable conflict of interest, safety problem, privacy concern, employment complication, or other methodological problem, the Registry may expressly omit active testing and continue with documentary research.

### Researcher relationship or conflict

When a researcher has an employment, tenancy, contractual, family, or other relationship that could materially affect the investigation, the project should record that limitation internally.

The public entry should not rely on confidential, privileged, or nonpublic information available only because of that relationship. Firsthand observations may be used as evidence, but material public claims should be corroborated with public or official sources where practical.

The existence of a relationship does not automatically disqualify desk research. It may, however, make active field testing inappropriate. Public disclosure of the relationship should be made when it is materially necessary to understand the evidence or potential bias, rather than as an automatic requirement for every entry.

If field verification later occurs, it should test a defined question under the standing scenario rather than manufacture misconduct or confrontation.

## 10. Evidence standard for field observations

A Red or other adverse field status should not be based solely on a contributor's characterization of events.

Where reasonably available, the Registry should seek to preserve or link:

- original video or audio recorded by the auditor;
- an unedited or substantially complete version sufficient to evaluate context;
- photographs of relevant signs or barriers;
- date, approximate time, and exact public location;
- police body-worn camera footage;
- dispatch/CAD records;
- 911 or nonemergency call recordings;
- incident or arrest reports;
- written exclusion or trespass notices;
- facility surveillance footage when lawfully obtainable;
- agency emails, messages, directives, or reports obtained through CPRA/FOIA;
- applicable policies and training materials;
- later agency correspondence.

Edited videos may be used for public presentation, but material legal conclusions should not depend on edits that omit context needed to evaluate the incident.

### Third-party submissions and incomplete recordings

Before assigning Red status based on a third-party audit or submission, a reviewer should determine whether the available evidence reasonably establishes the relevant facts from the canonical Standing Scenario during the material portion of the encounter.

A recording that begins only after the confrontation or omits material preceding events may still be useful evidence, but the project should not assume missing facts in either direction. When the available evidence is insufficient to apply the standard Registry methodology, the entry should remain Gray, pending, or otherwise expressly qualified rather than receiving an unsupported Red status.

## 11. Evidence integrity

When practical, significant original media should be preserved exactly as captured.

The project may record a cryptographic hash such as SHA-256 for an original file so a later copy can be compared against the preserved original.

A Registry entry may distinguish:

- `Original media preserved`;
- `Original-media hash`;
- `Public/edited version`;
- `Government-source media`;
- `Other supporting records`.

A hash verifies file identity. It does not independently prove that the recording is complete or that every factual interpretation of the recording is correct.

## 12. Separate fact, policy, and legal analysis

Each facility entry should clearly separate at least three layers.

### A. Official sources

What the government has published or officially produced.

Examples:

- rules;
- policies;
- official webpages;
- regulations;
- posted signs;
- CPRA/FOIA responses.

### B. Field observations

What was actually documented.

Use neutral chronological descriptions where possible.

Example:

> At 2:14 p.m., an employee approached the auditor and stated that recording was not allowed in the lobby. At 2:18 p.m., the employee contacted law enforcement. At 2:31 p.m., an officer stated that the auditor would be arrested for trespass if the auditor did not leave.

Avoid converting observation into legal conclusion inside the factual chronology.

### C. Legal analysis

What statutes, regulations, cases, or constitutional provisions may mean for the documented conduct.

Legal analysis should identify uncertainty, contrary authority, forum-specific limitations, and procedural posture where relevant.

## 13. Terminology standards

Preferred language includes:

- `documented adverse action`;
- `policy concern`;
- `unresolved legal question`;
- `appears inconsistent with`;
- `no supporting authority located as of [date]`;
- `binding authority`;
- `persuasive authority`;
- `field observation`;
- `agency response`;
- `corrected after notice`.

Avoid unsupported or inflammatory labels such as:

- `tyrant`;
- `criminal agency`;
- `corrupt facility`;
- `constitutional violator`;
- `target`;
- `hit list`;
- `go audit these people`.

Quoting another person who used such language is different from adopting the language as the Registry's own characterization, but quotes should be included only when materially relevant.

## 14. Future rubric or report-card scores

Numerical scores and report-card grades are **not part of the current Registry methodology**.

The Registry may eventually use a published 1A Audit Rubric or report-card system if the scoring criteria are developed in a separate proposal, adopted before they are applied to facilities, and remain transparent and reproducible.

Any score or grade should be described as:

> the project's evaluation under its published rubric

and not as:

> a judicial determination of legal liability.

Potential rubric categories may include:

- clarity of public-access rules;
- published recording/photography policy;
- consistency between facility rules and higher authority;
- response to peaceful protected activity;
- de-escalation and professional handling;
- law-enforcement response, if applicable;
- accuracy of legal articulation;
- records transparency;
- willingness to correct erroneous policy or signage.

A category that was not actually tested should be marked `NOT TESTED` or otherwise excluded from the denominator rather than scored as zero.

High scores, exemplary practices, constructive corrections, and meaningful improvements should be eligible for the same public visibility as adverse findings. The Registry should not be designed so that only poor outcomes are noteworthy.

The final scoring rubric should be developed in a separate proposal before facility grades are published.

## 15. Public-information and privacy rule

The Registry may use pertinent information that a government agency has publicly posted or officially released.

However, the project should collect and publish only information reasonably relevant to the public-access, recording, speech, transparency, or accountability question being documented.

The fact that information is technically obtainable does not automatically make republishing it necessary.

The Registry should avoid unnecessary publication of:

- private citizens' personal information;
- private phone numbers or addresses;
- personal schedules unrelated to official public duties;
- children's identifying information;
- medical or similarly sensitive personal information;
- detailed nonpublic security information.

If private information is incidentally visible in footage, the public-facing version should ordinarily redact or blur it when the information does not advance the accountability purpose.

## 16. Maps, GIS, and property-boundary research

Official GIS, parcel, right-of-way, map, easement, and property records may be used when they materially help establish:

- whether a location is publicly owned;
- whether a sidewalk or plaza is within public right-of-way;
- facility boundaries;
- public entrances and ordinary public-access routes.

The Registry should cite the government source and date consulted.

Mapping evidence should not be overstated. A GIS layer may be strong evidence of a boundary without necessarily resolving every legal question concerning access, easements, forum classification, or temporary restrictions.

## 17. Agency response and correction process

The Registry should maintain a clear way for an agency to provide:

- updated policies;
- corrections to factual statements;
- explanations of a rule;
- evidence that signage or policy has changed;
- relevant legal authority the project overlooked.

When practical, before publishing a materially adverse facility-specific factual claim or disputed legal characterization that depends on unresolved facts, the project should seek the agency's position. That is a source-quality practice, not an entitlement to prepublication review.

No separate contact is required merely to reproduce or analyze an agency's own published policy, public record, sign, court filing, or other sufficiently authenticated source.

An agency response should be evaluated under the same source standards as any other submission. The agency does not receive editorial control over the entry.

Valid corrections should be incorporated promptly and transparently through Git history.

The project should not erase prior history merely because a rule changed.

Example:

- `2026-09-10 — No-recording sign documented.`
- `2026-10-12 — Agency states sign was obsolete and has been removed.`
- `2026-10-15 — Removal independently verified.`

A scoped issue's current status or any future rubric treatment may improve when an agency corrects a problem, while the historical record remains visible.

## 18. Corrections when the project is wrong

The same standard applies to the project itself.

If later research shows that a status assignment or accompanying legal analysis was mistaken, incomplete, or overstated, the Registry should:

1. correct the entry;
2. cite the newly discovered authority or evidence;
3. explain the material change when appropriate;
4. preserve the correction history in Git;
5. change the affected scoped status if warranted.

The Registry's credibility depends on being willing to document when the government's interpretation was correct and the project's earlier interpretation was not.

## 19. Facility-entry schema

The detailed investigation worksheet is maintained in `docs/templates/facility-investigation-template.md`. The Registry should not maintain a competing investigative template.

A mature public Registry entry should contain, at minimum:

```text
Facility:
Agency:
Jurisdiction:
Facility type:
Official address:
Official website:
Last verified:
Research stage:
Current Registry status(es):
Status scope(s):
Status history:
Research flags:

AREA-BY-AREA ACCESS
- Area:
- Controlling/occupying entity:
- Public hours:
- Ordinary public-access condition:
- Access source / confidence:
- Check-in / badge / ID condition:
- Restricted boundary:
- Activity analyzed:
- Forum classification:
- Classification status / uncertainty:
- Anchor authority:
- Anchor authority binding level:
- Comparator similarities / differences:

POLICY AND IMPLEMENTATION
- Current written policy:
- Policy source / version:
- Posted signage:
- Exact wording:
- Sign location / scope:
- Claimed authority:
- Exclusion / removal authority:
- Separate police / criminal authority:

OFFICIAL SOURCES
- Agency/facility pages:
- Lease/property/control sources:
- Maps/GIS/floor plans:
- Policy/adoption sources:
- Retrieval dates:
- Preserved/archive references:

EVIDENCE HISTORY
- Passive observations:
- Field verification, if any:
- Prior incidents:
- Police/security involvement:
- Warnings / cease orders:
- Suspensions / trespass notices:
- Citations / arrests / prosecutions:
- Chilling / compliance events:
- Litigation / claims / injunctions:
- Post-visit records:
- Agency response:
- Corrections / policy changes:

RIGHTS-RISK / HISTORICAL ASSESSMENT
- Rights-Risk Signal:
- Signal scope:
- Time period reviewed:
- Historical event assessment(s):
- Then-controlling law:
- Current relevance:
- Evidence still needed:

LEGAL ANALYSIS
- Applicable Field Guide chapters:
- Controlling authority:
- Material factual predicates:
- Application:
- Limits / contrary authority:
- Unresolved questions:
- Methodological limitations / conflicts:

EVIDENCE INTEGRITY
- Original media preserved:
- Hash, if used:
- Public/redacted version:
```

A single street address may require several area records. Public ownership, leasehold control, ordinary public access, purpose-limited access, forum classification, and criminal trespass authority are separate fields and should not be collapsed into one label.

## 20. Proposed public Registry notice

A public Registry index may display concise language substantially similar to the following:

> ### About the Registry
>
> The California Public Facility 1A Registry documents how public facilities publish and apply rules affecting peaceful First Amendment activity. Statuses are scoped to identified areas, policies, activities, or incidents; they reflect documented evidence under a published methodology and are not judicial findings. Facility listings are not requests or instructions for anyone to visit, contact, confront, or audit a particular agency or employee.

The public Registry should also make favorable findings, high scores, verified improvements, and exemplary practices reasonably discoverable rather than presenting only adverse findings.

## 21. Working status

An initial mixed-use, leased-facility pilot has been used internally to test this methodology. The pilot demonstrated that the Registry needs:

- area-by-area rather than address-wide classification;
- separate treatment of common areas, public service areas, purpose-limited rooms, and restricted workspaces;
- separate property/control, public-access, forum, removal, and criminal-authority fields;
- a way to record posted restrictions whose source authority remains unresolved;
- a desk-research-only path when active field testing would be methodologically inappropriate;
- scoped statuses rather than one blanket color for an entire facility.

The pilot record itself is not required to preserve those methodological lessons and may be discarded after review.

The methodology is now suitable for controlled Registry population, but it remains a working project standard. Real entries may expose additional schema problems, which should be corrected transparently before large-scale population.

The project may publish evidence-status labels and research flags before a numerical rubric exists, but it should not publish report-card grades or numeric scores until a separate scoring methodology has been adopted and tested.