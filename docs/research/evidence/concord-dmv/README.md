# Concord DMV — Evidence Manifest

**Facility:** California Department of Motor Vehicles — Concord Field Office  
**Address:** 2070 Diamond Boulevard, Concord, CA 94520  
**Agency:** California Department of Motor Vehicles  
**Research date:** 2026-09-22  
**Boundary confidence:** **PARTIALLY-VERIFIED**

This manifest preserves the source chain for Sweep 009, the first cross-category Facility Prep test after the two Contra Costa library sites. It separates current official-source facts, assessor/map observations, access/control questions, and legal conclusions.

## Current parcel result

Facility Prep resolved the Concord DMV through the same countywide Contra Costa parcel layer used for Walnut Creek Library.

### Target parcel

- APN: `126-490-004` (`126490004` raw field)
- display/site address: `2070 DIAMOND BLVD - CONCORD`
- owner field: `CALIFORNIA STATE OF`
- second owner/name field: `DEPT MOTOR VEHICLES`
- assessor map: Book 126 Page 49
- assessor PDF: https://ccmap.cccounty.us/HTML5/assessorPDF/126p49x0.pdf
- assessor-map SHA-256: `d3e6dc5d5f889a5d8ab368c554c1b41d3573e68acc5e539be30584637a3e426c`

The parcel record also contains `full_n_address = 2415 1ST AVE MSA156`. That field is preserved as returned by the official GIS but is not substituted for DMV's public facility address.

Independent current corroboration includes:

- DMV's official Concord field-office page identifying 2070 Diamond Boulevard;
- a DMV facilities/equipment list identifying the Concord office as **State Owned**;
- City of Concord assessment-roll material identifying APN `126-490-004`, owner `CALIFORNIA STATE OF`, address 2070 Diamond Boulevard, and property class `PUB`.

These current sources strongly support State ownership and DMV operational use. They do not by themselves establish every access easement, driveway right, exact ROW edge, or forum classification.

## Assessor-map observations

Human review of Book 126 Page 49 shows the target in the Tract 5292 / Willowick 4 block context and materially changes the access question.

The sheet depicts:

- `TRACT 5292 (WILLOWICK 4) MB 212-47`;
- parcel `04`, approximately 3.49 acres, corresponding to the State/DMV parcel;
- Diamond Boulevard to the west;
- Meridian Park Boulevard to the east;
- Galaxy Way to the north;
- parcel `01` between parcel `04` and Diamond Boulevard;
- parcel `03` south of parcel `04`;
- parcel `05` to the north/northeast.

The official public address is on Diamond Boulevard while the assessor sheet does not visually show parcel `04` directly fronting Diamond.

Status:

`ADDRESS/FRONTAGE-MISMATCH / ACCESS-PATH-AND-EASEMENT-REVIEW-REQUIRED`

Potential explanations include an access easement, shared driveway, site-plan configuration, or other legal/physical arrangement. No particular explanation is adopted without supporting evidence.

Detailed review:

`assessor-map-review-2026-09-22.md`

## Recorded subdivision map — `212M47`

The exact assessor reference was resolved through Contra Costa Public Works Recorded Maps:

- `212M47`;
- entry ID `148419`;
- Subdivision Map;
- `WILLOWICK #4`;
- recorded June 28, 1978;
- permit `SD78-05292`;
- three imaged pages.

All three pages were retrieved through the ordinary anonymous public Laserfiche viewer and visually reviewed.

Page-image SHA-256 values:

- page 1: `35f880e041169a10c50f57a4a0b9c1d2b351b1cfeeb436fa1cd326eef24261fa`
- page 2: `fc8ccc28aee88090faf4d7d7f70c0bb034558d326629c35387913057dafbbd10`
- page 3: `4295d6b30b218d6ad276c50cfdcafd049883ee866b4b8601aa77555e5427178a`

The subdivision map materially confirms the assessor geometry:

- historical Lot 4 is approximately 3.49 acres;
- Lot 4 directly fronts Meridian Park Boulevard;
- Lots 1 and 2 lie between Lot 4 and Diamond Boulevard;
- no labeled access easement carrying Lot 4 across Lot 1 to Diamond is apparent on the reviewed drawing.

That negative visual observation is not conclusive and does not exclude a later-created easement or shared-access agreement.

The owner's certificate dedicates the mapped **Meridian Park Blvd** portion to public use. The City Clerk's certificate states that the City approved the final map but did not accept or reject the streets/easements shown as dedicated to public use at that time. Current Concord Road Centerlines independently identifies Meridian Park as Concord-owned/jurisdictional today.

Detailed review:

`recorded-map-212m47-review-2026-09-22.md`

## Adjacent-parcel candidates

The GIS intersection query returned four non-target candidates:

- `126-490-001` — 2090 Diamond Boulevard — `FLATIRONS STANWELL LLC`;
- `126-490-002` — 2050 Diamond Boulevard — `LEE JOHN S & HELEN Y TRE` / `NORTHS RESTAURANT INC`;
- `126-490-003` — 2055 Meridian Park Boulevard — `CONCORD FK PROPERTY LLC`;
- `126-490-005` — 2080 Diamond Boulevard — `EDSTAR ENTERPRISES` / `PAULA DOUGHERTY GP`.

These remain **candidate discovery results**. Parcel `01` is particularly relevant to the Diamond-frontage/access question because both the assessor sheet and recorded subdivision map place it between the State parcel and Diamond Boulevard. The present legal access/control relationship remains unresolved.

## Official road / sidewalk GIS leads

Concord Road Centerlines was queried around the DMV using the parcel centroid.

### Diamond Boulevard

- OBJECTID `226039`
- Street Owner / Jurisdiction: `Concord` / `Concord`
- road class: `Major Arterial`
- right-side address range: `2000–2098`
- sidewalk-left/right: `No / Yes`
- facility ID: `TCL174239`
- source update: 2020-04-27

### Meridian Park Boulevard

- OBJECTID `226244`
- Street Owner / Jurisdiction: `Concord` / `Concord`
- road class: `Major Arterial`
- left-side address range: `2033–2099`
- sidewalk-left/right: `Yes / No`
- facility ID: `TCL174444`
- source update: 2020-04-27

### Galaxy Way

- OBJECTID `226243`
- Street Owner / Jurisdiction: `Concord` / `Concord`
- road class: `Collector`
- sidewalk-left/right: `No / Yes`
- facility ID: `TCL174443`
- source update: 2020-04-27

These are official GIS attributes and geographic research leads. A centerline is not a surveyed ROW edge, and a sidewalk-presence field does not establish title to the sidewalk strip.

Detailed review:

`property-row-review-2026-09-22.md`

## Current DMV public-access / policy layer

DMV's official field-office page identifies the Concord Field Office, ordinary service hours, testing/services, and a self-service kiosk.

No dedicated public-facing California DMV field-office ordinary-patron photography/videography rule was located in the online sources reviewed as of September 22, 2026.

Approved wording:

> **No dedicated public-facing California DMV field-office ordinary-patron photography/videography rule was located in the online sources reviewed as of September 22, 2026.**

That is not proof that no internal, posted, branch-specific, examination-specific, privacy, security, or later rule exists.

DMV's current privacy materials establish substantial agency interests in protecting sensitive personal information, including driver-license identifiers, Social Security numbers, photographs, medical/disability information, fingerprints/thumbprints, and examination information. Those privacy duties are relevant to analysis of a specific restriction but do not themselves create a general camera prohibition.

### Knowledge testing

DMV's current California Driver's Handbook states that testing aids, including a **cell phone**, are not allowed during a knowledge test.

This is a narrow examination-integrity/device-use rule. It belongs to the knowledge-test activity and must not be silently converted into a branch-wide no-phone or no-camera policy.

Detailed review:

`policy-privacy-search-2026-09-22.md`

## Current forum-doctrine posture

No facility-wide classification is assigned. Federal and California classifications are separated where state doctrine may diverge.

| Area | Current documentary posture |
| --- | --- |
| Actual ordinary Concord municipal sidewalk / ROW | **Federal TPF / California public-forum treatment — HIGH CONFIDENCE once exact location is established** |
| Facility-specific Diamond access drive/walk | **Federal nonpublic treatment strongly supported if special-purpose facility segment; legal footprint unresolved / California classification unresolved** |
| DMV customer parking | **Federal nonpublic treatment strongly supported / California classification unresolved** |
| Exterior customer queue / immediate approach | **Federal nonpublic/purpose-limited treatment strongly supported; physical configuration pending / California unresolved** |
| Entrance threshold | **SUBAREA-SPECIFIC / UNRESOLVED** |
| Ordinary public lobby / waiting area | **Federal nonpublic-forum treatment strongly supported / California Speech Clause unresolved** |
| Service counters / transaction zones | **PURPOSE-LIMITED / NONPUBLIC ANALOGY STRONG; specific privacy/rule application pending** |
| Knowledge-testing / examination areas | **PURPOSE-LIMITED; specific cell-phone-as-testing-aid rule verified** |
| Employee / records / secure areas | **RESTRICTED / NOT ORDINARY PUBLIC-ACCESS SPACE** |

Principal current federal anchors:

- ordinary sidewalk: *United States v. Grace*;
- special-purpose facility access: *United States v. Kokinda* and *Jacobsen v. USPS*;
- administrative interior: *Sammartano* / *Cornelius*;
- recording as protected activity depending on location/restriction: *Askins v. DHS*.

California exterior cases including *Camenzind* materially strengthen the state-law public-forum argument for some freely accessible exterior spaces, but no close DMV/administrative-site case was located that justifies mechanically carrying those venue holdings into the DMV lot or facility approach.

Detailed analyses:

- `exterior-forum-analysis-2026-09-22.md`
- `interior-forum-authority-review-2026-09-22.md`

## Current confidence by issue

| Question | Current state |
| --- | --- |
| DMV APN `126-490-004` | **OFFICIAL-GIS-RESOLVED** |
| State owner field / DMV second-name field | **OFFICIAL-GIS-RESOLVED + INDEPENDENTLY-CORROBORATED** |
| Assessor Book 126 Page 49 | **HUMAN-REVIEWED / SOURCE-LIMITED** |
| Recorded map `212M47` | **OFFICIAL-INDEX-RESOLVED / PUBLIC-SCAN-RETRIEVED / HUMAN-REVIEWED** |
| State parcel direct Meridian Park frontage | **STRONGLY-SUPPORTED** |
| State parcel direct Diamond frontage | **NOT SUPPORTED; INTERVENING PARCEL SHOWN** |
| Present Diamond driveway/access easement | **UNRESOLVED / OUTCOME-DETERMINATIVE IF EXCLUSION LOCATION MATTERS** |
| Diamond / Meridian / Galaxy road-owner and sidewalk GIS fields | **OFFICIAL-GIS-RESOLVED-AS-ATTRIBUTES** |
| Exact street ROW edge | **UNRESOLVED** |
| State ownership vs. private lease | **STATE OWNERSHIP STRONGLY SUPPORTED** |
| Ordinary public lobby federal forum posture | **NONPUBLIC-FORUM TREATMENT STRONGLY SUPPORTED** |
| Ordinary public lobby California Speech Clause | **UNRESOLVED** |
| DMV-specific ordinary-patron camera rule | **NOT LOCATED IN SOURCES REVIEWED** |
| Knowledge-test cell-phone/testing-aid rule | **CURRENT-PUBLIC-RULE-VERIFIED** |

## Preserved machine evidence

Reviewed machine output promoted with this sweep:

- `facility-prep-2026-09-22/report.json`
- `facility-prep-2026-09-22/parcel.geojson`

The full binary/raw packet is also preserved in GitHub Actions run `35784583396` as artifact `facility-prep-concord-dmv-full`, artifact ID `10719403821`, ZIP SHA-256 `ed90611aabdf487199d196dbc955800e8dc173ef99df430f13d3d82ea7ba7c3d`.

## Next property/control question

The historical map chain has now done its job: it confirms the frontage mismatch rather than resolving the modern Diamond access route.

If exact access control becomes necessary, the next high-value sources are current State/DMV/DGS acquisition or site records, later easement/deed instruments, and/or current City site/engineering records showing the legal driveway/walkway connection from Diamond Boulevard.

Under the outcome-determinative boundary gate, that deeper step is required for a location-specific exclusion/trespass analysis on the Diamond approach, but not as a prerequisite to classifying an independently identified ordinary municipal sidewalk or analyzing the well-defined administrative interior.
