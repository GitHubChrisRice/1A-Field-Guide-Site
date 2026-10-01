# Concord Library — Recorded-Record Lookup Review

**Facility:** Concord Library  
**Address:** 2900 Salvio Street, Concord, California 94519  
**Library APN:** 111-240-006  
**Adjacent Civic Center APN:** 111-240-014  
**Reviewed:** 2026-09-22

## Purpose

The Contra Costa County assessor sheet for Book 111 Page 24 prints `3356 OR 502` on the Library parcel and `636 OR 390` on the adjacent City of Concord parcel. Official County-hosted legal descriptions use the same `#### OR ###` convention for **Book #### of Official Records, Page ###**.

Facility Prep therefore tested whether Contra Costa County's public RecorderWorks system could resolve those exact historical book/page references without browser automation, authentication, CAPTCHA bypass, purchase, or record modification.

## Public protocol discovery

RecorderWorks' public JavaScript exposes an Old Book `Display Document` workflow that posts to:

`Presentors/OldBookPresentor.aspx`

The public client sends book/page values and receives an opaque document identifier when the record is recognized. Facility Prep reproduced that read-only request in an ordinary anonymous session.

## Book 3356, Page 502

RecorderWorks accepted the exact book/page lookup with the recording-year field left blank and returned:

- **document identifier:** `16109166`
- **recording-year value required:** none / blank
- **server-side error marker:** none from the Old Book lookup

Facility Prep then passed that identifier to the same public ImagePresentor route used by RecorderWorks. The response was:

> Images may not be viewed online

No document image, instrument text, party names, document type, or legal description was exposed through that viewer response.

A separate read-only test of the site's public DetailsPresentor endpoint returned the same server error for several ordinary parameter variants:

`Error in DetailsPresentor : Render : Nullable object must have a value.`

Accordingly, the project has **resolved the RecorderWorks record identifier**, but has **not retrieved or interpreted the instrument**.

## Book 636, Page 390

RecorderWorks likewise accepted the exact book/page lookup with the recording-year field left blank and returned:

- **document identifier:** `12566187`
- **recording-year value required:** none / blank
- **server-side error marker:** none from the Old Book lookup

The public ImagePresentor response again stated:

> Images may not be viewed online

The DetailsPresentor probe produced the same nullable-value server error and exposed no useful instrument metadata.

Accordingly, the project has **resolved the RecorderWorks record identifier**, but has **not retrieved or interpreted the instrument**.

## Evidentiary consequence

This materially improves the research chain:

- the assessor-sheet references are no longer merely unexplained printed notations;
- each exact historical book/page reference is recognized by the County's public RecorderWorks system;
- each resolves reproducibly to a specific RecorderWorks document identifier;
- the County's public online viewer does not expose the underlying images for these records.

This does **not** establish:

- instrument type;
- grantor/grantee or other parties;
- recording date;
- present title;
- easement scope;
- dedication or right-of-way effect;
- legal boundary consequence;
- operational control;
- forum status.

The underlying instruments must still be obtained from the custodian or another official source and reviewed.

## Facility Prep disposition

Current normalized status:

- `3356 OR 502` → **OFFICIAL-RECORD-IDENTIFIER-RESOLVED / IMAGE-NOT-AVAILABLE-ONLINE / MANUAL-COPY-REQUIRED**
- `636 OR 390` → **OFFICIAL-RECORD-IDENTIFIER-RESOLVED / IMAGE-NOT-AVAILABLE-ONLINE / MANUAL-COPY-REQUIRED**

Facility Prep should stop automated acquisition at this point rather than attempt to evade the public viewer's image restriction or initiate a paid transaction without human authorization.

## Manual acquisition target

The Clerk-Recorder can now be given exact references rather than a broad research request:

1. **Book 3356 of Official Records, Page 502** — RecorderWorks document identifier `16109166`.
2. **Book 636 of Official Records, Page 390** — RecorderWorks document identifier `12566187`.

The purpose is to obtain ordinary copies for research and determine what those instruments actually establish about the Concord Library and Civic Center property. A certified copy is not necessary for the current research stage unless a later evidentiary need specifically requires certification.

## Preservation

Successful automated runs:

- RecorderWorks protocol discovery: GitHub Actions run `35760629012`.
- Old Book exact-record lookup: GitHub Actions run `35760918075`.
- Details/metadata probe: GitHub Actions run `35761235747`.

The review artifacts preserve the public page structure, JavaScript protocol evidence, lookup responses, document identifiers, ImagePresentor responses, and unsuccessful DetailsPresentor responses.
