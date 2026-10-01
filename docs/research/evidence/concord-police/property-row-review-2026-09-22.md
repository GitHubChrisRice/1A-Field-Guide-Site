# Concord Police Headquarters — Property / ROW Review

**Reviewed:** 2026-09-22

## Current parcel result

The standard Contra Costa / Concord Facility Prep parcel resolver matched Concord Police Headquarters at `1350 Galindo Street` to:

- APN `126-124-036`;
- owner field `CONCORD CITY OF`;
- display address `1350 GALINDO ST - CONCORD`;
- acreage `5.06`;
- building square footage field `71,913`;
- Assessor Book 126 Page 12.

The parcel record contains `full_n_address = 1950 PARKSIDE DR`. That source field is preserved but is not substituted for the Police Department's public facility address.

Current parcel posture:

`OFFICIAL-GIS-RESOLVED / CITY-OWNERSHIP-STRONGLY-SUPPORTED / HUMAN-MAP-REVIEW-COMPLETED / EXACT-LEGAL-BOUNDARY-PENDING-WHERE-MATERIAL`

## Assessor map

Official source:

https://ccmap.cccounty.us/HTML5/assessorPDF/126p12x0.pdf

SHA-256:

`b16a5c0407da51671e7daf89e6f45f4aac1bc711327d0c65c6d57178052f8f6c`

Book 126 Page 12 has been rendered and visually reviewed.

### Target parcel observation

The target is depicted as parcel `36`, approximately `5.06 Ac`, **east of Laguna Street and directly adjoining Galindo Street**. That is consistent with the official public address and with the closest Galindo centerline segment whose right-side address range includes `1350`.

This materially strengthens the current frontage conclusion:

`GALINDO-FRONTAGE-STRONGLY-SUPPORTED / NO-DMV-LIKE-ADDRESS-FRONTAGE-MISMATCH-OBSERVED`

The assessor sheet remains assessment evidence rather than a survey-grade legal-boundary determination.

### `VACATED 94-188992 7-25-94` notation

The assessor sheet contains a visible notation:

`VACATED 94-188992 7-25-94`

Visual review places that notation **west of Laguna Street in the parcel 24 / historical-lot area, not inside target parcel 36**.

Accordingly, the notation is retained as a map observation but is **not promoted as a current Police Headquarters boundary/access lead** absent later evidence tying the referenced vacation to the target parcel or a public approach used by Headquarters.

Current status:

`RECORDED-INSTRUMENT-LEAD-OBSERVED / APPEARS-OUTSIDE-TARGET-PARCEL / NOT-PROMOTED`

This is a useful application of the Facility Prep outcome-determinative gate: there is no reason to chase instrument `94-188992` merely because it appears somewhere on the assessor sheet when the map itself places the notation outside the target parcel.

### Historical map headings

The sheet also carries historical headings including:

- `RANCHO MONTE DEL DIABLO`;
- `FOSKETT'S SECOND ADDITION M.B. 3-73`;
- `JOHNSON'S ADDITION M.B. 20-512`.

Those headings are preserved as historical-chain context. They are not automatically treated as the controlling recorded-map reference for parcel 36 without a tighter parcel-to-map connection.

## Candidate adjoining parcels

The parcel resolver returned three non-target polygon-intersection candidates:

- APN `126-124-030` — 0.816 acre — owner `CONCORD CITY OF`;
- APN `126-124-032` — 0.384 acre — owner `LIU JULIE J` — 1302 Galindo Street;
- APN `126-124-033` — 0.67 acre — owner `CONCORD CITY OF`.

These remain candidate-discovery results rather than automatic legal adjacency/control findings.

The assessor sheet depicts parcel 32 east/northeast of the target and parcel 33 along the northern side of the broader block. The two City-owned candidates may matter to municipal circulation or site configuration, but current physical/site correlation is still required before assigning them a role in the public entrance, parking, or pedestrian path.

## Concord Road Centerlines

The Road Centerlines adapter was run from the target parcel/facility point against Galindo, Mount Diablo, Oak, and Laguna.

The source returned named segments for Galindo, Laguna, and Oak. It did not return a segment with `St_Name = Mount Diablo` for that exact-name query, so no Mount Diablo centerline conclusion is drawn from this run.

### Galindo Street

Closest ranked segment:

- OBJECTID `215722`;
- distance from facility point `61.9 m`;
- Street Owner `Concord`;
- Jurisdiction `Concord`;
- road class `Major Arterial`;
- right-side address range `1350–1370`;
- sidewalk L/R `No / Yes`;
- facility ID `TCL163922`;
- source update `2020-04-27`.

The address range containing `1350`, the official Headquarters address, and the assessor-sheet depiction of parcel 36 adjoining Galindo together make this the strongest current public-frontage lead.

They do not establish the surveyed ROW edge or title to the sidewalk strip.

### Laguna Street

Closest ranked segment:

- OBJECTID `199156`;
- distance `83.3 m`;
- Street Owner `Concord`;
- Jurisdiction `Concord`;
- road class `Collector`;
- sidewalks L/R `Yes / Yes`;
- address ranges L `2001–2099`, R `2000–2098`;
- facility ID `TCL147352`;
- source update `2020-04-27`.

The assessor sheet independently depicts Laguna immediately west of parcel 36, making this a relevant secondary exterior edge.

### Oak Street

Closest ranked segment:

- OBJECTID `227605`;
- distance `148.1 m`;
- Street Owner `Concord`;
- Jurisdiction `Concord`;
- road class `Local`;
- sidewalks L/R `No / No`;
- facility ID `TCL175807`;
- source update `2020-04-27`.

Oak is farther from the target and is not presently treated as the primary public approach.

## Evidentiary limits

The same Facility Prep limits apply:

- centerline geometry is not the surveyed ROW edge;
- a `Street Owner = Concord` attribute is governmental-control evidence, not a title opinion for every adjacent paved area;
- `Sidewalk = Yes` is the GIS dataset's sidewalk characterization, not proof of sidewalk-strip title;
- an address range is not a parcel-boundary survey;
- candidate parcel intersection is not proof of a legally material adjoining relationship;
- none of these GIS facts alone decide forum status or recording rights.

## Current boundary/access posture

Unlike Concord DMV, the evidence does **not** expose an address/frontage mismatch. The target parcel, City ownership, Galindo address range, and assessor geography are mutually consistent.

The remaining high-value physical question is narrower: where, on the current ground layout, do the ordinary municipal sidewalk/ROW, any public parking/drive aisle, the pedestrian approach, entrance threshold, and target parcel/control transitions actually lie?

Current status:

`PROPERTY-CHAIN-CLEANER-THAN-DMV / GALINDO-PUBLIC-FRONTAGE-STRONGLY-SUPPORTED / EXACT-SIDEWALK-ROW-EDGE-AND-PARKING/APPROACH-CONTROL-PENDING-WHERE-OUTCOME-DETERMINATIVE`

The next property task should therefore be current physical/site correlation rather than broad historical title archaeology.

## Probe provenance

GitHub Actions run `35790463489` completed successfully.

Artifact:

- `facility-prep-concord-police-full`;
- artifact ID `10722150330`;
- artifact ZIP digest `sha256:3ec90f203d894df4ba008f5e119cf8704b01b09e6a02471774b140f223a0622e`.
