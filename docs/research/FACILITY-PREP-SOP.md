---
title: Facility Prep SOP
jurisdiction: California
last_verified: 2026-09-22
status: project-methodology
---

# Facility Prep SOP

## Purpose

Facility Prep is the pre-publication research workflow that builds a reproducible evidence packet for a Registry facility before any field verification or final legal classification.

The Registry publishes reviewed facility findings. Facility Prep acquires, preserves, normalizes, and flags the underlying facility-specific evidence used to build those findings.

## 1. Standard property pass

Every facility should receive a baseline property/boundary pass wherever practical, even when the site initially appears simple.

The baseline pass should attempt to establish:

1. official facility address;
2. parcel/APN or equivalent identifier;
3. current record-owner field from an official source;
4. operational agency/controller when separately identifiable;
5. official parcel geometry or map reference;
6. immediately adjacent parcels relevant to entrances, sidewalks, plazas, parking, or campus circulation;
7. obvious public-right-of-way, easement, lease, shared-control, or joint-use questions;
8. source provenance and retrieval date;
9. boundary confidence: VERIFIED, PARTIALLY-VERIFIED, or UNRESOLVED.

A deeper boundary pass is required whenever those facts could materially affect access, forum, removal, trespass, or the location from which expressive activity occurs.

## 2. Automated official-source enrichment

When an agency or jurisdiction exposes a reliable machine-readable official source, Facility Prep should attempt automated acquisition before requiring repetitive manual lookup.

Preferred machine-readable sources include:

- ArcGIS REST / FeatureServer / MapServer query endpoints;
- official GIS/open-data APIs;
- county parcel shapefiles or geodatabases;
- official address-point datasets;
- official assessor endpoints;
- Socrata or equivalent government open-data APIs.

Automation is an acquisition aid, not an authority upgrade. A value returned by an official GIS service remains subject to the source's own limitations.

## 3. Preserve the result, not just a live lookup

A Registry entry should not depend on a live API call every time a reader opens the page.

For material machine-readable evidence, Facility Prep should preserve enough of the returned result to establish what the project reviewed on that date. Depending on the source, this may include:

- raw JSON response;
- GeoJSON parcel geometry;
- API/service URL and layer ID;
- query terms or address used;
- parcel/APN;
- source fields relied upon;
- retrieval timestamp;
- generated summary;
- static map/export/screenshot when useful.

The live official source should also be retained when available.

## 4. Human review before Registry promotion

Machine-generated output should not automatically alter a published Registry conclusion.

A reviewer should confirm:

- the returned facility/address match is plausible;
- the APN/parcel match is not an adjacent or mailing-address false positive;
- owner/control fields are being interpreted correctly;
- known source disclaimers are retained;
- adjacent-parcel results are treated as candidates rather than legal conclusions;
- unresolved ROW/easement/control questions remain flagged;
- stronger recorded-map, survey, deed, engineering, or agreement evidence is pursued when outcome-determinative.

Only reviewed results should be promoted into the facility evidence manifest.

## 5. Manual fallback

If automation is unavailable, blocked, ambiguous, or unreliable, perform the equivalent official-source lookup manually and document it.

Manual lookup is not a failure state. Some jurisdictions may require interactive assessor portals, CAPTCHA, proprietary viewers, clerk/recorder searches, or public-records requests.

The manual record should preserve the same provenance fields as automated acquisition wherever possible.

## 6. Deeper boundary chain

When property geography matters, continue beyond the APN as necessary:

`address → APN → assessor parcel map → recorded map/survey → adjacent parcels → public ROW/dedication → easements/access rights → ownership/control agreements → physical-area overlay → forum analysis`

Keep separate:

- fee ownership;
- operational control;
- public access;
- right-of-way status;
- easements/dedications;
- constitutional forum classification.

One does not automatically establish another.

## 7. Adapter model

Facility Prep should use jurisdiction/source adapters rather than assume one statewide parcel API.

Each adapter should normalize its output into a common evidence structure containing, when available:

- input facility/address;
- jurisdiction;
- source service and layer/dataset;
- APN/parcel identifier;
- owner fields;
- facility/site address fields;
- parcel geometry;
- acreage;
- assessor/parcel-map references;
- candidate adjacent parcels;
- government-owned-parcel layer match, when available;
- retrieval timestamp;
- source limitations;
- confidence flags;
- unresolved follow-up questions.

The first adapter is the City of Concord ArcGIS prototype for 2900 Salvio Street.

## 8. Legal-analysis boundary

Facility Prep may report factual source results such as:

> Official parcel service returned APN X and owner field Y.

It must not automatically conclude:

> This sidewalk is private property.

or:

> Recording is prohibited/permitted here.

Those conclusions require the Field Guide's legal analysis, stronger boundary evidence where necessary, and the actual physical-area facts.

## 9. Facility evidence directory

Material property/boundary evidence should be tracked in:

`docs/research/evidence/<facility-slug>/README.md`

Generated prototype output should remain outside the repository by default until reviewed. The current prototype writes to `facility-prep-output/`, which is git-ignored; GitHub Actions may upload that directory as a review artifact.

## 10. Prototype gate

Before generalizing a Facility Prep component statewide, test it against at least two facilities in the same category and then a materially different facility type.

Validation sequence completed to date:

1. Concord Library — first parcel/boundary prototype;
2. Walnut Creek Library — same-category reproducibility test and modular-adapter validation;
3. Concord DMV — first cross-category test against a State administrative-service facility.

The Concord DMV test validates the reusable evidence-acquisition method across categories, but it does **not** make every source adapter, physical-area inference, or legal anchor universal. The next architecture tests should deliberately choose materially different access/control regimes rather than repeat a parcel pattern that has already been validated.

Only patterns that survive the relevant source coverage, physical configuration, and legal-purpose tests should become generalized Registry automation.

## 11. Assessor-map and image-only source handling

Facility Prep should follow an official parcel-map or assessor-map link automatically when the parcel source exposes one and the source can be downloaded reliably.

For a material map, preserve when practical:

- source URL;
- retrieval timestamp;
- original PDF or image in the review artifact;
- SHA-256 hash of the retrieved source;
- page count;
- extracted text when available;
- candidate map/survey/record references found in extractable text;
- target and adjacent parcel identifiers associated with the map.

A failed text-extraction step must **not** be interpreted as absence of annotations, easements, right-of-way clues, deed references, or other map content. Many assessor maps are image-only or contain vector text that ordinary PDF extraction cannot recover.

When text extraction is empty or unreliable:

1. preserve the original map;
2. flag `MANUAL-MAP-REVIEW-REQUIRED`;
3. render or otherwise visually inspect the map when practical;
4. record the exact notation seen rather than silently interpreting abbreviations;
5. identify potentially relevant recorded-document, book/page, easement, dedication, ROW, survey, or revision references as **research leads**;
6. retrieve the underlying record before treating the notation as dispositive.

The reviewed facility evidence manifest should distinguish:

- **machine-resolved fact** — for example, the official API returned APN `111-240-006`;
- **map observation** — for example, the assessor sheet labels parcel `06` as `LIBRARY`;
- **record-reference lead** — for example, the map prints an unexplained `OR` notation;
- **legal conclusion** — which remains outside Facility Prep until the underlying authority and Field Guide analysis support it.

## 12. Facility Prep output stages

A mature parcel/boundary adapter should strive to produce three layers of output:

1. **raw evidence** — untouched JSON/GeoJSON/PDF or equivalent source material;
2. **normalized evidence** — APN, owner fields, acreage, address, map URL, adjacent candidates, hashes, confidence and unresolved-task fields;
3. **review note** — human-confirmed observations suitable for promotion into the facility evidence manifest.

The Registry should consume the reviewed layer, while retaining links to the raw and normalized evidence so a later reviewer can reproduce the chain.

## 13. Street / right-of-way research leads

When the facility fronts a public street or an exterior forum question depends on a sidewalk, driveway, street margin, median, plaza approach, or similar edge condition, Facility Prep should look for official street/ROW datasets in addition to parcel data.

Potential machine-readable sources include:

- road-centerline layers;
- street-owner or street-maintenance layers;
- sidewalk inventories;
- right-of-way polygons or lines;
- encroachment/engineering GIS;
- street-dedication or subdivision layers;
- maintained-road datasets.

Useful fields may include street owner, jurisdiction, road class, address ranges, sidewalk presence, steward/maintainer, facility ID, notes, and update date.

These fields should be normalized and preserved as **ROW research leads**, not silently converted into surveyed boundaries. In particular:

- a road-centerline geometry does not establish the ROW edge;
- a `Street Owner = City` field is governmental-control evidence, not a complete title opinion;
- a `Sidewalk = Yes` field establishes the dataset's sidewalk characterization, not title to the sidewalk strip;
- an address range may help orient which side of a centerline corresponds to a facility, but does not establish the property line;
- the exact ROW edge should remain **UNRESOLVED** until supported by engineering, dedication, recorded-map, survey, deed, or equivalent evidence appropriate to the question.

When the dataset returns many same-named streets, the adapter may rank candidate segments by distance from the facility's official address point or parcel geometry. It should preserve the full query result while clearly identifying the ranking method.

A reviewed street/ROW lead should record:

- layer/service and layer ID;
- segment/OBJECTID;
- street name and type;
- distance or other method used to select the relevant segment;
- street-owner and jurisdiction fields;
- road class;
- sidewalk-left/right fields;
- address ranges;
- source update date when returned;
- what stronger evidence is still required.

The first tested implementation is the Concord Road Centerlines adapter for Salvio Street and Parkside Drive around Concord Library.

## 14. Recorded-record portals and acquisition boundaries

When an assessor map, deed, survey, engineering record, or other official source identifies a specific recorded instrument, Facility Prep should attempt to resolve that reference through the custodian's public index before asking a researcher to perform a broad manual search.

A recorded-record adapter may, where the public system supports it:

- inspect the public portal and its ordinary client-side protocol;
- reproduce public read-only index/search requests;
- submit exact known identifiers such as book/page, instrument number, APN, or document number;
- preserve returned record identifiers and metadata;
- preserve a public document image only when the custodian makes that image available through the ordinary unmetered public viewer;
- record the exact point at which manual acquisition becomes necessary.

The adapter must not:

- bypass authentication, CAPTCHA, rate limits, access controls, or a viewer restriction;
- use alternate technical endpoints to evade an express `image not available online` condition;
- initiate a paid purchase, order, certification, or copy transaction without human authorization;
- treat a resolved index/document identifier as proof of the instrument's contents or legal effect.

When the public index recognizes the exact record but the underlying image is not available online, normalize the result as:

`OFFICIAL-RECORD-IDENTIFIER-RESOLVED / IMAGE-NOT-AVAILABLE-ONLINE / MANUAL-COPY-REQUIRED`

At that point Facility Prep should stop automated acquisition and produce a manual acquisition target containing, when available:

- custodian/portal;
- exact book/page or instrument number;
- portal document identifier;
- APN/facility relationship;
- why the record matters;
- whether an ordinary copy is sufficient for current research;
- the unresolved legal/factual questions the document may answer.

A failed metadata endpoint is itself useful workflow information but is not evidence about the instrument. Preserve the error or limitation and move to the custodian-copy stage rather than guessing.

The first tested implementation is Contra Costa RecorderWorks for Concord Library, where Book 3356/Page 502, Book 636/Page 390, and the historical Book 454/Page 154 reference each resolve to a specific public RecorderWorks document identifier but the public viewer responds that images may not be viewed online.

## 15. Recorded-map discovery relevance and stop rule

When a custodian exposes a searchable recorded-map index, Facility Prep should use exact facility identifiers before broad text discovery whenever possible.

A preferred escalation sequence is:

`specific map reference → APN / assessor-book metadata → road-vicinity or equivalent geographic metadata → targeted custodian/engineering request`

Search results must be screened for **facility relevance** before promotion. A same-street or same-road-vicinity hit is not enough by itself. Compare returned APN/parcel metadata, subdivision/tract information, map date, geography, and any available geometry against the facility evidence already established.

Use these states:

- `FACILITY-RELEVANT` — independent evidence ties the returned map to the facility/current-adjacent parcel;
- `HISTORICAL-CHAIN-RELEVANT` — the map is tied to a predecessor tract or historical chain but does not establish the current boundary;
- `BROAD-GEOGRAPHIC-HIT / NOT-PROMOTED` — a road/name query returned the record, but parcel or geographic evidence does not tie it to the facility;
- `RELEVANCE-UNRESOLVED` — metadata are insufficient to decide.

Do not retrieve and interpret every road-name hit merely because the search engine returned it. Preserve broad-result metadata when useful, but prioritize records whose identifiers or geography actually intersect the facility research question.

If:

1. the exact assessor/map references have been followed;
2. an APN/parcel-metadata search has been run where available;
3. a reasonable geographic/road-vicinity cross-check has found no clearly relevant later map; and
4. exact legal ROW or parcel edges remain outcome-determinative,

then broad automated map discovery is **substantially exhausted** for that source. Stop widening automated searches and generate a targeted request to the responsible engineering/survey/records custodian for the controlling current ROW, dedication, survey, or plan records.

The Concord Library prototype established this stop rule: the APN-metadata search for `111 24` returned only historical `7LSM51`; Salvio/Parkside road-vicinity searches returned later maps with mismatched APN metadata and no independent tie to the Library/Civic Center parcels. The appropriate next step is targeted City Engineering/current-record acquisition, not blind pursuit of those unrelated road-name hits.

## 16. Outcome-determinative boundary gate

Property research should be rigorous, but it should not become an artificial prerequisite to legal analysis when the unresolved boundary fact would not change the legal result.

Before delaying forum analysis for another deed, survey, ROW record, easement, or operating agreement, ask:

> **Would a reasonably plausible answer to this unresolved boundary/control question change the area classification, applicable legal standard, or enforcement analysis?**

If **yes**, keep the boundary issue open and pursue the stronger record before assigning a final classification. Typical examples include:

- a visually continuous walkway that could be either municipal ROW or a restricted facility path;
- a plaza crossing public and private parcels;
- a removal/trespass dispute in which the person's exact position matters;
- a shared parking area whose controller imposes materially different access conditions;
- an easement whose scope determines whether public passage or expressive use is permitted.

If **no**, the project may proceed to an area-specific legal analysis using the strongest verified facts available, while retaining the unresolved boundary point as a confidence limitation. Examples include:

- two adjoining parcels both strongly established as government-owned and openly used for the same civic pedestrian function, where the exact parcel line would not change the forum analysis;
- an identified ordinary municipal sidewalk whose traditional-public-forum doctrine is clear even though the exact surveyed edge against an adjacent government parcel remains to be mapped;
- historical title-chain gaps that do not alter the current official ownership/access evidence relevant to the forum question.

This is not permission to convert uncertain GIS geometry into a legal boundary. It is a **research sufficiency rule**: pursue boundary precision until additional precision is outcome-determinative, then stop treating perfect title reconstruction as a prerequisite to analyzing facts already established well enough for the legal question.

Use confidence qualifiers such as:

- `TPF-HIGH-CONFIDENCE / EXACT-EDGE-PENDING`;
- `TPF-STRONGLY-SUPPORTED / FIELD-VERIFICATION-PENDING`;
- `CLASSIFICATION-PENDING / BOUNDARY-OUTCOME-DETERMINATIVE`.

The exact edge should remain available for later removal/trespass analysis even when it is not necessary to reach a forum conclusion.

The Concord Library prototype established this gate. Current official evidence was sufficient to apply *Prigmore* to several exterior areas without waiting for every blocked historical deed, while the exact Salvio/Parkside ROW edge remains unresolved because it could matter in a location-specific enforcement dispute.

## 17. Anchor-case comparator method

After the factual/property pass reaches the point where area-specific forum analysis is possible, identify the best **area-and-activity-specific anchor authority** rather than reasoning from the facility type alone.

The preferred sequence is:

`defined area + defined activity → controlling/persuasive anchor authority → factors that drove that authority → local factual comparison → differences/limits → confidence-qualified classification`

The anchor should be as close as reasonably available in jurisdiction, physical setting, access condition, and activity. Controlling authority is preferred; persuasive authority may be used when controlling authority does not answer the narrower question.

For each material comparison, record:

- the exact area and activity being analyzed;
- the candidate anchor case and whether it is binding or persuasive;
- the forum classification actually reached in that case;
- the factual considerations that materially drove that classification;
- similarities between the precedent and the facility area;
- material differences;
- unresolved local facts that could change the analysis;
- the resulting classification and confidence level;
- any separate doctrine still required for the specific activity, such as recording, solicitation, leafleting, or removal/trespass.

Do **not** convert an anchor case into a facility-wide categorical rule. Different areas at one address may require different anchors. For example, one library may use a library-exterior case for its entrance/parking analysis and a different meeting-room case for an intentionally opened room.

Do **not** force an analogy when no sufficiently close case exists. In that situation, apply the general public-forum authorities directly and state that no closer anchor was located.

The comparator also must respect the activity actually decided by the precedent. A case classifying an exterior area during leafleting may strongly support the area's forum status without independently establishing a right to record there. Forum classification and the specific expressive-activity doctrine remain separate steps.

Concord Library is the first tested implementation: *Prigmore v. City of Redding* functions as the exterior-area comparator, while *Faith Center Church Evangelistic Ministries v. Glover* supplies the closer anchor for the meeting-room channel. The project should carry this **anchor-authority, not facility-label** method into later libraries, administrative buildings, police facilities, DMVs, post offices, and other public properties.

## 18. Second-site validation and modular-adapter rule

A component should not be called generalized merely because it worked at the first facility. The second same-category test should deliberately challenge source coverage, field naming, map notation, neighboring-parcel logic, and physical configuration.

Walnut Creek Library supplied the second test after Concord and established several reusable rules.

### Countywide core, local enrichment

A source service may mix datasets with different geographic coverage. Do not assume every layer on the same server is countywide merely because one layer is.

Where the evidence supports it, prefer an architecture such as:

`countywide parcel core + municipality-specific address / street / ROW / owned-property / facility-control enrichment`

Record the geographic scope of each source component independently.

### Validate source enumerations, not just local aliases

If a public form exposes an enumerated source field such as record type, document type, map type, or jurisdiction, an adapter alias is not considered validated until a live test confirms the **actual source query** contains the intended source value.

For example, an assessor shorthand such as `MB` may mean a subdivision-map book locally, but the public records system may require the literal option `Subdivision Map`. Normalize the shorthand, then verify the generated query rather than merely changing a local label.

### Neighbor discovery requires relevance screening

Spatial intersection/touching results remain candidates. A second-site test should confirm that the workflow can distinguish a materially relevant adjoining civic parcel from private parcels or tiny remnants that happen to share an edge or vertex.

Promotion requires independent relevance evidence tied to the actual access/control question.

### Current evidence outranks unnecessary historical archaeology

Historical maps may establish chain/context without resolving today's access question. Once historical references are identified and preserved, prefer current engineering plans, current ROW records, current leases/control documents, and current physical evidence when those sources are more likely to change the present forum/removal analysis.

Do not retrieve every old map simply because the index makes it possible.

### Generalize the method, not the conclusion

The second-site test must also challenge the legal comparator. Walnut Creek demonstrates that one civic site can contain ordinary sidewalks, an open civic plaza, a public park, outdoor surface parking, an enclosed underground garage, opened rental rooms, study rooms, and purpose-limited children's areas.

The same anchor case should not be stretched across all of them.

The reusable output is therefore the **area-specific comparator process**, while the actual anchor and classification remain facts-and-authority dependent.

### Prototype-gate consequence

After two same-category facilities, the project may promote behaviors that survived both tests into the reusable architecture. Municipality-specific enrichments remain modular until independently validated elsewhere.

Cross-category validation has now been completed at Concord DMV. The reusable core may therefore be treated as cross-category validated for its evidence-acquisition method, while source coverage, municipality-specific enrichments, physical-area facts, and legal anchors remain modular and must be validated independently. Further facility categories test the breadth and limits of the architecture; they do not convert it into a universal statewide data source or a universal forum conclusion.

## 19. Cross-category validation: frontage/access path and doctrinal reset

A materially different facility category requires two additional checks before Facility Prep findings are promoted into a Registry entry.

### Address, frontage, and public access path are separate facts

A facility's public mailing or street address does not prove that its parcel directly fronts that street, that the visible approach lies on the facility parcel, or that the public reaches the facility through a particular legal interest.

If assessor, parcel, recorded-map, or current physical evidence shows that the public address and parcel frontage do not align, create an explicit:

`ADDRESS/FRONTAGE-MISMATCH`

Then separately identify, to the level needed by the legal question:

- the actual physical ingress/egress route used by the public;
- the parcel or ROW crossed by that route;
- whether the route is municipal ROW, facility-owned land, an easement, shared drive, license, leasehold, or another arrangement;
- the entity with operational control over the relevant subarea;
- current signs, barriers, circulation patterns, and public-use conditions.

Do not infer ownership, control, forum status, or trespass authority for the approach from the facility address alone.

The outcome-determinative boundary gate still applies. A modern easement/deed/site-plan/access instrument need not be reconstructed merely for completeness if every reasonably plausible answer would leave the legal result unchanged. It becomes high priority when the person's exact location or controller could change forum, removal, or criminal-trespass analysis.

Concord DMV established this rule: the State/DMV parcel is strongly supported at 2070 Diamond Boulevard, but assessor and recorded-map evidence place an intervening parcel between the DMV parcel and Diamond Boulevard. The correct result is an unresolved modern Diamond access right, not an assumed State-owned approach.

### New facility category requires a doctrinal reset

When the governmental purpose materially changes, restart the anchor-authority analysis from the specific area and activity. Do not carry the previous facility category's cases or conclusions forward merely because the physical features look similar.

Use:

`new facility purpose → defined subarea/activity → current access/control facts → fresh controlling/persuasive authority search → comparator analysis → confidence-qualified result`

For example, library exterior cases may remain useful background when facts genuinely overlap, but they are not the default anchors for a DMV administrative lobby, testing area, or customer parking lot. The comparator **method** is reusable; the comparator **case** is not presumed reusable.

Federal and California forum analyses must continue to be separated when state constitutional doctrine may diverge. A federal nonpublic-forum conclusion must not be copied automatically into the California Speech Clause column.

### Preserve the scope of agency-purpose rules

A facility-specific privacy duty, examination-integrity rule, device-use rule, security procedure, or records practice is evidence only for the activity and area to which it actually applies unless a broader rule is independently established.

Do not silently transform:

- a privacy obligation into a general camera ban;
- a knowledge-test cell-phone rule into a field-office-wide phone prohibition;
- a restricted employee-area rule into a lobby rule;
- a purpose-limited transaction requirement into a facility-wide expressive-activity rule.

Record the exact text, source, scope, physical location, and asserted authority of any restriction before applying constitutional analysis.

### Cross-category validation does not universalize source adapters

A parcel core, map resolver, recorded-record workflow, or other acquisition module is reusable only within the geographic/source coverage actually established. Municipal road/ROW layers, address points, facility-control datasets, and agency policies remain modular.

The project should therefore preserve this architecture:

`reusable evidence method + source-specific adapters + area/activity-specific facts + facility-purpose doctrinal reset`

rather than treating one successful cross-category run as proof of statewide technical or doctrinal uniformity.

## 20. Restriction-existence, activity-anchor, and recording-subject rule

A forum classification answers **what constitutional standard governs a restriction**. It does not, by itself, prove that a restriction exists.

For every facility-area/activity analysis, keep these questions separate:

1. **Where is the person?** — exact subarea, access condition, property/control and forum classification;
2. **What activity is occurring?** — filming, audio recording, leafleting, petitioning, observing, speaking, soliciting, attending, etc.;
3. **What or who is the activity directed at?** — for recording, for example, an officer performing a public-facing duty, an uninvolved patron, a victim report, a computer screen, a confidential document, or a restricted/security feature;
4. **What actual restriction exists?** — statute, regulation, ordinance, adopted policy, posted rule, order, security condition, or conduct-based direction;
5. **What authority governs the specific activity?** — activity-specific constitutional/statutory/case authority may differ from the best forum-classification authority;
6. **What enforcement bridge is being asserted?** — removal, trespass, obstruction, detention, arrest, or another consequence must be separately supported.

Do not infer:

`nonpublic forum → recording prohibited`

or:

`agency confidentiality duty → visitor camera ban`.

Instead use:

`area/forum + activity + subject + actual restriction + activity-specific authority + enforcement authority`.

### Dual-anchor method

The closest authority for **forum/access classification** may not be the closest authority for the **specific expressive activity**. Facility Prep and the Registry may therefore use two distinct anchors:

- **forum/access anchor** — the best controlling/persuasive authority for the physical area/channel and governmental purpose;
- **activity anchor** — the best controlling/persuasive authority, statute, or agency rule addressing the actual activity at issue.

The Concord Police Headquarters sweep established this refinement. General forum authorities such as *Cornelius* and *Sammartano* are stronger for classifying a purpose-limited public police lobby, while *Fordyce*, Penal Code § 148(g), CPD Policy 423, and the highly fact-specific local district-court decision *Wilson v. County of Contra Costa* are more directly relevant to recording officers while lawfully present.

One case need not perform both analytical jobs.

### Recording-subject field

Where recording is a material Registry activity, preserve both:

`recorder location` and `recording subject`.

At minimum, distinguish when relevant:

- government employee/officer performing a public-facing official duty;
- uninvolved visitor/patron;
- victim/witness/confidential source;
- juvenile;
- protected record or computer display;
- private/confidential conversation;
- access-control/security feature;
- restricted operational area.

The same physical vantage point can produce materially different privacy, security, audio-recording and reasonableness questions depending on what is being captured.

### Constitutional savings clauses belong in the enforcement chain

If the proposed criminal/removal authority contains an express constitutional-activity carveout, test that carveout before promoting the statute as an enforcement bridge.

For example, current California Penal Code § 602.1(d)(2) states that § 602.1 does not apply to a person on the premises engaging in activities protected by the California or United States Constitution. That does not immunize independently unprotected obstruction, intimidation or other unlawful conduct, but it means the project must not treat the disputed expressive activity itself as satisfying § 602.1 without first resolving the protection question.

