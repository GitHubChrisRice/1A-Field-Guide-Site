---
title: Sweep 009 — Concord DMV Field Office
jurisdiction: California
last_verified: 2026-09-22
status: documentary-research-developed
---

# Sweep 009 — Concord DMV Field Office

## Scope

Sweep 009 is the first deliberate **cross-category Facility Prep validation** after the Concord and Walnut Creek public-library tests.

**Facility:** California Department of Motor Vehicles — Concord Field Office  
**Agency:** California Department of Motor Vehicles  
**Address:** 2070 Diamond Boulevard, Concord, California 94520  
**Research mode:** documentary / pre-field  
**Field observation:** none yet

Official DMV field-office page:

https://www.dmv.ca.gov/portal/field-office/concord/

As reviewed September 22, 2026, DMV identifies the Concord Field Office at 2070 Diamond Boulevard and lists ordinary office hours Monday–Tuesday and Thursday–Friday 8 a.m.–5 p.m., Wednesday 9 a.m.–5 p.m., Saturday–Sunday closed. The office also has a self-service kiosk.

No facility-wide forum classification is assigned. Sweep 009 follows the project's **facility → specific area/activity** rule and separately analyzes municipal sidewalk/ROW, facility approaches, customer parking, exterior queueing, entrance threshold, lobby/waiting space, transaction counters, knowledge-test areas, kiosk space, and employee/restricted areas.

Canonical evidence manifest:

`docs/research/evidence/concord-dmv/README.md`

---

# 1. Why DMV is the cross-category test

Concord DMV changes the governmental purpose while preserving enough geography to test which parts of Facility Prep genuinely generalized.

Useful constants:

- Contra Costa County parcel/assessor sources remain available;
- Concord municipal GIS/ROW sources can be reused where their actual geographic coverage fits;
- the same recorded-map custodian and adapters remain available.

Material changes:

- the operating agency is a California state administrative agency rather than a county library;
- the facility exists to conduct transactions, examinations, records work, licensing and related administrative services;
- the interior contains more purpose-limited customer zones;
- privacy and examination-integrity interests are materially different;
- the closest legal comparators are no longer the library cases.

The test therefore asks whether the project generalized **evidence methods** rather than library assumptions.

---

# 2. Current facility facts

Official DMV page:

https://www.dmv.ca.gov/portal/field-office/concord/

Current public facts reviewed include:

- address `2070 Diamond Boulevard, Concord, CA 94520`;
- ordinary weekday public hours;
- self-service kiosk;
- driver-license/ID, testing, registration/title and related field-office services.

A current DMV facilities/equipment list independently identifies the Concord office at the same address as **State Owned**.

That source, together with current parcel evidence below, makes a privately leased storefront characterization unsupported on the present record.

---

# 3. Facility Prep parcel result

The countywide Contra Costa parcel adapter successfully transferred from Walnut Creek Library to a State-owned DMV facility without code changes.

Official GIS resolves:

- APN `126-490-004`;
- raw APN `126490004`;
- display address `2070 DIAMOND BLVD - CONCORD`;
- owner field `CALIFORNIA STATE OF`;
- second owner/name field `DEPT MOTOR VEHICLES`;
- tract `5292`;
- Assessor Book 126 Page 49.

The record also returns `full_n_address = 2415 1ST AVE MSA156`. That value is preserved as source output but is not substituted for the facility's public address.

Current ownership posture:

`STATE-OWNERSHIP-STRONGLY-SUPPORTED / DMV-OPERATION-VERIFIED`

Reviewed machine evidence:

- `docs/research/evidence/concord-dmv/facility-prep-2026-09-22/report.json`
- `docs/research/evidence/concord-dmv/facility-prep-2026-09-22/parcel.geojson`

---

# 4. Assessor map and the address/frontage problem

Official assessor PDF:

https://ccmap.cccounty.us/HTML5/assessorPDF/126p49x0.pdf

SHA-256:

`d3e6dc5d5f889a5d8ab368c554c1b41d3573e68acc5e539be30584637a3e426c`

The image-only assessor sheet was visually reviewed.

Book 126 Page 49 depicts:

- `TRACT 5292 (WILLOWICK 4) MB 212-47`;
- parcel `04`, approximately 3.49 acres;
- Diamond Boulevard to the west;
- Meridian Park Boulevard to the east;
- Galaxy Way to the north;
- parcel `01` between parcel `04` and Diamond Boulevard;
- parcel `03` south of parcel `04`;
- parcel `05` north/northeast of parcel `04`.

The significant finding is that DMV and current GIS use **2070 Diamond Boulevard**, but the State/DMV parcel does **not** appear to directly front Diamond Boulevard on the assessor sheet. Parcel 01 lies between them.

Status:

`ADDRESS/FRONTAGE-MISMATCH / ACCESS-PATH-AND-EASEMENT-REVIEW-REQUIRED`

The public address cannot be used as proof that the entire approach from Diamond is State property, municipal ROW, or a particular easement.

Detailed review:

`docs/research/evidence/concord-dmv/assessor-map-review-2026-09-22.md`

---

# 5. Candidate adjacent parcels

The official GIS intersection query returned four non-target candidates:

- `126-490-001` — 2090 Diamond Boulevard — `FLATIRONS STANWELL LLC`;
- `126-490-002` — 2050 Diamond Boulevard — `LEE JOHN S & HELEN Y TRE` / `NORTHS RESTAURANT INC`;
- `126-490-003` — 2055 Meridian Park Boulevard — `CONCORD FK PROPERTY LLC` / `FK CONTINENTAL LLC`;
- `126-490-005` — 2080 Diamond Boulevard — `EDSTAR ENTERPRISES` / `PAULA DOUGHERTY GP`.

These remain candidate-discovery results rather than automatic legal adjacency/control findings.

Parcel 01 is materially relevant because both the assessor sheet and recorded subdivision map place it between the DMV parcel and Diamond Boulevard.

---

# 6. Recorded subdivision map — Willowick 4 / 212M47

The assessor sheet supplied an exact historical reference:

`TRACT 5292 (WILLOWICK 4) MB 212-47`

Contra Costa Public Works Recorded Maps independently resolved:

- `212M47`;
- entry ID `148419`;
- record type `Subdivision Map`;
- subdivision `WILLOWICK #4`;
- recorded June 28, 1978;
- permit `SD78-05292`;
- three imaged pages.

All three pages were retrieved through the ordinary anonymous public Laserfiche viewer and reviewed.

Rendered-page SHA-256 values:

- page 1: `35f880e041169a10c50f57a4a0b9c1d2b351b1cfeeb436fa1cd326eef24261fa`;
- page 2: `fc8ccc28aee88090faf4d7d7f70c0bb034558d326629c35387913057dafbbd10`;
- page 3: `4295d6b30b218d6ad276c50cfdcafd049883ee866b4b8601aa77555e5427178a`.

## Ownership / dedication certificate

The owner's certificate identifies the original subdivision owner and offers the portions designated as **Meridian Park Blvd** for public use. It also references easements shown on the premises or of record.

## City certificate

The City Clerk's certificate records Concord City Council approval of the final map in 1978 while stating that the City did not at that time accept or reject on behalf of the public the streets/easements shown as dedicated.

The project therefore keeps the **dedication offer** and the **City's contemporaneous acceptance posture** separate.

Current Concord Road Centerlines independently identifies Meridian Park Boulevard as Concord-owned/jurisdictional today.

## Lot geometry

The subdivision drawing shows five lots and materially corresponds to the modern parcel arrangement.

Historical Lot 4:

- approximately 3.49 net acres;
- occupies the large central/eastern tract area;
- directly fronts Meridian Park Boulevard;
- is separated from Diamond Boulevard by Lots 1 and 2.

No labeled access easement carrying Lot 4 westward across Lot 1 to Diamond is apparent on the reviewed subdivision drawing.

That is a negative visual observation, **not** a title conclusion. A later easement, shared-access agreement, deed or site-plan arrangement could exist.

Current result:

`HISTORICAL-GEOMETRY-STRONGLY-SUPPORTED / MODERN-DIAMOND-ACCESS-RIGHT-UNRESOLVED`

Detailed review:

`docs/research/evidence/concord-dmv/recorded-map-212m47-review-2026-09-22.md`

---

# 7. Current road / sidewalk evidence

The existing Concord Road Centerlines adapter was reused because its geographic coverage includes this Concord facility. This is jurisdiction-specific reuse, not an assumption that the layer is statewide or countywide.

## Diamond Boulevard

Closest ranked segment:

- OBJECTID `226039`;
- street owner `Concord`;
- jurisdiction `Concord`;
- Major Arterial;
- right-side address range `2000–2098`;
- sidewalk L/R `No / Yes`;
- facility ID `TCL174239`;
- source update 2020-04-27.

## Meridian Park Boulevard

Closest ranked segment:

- OBJECTID `226244`;
- street owner `Concord`;
- jurisdiction `Concord`;
- Major Arterial;
- left-side address range `2033–2099`;
- sidewalk L/R `Yes / No`;
- facility ID `TCL174444`;
- source update 2020-04-27.

## Galaxy Way

Closest ranked segment:

- OBJECTID `226243`;
- street owner `Concord`;
- jurisdiction `Concord`;
- Collector;
- sidewalk L/R `No / Yes`;
- facility ID `TCL174443`;
- source update 2020-04-27.

Limits remain:

- centerline ≠ surveyed ROW edge;
- street-owner field ≠ complete title opinion;
- sidewalk-presence field ≠ sidewalk title;
- address range ≠ parcel frontage.

Detailed review:

`docs/research/evidence/concord-dmv/property-row-review-2026-09-22.md`

---

# 8. Public-facing camera-policy search

Current DMV public-facing facility, privacy, records, terms/use and testing sources were reviewed, with targeted searches for photography, video, filming, camera, recording, cell-phone and related field-office terms.

Approved finding:

> **No dedicated public-facing California DMV field-office ordinary-patron photography/videography rule was located in the online sources reviewed as of September 22, 2026.**

This is not proof that no internal, posted, branch-specific, examination-specific, privacy, security or later rule exists.

Do not shorten the finding to `DMV has no photography policy`.

Current physical-signage verification remains necessary.

Detailed review:

`docs/research/evidence/concord-dmv/policy-privacy-search-2026-09-22.md`

---

# 9. Privacy and purpose-limited DMV rules

DMV's current privacy materials identify substantial protections for personal information, including driver-license/ID numbers, Social Security numbers, photographs, medical/disability information, fingerprints/thumbprints and examination information.

Those interests are materially relevant when analyzing a specific restriction around counters, records or examinations.

They do **not** themselves create a general camera prohibition.

The proper chain is:

`DMV privacy duty → actual information exposed in the physical area → identified restriction → forum classification → constitutional/statutory analysis`

## Knowledge test

DMV's current California Driver's Handbook states that testing aids, including a **cell phone**, may not be used during a knowledge test.

Status:

`CURRENT-PUBLIC-RULE-VERIFIED / EXAMINATION-ACTIVITY-SPECIFIC`

This must not be generalized into a branch-wide no-phone or no-camera rule.

---

# 10. Federal interior forum analysis

No controlling Ninth Circuit or published California appellate decision specifically adjudicating ordinary-patron filming inside a California DMV field office was located.

## Published controlling framework

### Cornelius / Perry

The forum must be defined by the access sought, governmental intent and purpose. Public access to conduct government business does not itself establish a traditional/designated public forum.

### Sammartano v. First Judicial District Court

Published Ninth Circuit authority strongly supports the administrative-interior analogy.

The judicial/municipal complex there was treated as a **nonpublic forum** even though members of the public entered to conduct public business. Restrictions in such a forum still must be reasonable in light of the forum's purpose and viewpoint neutral.

## Close nonprecedential administrative-lobby comparator

*Freedom Foundation v. Washington Department of Ecology*, No. 20-35007 (9th Cir. Dec. 21, 2020), is an unpublished memorandum and is not binding precedent. Its facts are nevertheless useful: a state-agency lobby organized around reception/security, workspaces, seating and passage to secured areas was treated as nonpublic based on purpose, physical configuration and policy/practice.

It is retained only as a close factual comparator.

## DMV-specific persuasive cases

Recent out-of-circuit DMV cases, including *Martin v. North Carolina Division of Motor Vehicles*, provide additional persuasive context but do not control California.

The *Martin* court resolved the individual-capacity claim through qualified-immunity / clearly-established-law analysis and expressly did not need to decide the constitutionality of the particular restriction. It is therefore not represented as a merits holding validating every DMV camera ban.

## Working federal lobby classification

`FEDERAL NONPUBLIC-FORUM TREATMENT STRONGLY SUPPORTED`

This applies to the defined ordinary lobby/waiting channel, not every interior subarea by inheritance.

Detailed review:

`docs/research/evidence/concord-dmv/interior-forum-authority-review-2026-09-22.md`

---

# 11. California Speech Clause — interior

Federal classification is not automatically copied into California Constitution article I, § 2(a).

*Camenzind v. California Exposition & State Fair*, 84 F.4th 1102 (9th Cir. 2023), reinforces that federal and California forum analyses are separate and that current California classification can diverge for some exterior spaces.

No sufficiently close California appellate authority classifying an ordinary state administrative-service lobby like DMV was located in this review.

Current posture:

`CALIFORNIA SPEECH-CLAUSE CLASSIFICATION UNRESOLVED / NO CLOSE DMV OR ADMINISTRATIVE-LOBBY STATE AUTHORITY LOCATED`

That is an intentionally narrower result than simply labeling the lobby nonpublic under both systems.

---

# 12. Recording doctrine — Askins

*Askins v. U.S. Department of Homeland Security*, 899 F.3d 1035 (9th Cir. 2018), is the principal controlling recording authority added to this facility analysis.

It recognizes First Amendment protection for photography/recording of matters of public interest while making clear that the nature of the location and actual governmental restriction matter.

It does **not** establish an unfettered right to film every government interior.

Sweep 009 therefore preserves the sequence:

`forum/area classification → exact recording restriction → actual government justification → recording/privacy/security doctrine`

A nonpublic-forum label does not itself equal `recording prohibited`.

---

# 13. Exterior forum analysis

Canonical analysis:

`docs/research/evidence/concord-dmv/exterior-forum-analysis-2026-09-22.md`

| Area | Federal posture | California posture |
| --- | --- | --- |
| Actual ordinary Diamond municipal sidewalk / ROW | **TPF — HIGH CONFIDENCE once location established** | **Public-forum treatment — HIGH CONFIDENCE** |
| Actual ordinary Meridian Park municipal sidewalk / ROW | **TPF — HIGH CONFIDENCE once location established** | **Public-forum treatment — HIGH CONFIDENCE** |
| Facility-specific Diamond access drive/walk | **Nonpublic treatment strongly supported if purpose-built facility segment; footprint unresolved** | **UNRESOLVED** |
| DMV customer parking | **Nonpublic treatment strongly supported; current physical/use verification pending** | **UNRESOLVED; exterior state-law cases materially strengthen public-forum argument** |
| Exterior customer queue / immediate approach | **Nonpublic/purpose-limited treatment strongly supported; exact physical area pending** | **UNRESOLVED** |
| Entrance threshold | **SUBAREA-SPECIFIC / UNRESOLVED** | **UNRESOLVED** |
| Drive aisles / vehicle test routes / driveway throats | **No broad speech-zone conclusion; safety/compatibility interests dominate** | **Same practical caution** |

## Ordinary municipal sidewalks

*United States v. Grace* supplies the paradigmatic ordinary-sidewalk baseline.

The unresolved exact ROW edge remains important in a location-specific exclusion/trespass dispute, but does not prevent classification of a location independently established to be the ordinary municipal sidewalk.

## Purpose-built access route

*United States v. Kokinda* and Ninth Circuit *Jacobsen v. USPS* are substantially closer federal comparators than *Prigmore* for a special-purpose walkway/approach created to move customers between parking/access facilities and a government service building.

The Diamond approach cannot yet be given a final property-based classification because its current legal geometry is unresolved.

## Customer parking

The federal record strongly supports special-purpose/nonpublic treatment. Public customer access alone does not show intent to open the parking lot for public discourse.

The project does **not** import *Prigmore* merely because both a library and a DMV have public parking.

California is more difficult. *Camenzind* and earlier exterior-venue cases show broader state Speech Clause protection for some freely accessible parking/walkway areas. DMV's administrative purpose is materially different from fairgrounds/stadium-type venues, and no sufficiently close state authority was located. The California lot classification therefore remains unresolved.

---

# 14. Interior subarea matrix

| Area | Current documentary posture |
| --- | --- |
| Ordinary lobby / waiting | **Federal nonpublic-forum treatment strongly supported / California unresolved** |
| Customer service counters / transaction zones | **Purpose-limited; federal nonpublic analogy strong; privacy/rule application pending** |
| Knowledge-test stations | **Purpose-limited examination channel; cell-phone-as-testing-aid restriction verified** |
| Self-service kiosk area | **Public customer access verified; final area classification depends on physical placement** |
| Restroom access, if public | **Physical/access conditions not yet established** |
| Employee / records / equipment / secure areas | **Restricted / not ordinary public-access space** |

An ordinary patron's ability to enter a lobby or approach a counter does not establish a right to enter employee workspaces, records areas or marked restricted zones.

---

# 15. Removal / trespass posture

No Concord DMV enforcement incident is being analyzed.

Keep separate:

- public access;
- forum classification;
- exact facility rule;
- operational control;
- direction to leave;
- administrative exclusion;
- police detention/arrest;
- Penal Code trespass elements.

State ownership and DMV operation do not make any employee instruction automatically equivalent to a criminal trespass predicate.

The actual California Penal Code subsection, location, authority and elements would have to be identified for a concrete encounter.

The Diamond access-path mismatch makes this especially important: the controller may differ depending on whether the person's exact location is municipal ROW, a private parcel, an easement, a shared drive or State property.

---

# 16. Facility Prep cross-category validation

Sweep 009 validates the reusable property/evidence pipeline across a materially different facility category while exposing two durable additions.

Transferred successfully:

- official facility identification;
- countywide Contra Costa parcel/APN lookup;
- owner/address normalization;
- adjacent-parcel candidate discovery;
- assessor-map acquisition/hash/review;
- exact recorded-map reference resolution;
- public Laserfiche page rendering;
- Concord road/sidewalk enrichment where geographically applicable;
- outcome-determinative boundary gate;
- raw → normalized → reviewed evidence stages;
- anchor-authority method.

New durable lessons:

1. **Address ≠ frontage ≠ legal access path.** A mismatch must create a distinct access-path/easement inquiry rather than an ownership assumption.
2. **Cross-category doctrine must reset.** Reuse the comparator method, not the previous facility's anchor cases or conclusions.
3. **Agency-purpose rules remain scoped.** Privacy duties and a knowledge-test cell-phone rule do not silently become a field-office camera ban.

Canonical checkpoint:

`docs/research/evidence/concord-dmv/facility-prep-cross-category-validation-2026-09-22.md`

Validation run:

- GitHub Actions run `35784583396`;
- conclusion `success`;
- artifact `facility-prep-concord-dmv-full`;
- artifact ID `10719403821`;
- ZIP SHA-256 `ed90611aabdf487199d196dbc955800e8dc173ef99df430f13d3d82ea7ba7c3d`.

---

# 17. Current research flags

- `ADDRESS/FRONTAGE-MISMATCH`
- `DIAMOND-PUBLIC-ACCESS-LEGAL-GEOMETRY-UNRESOLVED`
- `EXACT-ROW-EDGE-PENDING-WHERE-OUTCOME-DETERMINATIVE`
- `CURRENT-ENTRANCE/QUEUE/PARKING-PHYSICAL-VERIFICATION-PENDING`
- `DMV-LOBBY-FEDERAL-NONPUBLIC-STRONGLY-SUPPORTED`
- `DMV-LOBBY-CALIFORNIA-SPEECH-CLAUSE-UNRESOLVED`
- `DMV-PARKING-CALIFORNIA-SPEECH-CLAUSE-UNRESOLVED`
- `KNOWLEDGE-TEST-CELL-PHONE-RULE-ACTIVITY-SPECIFIC`
- `NO-DEDICATED-DMV-FIELD-OFFICE-CAMERA-RULE-LOCATED-IN-SOURCES-REVIEWED`
- `REMOVAL/TRESPASS-AUTHORITY-AREA-AND-FACT-SPECIFIC`

---

# 18. Documentary sweep posture

The Concord DMV **documentary** cross-category sweep is substantially developed.

The highest-value remaining work is now narrow and physical/current rather than broad historical archaeology:

1. verify the actual Diamond Boulevard entrance drive/walk and current signs;
2. identify the current legal access instrument only if the Diamond approach becomes outcome-determinative;
3. verify current customer parking, exterior queueing, pedestrian circulation and any vehicle-test lanes;
4. inspect current lobby/counter/testing/kiosk signs for camera, cell-phone, privacy or conduct restrictions;
5. preserve the exact text and asserted authority of any rule encountered before constitutional analysis;
6. analyze any concrete removal/trespass incident under the actual subarea/controller/facts.

The historical subdivision chain is sufficiently developed for present purposes: it confirms the frontage mismatch and direct Meridian Park relationship but does not resolve a later/current Diamond access right.

Current facility posture:

`DOCUMENTARY-SWEEP-SUBSTANTIALLY-DEVELOPED / CROSS-CATEGORY-VALIDATION-SUCCESSFUL / FIELD-AND-CURRENT-ACCESS-VERIFICATION-PENDING`
