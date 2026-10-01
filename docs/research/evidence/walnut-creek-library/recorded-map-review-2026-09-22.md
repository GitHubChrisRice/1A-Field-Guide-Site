# Walnut Creek Library — Recorded Map Review

**Research date:** 2026-09-22  
**Custodian:** Contra Costa County Public Works Recorded Maps / Laserfiche WebLink  
**Public search:** https://records.pw.contra-costa.org/WebLink/CustomSearch.aspx?SearchName=RecordedMaps&dbid=0&repo=PWRecords

## Purpose

Follow the historical map references printed on Assessor Book 178 Page 30 and determine whether the County's public recorded-map index contains facility-relevant records.

The search was performed through the same anonymous, read-only form/query/listing services used by the public WebLink client. No authentication, CAPTCHA, access-control, or paid-copy restriction was bypassed.

## 1. APN / assessor-book metadata search

Search field:

`APN = 178 30`

Result:

- search generated successfully;
- `hitCount = 0`;
- `failed = false`.

Interpretation:

This establishes only that the Recorded Maps index did not return a record whose **current indexed APN metadata exactly matched `178 30`**. It is not proof that no relevant recorded map exists. Historical subdivision maps may predate modern APNs, may carry older assessor-book formatting, or may be discoverable only by book/page, tract/subdivision, permit, or geographic metadata.

## 2. Rancho Dolores — assessor reference `MB 2-36`

The first probe searched Book `2`, Page `36`. Because the then-current adapter did not yet map the user-facing `MB` alias to the WebLink option `Subdivision Map`, the initial query was broader than intended and returned four record types sharing that book/page.

Human relevance screening identified one exact match to the assessor annotation:

- name: `2M36`
- entry ID: `482387`
- record type: `Subdivision Map`
- APN metadata: `178 030`
- city: `Walnut Creek`
- date recorded: `7/26/1909`
- subdivision name: `RANCHO DOLORES`
- Book: `2`
- Page: `36`

This independently verifies the identity of the historical subdivision reference printed on Assessor Book 178 Page 30.

The other Book 2/Page 36 hits had different record types and/or APN/geographic metadata and were not promoted as facility evidence merely because the book/page numbers coincided.

## 3. Oak Park — assessor reference `MB 18-385`

The Book `18`, Page `385` search returned one record:

- name: `18M385`
- entry ID: `128855`
- page count: `2`
- city: `Walnut Creek`
- date recorded: `3/4/1922`
- engineer/surveyor: `CLYDE LAIRD`
- permit: `SD1922-01083`
- record type: `Subdivision Map`
- Book: `18`
- Page: `385`
- road vicinity: `MAIN ST, SPENCER, LINCOLN AVE, CAMPLIN AVE, DEWING WAY`
- subdivision name: `OAK PARK`

This exactly corresponds to the `OAK PARK SUB'N MB 18-385 3/4/1922` annotation on the assessor sheet.

## 4. Adapter lesson and correction

Sweep 008 exposed a useful generalization defect in `laserfiche_recorded_map_lookup.py`.

The Concord prototype had only needed aliases for:

- `LSM` / record of survey;
- `CR` / corner record.

When Walnut Creek introduced old assessor annotations using `MB`, the adapter accepted the argument but failed to select the WebLink `Record Type = Subdivision Map` option. The book/page query itself remained valid and the relevant records could be screened manually, but the request was not as narrowly constrained as intended.

The adapter was corrected during Sweep 008 to support:

- `LSM` / `RS` → Record of Survey;
- `CR` → Corner Record;
- `MB` / `subdivision` → Subdivision Map;
- `PM` / `parcel` → Parcel Map.

This is precisely why the Facility Prep SOP requires a second same-category validation before treating a jurisdiction adapter as generalized.

## 5. Evidentiary value

Current status:

- Rancho Dolores map identity: **OFFICIAL-INDEX-RESOLVED / HISTORICAL-CHAIN-RELEVANT**
- Oak Park map identity: **OFFICIAL-INDEX-RESOLVED / HISTORICAL-CHAIN-RELEVANT**
- present Library parcel geometry: **not established by these historical records alone**
- present North Broadway/Lincoln ROW: **UNRESOLVED by these records**
- present plaza/parking/garage control: **UNRESOLVED by these records**

The recorded-map search should therefore not become an archaeological detour. Current City plans, engineering/ROW sources, and current operational documents have greater potential to change the present forum/removal analysis.

Under the outcome-determinative boundary gate, deeper retrieval of these century-old subdivision maps should be pursued only if a current disputed boundary/easement question makes their contents material.
