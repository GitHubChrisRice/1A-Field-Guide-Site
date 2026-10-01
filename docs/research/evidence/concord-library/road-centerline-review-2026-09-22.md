# Concord Library — Road Centerline / ROW Lead Review

**Facility:** Concord Library  
**Address:** 2900 Salvio Street, Concord, California 94519  
**Facility point used by resolver:** 37.98155445, -122.02529236  
**Official layer:** City of Concord BaseMap, Road Centerlines (Layer 8)  
**Layer URL:** https://gis.cityofconcord.org/gsrv1/rest/services/BaseMap/MapServer/8  
**Facility Prep run:** GitHub Actions `35758041991`  
**Verified:** 2026-09-22

## Purpose

This review records official GIS street/sidewalk attributes for the centerline segments closest to the Concord Library AddressPoint and compares them with other official City right-of-way materials. It is a **right-of-way research lead**, not a surveyed right-of-way determination.

The Road Centerlines layer exposes fields including `ST_OWN` (Street Owner), road class, jurisdiction, address ranges, and `SIDEWALK_L` / `SIDEWALK_R`. The resolver queried all features named `Salvio` or `Parkside`, ranked them by distance from the official Concord Library AddressPoint, and preserved the raw JSON/GeoJSON in the Actions review artifact.

## Closest Salvio Street segment

**OBJECTID:** `199013`  
**Distance from facility point:** approximately 43.1 m  
**Street owner field:** `Concord`  
**Concord road class:** `Collector`  
**RoadClass:** `S1400`  
**Jurisdiction:** `Concord`  
**Street type:** `Street`  
**Sidewalk left:** `Yes`  
**Sidewalk right:** `Yes`  
**Left address range:** 2901–2971  
**Right address range:** 2900–2936  
**GIS update date returned:** 2020-04-27

The facility address `2900 Salvio Street` falls within the returned **right-side address range** for this closest centerline segment. That is useful for orienting the segment relative to the facility, but it is not itself a legal boundary or sidewalk-title determination.

## Closest Parkside Drive segment

**OBJECTID:** `199079`  
**Distance from facility point:** approximately 36.4 m  
**Street owner field:** `Concord`  
**Concord road class:** `Collector`  
**RoadClass:** `S1400`  
**Jurisdiction:** `Concord`  
**Street type:** `Drive`  
**Sidewalk left:** `Yes`  
**Sidewalk right:** `Yes`  
**Left address range:** 1901–1999  
**Right address range:** 1900–1998  
**GIS update date returned:** 2020-04-27

The Civic Center candidate parcel is returned by the parcel layer as `1950 Parkside Drive`, which falls within this segment's **right-side address range**. That helps correlate the street segment with APN `111-240-014`; it does not establish the legal parcel/ROW line.

## Supplemental official City ROW evidence

### Encroachment / sidewalk treatment

City of Concord Encroachment page:

https://www.cityofconcord.org/277/Encroachment

The City states that an encroachment permit is required for work or encroachment in public right-of-way and identifies curb/gutter, sidewalks, driveways, and sewer laterals as standard items of work in public ROW. This supports the project's treatment of sidewalk/driveway location as a ROW question rather than assuming the parcel line follows the visible curb or sidewalk.

The City's FAQ also expressly addresses responsibility for a **sidewalk within the public right-of-way**, confirming that Concord recognizes sidewalk areas that lie within public ROW:

https://www.cityofconcord.org/m/FAQ

Neither source identifies the exact ROW edge at 2900 Salvio.

### East Downtown pedestrian project

The City's adopted FY 2018-19 / FY 2019-20 Capital Improvement Program includes East Downtown Concord pedestrian improvements on Parkside Drive and Salvio Street:

https://www.cityofconcord.org/DocumentCenter/View/586/Adopted-Biennial-Capital-Budget-for-Fiscal-Year-2018-to-2019-and-2019-to-2020-PDF

For that project the City stated that the sidewalk improvements were anticipated to occur within City right-of-way, while also warning that construction easements/right-of-entry might be required and that **boundary surveys must be performed to locate exact property lines**. The project included a Parkside Drive segment beginning at Salvio Street.

This is unusually useful methodology evidence: the City's own project documents distinguish an anticipated City-ROW condition from the survey work needed to establish exact property lines. Sweep 007 should make the same distinction.

### Current sidewalk-gap records

A 2026 City bicycle/pedestrian planning record identifies Parkside Drive from Salvio Street toward Bonifacio Street as a sidewalk-gap segment and separately lists Salvio Street segments:

https://www.cityofconcord.org/AgendaCenter/ViewFile/Agenda/_06102026-1321

This supports continued City planning/control activity along these streets, but does not establish the exact ROW boundary at the library parcel.

## What this resolves

Current official evidence now supports that the road-centerline segments immediately associated with the library/Civic Center frontage are characterized by the City dataset as:

- **Street owner:** Concord;
- **Jurisdiction:** Concord;
- **Road class:** Collector;
- **Sidewalk presence:** Yes on both sides of the closest Salvio and Parkside segments.

Additional City engineering/planning material treats sidewalk work on these corridors as a City-ROW issue and, importantly, recognizes that exact property lines require boundary-survey-level work.

These are useful governmental-control and physical-context facts for the deeper boundary investigation.

## What this does not resolve

The current City GIS and planning/engineering sources do **not** by themselves establish:

- the surveyed edge of the Salvio Street or Parkside Drive public right-of-way;
- whether a particular sidewalk slab lies wholly in ROW, wholly on an adjoining parcel, or crosses a boundary;
- title to the sidewalk strip;
- dedications, easements, encroachments, setbacks, or reciprocal access rights;
- operational control of the library parking lots or entrance approaches;
- constitutional forum classification.

The current project should therefore describe the street-owner and sidewalk fields as **official GIS attributes** and the City's ROW references as supporting context, while keeping the exact legal ROW boundary **UNRESOLVED** pending engineering, dedication, recorded-map, survey, or equivalent evidence.

## Next documentary targets

1. City engineering / public-works right-of-way or street-dedication material for the Salvio/Parkside frontage around APNs `111-240-006` and `111-240-014`.
2. Underlying recorded records associated with assessor-sheet notations `3356 OR 502` and `636 OR 390`, if retrievable.
3. Any subdivision/parcel map or record of survey that fixes the relevant street or parcel geometry more strongly than the GIS centerline layer.
4. Physical overlay of the confirmed ROW/parcel lines onto the front parking lot, entrance walk/forecourt, rear Civic Center lot, and public sidewalks.

Only after those steps should the project apply *Prigmore* to a specific Concord exterior area.
