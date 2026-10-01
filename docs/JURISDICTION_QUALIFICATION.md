# Jurisdiction Qualification and Field Guide Overlay Model

Issue: #40

This document defines how the nationwide Field Guide reuses a canonical legal/research framework while qualifying jurisdiction-specific overlays for facility analysis. It implements the separation established in D-003 between Field Guide qualification and post-activation facility-research maturity.

## Core model

The project does not maintain 51 independent Field Guides that duplicate the same federal doctrine and methodology.

It maintains:

1. a **canonical national core** containing project methodology, standing scenarios, encounter/decision-tree structure, U.S. constitutional doctrine, and U.S. Supreme Court authority that applies nationally;
2. an **applicable federal layer** containing circuit-specific and other federal authority that varies by jurisdiction or facility type;
3. a **jurisdiction overlay** containing state constitutional provisions, state statutes/regulations, state appellate authority, and other jurisdiction-specific law needed to resolve the canonical scenarios;
4. a **local/facility layer** containing ordinances, regulations, agency/facility policy, access facts, actual practice, enforcement evidence, and incident facts.

The analytical structure is:

```text
canonical standing scenario / encounter
                |
        +-------+-------+
        |               |
FEDERAL TRACK       STATE TRACK
U.S. Constitution   State constitution
        |               |
U.S. Supreme Court  State supreme/appellate authority
        |               |
Applicable circuit  State statutes/regulations
and federal law         |
        +-------+-------+
                |
local ordinance / delegated authority / preemption
                |
agency / facility policy
                |
actual practice / enforcement evidence
                |
specific facts
                |
field-rule / facility conclusion
```

The federal and state tracks are related but not a single simple hierarchy. Federal constitutional protection supplies the federal floor for state/local government action; a state constitution or state law may create independent or additional protection where valid. State courts ordinarily control the meaning of their own state constitution and state law, while federal courts control federal law within the normal hierarchy. Local rules must also be checked for lawful delegated authority and preemption where those questions matter. The controlling question at each node remains what authority governs the particular proposition.

## California reference implementation

California is the first reference overlay, not a freestanding model to copy verbatim and not a jurisdiction exempt from this qualification standard.

Its existing structure demonstrates the required functions:

- a canonical standing factual baseline;
- constitutional foundations;
- public-forum doctrine and activity analysis;
- recording/information-gathering law;
- police encounters, detention, identification, and device-search issues;
- trespass/removal;
- disorderly-conduct and meeting-disruption predicates;
- assemblies/emergency scenes;
- public meetings;
- public records and evidence preservation;
- facility-investigation methodology;
- restriction auditing;
- an authority index preserving binding level, research status, limitations, and unresolved work; and
- facility-type research where needed, such as public libraries.

A new jurisdiction reuses the canonical structure and national authority. It replaces or supplements the circuit, state, and local layers rather than copying California-specific conclusions.

California must ultimately be represented in the same qualification matrix used for every other jurisdiction. Existing California content seeds that matrix; it does not grandfather a branch as Supported or excuse a material Gap.

### Canonical standing scenario

The jurisdiction-neutral standing baseline is now:

- `docs/national-core/standing-scenario.md`
- canonical ID `NC-STANDING-01`
- current version `v1`

It contains facts and project methodology only. It intentionally does **not** import California Penal Code mappings, Brown Act rules, Ninth Circuit holdings, or any other jurisdiction-specific legal conclusion.

Jurisdiction overlays may map the neutral facts to their own statutes, regulations, constitutional rules, and cases. California does so in `docs/california/standing-scenario.md`.

Other jurisdictions must reuse the neutral baseline rather than copying California's overlay conclusions.

If a branch needs different facts, the changed fact must be explicit and versioned in the relevant canonical scenario or encounter record rather than silently altering `NC-STANDING-01`.

## Qualification statuses

### Inactive

The jurisdiction exists in the national system, but no qualified overlay is available for Coalition facility analysis.

Contributors may research its law and propose overlay material. Facility-research maturity is null.

### Field Guide Development

The overlay is being built and tested against the canonical scenario/encounter matrix.

This status permits legal research and review but not authoritative Coalition facility conclusions under that jurisdiction.

Real facility policies or facts may be used as test fixtures to exercise an incomplete decision tree during development, but that work does not count as facility-research maturity, does not move the jurisdiction to Researching, and must not be published as a qualified Coalition facility conclusion before activation.

### Active

The overlay has passed human qualification and is sufficiently functional to analyze the canonical scenarios and encounters without material authority gaps.

Activation initializes facility-research maturity to **Unresearched** and creates or validates the complete county/county-equivalent inventory for the state. County inventory creation is an activation-transition requirement, but county research completion is **not** a prerequisite to state qualification.

Active does not mean exhaustive, final, or immune from later correction. It means the Field Guide is sufficiently reliable to serve as the analytical instrument for facility research.

## Qualification is functional, not volumetric

A jurisdiction does not qualify because it has:

- a particular number of pages;
- a particular number of cases;
- a percentage-complete progress bar;
- a contribution-point total;
- a volunteer Division Lead; or
- every conceivable legal question resolved.

The qualification question is:

> Can the jurisdiction-specific overlay run the Coalition's canonical standing scenarios and encounter decision trees with sufficient authoritative support to produce responsible facility analysis?

A branch may be qualified even when the legal answer is genuinely unresolved, provided the relevant authority has been adequately researched and the unresolved posture is documented.

An unresearched material branch is a **Gap** and cannot be relabeled Unresolved merely to satisfy qualification.

### Materiality cannot be self-waived

A branch is material when its answer can reasonably change the legal classification, field rule, enforcement/removal analysis, police-encounter analysis, evidence path, or facility conclusion for an ordinary canonical scenario.

Materiality is determined by the canonical scenario/encounter matrix and qualification review, not unilaterally by the jurisdiction contributor or division seeking activation.

A jurisdiction may document that a branch is conditional or local-dependent, but it may not omit a difficult branch merely by labeling it immaterial. Adding, removing, or globally reclassifying a canonical required branch is a national methodology/governance change and must follow the applicable review path.

## Canonical scenario and encounter coverage

The qualification matrix is derived from the functions demonstrated by the California reference implementation. At minimum, the overlay must support the ordinary facility-analysis branches implicated by the standing scenario and project methodology.

Required coverage families are:

Two canonical national-core scenarios are presently required for every jurisdiction:

- **NC-COMPLAINT-01 — Complaint-Driven Police Encounter / Disputed Trespass and Immediately Available Exculpatory Evidence**, defined in [Complaint-Driven Police Encounter](national-core/complaint-driven-police-encounter.md). A jurisdiction may not satisfy the trespass or police-encounter families merely by locating a generic trespass statute; it must be able to run the disputed-entry, leave-on-request, current-remain, prospective-notice/identification, caller-reliability, exculpatory-evidence, dissipation, retaliation, false-report, evidence-preservation, and conditional-access/derivative-trespass branches.
- **NC-VANTAGE-01 — Lawful-Vantage Observation and Recording / Matters Exposed to Public View**, defined in [Lawful-Vantage Observation and Recording](national-core/lawful-vantage-observation-recording.md). A jurisdiction must be able to distinguish lawful vantage from unlawful presence, ordinary visual observation/recording from intrusion or manipulation, transparent-barrier observation from barrier defeat, visible sensitive information from unlawfully accessed information, visual recording from separately regulated audio/interception, and objection from an independently lawful restriction or exclusion basis.

1. **Lawful presence and area classification**
   - public access versus forum status;
   - traditional, designated, limited, and nonpublic forum analysis where applicable;
   - area-specific classification rather than whole-building assumptions;
   - hours, restricted areas, and changed access facts.

2. **Protected activity and recording**
   - peaceful observation, photography, video, audio, questioning, criticism, and information gathering, including lawful-vantage/exposed-to-public-view analysis;
   - recording public officials/police;
   - privacy/confidential-communication rules and material exceptions;
   - credential-neutral treatment of ordinary members of the public.

3. **Government restrictions**
   - content/viewpoint analysis;
   - time/place/manner or applicable forum-specific reasonableness/tailoring tests;
   - asserted safety, privacy, security, operational, or confidentiality interests;
   - policy/sign/order versus actual legal authority, including conditional-access demands such as `stop recording or leave`;
   - legality of an underlying restriction/exclusion before downstream trespass enforcement is treated as analytically independent;
   - delegated authority and state/federal preemption where material.

4. **Trespass, exclusion, and removal**
   - authority to restrict access or order departure;
   - applicable trespass/interference statutes;
   - public-property/public-agency distinctions;
   - disputed property boundary/current location;
   - never-entered versus entered-and-left versus currently-remains versus prospective-no-entry notice;
   - prospective no-entry notice versus any separate legal duty to identify;
   - effect of a later removal order on an initially lawful presence, including whether the order itself rests on a lawful restriction/exclusion;
   - suspension/exclusion process where material.

5. **Police encounters**
   - consensual contact versus detention;
   - reasonable suspicion;
   - allegation/caller reliability and investigation;
   - allegation-to-elements analysis rather than reliance on labels such as trespassing/hostile/disruptive;
   - immediately available exculpatory evidence and the applicable circuit rule;
   - preservation of whether identified video/evidence was offered, reviewed, or declined;
   - dissipation of reasonable suspicion or probable cause;
   - identification request versus legal duty;
   - frisk/search/seizure issues material to recording devices;
   - arrest/probable cause;
   - Fifth Amendment/Miranda distinctions where the encounter tree requires them.

6. **Disorder, obstruction, and reaction-based allegations**
   - disturbance/noise;
   - obstruction/interference;
   - fighting words/threats or analogous offenses where material;
   - another person's objection or anger versus statutory elements;
   - allegation-to-elements analysis.

7. **Public meetings and assemblies**
   - attendance/recording/comment rules;
   - actual disruption/removal standards;
   - assembly/dispersal rules where material.

8. **Emergency and law-enforcement scenes**
   - lawful perimeter/access restrictions;
   - interference/obstruction distinctions;
   - recording from lawful locations.

9. **Public records and evidence**
   - state public-records framework;
   - records-request process relevant to facility investigations;
   - preservation/retention distinctions;
   - access to policy, incident, dispatch/body-camera/CCTV or analogous evidence subject to applicable exemptions.

10. **Remedies and retaliation sufficient for field use**
    - retaliation principles material to protected activity;
    - preservation/escalation paths needed by the research methodology;
    - clear identification of material remedy areas still outside current operational scope.

11. **Facility research methodology**
    - rule fact separated from constitutional posture;
    - facility versus area versus restriction versus incident versus conclusion;
    - local ordinance/policy/practice treated as evidence to be tested, not self-validating law;
    - contrary authority and changed facts preserved.

These are functional coverage families, not requirements that every jurisdiction use California filenames or identical statutes.

## Decision-tree branch statuses

Each material canonical branch receives one qualification status for the jurisdiction:

### Supported

Applicable authority has been identified and reviewed sufficiently to support the branch's field rule or analytical test.

The supporting source may be constitutional text, statute/regulation, binding case law, or an appropriate combination. A case is not required where controlling text adequately supplies the rule.

Source sufficiency is proposition-specific. A statute may establish statutory elements, duties, or authorization, but the statute's existence alone does not prove that a challenged restriction is constitutional. Constitutional posture must be supported by the authority appropriate to that proposition.

### Researched-Unresolved

The relevant authority has been systematically investigated, but the controlling answer remains genuinely unsettled, conflicting, fact-dependent beyond the canonical assumptions, or otherwise unresolved.

The record must identify what was searched, the best authority found, the uncertainty, and why the branch cannot responsibly be resolved further.

Researched-Unresolved is a valid qualification result.

### Gap

The branch lacks sufficient research or authority to support facility analysis.

Examples include:

- the applicable state statute has not been checked;
- the circuit/state case layer has not been meaningfully researched;
- a California rule was copied without confirming its counterpart;
- a material conflict was noticed but not analyzed;
- the decision tree reaches a question for which no adequate research record exists.

A material Gap blocks activation.

### Not Applicable

The branch does not apply in the jurisdiction or to the canonical scenario for a documented legal reason.

Not Applicable requires a reason; it is not a substitute for research.

## Qualification matrix

The qualification record should identify, for every material branch:

| Field | Purpose |
| --- | --- |
| Scenario/encounter ID | Stable canonical branch being tested |
| Canonical branch version | Version/revision of the canonical branch against which qualification was performed |
| Issue | Legal/factual question the branch answers |
| National authority | Applicable constitutional/Supreme Court source |
| Circuit/federal authority | Applicable federal overlay |
| State constitutional authority | Applicable state constitutional overlay or documented none |
| State statute/regulation | Applicable primary text or documented none |
| State case law | Applicable binding/persuasive state authority |
| Contrary/conflicting authority | Material contrary authority |
| Local dependency | Whether the answer must be completed per locality/facility |
| Branch status | Supported / Researched-Unresolved / Gap / Not Applicable |
| Field rule/test | Operational rule or analytical question |
| Verification date | Currency control |
| Reviewer | Human qualification provenance |
| Notes | Limitations, open questions, changed-fact triggers |

The matrix is evidence for qualification. It does not activate the jurisdiction automatically.

## Activation gate

### Normal activation path

A jurisdiction may be recommended for Active status only when:

1. every canonical scenario and encounter family has been mapped to the jurisdiction;
2. every material decision-tree branch is Supported, Researched-Unresolved, or documented Not Applicable;
3. no material Gap remains that would prevent responsible ordinary facility analysis;
4. primary legal text and controlling authority have current verification records;
5. binding versus persuasive authority is distinguished;
6. contrary authority and meaningful limitations are preserved;
7. state/local rules have not been mistaken for constitutional validity;
8. the standing scenario can be run without importing California-specific statutes or conclusions;
9. at least one independent qualified reviewer who is not the primary author/researcher for the qualification record has examined the coverage record; and
10. an authorized human makes the activation decision.

Under the ordinary permission model, the authority-changing action `Change Field Guide qualification` belongs to the Administrator role; reviewers and Division Leads may recommend qualification but do not activate the jurisdiction by role alone.

The exact reviewer count may be tightened by governance later. No automated score, point threshold, or completeness percentage can satisfy item 10.

### Founder/bootstrap activation exception

The project must not become permanently unable to activate its first or early jurisdictions merely because no independent qualified human reviewer exists or is reasonably available.

When that condition is documented, the **Founder may make a founding/bootstrap activation decision without satisfying item 9 above**. This is an exception to the reviewer-independence requirement only. Items 1–8 remain mandatory, and the activation must still be a deliberate human decision.

A reviewer is not reasonably available when, for example, the Coalition presently has no other suitably qualified independent human, or no such person is available and willing to perform the review within a practical project timeframe. No arbitrary waiting period or public recruitment campaign is required when the project objectively has no qualified independent reviewer. Convenience alone is not enough to invoke the exception when a suitable independent reviewer is actually available.

Before a bootstrap activation, the record must show:

- a complete qualification matrix for the jurisdiction;
- a fresh material-Gap sweep confirming no activation-blocking Gap remains;
- current verification of primary legal text and controlling authority;
- preservation of contrary authority, meaningful limitations, and all Researched-Unresolved branches;
- a distinct adversarial review pass focused on overstatement, omitted contrary authority, unsupported inheritance from another jurisdiction, and changed-fact failure points;
- the objective basis for concluding that an independent qualified human reviewer is not reasonably available;
- the Founder as the accountable activation actor;
- the activation date, scope, qualification-record version, and any unresolved issues or review warnings; and
- an AuditEvent or equivalent immutable provenance record identifying the activation as `founding/bootstrap`.

AI, automation, or a service principal may assist with source checking, adversarial review, gap detection, or drafting, but it **does not count as the missing independent human reviewer** and must not be represented as one.

A bootstrap-activated jurisdiction is genuinely **Active**; it is not a temporary pseudo-status and does not expire merely because time passes. When a suitably qualified independent reviewer later becomes available, the jurisdiction should be queued for retrospective independent qualification review. That later availability does **not** automatically deactivate the jurisdiction. Normal correction/change-management rules apply if the retrospective review identifies a material defect.

Once an independent qualified reviewer is reasonably available, the normal activation path should be used for future jurisdiction activations unless a separate documented bootstrap condition exists.

The Founder/bootstrap exception is a deliberate governance exception, not permission for automated activation, self-described completeness, contribution points, or convenience to substitute for the substantive qualification gate.

## Local dependencies do not necessarily block state activation

Some questions cannot be answered statewide because they depend on a city's ordinance, an agency's regulation, a facility's purpose, a posted rule, an access configuration, or actual enforcement practice.

The state overlay qualifies when it supplies the legal framework needed to analyze those local facts.

For example, the overlay need not predetermine the forum status of every government lobby. It must provide a sufficiently supported decision tree for classifying the particular area and testing the particular restriction when facility facts are supplied.

A branch marked as a local dependency therefore can qualify if the state/national analytical framework for resolving that dependency is complete.

## Post-activation facility-research maturity

Facility-research maturity is separate from Field Guide qualification.

### Unresearched

The jurisdiction is Active, but no meaningful facility research program has begun.

### Researching

One or more facility investigations, registry sweeps, or systematic facility-type analyses are underway under the qualified Field Guide.

### Established

The jurisdiction has a maintained body of facility research sufficient to demonstrate recurring application of the Field Guide across meaningful facility contexts.

Established is a human-reviewed maturity classification, not an automatic facility-count threshold. A large number of shallow entries does not establish maturity.

## Post-activation county/county-equivalent inventory

State activation and county research are deliberately sequential.

A state **does not** need every county researched before it may become Active. The state qualifies when its national, circuit/federal, state, and local-dependency framework is sufficient to analyze ordinary facility questions responsibly.

As part of the transition to Active, however, the project must create or validate a complete current inventory of the state's counties or county-equivalents against an authoritative geographic source. This inventory is geographic/research scaffolding, not a second legal-qualification gate.

Each county/county-equivalent record begins with a local-research coverage status of:

- **Unresearched** - the geographic record exists, but no meaningful county-specific research has been reconciled against the Active state framework;
- **Researching** - county/local ordinances, policies, agencies, facilities, enforcement history, records practices, or other local dependencies are being investigated under the Active state framework;
- **Established** - a maintained county-level body of local research exists across meaningful agencies/facility contexts.

These county coverage labels do **not** mean the county has an independently qualified Field Guide. Counties inherit the applicable national core, federal/circuit layer, and Active state overlay. County work should record what is actually local, including:

- county ordinances and delegated local authority;
- county-board or analogous public-meeting rules;
- sheriff/law-enforcement policies and practices;
- county library, administrative-building, and other agency/facility systems;
- local exclusion/removal procedures;
- local public-records practices where they materially vary;
- documented enforcement/chilling history;
- municipality, special-district, or facility dependencies encountered within the county; and
- unresolved local questions that must be answered before a particular facility conclusion can be published.

Existing pre-activation facility research may seed the county record after activation, but it must be reconciled against the qualified state framework before it supports a higher county-coverage status. File count or the mere existence of prior research does not automatically promote a county from Unresearched.

The county inventory should use stable geographic identifiers and preserve county-equivalent terminology so the same model can represent states whose primary county-level units are not literally called counties.

County coverage is a discovery and research-management layer. It must not duplicate national/state doctrine merely to make every county look self-contained. It also does not establish a legal parent-child relationship between county government and every municipality, special district, state agency, federal facility, or other entity geographically located there; authority must still be traced to the actual governing body, and cross-county entities may reference multiple coverage units.

## Change management after activation

Activation is not permanent certification of every proposition.

When new controlling authority, statutory amendment, or a discovered research defect materially affects a canonical branch:

1. mark the affected branch for re-verification;
2. identify published facility conclusions that depend on it;
3. update or suspend those conclusions where necessary;
4. preserve the prior provenance/correction history; and
5. determine whether the defect is localized or serious enough to require a human qualification review of the jurisdiction.

Routine updates do not automatically deactivate an otherwise functional jurisdiction. A material defect that makes ordinary facility analysis unreliable must not be hidden behind Active status.

## Federal premises

Federal premises remain a separate applicability track.

Physical location inside a state does not automatically make the state's conduct, records, or facility rules govern federal property. Federal-premises analysis begins with the national constitutional core, applicable federal statutes/regulations, agency rules, and federal cases, then adds state law only when a specific jurisdictional or incorporation rule makes it relevant.

## Implementation consequences

The eventual platform should:

- store canonical scenario/encounter IDs and versions separately from jurisdiction overlays;
- let national authority be referenced rather than duplicated into every state;
- associate circuit authority with the jurisdictions where it is applicable;
- store jurisdiction-specific branch resolutions and their authority records;
- compute coverage reports without allowing them to change qualification status;
- prevent facility conclusions from being published for a jurisdiction that is not Active;
- preserve Researched-Unresolved as a first-class result;
- expose material Gaps during Field Guide Development;
- initialize facility-research maturity to Unresearched only upon activation;
- create or validate the complete county/county-equivalent inventory as part of state activation, with county research coverage beginning at Unresearched unless reconciled existing work supports a later human-reviewed status;
- treat county coverage as inherited local research rather than an independently qualified duplicate Field Guide; and
- support dependency tracking so changes to canonical branch versions or national/circuit/state authority can flag affected branches and facility conclusions for review.

## Decisions intentionally deferred

This design does not decide:

- exact UI for the national coverage matrix;
- exact database schema for authority-node inheritance;
- exact numerical contribution points;
- the detailed submission/review workflow owned by #42;
- detailed privacy/retention rules owned by #43;
- GitHub integration mechanics owned by #45; or
- a permanent numerical threshold for Established facility-research maturity.

Those decisions must not be inferred from this qualification model.
