# Concord Police Headquarters — Evidence Manifest

**Facility:** Concord Police Department Headquarters  
**Address:** 1350 Galindo Street, Concord, CA 94520  
**Agency:** City of Concord Police Department  
**Research date:** 2026-09-22  
**Boundary confidence:** **PARTIALLY-VERIFIED**

This manifest tracks Sweep 010 evidence for the ordinary public police lobby and related public-access subareas. It separates public-access facts, agency policy, property/control, physical configuration, forum classification, recording doctrine, privacy/audio doctrine, and removal/trespass analysis.

## Current official access sources

Police Department:

https://www.cityofconcord.org/police

Community Service Desk:

https://www.cityofconcord.org/194/Community-Service-Desk

Records Unit:

https://www.cityofconcord.org/214/Records-Unit

Current verified access facts:

- Police Headquarters is identified at 1350 Galindo Street;
- the Community Service Desk is located in the police lobby;
- the City calls the Community Service Desk the department's primary public-facing point of contact;
- lobby/Community Service Desk hours are Monday–Friday, 8:00 a.m.–5:00 p.m., closed holidays;
- the Records Unit serves the public at the lobby counter during the same weekday hours;
- the current Community Service Desk page states that CPD no longer offers LiveScan/fingerprinting services.

Status:

`ORDINARY-PUBLIC-LOBBY-ACCESS-VERIFIED-DURING-BUSINESS-HOURS / CURRENT-PHYSICAL-CONFIGURATION-PENDING`

## Current parcel / property evidence

The standard Facility Prep parcel resolver matches 1350 Galindo Street to:

- APN `126-124-036`;
- owner field `CONCORD CITY OF`;
- acreage `5.06`;
- building-square-footage field `71,913`;
- Assessor Book 126 Page 12.

Assessor PDF:

https://ccmap.cccounty.us/HTML5/assessorPDF/126p12x0.pdf

SHA-256:

`b16a5c0407da51671e7daf89e6f45f4aac1bc711327d0c65c6d57178052f8f6c`

Human review identifies target parcel `36`, approximately `5.06 Ac`, **east of Laguna Street and directly adjoining Galindo Street**.

A sheet notation `VACATED 94-188992 7-25-94` appears **west of Laguna Street, outside target parcel 36**. It is preserved as a map observation but is not promoted as a Headquarters access/boundary lead absent later contrary evidence.

Candidate parcel intersections include:

- `126-124-030` — City of Concord — 0.816 acre;
- `126-124-032` — Julie J. Liu — 0.384 acre;
- `126-124-033` — City of Concord — 0.67 acre.

These are discovery candidates, not automatic control conclusions.

Detailed review:

`property-row-review-2026-09-22.md`

## Current Galindo / ROW evidence

The Concord Road Centerlines layer returns the closest Galindo segment as:

- OBJECTID `215722`;
- Street Owner `Concord`;
- Jurisdiction `Concord`;
- Major Arterial;
- right-side address range `1350–1370`;
- sidewalk L/R `No / Yes`;
- facility ID `TCL163922`;
- source update `2020-04-27`;
- approximately `61.9 m` from the facility point used for ranking.

The matching `1350–1370` address range, public facility address and assessor-sheet geography strongly support Galindo frontage. The centerline and sidewalk attributes do not establish the surveyed ROW edge or sidewalk-strip title.

The same run returned nearby Concord-owned/jurisdictional Laguna and Oak segments. The exact-name query did not return `Mount Diablo`, so no Mount Diablo centerline conclusion is drawn from that run.

Current property posture:

`PROPERTY-CHAIN-CLEANER-THAN-DMV / GALINDO-PUBLIC-FRONTAGE-STRONGLY-SUPPORTED / NO-ADDRESS-FRONTAGE-MISMATCH-OBSERVED / EXACT-SIDEWALK-ROW-EDGE-AND-PARKING/APPROACH-CONTROL-PENDING-WHERE-OUTCOME-DETERMINATIVE`

## Current agency recording policy

Concord Police Department Policy Manual:

https://www.cityofconcord.org/1196/Department-Policy-Manual

Policy 423, **Public Recording of Law Enforcement Activity**, is a material facility-specific source.

Current verified policy propositions include:

- CPD recognizes lawful recording of department members performing official duties;
- members are directed not to prohibit or intentionally interfere with lawful recordings;
- recordings may be made from public places or private property where the individual has the legal right to be present;
- recording alone is distinguished from interference;
- safety/interference can justify location or behavior limits;
- warnings/directions should be clear and specific when practicable;
- enforcement and seizure remain constrained by constitutional/state law and department policy.

California Penal Code § 148(g) separately provides that photographing or audio/video recording a public or peace officer, while the officer is in a public place or the recorder is in a place the recorder has the right to be, does not by itself constitute § 148(a) obstruction and does not by itself create reasonable suspicion or probable cause.

Status:

`POLICY-423-VERIFIED / §148(g)-PRIMARY-TEXT-VERIFIED / EXACT-LOBBY-APPLICATION-REQUIRES-DEFINED-ACTIVITY-AND-LAWFUL-PRESENCE-ANALYSIS`

Policy 423 and § 148(g) are not treated as blanket authorization to record uninvolved visitors, confidential communications, protected records, computer screens, security features, or restricted operational areas.

Detailed review:

`policy-recording-review-2026-09-22.md`

## Narrow confidentiality / information-security policies

Current CPD policies separately protect Records Unit files, sensitive reports, protected law-enforcement information/systems, and specified confidential communications. These rules materially support protecting **actual** sensitive information and workspaces.

They do not themselves create a public-facing lobby-wide camera prohibition.

Current distinction:

`NARROW-CONFIDENTIALITY/INFORMATION-SECURITY-DUTIES-VERIFIED / NO-AUTOMATIC-RECIPROCAL-PUBLIC-CAMERA-BAN`

## Audio privacy — Penal Code § 632

Penal Code § 632 applies to intentional recording/eavesdropping of a **confidential communication** without consent of all parties. The statutory definition excludes circumstances in which parties may reasonably expect the communication to be overheard or recorded.

Under *Flanagan v. Flanagan*, 27 Cal.4th 766 (2002), the confidentiality test is whether a party has an **objectively reasonable expectation that the conversation is not being overheard or recorded**.

This means neither of the following is safe as a categorical field rule:

- `public police lobby = all audio may always be recorded`; or
- `police conversation = automatically confidential`.

The actual acoustic/physical setting, privacy measures, participants and circumstances matter.

The local *Wilson* case supplies a concrete lobby application: at the pleading stage, the court rejected a § 632 theory where the plaintiff alleged that various members of the public were present and could hear the conversations.

Current audio posture:

`§632-FACT-SPECIFIC / FLANAGAN-OBJECTIVE-CONFIDENTIALITY-TEST / WILSON-PUBLIC-LOBBY-APPLICATION-PERSUASIVE-ONLY`

## Closest local officer-recording comparator — Wilson

**Wilson v. County of Contra Costa**, No. 14-cv-03491-SI (N.D. Cal. May 6, 2015), involved recording officers in the **public lobby of the Contra Costa County Sheriff's Office**.

At the Rule 12(b)(6) stage, the Northern District of California held that the plaintiff had sufficiently pleaded a First Amendment retaliation claim based on recording officers performing their duties in that public lobby and declined to grant qualified immunity on the facts alleged. The court relied on *Fordyce*'s First Amendment right to film matters of public interest.

Limits are substantial:

- federal district court, not binding Ninth Circuit precedent;
- pleading-stage allegations assumed true;
- no formal lobby public-forum classification;
- no neutral preexisting lobby-wide anti-recording rule adjudicated;
- no final merits adjudication after discovery/trial; the case later ended after failure-to-prosecute proceedings.

Status:

`HIGHLY-RELEVANT-LOCAL-DISTRICT-COURT-COMPARATOR / PLEADING-STAGE / NONBINDING / NO-FINAL-MERITS-ADJUDICATION`

Detailed review:

`wilson-contra-costa-sheriff-lobby-2015.md`

## Dedicated lobby-camera-rule search

Targeted review of current public-facing CPD pages, the policy manual, Community Service Desk material, Records Unit material, and police-facility pages did not locate a separate published rule categorically prohibiting ordinary-patron photography/audio/video recording throughout the Concord Police lobby.

Approved wording:

> **No dedicated public-facing Concord Police Headquarters lobby-wide ordinary-patron photography/videography prohibition was located in the online sources reviewed as of September 22, 2026.**

This is not proof that no current physical sign, internal directive, narrow privacy/security rule, or later policy exists.

## Separate public Community Meeting Room channel

Official facility source:

https://www.cityofconcord.org/facilities/facility/details/Police-Department-Community-Rooms-33

The Department advertises a Community Meeting Room for nonprofit community groups discussing community issues, subject to reservation/contract restrictions. The public page states that the Department may impose reasonable **content-neutral time, place, and manner restrictions**.

The page says a Community Room Contract form is required after reservation, but the contract itself was not located in the online sources reviewed.

Status:

`SEPARATE-OPENED-CHANNEL / CONTRACT-NOT-LOCATED-ONLINE / ACTUAL-PRACTICE-PENDING`

The Community Meeting Room does not inherit the ordinary police lobby's eventual classification.

## Forum / recording posture

No building-wide forum classification is assigned.

Current authority review supports the following working posture:

| Question | Status |
| --- | --- |
| Ordinary lobby open to public for police services | **VERIFIED during stated business hours** |
| Federal lobby forum framework | **LIMITED/NONPUBLIC STANDARD STRONGLY SUPPORTED; no published Ninth Circuit police-lobby filming holding located** |
| California Speech Clause classification | **UNRESOLVED; no close published California police-lobby case located** |
| CPD Policy 423 | **CURRENT AGENCY POLICY VERIFIED** |
| Penal Code § 148(g) | **PRIMARY TEXT VERIFIED; recording alone is not §148(a)/RS/PC under the statute's location conditions** |
| Local Wilson comparator | **First Amendment officer-recording claim in Contra Costa sheriff lobby survived pleading; nonbinding and no final merits adjudication** |
| Penal Code § 632 | **FACT-SPECIFIC confidentiality analysis; public-lobby audio is not categorically lawful or confidential** |
| Dedicated lobby-wide camera/photography prohibition | **NOT LOCATED IN ONLINE SOURCES REVIEWED** |
| Privacy/security interests | **CLEARLY MATERIAL; exact subject/location/rule application required** |
| Community Meeting Room | **SEPARATE OPENED CHANNEL; contract not located online** |
| Removal/trespass authority | **SUBAREA / RULE / FACT / CONSTITUTIONAL-ACTIVITY SPECIFIC** |

Detailed authority review:

`interior-forum-authority-review-2026-09-22.md`

## Penal Code § 602.1 — important constitutional-activity carveout

Section 602.1(b) does not reduce a public-agency trespass/interference case to `asked to leave + refused`.

Its public-agency offense requires intentional interference with lawful agency business **by obstructing or intimidating** employees/persons carrying on or transacting business, followed by refusal after a qualifying request.

Current § 602.1(d)(2) adds a critical limitation:

> `This section shall not apply` to a person on the premises engaging in activities protected by the California Constitution or United States Constitution.

That means the analysis must first identify whether the activity at issue is constitutionally protected rather than assuming § 602.1 applies merely because an employee objects to recording.

But the carveout is not immunity for additional unprotected conduct. Actual obstruction, intimidation, threats, interference or other independent unlawful behavior must be analyzed separately. Section 602.1(e) also preserves the possible application of other law.

For Sweep 010 the removal chain is therefore:

`exact subarea + lawful presence → actual activity → is that activity constitutionally protected? → §602.1(d)(2) if yes → any additional obstruction/intimidation conduct? → qualifying request/authority → any other applicable trespass or criminal provision`

## Important Concord-specific distinction

This is not presently an ordinary `police lobby + published no-recording rule` case.

CPD Policy 423 affirmatively recognizes lawful recording of officers performing official duties. *Wilson* supplies a highly relevant local officer-recording comparator, and § 148(g) says recording alone does not itself establish § 148(a), reasonable suspicion or probable cause within its location conditions.

Therefore a purpose-limited/nonpublic federal forum classification does **not** itself answer whether a specific recording is allowed or prohibited.

The working chain is:

`defined lobby subarea → lawful presence → subject/activity being recorded → forum/access anchor + activity-specific anchor → Policy 423 + §148(g) + Wilson → actual narrower rule → privacy/§632/security facts → restriction standard → §602.1 constitutional carveout/elements → removal/trespass analysis`

## Methodological consequence

Sweep 010 is now strongly supporting a **two-anchor method** for facilities in which forum status and a specific expressive activity have different best authorities:

- **forum/access anchor:** cases such as *Cornelius* / *Sammartano* plus facility-purpose and access facts;
- **activity anchor:** cases/statutes/policies addressing the actual activity, such as *Fordyce*, § 148(g), CPD Policy 423 and *Wilson* for recording officers.

Forum classification determines the constitutional standard applicable to a restriction. It does **not** prove that a restriction exists, and it does not by itself resolve whether the specific activity is protected.

## Probe provenance

Latest full Facility Prep run:

- GitHub Actions run `35790463489`;
- conclusion `success`;
- artifact `facility-prep-concord-police-full`;
- artifact ID `10722150330`;
- artifact digest `sha256:3ec90f203d894df4ba008f5e119cf8704b01b09e6a02471774b140f223a0622e`.

The Road Centerlines resolver also exposed a reusable stale-label bug inherited from the original Concord Library prototype (`Concord Library AddressPoint` in generated output). The resolver has been generalized on the Sweep 010 branch so future facility packets refer generically to the supplied facility point.

## Next evidence pass

Highest-value remaining work:

1. verify the current physical lobby entrance, counter/seating layout, controlled doors, privacy screens and posted camera/conduct/security signs;
2. correlate the City-owned candidate parcels and front parking/pedestrian approach to the current site;
3. obtain the Community Room Contract only if that separate opened channel is being classified for publication;
4. perform a final check for closer published Ninth Circuit/California police-lobby authority;
5. keep audio/privacy analysis tied to actual lobby acoustics, participants and privacy measures;
6. keep any removal/trespass issue tied to the exact subarea, protected activity, rule, authority and additional conduct rather than the mere act of recording.
