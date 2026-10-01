# Concord Library — Property / Boundary Evidence Manifest

**Facility:** Concord Library  
**Address:** 2900 Salvio Street, Concord, California 94519  
**Sweep:** 007  
**Last verified:** 2026-09-22  
**Boundary confidence:** PARTIALLY-VERIFIED / EXACT-MODERN-ROW-EDGE-UNRESOLVED

This manifest tracks the official sources and preserved evidence used for the Concord Library boundary analysis. It is an evidence inventory, not a title opinion, survey, or constitutional forum conclusion.

## Current parcel result

Facility Prep queried the City of Concord's official ArcGIS AddressPoint, Parcels, and City Owned Parcels layers.

Current machine-readable result:

- **Library APN:** `111-240-006` (`111240006`)
- **display/site address:** `2900 SALVIO ST - CONCORD`
- **owner field:** `CONCORD CITY OF`
- **acreage:** `0.84`
- **City Owned Parcels layer:** positive match
- **assessor map:** Book 111 Page 24
- **AddressPoint:** approximately 37.98155445, -122.02529236
- **adjoining Civic Center candidate parcel:** APN `111-240-014`, `1950 PARKSIDE DR - CONCORD`, owner field `CONCORD CITY OF`, 3.68 acres

The Library parcel record also returns `1950 PARKSIDE DR` in a separate `full_n_address` field. That value is preserved as returned but is not interpreted as changing the Library's site address or merging the two APNs.

The City expressly warns that its GIS is general-reference data and is not for determining legal boundaries.

## Assessor map — Book 111 Page 24

Facility Prep downloaded and preserved the official assessor-map PDF:

https://ccmap.cccounty.us/HTML5/assessorPDF/111p24x0.pdf

Preserved SHA-256:

`ba30d406493dcda4b1f1ef92759d155a879062c2595614711f90fbfd8966c62d`

Canonical review note:

`docs/research/evidence/concord-library/assessor-map-review-2026-09-22.md`

Human review found:

- parcel **06** labeled **LIBRARY**, approximately **0.84 acres**, notation `3356 OR 502`;
- parcel **14** immediately east, labeled **CITY OF CONCORD**, approximately **3.68 acres**, notation `636 OR 390`;
- parcel 06 fronts Salvio Street and lies immediately east of Parkside Drive;
- parcel 14 also fronts Salvio Street;
- `40` dimension callouts on each side of the depicted Salvio centerline;
- a `50'` dimension near the Parkside strip;
- revision entry `10/10/96 — CREATE 013 & 014`.

These are assessor-map observations and record leads, not a final survey-grade boundary determination.

## Current City street / sidewalk evidence

Canonical review note:

`docs/research/evidence/concord-library/road-centerline-review-2026-09-22.md`

The City's official Road Centerlines layer returned the closest relevant segments as follows.

**Salvio Street — OBJECTID `199013`:**

- street owner `Concord`;
- jurisdiction `Concord`;
- Collector;
- sidewalk left/right `Yes / Yes`;
- right-side address range includes 2900;
- returned update date 2020-04-27.

**Parkside Drive — OBJECTID `199079`:**

- street owner `Concord`;
- jurisdiction `Concord`;
- Collector;
- sidewalk left/right `Yes / Yes`;
- right-side address range includes 1950;
- returned update date 2020-04-27.

These are strong governmental-control/context attributes. A road centerline and sidewalk-presence field do not establish the surveyed ROW edge or title to a sidewalk strip.

City engineering materials also treat sidewalks/driveways as ordinary public-ROW work and, for a Parkside/Salvio-area pedestrian project, anticipated work within City ROW while expressly recognizing that boundary surveys may be necessary to locate exact property lines.

## Historical recorded survey — 7 LSM 51

Facility Prep resolved the assessor annotation `7 LSM 51` through Contra Costa County Public Works' public Laserfiche Recorded Maps search:

- entry `126622`;
- name `7LSM51`;
- Record of Survey Map;
- County APN-book metadata `111 24`;
- recorded September 24, 1940;
- surveyor metadata C. W. Gibbs;
- one scanned page.

The entry is an imaged Laserfiche record rather than an electronic PDF. The ordinary public viewer exposes the scan, which Facility Prep rendered and preserved. Canonical human review:

`docs/research/evidence/concord-library/record-of-survey-7LSM51-review-2026-09-22.md`

The survey depicts a portion of the historical Concord Home Acres Company property, identifies deed reference `454 OR 154`, uses Salvio Street as extended as a bearing basis, and depicts Willow Pass Road and the former Sacramento Northern Railway corridor. It predates the current Library and modern parcel configuration and is therefore retained as **historical-chain evidence**, not the present legal boundary.

## Recorded-map discovery checkpoint

Canonical checkpoint:

`docs/research/evidence/concord-library/record-chain-checkpoint-2026-09-22.md`

Facility Prep tested the public Public Works Recorded Maps index beyond the printed assessor annotation.

### APN metadata search

Querying APN metadata `111 24` returned **one hit only: `7LSM51`**.

This does not prove that no other relevant record exists; it means no additional map with that exact APN metadata surfaced in the tested public index.

### Road-vicinity cross-check

`SALVIO` returned one later map, `168PM050`, but its APN metadata is `121-25`.

`PARKSIDE` returned three later maps — `93LSM40`, `158PM009`, and `172PM036` — with APN metadata `128 10`, `124 25`, and `117 11` respectively.

None matches the Library/Civic Center assessor book/page `111 24`, and no independent geographic evidence presently ties those maps to APNs `111-240-006` or `111-240-014`. They remain **BROAD-GEOGRAPHIC-HIT / NOT-PROMOTED**.

Result: the useful anonymous automated Public Works recorded-map discovery path is now **substantially exhausted** for this facility. The next exact-boundary step is targeted current-record acquisition rather than blind pursuit of same-street hits.

## Official Records references — exact identifiers resolved

RecorderWorks recognizes all three known historical Official Records references:

| Reference | RecorderWorks document ID | Relevance | State |
| --- | ---: | --- | --- |
| `3356 OR 502` | `16109166` | assessor notation on Library parcel 06 | image not viewable online; manual copy required |
| `636 OR 390` | `12566187` | assessor notation on Civic Center parcel 14 | image not viewable online; manual copy required |
| `454 OR 154` | `12286714` | deed identified on historical survey 7LSM51 | image not viewable online; manual copy required |

Canonical acquisition-target note:

`docs/research/evidence/concord-library/manual-record-acquisition-targets-2026-09-22.md`

Facility Prep stopped at the public viewer restriction. No paid transaction, authentication/CAPTCHA bypass, or alternate image route was attempted.

## City Engineering / current ROW target

Because the public map/index chain did not expose a clearly relevant modern map fixing the present Salvio/Parkside ROW edges, the next decisive source is targeted City Engineering/current-record acquisition.

Prepared request target:

`docs/research/evidence/concord-library/city-engineering-row-request-target-2026-09-22.md`

The request asks for existing current ROW maps, surveys, dedication/acceptance records, engineering plans, or controlling plan/map numbers adjacent to APNs `111-240-006` and `111-240-014`, plus any material easement or control records affecting sidewalks, driveways, entrance approaches, or shared parking/circulation.

## Preserved Facility Prep evidence

Reviewed v0.1 machine-readable output is preserved under:

`docs/research/evidence/concord-library/facility-prep-2026-09-22/`

It includes normalized parcel results, raw address/parcel responses, parcel GeoJSON, City-owned-layer evidence, and candidate-adjacent-parcel data.

Later GitHub Actions artifacts preserved assessor-map acquisition, Road Centerline queries, Laserfiche search metadata, RecorderWorks identifier resolution, recorded-map/APN searches, road-vicinity searches, and the rendered 7LSM51 scan.

Key successful runs include:

- parcel/assessor pass: `35757066338`;
- Road Centerline pass: `35758041991`;
- recorded-survey scan pass: `35763499806`;
- consolidated APN / road-vicinity record-chain pass: `35765300190`.

## Source inventory

| ID | Source | Type | Supports | Limitation / state |
| --- | --- | --- | --- | --- |
| CON-BOUND-001 | https://www.cityofconcord.org/DocumentCenter/View/981/Building-Map-PDF | City Civic Center map | physical relationship; areas labeled public parking | not cadastral/title/ROW evidence |
| CON-BOUND-002 | https://ccclib.org/locations/7/ | CCCL branch page | address; public-facing parking descriptions | not title/ROW/forum evidence |
| CON-BOUND-003 | https://www.cityofconcord.org/510/Schools-Library | City library page | CCCL operation / Civic Center adjacency | not boundary allocation |
| CON-BOUND-004 | https://www.cityofconcord.org/DocumentCenter/View/397/Projects-PDF | historical City capital document | City/County operating context | not current agreement/boundary |
| CON-BOUND-005 | https://www.cityofconcord.org/737/GIS-Maps-Portal | City GIS portal | official GIS route/disclaimer | not legal-boundary source |
| CON-BOUND-006 | 2020 CCCL Commission packet | official library record | express historical statement that building is City-owned | current deed/control still separate |
| CON-BOUND-007 | City Owned Parcels, BaseMap layer 9 | ArcGIS | 111-240-006 City-owned-layer match | GIS limitation applies |
| CON-BOUND-008 | Parcels, BaseMap layer 10 | ArcGIS | APN/owner/acreage/geometry/adjacent candidate | not survey-grade |
| CON-BOUND-009 | https://www.contracosta.ca.gov/552/Maps-Property-Information | County Assessor | official parcel research route | does not itself resolve ROW/easements |
| CON-BOUND-010 | https://www.contracosta.ca.gov/438/Maps-Records | County Public Works | official map/survey research chain | index/map completeness limits remain |
| CON-BOUND-011 | County CCMAP APN instructions | official instructions | manual APN procedure | procedure only |
| CON-BOUND-012 | Facility Prep v0.1 | automated acquisition | reproducible APN/owner/geometry result | not legal boundary |
| CON-BOUND-013 | Assessor Book 111 Page 24 | assessor map | current assessor geometry/labels/reference leads | not deed/survey/complete easement report |
| CON-BOUND-014 | Facility Prep v0.2 | automated evidence | assessor PDF/hash + geometry context | human review required |
| CON-BOUND-015 | City Road Centerlines layer 8 | ArcGIS | owner/jurisdiction/sidewalk/street attributes | no surveyed ROW edge |
| CON-BOUND-016 | Facility Prep Road Centerline pass | automated evidence | relevant Salvio/Parkside segments | no sidewalk title/ROW edge |
| CON-BOUND-017 | Public Works `7LSM51`, entry 126622 | Record of Survey | historical tract / Salvio relationship; 454 OR 154 lead | historical, not current parcel boundary |
| CON-BOUND-018 | Public Works APN-metadata search `111 24` | Recorded Maps index | only 7LSM51 returned | absence of hit ≠ absence of record |
| CON-BOUND-019 | Public Works Road Vicinity searches | Recorded Maps index | geographic cross-check | returned later maps have mismatched APN metadata; not promoted |
| CON-BOUND-020 | RecorderWorks Old Book index | Recorder index | exact docids for 3356/502, 636/390, 454/154 | images unavailable online; contents unresolved |
| CON-BOUND-021 | City Engineering / Permit Records routes | City records process | current ROW/current-plan acquisition route | records not yet obtained |
| CON-BOUND-022 | `record-chain-checkpoint-2026-09-22.md` | project review | documents automated-discovery stop point | not independent government evidence |

## Current confidence by question

| Question | Current result | Confidence |
| --- | --- | --- |
| Facility APN | `111-240-006` | OFFICIAL-GIS-RESOLVED |
| Current GIS owner field | `CONCORD CITY OF` | OFFICIAL-GIS-RESOLVED |
| City-owned layer match | Yes | OFFICIAL-GIS-RESOLVED |
| GIS parcel geometry | preserved GeoJSON | OFFICIAL-GIS-RESOLVED / NOT-SURVEY-GRADE |
| Assessor map | Book 111 Page 24 reviewed | VERIFIED-AS-ASSESSOR-EVIDENCE |
| Neighboring Civic Center parcel | `111-240-014` / City owner field | STRONGLY-SUPPORTED / NOT-SURVEY-GRADE |
| 7LSM51 | official scan/index resolved and reviewed | VERIFIED-HISTORICAL-SURVEY |
| 3356 OR 502 | docid `16109166` | IDENTIFIER-RESOLVED / MANUAL-COPY-REQUIRED |
| 636 OR 390 | docid `12566187` | IDENTIFIER-RESOLVED / MANUAL-COPY-REQUIRED |
| 454 OR 154 | docid `12286714` | IDENTIFIER-RESOLVED / MANUAL-COPY-REQUIRED |
| Salvio owner/jurisdiction | Concord / Concord | OFFICIAL-GIS-RESOLVED-AS-ATTRIBUTE |
| Salvio sidewalk attributes | Yes / Yes | OFFICIAL-GIS-RESOLVED-AS-ATTRIBUTE |
| Parkside owner/jurisdiction | Concord / Concord | OFFICIAL-GIS-RESOLVED-AS-ATTRIBUTE |
| Parkside sidewalk attributes | Yes / Yes | OFFICIAL-GIS-RESOLVED-AS-ATTRIBUTE |
| Clearly relevant later Public Works map | none found by tested APN/road-vicinity searches | DISCOVERY-SUBSTANTIALLY-EXHAUSTED / NOT-PROOF-OF-NONEXISTENCE |
| Legal/survey-grade current parcel boundary | not established | UNRESOLVED |
| Salvio/Parkside exact public ROW edge | strong context; exact edge not established | PARTIALLY-VERIFIED / LEGAL-EDGE-UNRESOLVED |
| Front-lot parcel/control | not conclusively mapped | UNRESOLVED |
| Rear-lot parcel/control | not conclusively mapped | UNRESOLVED |
| Easements/dedications | not resolved | UNRESOLVED |
| City/County exterior operating-control allocation | not resolved | UNRESOLVED |

## Next research chain

The broad anonymous automated discovery stage is complete enough to stop widening searches. Next:

1. seek current City Engineering/ROW records using the prepared APNs and exact street segments;
2. obtain `3356 OR 502` and `636 OR 390` manually if their contents are needed to resolve the current parcel chain;
3. obtain any current dedication/easement/plan records identified by Engineering;
4. locate current City/County operating/parking/maintenance agreements if control remains material;
5. overlay those records onto the front lot, rear lot, entrance walks/forecourt, Salvio sidewalk/ROW, Parkside sidewalk/ROW, and Civic Center circulation;
6. only then finalize area-specific *Prigmore* / forum classifications where the boundary result matters.

## Preservation rule

A preserved GIS response, assessor map, index hit, or scanned survey establishes what the official source returned on the review date. It is not automatically a deed, title opinion, complete easement report, final legal-boundary determination, or constitutional classification.
