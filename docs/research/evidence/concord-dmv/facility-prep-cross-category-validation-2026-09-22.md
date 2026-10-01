# Facility Prep — Cross-Category Validation Checkpoint

**Facility:** California DMV — Concord Field Office  
**Date:** 2026-09-22  
**Branch:** `field-guide/sweep-09-concord-dmv`

## Purpose

Test whether the Facility Prep architecture developed against two public-library sites survives a materially different government-facility category without importing library-specific property assumptions, policy assumptions, or forum conclusions.

## Result

**CROSS-CATEGORY VALIDATION SUCCESSFUL, WITH A NEW ACCESS-PATH STAGE AND A DOCTRINAL RESET.**

The reusable evidence pipeline transferred to the DMV site, but the first administrative-facility test exposed a new class of problem that the library sites had not forced into the foreground:

> **public facility address ≠ parcel frontage ≠ legal public access path.**

It also confirmed that the legal comparator must reset when the governmental purpose changes.

## What generalized successfully

The Concord DMV completed the reusable chain:

`official facility address → countywide parcel/APN → owner/address fields → candidate adjoining parcels → assessor-map acquisition/hash → human map review → exact recorded-map follow-up → municipal road/sidewalk leads → policy/control research → area-specific forum analysis`

Key current results:

- APN `126-490-004`;
- owner field `CALIFORNIA STATE OF`;
- second owner/name field `DEPT MOTOR VEHICLES`;
- Assessor Book 126 Page 49;
- exact historical subdivision reference `WILLOWICK 4`, Map Book 212 Page 47;
- official Recorded Maps entry `212M47`, entry `148419`, three public imaged pages;
- Concord Road Centerlines results for Diamond Boulevard, Meridian Park Boulevard and Galaxy Way.

The same Contra Costa parcel core therefore transferred from municipal-library property to a State-owned administrative facility without code changes.

## New issue exposed — address/frontage mismatch

DMV and the current parcel feed identify the public facility address as `2070 Diamond Boulevard`.

But both the current assessor sheet and the exact 1978 subdivision map place the land corresponding to the DMV parcel / historical Lot 4 directly on Meridian Park Boulevard while separate Lots/Parcels 1 and 2 lie between it and Diamond Boulevard.

No labeled westward access easement across Lot 1 to Diamond is apparent on the reviewed 1978 subdivision drawing.

That does not establish that no access right exists today. It establishes that the public address is not a sufficient legal substitute for researching the actual access route.

Architecture consequence:

> When a facility address and parcel frontage do not align, Facility Prep should create an `ADDRESS/FRONTAGE-MISMATCH` flag and separately resolve the actual public ingress/egress path before assigning ownership/control or forum consequences to the approach.

Current access evidence may require a later easement, deed, site plan, acquisition file, shared-access agreement, or current engineering record rather than more historical-map searching.

## Municipal enrichment remained modular

Because this DMV is also in Concord, the existing Concord Road Centerlines adapter could legitimately be reused as a **jurisdiction-specific** enrichment.

That is not evidence that a road adapter generalized across facility categories or cities. It means its geographic coverage actually includes this address.

This distinction remains important:

`countywide parcel core + municipality-specific ROW enrichment + facility/agency-specific policy/control research`

## Recorded-map handling transferred successfully

The assessor sheet exposed `TRACT 5292 (WILLOWICK 4) MB 212-47`.

The existing Contra Costa Recorded Maps adapter correctly translated `MB` to source value `Subdivision Map`, resolved the exact index record, and the existing public-page renderer retrieved all three imaged pages.

The resulting evidence clarified the historical street/lot geometry and dedication chain without being treated as a current title opinion.

This confirms that the recorded-map components are reusable evidence-acquisition modules independent of the library category.

## Doctrinal reset

The property pipeline generalized; the **legal anchor did not**.

The library sites had close library-specific exterior authority in *Prigmore* and room-channel authority in *Faith Center*.

For DMV, the closer structure is:

- ordinary municipal sidewalk → *Grace* / ordinary sidewalk doctrine;
- purpose-built government access walk → *Kokinda* / Ninth Circuit *Jacobsen* comparison;
- administrative public lobby → *Cornelius* + published Ninth Circuit *Sammartano*;
- state administrative-lobby factual comparison → unpublished/nonprecedential *Freedom Foundation* only as a close factual comparator;
- recording activity → *Askins*, separately from forum classification;
- California Speech Clause → independently analyzed under current authorities including *Camenzind*, not copied from the federal forum label.

Architecture consequence:

> A cross-category Facility Prep run must reset the area/activity anchor authority from the governmental purpose and physical area. Reuse the comparator **method**, not the previous facility's cases or classifications.

## Agency-purpose rules did not become site-wide restrictions

The DMV test also exposed a useful policy-scope distinction.

DMV publicly identifies significant privacy interests in personal records and publishes a rule that a cell phone may not be used as a testing aid during a knowledge examination.

Neither fact is silently transformed into a general field-office camera ban.

Architecture consequence:

> Preserve the scope of an agency rule at the activity/channel where it applies. A privacy duty or examination-integrity rule is evidence relevant to a specific restriction; it is not itself proof of a facility-wide prohibition.

The current search did not locate a dedicated public-facing California DMV field-office ordinary-patron photography/videography rule.

## Validation run

The complete live cross-category evidence packet was generated successfully in GitHub Actions:

- run ID `35784583396`;
- conclusion **success**;
- artifact `facility-prep-concord-dmv-full`;
- artifact ID `10719403821`;
- artifact ZIP SHA-256 `ed90611aabdf487199d196dbc955800e8dc173ef99df430f13d3d82ea7ba7c3d`.

The artifact contains the parcel evidence, assessor map, Concord road/sidewalk evidence, Recorded Maps result, and the three rendered `212M47` pages. Reviewed conclusions are promoted separately into the facility evidence manifest.

## Cross-category architecture consequence

After Concord Library, Walnut Creek Library and Concord DMV, the project has now validated a reusable core consisting of:

- official facility/address identification;
- countywide parcel/APN normalization where a genuine countywide source exists;
- assessor-map acquisition and hashing;
- candidate-neighbor discovery plus human relevance screening;
- exact recorded-map/reference follow-up;
- public scanned-record rendering where the ordinary public viewer exposes it;
- source-specific municipal ROW enrichment;
- outcome-determinative boundary stop rules;
- raw → normalized → reviewed evidence separation;
- area-specific anchor-authority analysis.

The DMV test adds two durable stages:

1. **frontage/access-path validation** when the public address does not correspond to direct parcel frontage; and
2. **facility-purpose doctrinal reset** before carrying forum conclusions into a new category.

The prototype can now proceed to another materially different facility type without treating its current modules as universally statewide. Source coverage and legal anchors remain explicit, modular and independently validated.
