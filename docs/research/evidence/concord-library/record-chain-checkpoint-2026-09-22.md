# Concord Library — Recorded-Map / Instrument Checkpoint

**Facility:** Concord Library, 2900 Salvio Street, Concord, CA 94519  
**Prepared:** 2026-09-22  
**Status:** AUTOMATED-PUBLIC-RECORD-DISCOVERY-SUBSTANTIALLY-EXHAUSTED / MANUAL-ROW-RECORD-STAGE

This checkpoint consolidates the deeper recorded-map and recorded-instrument work performed after Facility Prep resolved current APN `111-240-006`, adjoining City parcel `111-240-014`, assessor Book 111 Page 24, and City Road Centerline evidence.

## 1. Assessor annotation → historical survey

The assessor-map annotation `7 LSM 51` was resolved through Contra Costa County Public Works' public Laserfiche `Recorded Maps` search to:

- entry ID `126622`;
- name `7LSM51`;
- record type `Record of Survey Map`;
- recorded maps Book 7, Page 51;
- County APN-book metadata `111 24`;
- recorded September 24, 1940;
- surveyor metadata C. W. Gibbs;
- one scanned page.

The entry has no electronic PDF, but its scanned page is exposed through the ordinary anonymous public Laserfiche viewer. Facility Prep preserved a rendered page and a human review note:

`docs/research/evidence/concord-library/record-of-survey-7LSM51-review-2026-09-22.md`

The survey is historical geometry/provenance evidence. It predates the present Library and current parcel configuration and is not treated as the modern legal boundary.

## 2. APN-wide Public Works recorded-map search

Facility Prep separately searched the Public Works `Recorded Maps` index using APN metadata `111 24` rather than relying only on the single annotation printed on the assessor sheet.

Result:

- hit count: **1**;
- returned record: `7LSM51` only.

This means the current public Recorded Maps index exposed no additional map carrying the exact APN metadata `111 24`. It does **not** prove that no other recorded map, dedication, survey, engineering plan, deed, or easement affects the property.

## 3. Road-vicinity Public Works recorded-map search

To test whether later maps might be indexed by street rather than APN, Facility Prep searched `Road Vicinity` for `SALVIO` and `PARKSIDE`.

### Salvio result

One result was returned:

- `168PM050`, entry `328336`;
- Parcel Map, Book 168 Page 50;
- recorded March 25, 1999;
- APN metadata `121-25`;
- subdivision metadata `PARCEL C BAILEYS ADDITION ACRES`.

The APN metadata does not match the Library's assessor book/page (`111 24`). It is retained as a broad road-name hit only and is **not promoted as Concord Library boundary evidence**.

### Parkside results

Three results were returned:

- `93LSM40`, entry `178793`, APN metadata `128 10`;
- `158PM009`, entry `316859`, APN metadata `124 25`;
- `172PM036`, entry `338664`, APN metadata `117 11`.

None matches assessor book/page `111 24`. They are retained as broad road-name hits only and are **not promoted as Library/Civic Center boundary evidence** absent an independent geographic connection.

## 4. Official Records identifiers

The assessor sheet and 7LSM51 supplied three Official Records references. Contra Costa RecorderWorks recognizes all three through its public Old Book workflow:

| Reference | Public RecorderWorks document ID | Current state |
| --- | ---: | --- |
| `3356 OR 502` | `16109166` | identifier resolved; image not viewable online; manual copy required |
| `636 OR 390` | `12566187` | identifier resolved; image not viewable online; manual copy required |
| `454 OR 154` | `12286714` | identifier resolved; image not viewable online; manual copy required |

Canonical acquisition-target note:

`docs/research/evidence/concord-library/manual-record-acquisition-targets-2026-09-22.md`

The automated acquisition stop rule applies. No paid copy transaction, authentication bypass, CAPTCHA bypass, or alternate image route was attempted.

## 5. Current conclusion

The useful anonymous/publicly machine-readable County record path has now been pushed substantially beyond the original APN lookup:

`address → current APN/geometry → assessor sheet → assessor annotation → historical record of survey → public Recorded Maps APN search → road-vicinity cross-check → exact Official Records identifiers`

No clearly relevant later/current Public Works recorded map surfaced through the tested APN or road-vicinity searches. The remaining exact modern boundary questions should therefore move to **targeted acquisition**, not increasingly broad blind automation.

The decisive remaining targets are:

1. ordinary copies of `3356 OR 502` and `636 OR 390` if their contents are needed to interpret the present parcel chain;
2. City of Concord Engineering records fixing the current Salvio Street and Parkside Drive public-right-of-way edges adjacent to APNs `111-240-006` and `111-240-014`;
3. any current dedication/easement/ROW plan referenced by those engineering records;
4. any City/County agreement that allocates operational control of the Library exterior, Civic Center parking, entrance walks, or shared circulation differently from fee ownership.

Until those records are obtained, current parcel ownership/control context is strongly developed, but the exact legal ROW edge remains unresolved.

## 6. Facility Prep lesson

For future facilities, an APN-wide or road-vicinity recorded-map search should be used as a discovery cross-check, not as an invitation to follow every same-street result. A returned map with mismatched parcel/APN metadata remains an unpromoted lead unless geometry or another official source ties it to the facility.

When exact known instrument identifiers have been resolved and no clearly relevant later map appears in the public index, Facility Prep should stop broad automated searching and generate a targeted custodian/engineering acquisition request.
