# Facility Prep — Second-Site Validation Checkpoint

**Facility:** Walnut Creek Library  
**Date:** 2026-09-22  
**Branch:** `field-guide/sweep-08-walnut-creek-library`

## Purpose

Test whether the Facility Prep architecture developed at Concord Library survives a second Contra Costa County Library branch with materially different municipal GIS coverage, parcel geometry, assessor notation, civic context, and public-access subareas.

## Result

**SECOND-SITE VALIDATION SUCCESSFUL, WITH MODULARIZATION REQUIRED.**

The core evidence pipeline transferred successfully, but the test exposed assumptions that correctly remain jurisdiction/source-specific.

## What generalized successfully

The second site successfully completed:

`facility address → official countywide parcel match → APN → current owner/address fields → parcel geometry → GIS intersection candidates → assessor-map download/hash → human assessor review → recorded-map-index follow-up → relevance screening → area-specific legal analysis`

Walnut Creek parcel result:

- APN `178-300-039`;
- owner field `WALNUT CREEK CITY OF`;
- 2.202 acres;
- Assessor Book 178 Page 30;
- facility-relevant adjoining City parcel `178-300-040`, 1375 Civic Drive, 7.548 acres.

## What did not generalize unchanged

### Concord AddressPoint

Concord's AddressPoint enrichment is not a countywide address resolver. Walnut Creek required a countywide parcel-address search instead.

Architecture consequence:

> a countywide parcel core may be reusable even when municipal AddressPoint/road/owned-property enrichment remains city-specific.

### Road/ROW enrichment

Concord's Road Centerlines adapter is a Concord municipal source. It was not reused as though it described Walnut Creek streets.

Walnut Creek ROW research instead starts from Walnut Creek Engineering, current City plans/records, and any Walnut Creek-specific GIS layer later identified.

### Adjacent parcels

The same GIS-intersection method returned six non-target Walnut Creek parcels. Only one — City parcel `178-300-040` at 1375 Civic Drive — was strongly tied by independent evidence to the material Library/Civic Park question.

Architecture consequence:

> intersection results are discovery candidates; they require human relevance screening before promotion.

### Recorded-map type aliases

The Walnut Creek assessor sheet used `MB` for historical subdivision references. The Concord-era recorded-map adapter had only been validated against LSM/record-of-survey and corner-record usage.

The initial Walnut Creek Book/Page query therefore failed to constrain the `Record Type` field even though it still returned identifiable book/page records.

The adapter was corrected to normalize:

- `LSM` / `RS` → `Record of Survey Map`;
- `CR` → `Corner Record`;
- `MB` / `subdivision` → `Subdivision Map`;
- `PM` / `parcel` → `Parcel Map`.

## Live post-fix verification

GitHub Actions run:

- run ID: `35779391449`
- job ID: `106920689651`
- conclusion: **success**
- artifact: `facility-prep-walnut-creek-parcel`
- artifact ID: `10716842873`
- artifact ZIP SHA-256: `91f683b20188b3f70bb0480df8ef4cf014c399ee410f40fb4f70e3dc6d3432d4`.

The corrected Rancho Dolores query generated:

`([Recorded Maps Book]="2" AND [Recorded Maps Page]="36" AND [Record Type]="Subdivision Map")`

and returned exactly one result:

- `2M36`
- entry `482387`
- `Subdivision Map`
- APN metadata `178 030`
- Walnut Creek
- `RANCHO DOLORES`
- recorded 7/26/1909.

The corrected Oak Park query likewise included `Record Type = Subdivision Map` and returned exactly one result:

- `18M385`
- entry `128855`
- `Subdivision Map`
- Walnut Creek
- `OAK PARK`
- recorded 3/4/1922.

This verifies that the fix changed the actual source query rather than merely changing local labels.

## Legal-analysis validation

Walnut Creek also validates the anchor-case comparator design.

The same site contains areas for which different analytic anchors are appropriate:

- ordinary municipal sidewalk → ordinary sidewalk/*Grace* doctrine;
- civic plaza, public entrance, open surface parking → *Prigmore* is a strong comparator;
- public park → traditional park doctrine;
- underground garage → *Prigmore* is not enough; *Cornelius*, *Kokinda*, *Sammartano* and general forum-purpose analysis become materially more important;
- Oak View / Las Trampas opened room channels → *Faith Center* is the closer comparator;
- study rooms / children's patio → separate purpose/access analysis.

The test therefore supports the rule:

> generalize the comparator method, not a facility-type conclusion.

## Research-sufficiency validation

The assessor map exposed century-old subdivision references. Facility Prep resolved their identities, but current City planning/engineering/access sources are more likely to answer present plaza/ROW/garage questions.

The outcome-determinative boundary gate therefore works as intended: preserve the historical chain, but do not turn it into mandatory title archaeology unless a present boundary/easement dispute makes it material.

## Workflow state

The temporary Walnut Creek probe workflow was used with a branch-push trigger during live validation, then returned to manual-only execution after the final successful test. Before the Sweep 008 PR, the temporary workflow was removed from the branch entirely.

Machine-generated output remains artifact-only by default. Reviewed evidence is promoted manually into the facility evidence manifest.

The canonical `.github/workflows/facility-prep.yml` remains the retained prototype workflow; Walnut Creek's validation workflow is intentionally not promoted as a second permanent facility-specific workflow.

## Development consequence

After Concord + Walnut Creek, Facility Prep can reasonably treat the following as reusable architecture within Contra Costa County:

- countywide parcel lookup/normalization;
- assessor-map acquisition and preservation;
- candidate-neighbor discovery plus human relevance screening;
- Contra Costa Public Works recorded-map index adapter;
- evidence-stage separation;
- stop rules;
- outcome-determinative boundary gate;
- anchor-case comparator method.

Municipal AddressPoint, municipal road/ROW, owned-property, site-plan, parking, park, and facility-control sources remain modular enrichments.

The next architecture test should therefore be a **materially different facility category**, rather than pretending another library is necessary to prove every module universal.
