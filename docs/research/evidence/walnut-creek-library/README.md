# Walnut Creek Library — Evidence Manifest

**Facility:** Walnut Creek Library  
**Address:** 1644 N. Broadway, Walnut Creek, CA 94596  
**System:** Contra Costa County Library  
**Research date:** 2026-09-22  
**Boundary confidence:** **PARTIALLY-VERIFIED**

This manifest preserves the source chain used for Sweep 008. It separates current official-source facts from map observations, historical-record leads, operational-control questions, and legal conclusions.

## Current parcel result

Facility Prep's second-site test successfully resolved the Walnut Creek Library against the countywide assessor/parcel layer exposed through the official City of Concord public ArcGIS service.

### Target parcel

- APN: `178-300-039` (`178300039` raw field)
- display/site address: `1644 BROADWAY - WALNUT CREEK`
- owner field: `WALNUT CREEK CITY OF`
- acreage: `2.202`
- building-square-foot field: `43169`
- assessor map: Book 178 Page 30
- assessor PDF: https://ccmap.cccounty.us/HTML5/assessorPDF/178p30x0.pdf
- assessor-map SHA-256: `0480ff4b000aa6593dd85600c4e6165a9359ed5ac3dd42c6c6765b90b84e99da`

The parcel record also contains `full_n_address = 1666 N MAIN ST`. That field is preserved as returned but is **not** treated as changing the Library's official public address.

### Material adjoining civic parcel

The GIS polygon-intersection query returned six non-target candidates. The strongest facility-relevant candidate is:

- APN: `178-300-040`
- display address: `1375 CIVIC DR - WALNUT CREEK`
- owner field: `WALNUT CREEK CITY OF`
- acreage: `7.548`
- same assessor sheet: Book 178 Page 30

Human review of the assessor sheet shows parcel 40 immediately adjoining parcel 39 and labels it `CITY OF WALNUT CREEK`. City sources identify Civic Park Community Center at 1375 Civic Drive, strongly supporting parcel 40 as part of the adjoining Civic Park/City civic complex.

The other intersection results remain screening candidates rather than control conclusions.

## Assessor-map observations

Human review of Book 178 Page 30 confirms:

- parcel `39`, `CITY OF WALNUT CREEK`, `2.202 Ac`;
- parcel `40`, `CITY OF WALNUT CREEK`, `7.548 Ac`;
- separate City parcel `37`, approximately `2.0 Ac`, south/across North Broadway;
- North Broadway, Lincoln Avenue, Civic Drive, North Main Street and Carlback Avenue;
- `RANCHO DOLORES SUB'N MB 2-36 7/26/1909`;
- `OAK PARK SUB'N MB 18-385 3/4/1922`;
- `FM 19-25, 20-29`;
- notation `NE COR. LEASE 1217 OR 76`.

The lease notation remains a record-reference lead only. The assessor sheet's own assessment-purpose disclaimer is retained.

Review:

`assessor-map-review-2026-09-22.md`

## Recorded-map index findings

Contra Costa Public Works' public Recorded Maps index was queried anonymously/read-only.

### APN metadata search

`APN = 178 30` returned zero exact metadata hits. This is a negative search result, not proof that no relevant recorded map exists.

### Historical assessor references

**Rancho Dolores — Book 2 Page 36**

- `2M36`
- entry `482387`
- `Subdivision Map`
- APN metadata `178 030`
- Walnut Creek
- recorded 7/26/1909
- `RANCHO DOLORES`

**Oak Park — Book 18 Page 385**

- `18M385`
- entry `128855`
- `Subdivision Map`
- Walnut Creek
- recorded 3/4/1922
- engineer/surveyor `CLYDE LAIRD`
- permit `SD1922-01083`
- `OAK PARK`
- road-vicinity metadata includes Main Street and Lincoln Avenue

These are historical-chain records, not modern boundary/ROW conclusions.

Review:

`recorded-map-review-2026-09-22.md`

## Facility Prep second-site validation

Sweep 008 exposed and fixed a source-enumeration bug in the recorded-map adapter. The initial resolver accepted the assessor shorthand `MB` but did not constrain WebLink's actual `Record Type` field to `Subdivision Map`.

The corrected live test generated source queries containing:

`[Record Type]="Subdivision Map"`

and returned exactly one matching subdivision map for each tested assessor reference.

Live validation:

- run `35779391449`
- job `106920689651`
- conclusion **success**
- artifact `10716842873`
- artifact ZIP SHA-256 `91f683b20188b3f70bb0480df8ef4cf014c399ee410f40fb4f70e3dc6d3432d4`

Full checkpoint:

`facility-prep-second-site-validation-2026-09-22.md`

The reusable lesson is now enshrined in `docs/research/FACILITY-PREP-SOP.md`.

## Facility / access / design evidence

### CCCL branch page

https://ccclib.org/locations/26/

Current public facts include:

- Monday–Thursday 10 a.m.–8 p.m.; Friday–Saturday 9 a.m.–5 p.m.; Sunday closed;
- cafe, computer lab, meeting room and study room;
- Library underground garage: 120 spaces, four-hour limit;
- Library surface lot: 20 four-hour spaces and 10 thirty-minute spaces;
- separate nearby Broadway Garage at 1390 N. Broadway.

The Broadway Garage is not treated as part of the Library parcel.

### Current Self-Service Sunday status

CCCL's current FAQ lists Self-Service Sundays at Concord and San Pablo, with Pittsburg coming soon. Walnut Creek is not listed and its branch page lists Sunday closed.

Review:

`self-service-sunday-status-2026-09-22.md`

### City design history

https://www.walnutcreekca.gov/home/showpublisheddocument/84/635672432775130000

The City's design-period description states that the Library was designed to be accessible from:

- a new civic plaza at Broadway and Lincoln;
- a formal Broadway entrance;
- the surface parking lot;
- a Civic Park entrance.

It also states that the underground garage was intended to serve Library patrons, community-center users and other downtown visitors.

### Public-art plan

https://www.walnutcreekca.gov/home/showpublisheddocument/11536/636136819628970000

The City Public Art Master Plan identifies Civic Park walkways/entries, sidewalks/street furniture and `Library Outdoor Plazas` as potential public-art sites.

### Civic Park

Current City park directory:

https://www.walnutcreekartsrec.org/Home/Components/FacilityDirectory/FacilityDirectory/45/1920

Current public facts include:

- 1375 Civic Drive;
- 16.7 acres;
- dawn-to-dusk access;
- Library, Community Center, parking, picnic area, restrooms and trail connections;
- connections to the Iron Horse Trail and Creek Walk.

Current access/control review:

`current-access-control-review-2026-09-22.md`

## Exterior forum analysis

Canonical area-by-area note:

`exterior-forum-analysis-2026-09-22.md`

Current documentary posture:

| Area | Current status |
| --- | --- |
| Actual North Broadway municipal sidewalk / ROW | **TPF — HIGH CONFIDENCE; exact edge pending where ambiguous** |
| Actual Lincoln Avenue municipal sidewalk / ROW | **TPF — HIGH CONFIDENCE; exact edge pending where ambiguous** |
| Broadway–Lincoln civic plaza / Library outdoor plaza | ***Prigmore* TPF treatment strongly supported; physical verification pending** |
| Formal Broadway entrance / immediate exterior approach | ***Prigmore* TPF treatment strongly supported; field verification pending** |
| Civic Park entrance / connective pedestrian route | **TPF treatment strongly supported; exact line pending if material** |
| Civic Park proper | **TPF — HIGH CONFIDENCE; ordinary park/reservation rules remain applicable** |
| Library surface lot | ***Prigmore* TPF treatment strongly supported for lawful pedestrian expressive use; safety rules remain material** |
| Underground Library garage | **PUBLIC-ACCESS-VERIFIED / FORUM-UNRESOLVED** |
| Garage ramps / vehicle portals | **No broad speech-zone conclusion** |
| Garage pedestrian nodes | **UNRESOLVED / SUBAREA-SPECIFIC** |
| Children's patio | **PURPOSE/ACCESS REVIEW REQUIRED** |

*Prigmore* is used as a forum comparator, not a stand-alone right-to-record holding.

## Room / control evidence

### Oak View Room

Current City source:

https://www.walnutcreekartsrec.org/parks-facilities/facility-rentals/walnut-creek-library-oak-view-room

Current City materials show:

- City Facility Rentals management;
- second-floor room;
- meetings, corporate events, trainings, book signings, dinners/social events among identified uses;
- Library-programming priority during Library hours;
- separate after-hours entrance;
- after-hours use while the rest of the Library is closed;
- metered underground parking accessible after hours.

Current forum posture:

`LIMITED-PUBLIC-FORUM TREATMENT STRONGLY SUPPORTED / EVENT-SPECIFIC RULE APPLICATION REMAINS`

### Las Trampas Conference Room

Current live sources:

- https://ccclib.org/las-trampas-room-policy/
- https://ccclib.org/rooms/

The current live policy opens the room to organizations, businesses or groups and provides direct CCCL/online booking.

Current forum posture:

`LIMITED PUBLIC FORUM — STRONGLY SUPPORTED UNDER FAITH CENTER COMPARATOR / PRACTICE VERIFICATION PENDING`

An older 2025-revised system Room Use PDF says both Oak View and Las Trampas arrangements are through City Facility Rentals. The current City Oak View page now expressly states that smaller rooms such as Las Trampas are reserved directly through CCCL.

Working treatment:

`CURRENT-LIVE-SOURCES-SUPPORT-CCCL-LAS-TRAMPAS-BOOKING / OLDER-PDF-DISCREPANCY-PRESERVED`

### Group study rooms

https://ccclib.org/walnut-creek-library-group-study-room-rules/

Four rooms serve individuals/small groups through same-day in-person use, generally up to two hours. Advertising, petitions, solicitations and sales are prohibited.

Status:

`PURPOSE-LIMITED CHANNEL / FINAL CLASSIFICATION UNRESOLVED`

## ROW / current-plan source family

Walnut Creek Engineering:

https://www.walnutcreekca.gov/government/public-works/engineering-services/encroachment-permits

Site-plan standards:

https://www.walnutcreekca.gov/government/community-development-department/permits/building-permits/site-plans-and-diagrams

Building-record request process:

https://www.walnutcreekca.gov/government/community-development-department/permits/building-permits/request-building-records

These are the correct current source family for any outcome-determinative Broadway/Lincoln/plaza/garage boundary question. No publicly indexed current Library site/engineering plan was located during this sweep that fixes those exact edges.

## Photography / videography policy search

> **No dedicated public-facing Walnut Creek-specific ordinary-patron photography/videography rule was located in the online sources reviewed as of September 22, 2026.**

That is a source-review finding, not proof that no internal, posted, program-specific, lease-specific or later rule exists.

## Current confidence by issue

| Question | Current state |
| --- | --- |
| Library APN `178-300-039` | **OFFICIAL-GIS-RESOLVED** |
| GIS owner field `WALNUT CREEK CITY OF` | **OFFICIAL-GIS-RESOLVED** |
| Parcel geometry / assessor map | **OFFICIAL-GIS-RESOLVED / SOURCE-LIMITED** |
| Adjoining City parcel `178-300-040` / Civic Park context | **STRONGLY-SUPPORTED** |
| Assessor parcel 39/40 relationship | **HUMAN-REVIEWED / SOURCE-LIMITED** |
| Rancho Dolores / Oak Park historical identities | **OFFICIAL-INDEX-RESOLVED / HISTORICAL-CHAIN-RELEVANT** |
| Exact modern parcel/ROW edge | **UNRESOLVED WHERE OUTCOME-DETERMINATIVE** |
| Civic plaza / outdoor-plaza public-facing function | **STRONGLY-SUPPORTED** |
| Underground garage public access | **CURRENT-OFFICIAL-SOURCE-VERIFIED** |
| Underground garage forum status | **UNRESOLVED** |
| Oak View current City rental management | **CURRENT-OFFICIAL-SOURCE-VERIFIED** |
| Las Trampas current CCCL booking | **CURRENT-LIVE-SOURCES-STRONGLY-SUPPORTED** |
| Walnut Creek Self-Service Sunday | **NOT CURRENTLY LISTED / SUNDAY CLOSED** |
| Walnut Creek-specific ordinary-patron camera rule | **NOT LOCATED IN SOURCES REVIEWED** |

## Preserved reviewed evidence

- `facility-prep-2026-09-22/report.json`
- `facility-prep-2026-09-22/parcel.geojson`
- `facility-prep-2026-09-22/adjacent-parcels.json`
- `assessor-map-review-2026-09-22.md`
- `recorded-map-review-2026-09-22.md`
- `current-access-control-review-2026-09-22.md`
- `exterior-forum-analysis-2026-09-22.md`
- `facility-prep-second-site-validation-2026-09-22.md`
- `self-service-sunday-status-2026-09-22.md`

## Remaining high-value questions

The documentary sweep no longer requires indiscriminate historical-map retrieval. Remaining work is narrower:

1. current physical/signage verification of plaza, entrances, surface lot and garage;
2. exact modern site/ROW plan only where a few feet could change an enforcement result;
3. current garage conduct/access signs and pedestrian-node layout;
4. cafe lease/control evidence only if that subarea is analyzed;
5. ordinary-interior recording/forum doctrine as the broader library research develops;
6. any future concrete removal/trespass event, analyzed under its actual area/controller/facts.
