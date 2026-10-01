---
title: Sweep 008 — Walnut Creek Library Branch
jurisdiction: California
last_verified: 2026-09-22
status: branch-research-in-progress
---

# Sweep 008 — Walnut Creek Library Branch

## Scope

Sweep 008 is the second branch-level Contra Costa County Library investigation and the first deliberate same-category validation of the Facility Prep prototype after Concord.

**Facility:** Walnut Creek Library  
**System:** Contra Costa County Library (CCCL)  
**Address:** 1644 N. Broadway, Walnut Creek, California 94596  
**Research mode:** documentary / pre-field  
**Field observation:** none yet

Walnut Creek changes the physical problem while holding much of the library-system policy layer constant. The branch occupies a dense downtown civic setting with a civic plaza, Civic Park connection, surface parking, an underground garage, multiple public entrances, public-facing outdoor space, and differently managed room channels.

No branch-wide forum conclusion is assigned. The analysis follows **system → branch → area/activity**.

Canonical project sources:

- `docs/california/standing-scenario.md`
- `docs/california/facility-investigation-methodology.md`
- `docs/california/public-libraries.md`
- `docs/research/FACILITY-PREP-SOP.md`
- `docs/research/evidence/walnut-creek-library/README.md`

---

# 1. Research questions

Sweep 008 asks:

1. whether Facility Prep can resolve a non-Concord Contra Costa branch without relying on Concord-only AddressPoint data;
2. what parcel contains the Library and which adjoining parcels are materially relevant to public access;
3. how the Broadway/Lincoln civic plaza, formal entrance, Civic Park connection, surface lot and municipal sidewalks compare with *Prigmore* and ordinary sidewalk/park doctrine;
4. whether the underground public garage presents a materially different forum problem from the outdoor lot;
5. how Oak View, Las Trampas and group study rooms differ as opened/purpose-limited channels;
6. whether a current Walnut Creek-specific ordinary-patron photography/videography rule is publicly posted online;
7. which unresolved boundary/control facts could actually change removal, trespass or forum analysis.

---

# 2. Current branch facts

Official CCCL branch page:

https://ccclib.org/locations/26/

As reviewed September 22, 2026:

- Monday–Thursday: 10 a.m.–8 p.m.;
- Friday–Saturday: 9 a.m.–5 p.m.;
- Sunday: closed;
- listed facilities include a cafe, computer lab, meeting room and study room.

CCCL identifies:

- **Library underground garage:** 120 spaces, four-hour limit;
- **Library surface lot:** 20 four-hour spaces and 10 thirty-minute spaces;
- **Broadway Garage:** separate nearby downtown garage at 1390 N. Broadway.

The Broadway Garage is not treated as part of the Library parcel merely because it is listed as nearby parking.

CCCL branch history/design page:

https://ccclib.org/about-walnut-creek-library/

It describes the 2010 Library near Civic Park and identifies, among other features, a children's wing and patio, Teen Zone, cafe, conference room, study rooms, Community Art Gallery and Oak View meeting room.

## Self-Service Sunday

Current CCCL FAQ identifies Self-Service Sundays at Concord and San Pablo, with Pittsburg coming soon. Walnut Creek is not listed as a participating branch and its current branch page lists Sunday closed.

Source:

https://ccclib.org/faq/meeting/

Status:

`NO-CURRENT-SELF-SERVICE-SUNDAY-ACCESS-LOCATED / ORDINARY-SUNDAY-CLOSED`

Walnut Creek therefore does not inherit Concord's special Sunday card/PIN access regime.

---

# 3. Facility Prep property result

Sweep 008 added:

`tools/facility_prep/contra_costa_parcel_resolver.py`

The Concord-specific AddressPoint layer was not treated as countywide. The new adapter instead searches the countywide assessor/parcel layer exposed through the official City of Concord ArcGIS service.

## Library parcel

Official GIS result:

- APN: `178-300-039`;
- display address: `1644 BROADWAY - WALNUT CREEK`;
- owner field: `WALNUT CREEK CITY OF`;
- acreage: `2.202`;
- building-square-foot field: `43169`;
- assessor map: Book 178 Page 30;
- assessor PDF: https://ccmap.cccounty.us/HTML5/assessorPDF/178p30x0.pdf.

The returned `full_n_address` field is `1666 N MAIN ST`. That alternate/natural-address field is preserved as returned but is not substituted for the Library's official public address.

## Adjoining civic parcel

The GIS polygon-intersection query returned six non-target candidates. Human relevance screening identified one material civic candidate:

- APN: `178-300-040`;
- display address: `1375 CIVIC DR - WALNUT CREEK`;
- owner field: `WALNUT CREEK CITY OF`;
- acreage: `7.548`.

The assessor sheet depicts parcel 40 immediately adjoining parcel 39 and labels both `CITY OF WALNUT CREEK`. City sources place Civic Park Community Center at 1375 Civic Drive. This strongly supports parcel 40 as the adjoining Civic Park/City civic parcel while leaving exact subarea boundaries/control separate.

The other GIS-intersection parcels remain candidate-only. A polygon touching/intersection result does not itself prove material adjacency or control.

Preserved evidence:

- `docs/research/evidence/walnut-creek-library/facility-prep-2026-09-22/report.json`
- `docs/research/evidence/walnut-creek-library/facility-prep-2026-09-22/parcel.geojson`
- `docs/research/evidence/walnut-creek-library/facility-prep-2026-09-22/adjacent-parcels.json`

---

# 4. Assessor / recorded-map chain

## Assessor Book 178 Page 30

Human review confirms:

- parcel `39`, `CITY OF WALNUT CREEK`, `2.202 Ac`;
- parcel `40`, `CITY OF WALNUT CREEK`, `7.548 Ac`;
- separate City parcel `37`, approximately 2.0 acres, south/across North Broadway;
- North Broadway, Lincoln Avenue, Civic Drive, North Main Street and Carlback Avenue;
- `RANCHO DOLORES SUB'N MB 2-36 7/26/1909`;
- `OAK PARK SUB'N MB 18-385 3/4/1922`;
- footer references `FM 19-25, 20-29`;
- notation `NE COR. LEASE 1217 OR 76`.

The lease notation remains a research lead only. It is not assigned to the Library parcel without stronger positional/record evidence.

The assessor sheet expressly carries assessment-purpose accuracy limitations and is not treated as a survey-grade legal boundary.

Detailed review:

`docs/research/evidence/walnut-creek-library/assessor-map-review-2026-09-22.md`

## Public Works Recorded Maps

An exact APN-metadata search for `178 30` returned zero hits. That means only that no indexed map carried that exact APN metadata.

The assessor-sheet map references were separately resolved:

### Rancho Dolores — MB 2-36

- entry name `2M36`;
- entry ID `482387`;
- record type `Subdivision Map`;
- APN metadata `178 030`;
- Walnut Creek;
- recorded July 26, 1909;
- subdivision `RANCHO DOLORES`.

### Oak Park — MB 18-385

- entry name `18M385`;
- entry ID `128855`;
- record type `Subdivision Map`;
- Walnut Creek;
- recorded March 4, 1922;
- engineer/surveyor Clyde Laird;
- subdivision `OAK PARK`;
- road-vicinity metadata includes Main Street and Lincoln Avenue.

These verify the historical assessor annotations. They do not automatically establish the present Library boundary, present ROW, plaza geometry or easements.

Detailed review:

`docs/research/evidence/walnut-creek-library/recorded-map-review-2026-09-22.md`

---

# 5. Facility Prep second-site validation

Walnut Creek materially validated the pipeline while exposing hidden first-site assumptions.

## Countywide core + local enrichment

The parcel layer was reusable outside Concord; the Concord AddressPoint and Road Centerlines layers were not assumed to be countywide.

Working architecture:

`countywide parcel core + municipality-specific address / street / ROW / owned-property / facility-control enrichment`

## Recorded-map alias defect found and fixed

The Concord-era map resolver had been tested against LSM/record-of-survey and corner-record references. Walnut Creek's assessor sheet introduced `MB` shorthand.

The initial Book/Page search did not constrain WebLink's `Record Type` selector. The adapter was corrected so:

- `LSM` / `RS` → `Record of Survey Map`;
- `CR` → `Corner Record`;
- `MB` / `subdivision` → `Subdivision Map`;
- `PM` / `parcel` → `Parcel Map`.

A live post-fix run confirmed that the actual WebLink search syntax contained `Record Type = "Subdivision Map"` and returned exactly one relevant result for each tested historical reference.

Validation run:

- run ID `35779391449`;
- job ID `106920689651`;
- conclusion **success**;
- artifact ID `10716842873`;
- artifact ZIP SHA-256 `91f683b20188b3f70bb0480df8ef4cf014c399ee410f40fb4f70e3dc6d3432d4`.

Detailed checkpoint:

`docs/research/evidence/walnut-creek-library/facility-prep-second-site-validation-2026-09-22.md`

The Facility Prep SOP now preserves the second-site lessons as reusable methodology rather than Walnut Creek-only lore.

---

# 6. Civic design and public-access evidence

A City design-period publication states that the Library was designed to be accessible from:

1. a new civic plaza at Broadway and Lincoln;
2. a formal entrance on Broadway;
3. the surface parking lot; and
4. a Civic Park entrance.

It also states that the underground garage was intended to serve Library patrons, community-center users and other downtown visitors.

Source:

https://www.walnutcreekca.gov/home/showpublisheddocument/84/635672432775130000

The City's Public Art Master Plan independently identifies `Library Outdoor Plazas`, Civic Park walkways/entries, sidewalks and street furniture as potential public-art locations:

https://www.walnutcreekca.gov/home/showpublisheddocument/11536/636136819628970000

These are strong intended-use/circulation sources, not cadastral surveys.

---

# 7. Civic Park

Current City park directory:

https://www.walnutcreekartsrec.org/Home/Components/FacilityDirectory/FacilityDirectory/45/1920

Current facts include:

- 1375 Civic Drive;
- 16.7 acres;
- dawn-to-dusk access;
- Community Center;
- Library;
- parking;
- picnic area;
- restrooms;
- trail connections, including connections to the Iron Horse Trail and Creek Walk.

A City publication separately describes Civic Park as open approximately 30 minutes before sunrise until 30 minutes after dusk, subject to special evening events:

https://www.walnutcreekca.gov/home/showpublisheddocument/30891/638418828841230000

These current sources reinforce the public-park/access record while leaving specific reservation, closure and event rules intact.

---

# 8. Exterior forum analysis

Canonical analysis:

`docs/research/evidence/walnut-creek-library/exterior-forum-analysis-2026-09-22.md`

| Area | Current documentary posture |
| --- | --- |
| Actual North Broadway municipal sidewalk / ROW | **TPF — HIGH CONFIDENCE; exact edge pending where ambiguous** |
| Actual Lincoln Avenue municipal sidewalk / ROW | **TPF — HIGH CONFIDENCE; exact edge pending where ambiguous** |
| Broadway–Lincoln civic plaza / Library outdoor-plaza area | ***Prigmore* TPF treatment strongly supported; current physical verification pending** |
| Formal Broadway entrance / immediate exterior approach | ***Prigmore* TPF treatment strongly supported; field verification pending** |
| Civic Park entrance / connective public pedestrian route | **TPF treatment strongly supported; exact subarea line pending if material** |
| Civic Park proper | **TPF — HIGH CONFIDENCE, subject to ordinary park/reservation rules** |
| Library surface lot | ***Prigmore* TPF treatment strongly supported for lawful pedestrian expressive use; traffic/safety rules remain material** |
| Underground Library garage | **FORUM CLASSIFICATION UNRESOLVED** |
| Garage ramps / vehicle portals | **No broad speech-zone conclusion; vehicle/safety function dominates** |
| Garage pedestrian exits, stairs, elevators and connective corridors | **UNRESOLVED / SUBAREA-SPECIFIC** |
| Children's patio | **Separate purpose/access review required; no broad exterior TPF conclusion** |

## Underground garage

The garage is deliberately open to the public, but it is also an enclosed special-purpose vehicle-storage/circulation structure. Public access alone does not make it a public forum.

Current evidence includes:

- CCCL: 120 Library underground spaces, four-hour limit;
- City Oak View page: metered underground parking remains accessible during after-hours events;
- City design source: garage intended for Library patrons, community-center users and other downtown visitors;
- City sustainability materials: public EV chargers at the Library.

These facts make an employee-only/private-garage characterization implausible, but they do not answer forum classification.

*Cornelius*, *Kokinda* and *Sammartano* are useful cautionary/general comparators for purpose-built access space. *Prigmore* remains much closer to the open plaza/entrance/surface-lot areas. None directly decides this garage.

Status:

`PUBLIC-ACCESS-VERIFIED / FORUM-UNRESOLVED`

## Recording-specific limit

*Prigmore* and the other forum cases classify spaces; they do not independently decide every photography/videography restriction. Once forum status is established, the specific recording restriction must still be tested under the applicable speech, newsgathering/recording, privacy and time/place/manner doctrines.

---

# 9. Room / channel analysis

## Oak View Room

Current City source:

https://www.walnutcreekartsrec.org/parks-facilities/facility-rentals/walnut-creek-library-oak-view-room

Current public record shows:

- second-floor room;
- City Facility Rentals management;
- meetings, corporate events, trainings, book signings, dinners and social events among identified uses;
- Library programming priority during Library hours;
- separate after-hours entrance;
- use while the rest of the Library is closed;
- metered underground parking accessible for after-hours events;
- inquiry/application/contract process.

Current forum posture:

`LIMITED-PUBLIC-FORUM TREATMENT STRONGLY SUPPORTED / CURRENT USE-RULE APPLICATION REMAINS EVENT-SPECIFIC`

*Faith Center* is a strong comparator for an intentionally opened library-associated room, but it did not adjudicate Walnut Creek's current City rental program.

## Las Trampas Conference Room

Current live CCCL sources:

- https://ccclib.org/las-trampas-room-policy/
- https://ccclib.org/rooms/

The room is opened to organizations, businesses or groups, supports advance reservations and is governed by capacity, conduct and operational rules during Library hours.

Current forum posture:

`LIMITED PUBLIC FORUM — STRONGLY SUPPORTED UNDER FAITH CENTER COMPARATOR / PRACTICE VERIFICATION PENDING`

### Booking-control discrepancy

A 2025-revised CCCL Room Use PDF says Oak View and Las Trampas arrangements are made through City Facility Rentals:

https://ccclib.org/wp-content/uploads/sites/72/2026/03/LP-RMS-MeetingRoomRules_2025E_ADA.pdf

Current live CCCL pages provide direct CCCL/online booking for Las Trampas, and the current City Oak View page expressly states that smaller Library rooms such as Las Trampas are reserved directly through CCCL rather than City Facility Rentals.

Working treatment:

`CURRENT-LIVE-SOURCES-SUPPORT-CCCL-LAS-TRAMPAS-BOOKING / OLDER-PDF-DISCREPANCY-PRESERVED`

This resolves the current-use description more strongly than the initial sweep, while leaving any underlying formal property/control allocation open if it later matters to exclusion authority.

## Group study rooms

Current rule:

https://ccclib.org/walnut-creek-library-group-study-room-rules/

Four rooms are available to individuals/small groups through same-day in-person use, generally up to two hours. Rules prohibit advertising, petitions, solicitations and sales and impose operational conditions.

Current forum posture:

`PURPOSE-LIMITED CHANNEL / FINAL CLASSIFICATION UNRESOLVED`

They do not inherit the larger meeting/rental-room classification merely because all are public-use rooms.

---

# 10. Ordinary interior, children's area and cafe

## Ordinary interior

Sweep 006's unresolved system-level issue remains:

`AUTHORITY-UNRESOLVED`

Current research has not located controlling California/Ninth Circuit authority establishing a categorical forum classification or blanket recording rule for ordinary public-library interiors. Public access and government ownership do not themselves establish traditional-public-forum status.

## Children's wing and patio

The branch expressly includes a children's wing and patio. Current CCCL children/teen-area rules and the actual patio/access geometry must be applied before a final classification.

Status:

`PURPOSE/ACCESS-REVIEW-REQUIRED`

## Cafe

The branch identifies a cafe, but this sweep has not established the current operator, lease/license terms, exact footprint or separate access rules.

Status:

`CONTROL/ACCESS-UNRESOLVED`

No forum or removal conclusion is inferred merely because the cafe sits within the Library facility.

---

# 11. Photography / videography policy search

Current CCCL system and Walnut Creek branch policy sources were searched for an ordinary-patron photography/videography rule.

Approved finding:

> **No dedicated public-facing Walnut Creek-specific ordinary-patron photography/videography rule was located in the online sources reviewed as of September 22, 2026.**

This is not proof that no internal, posted, program-specific, lease-specific or later rule exists.

Current physical-signage verification remains necessary before publishing a final field-facing branch statement.

---

# 12. ROW / current-plan source family

Walnut Creek Engineering states that work within public ROW requires an encroachment permit and identifies sidewalk, curb/gutter, driveway-approach and traffic/pedestrian-control work among the relevant categories:

https://www.walnutcreekca.gov/government/public-works/engineering-services/encroachment-permits

Current City site-plan standards require depiction of:

- property boundaries/easements;
- adjacent streets/public ROW;
- parking/circulation;
- pedestrian and vehicle ingress/egress;
- street dedications/improvements;
- public/private street status.

Source:

https://www.walnutcreekca.gov/government/community-development-department/permits/building-permits/site-plans-and-diagrams

The City also maintains official building records/plans and a records-request process:

https://www.walnutcreekca.gov/government/community-development-department/permits/building-permits/request-building-records

No publicly indexed current Library site/engineering plan was located during this sweep that fixes the exact Broadway/Lincoln/plaza/garage edges.

Under the outcome-determinative boundary gate, a targeted current-plan request is warranted only if the exact line would change the legal result—for example, a location-specific exclusion/trespass dispute at a visually ambiguous plaza/sidewalk transition.

---

# 13. Removal / trespass posture

No Walnut Creek enforcement incident is being analyzed.

Keep separate:

- forum classification;
- facility/room/park/garage policy;
- operational control;
- authority to order departure;
- administrative suspension/exclusion;
- police detention;
- criminal trespass elements.

The CCCL Suspension Policy's generic Penal Code § 602 reference remains subject to Sweep 006's `POLICY-TO-CRIMINAL-AUTHORITY-GAP` until a particular subsection and element chain are identified for a concrete scenario.

Walnut Creek's mixed City/County/rental/park/parking environment makes area-specific control particularly important.

---

# 14. Current research flags

- `ORDINARY-INTERIOR-RECORDING-AUTHORITY-UNRESOLVED`
- `UNDERGROUND-GARAGE-FORUM-UNRESOLVED`
- `GARAGE-PEDESTRIAN-SUBAREAS-UNRESOLVED`
- `CHILDRENS-PATIO-PURPOSE-ACCESS-REVIEW-REQUIRED`
- `CAFE-CONTROL-ACCESS-UNRESOLVED`
- `LAS-TRAMPAS-CURRENT-LIVE-POLICY-OLDER-PDF-DISCREPANCY`
- `EXACT-ROW-EDGE-PENDING-WHERE-OUTCOME-DETERMINATIVE`
- `CURRENT-PLAZA/SIGNAGE-PHYSICAL-VERIFICATION-PENDING`
- `POLICY-TO-CRIMINAL-AUTHORITY-GAP`
- `NO-DEDICATED-BRANCH-CAMERA-RULE-LOCATED-IN-SOURCES-REVIEWED`

---

# 15. Facility Prep validation result

Walnut Creek demonstrates that Facility Prep is becoming a reusable pipeline rather than a Concord-specific script.

Transferred successfully:

- address → parcel/APN;
- owner/address/acreage fields;
- parcel geometry;
- neighboring-parcel candidate discovery;
- assessor-map acquisition/hash/review;
- Contra Costa recorded-map index probing;
- human relevance screening;
- evidence-stage separation;
- outcome-determinative boundary gate;
- anchor-case comparator analysis.

Remained modular:

- AddressPoint enrichment;
- municipal road/ROW data;
- municipal owned-property layers;
- current site/engineering records;
- parking/park operations;
- room/facility control.

The same-category prototype gate has therefore served its purpose. The next architecture test should be a materially different facility category rather than another library merely to repeat the same parcel pattern.

---

# 16. Documentary sweep posture

The Walnut Creek **documentary** branch sweep is now substantially developed.

What still matters before a final branch entry is not more indiscriminate historical-record searching. The remaining high-value items are:

1. current physical/signage verification of the civic plaza, entrances, surface lot and garage;
2. exact modern ROW/site-plan acquisition only where the line becomes outcome-determinative;
3. current garage conduct/access signs and pedestrian-node layout;
4. any current cafe lease/control evidence if that subarea is actually analyzed;
5. ordinary-interior recording/forum doctrine as the broader statewide/library issue develops;
6. any future concrete removal/trespass incident, analyzed under its actual area/controller/facts.

The branch remains **Gray / unresolved overall**. That overall status coexists with several area-level conclusions that are already well supported.
