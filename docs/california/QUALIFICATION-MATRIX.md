# California Jurisdiction Qualification Matrix

**Jurisdiction:** California  
**Qualification status:** Active  
**Matrix stage:** Qualification complete; California activated 2026-09-30  
**Skeleton baseline:** `main@f6f5a9b7e2bcaeffeeb0fc0f034b531c62e05a3b`  
**Functional-coverage baseline alias:** `JQ@f6f5a9b` = `docs/JURISDICTION_QUALIFICATION.md` at `f6f5a9b7e2bcaeffeeb0fc0f034b531c62e05a3b`  
**Qualification method:** [Jurisdiction Qualification and Field Guide Overlay Model](../JURISDICTION_QUALIFICATION.md)  
**Canonical standing baseline:** `NC-STANDING-01 v1` (`docs/national-core/standing-scenario.md`)

This is the formal working matrix for determining whether the California overlay can run the Coalition's canonical scenarios and encounter decision trees without material authority gaps.

The original existing-research population mapped all 73 rows before new Gap research began. GAP-01 through GAP-08 received fresh California sweeps, CA-GATE-08 canonicalized the national standing baseline, and the final adversarial review rechecked all row statuses and substantive controls. No matrix row remains in Gap status. The four Researched-Unresolved rows remain first-class constraints. CA-GATE-09 is satisfied through the documented Founder/bootstrap exception, CA-GATE-10 is satisfied by the Founder's 2026-09-30 activation decision, and California is Active. Detailed authority bundles and status rationales are maintained in [California Qualification Existing-Research Map](QUALIFICATION-EVIDENCE-MAP.md).

## Status rule

`Not assessed` was the workflow placeholder used while the skeleton was empty. The existing-research population pass has now removed that placeholder from all 73 rows. It remains **not** a fifth qualification result.

After assessment, every material branch must resolve to exactly one approved qualification status:

- **Supported**
- **Researched-Unresolved**
- **Gap**
- **Not Applicable**

A material **Gap** blocks activation.

## Row-key rule

Rows beginning `CA-F...` are stable California qualification-matrix keys derived from the functional coverage families in `JURISDICTION_QUALIFICATION.md`. They are **not** new national canonical scenario IDs.

Rows beginning `NC-COMPLAINT-01...` are actual canonical national-core branch IDs and retain that identity here.

If later national-core work promotes a functional coverage row into a canonical scenario/branch ID, preserve the California row's history and record the superseding canonical reference rather than silently renaming prior review records.

## Required branch record

Every row must ultimately preserve these fields:

| Field | Requirement |
| --- | --- |
| Row/scenario ID | Stable California matrix row key or canonical national branch ID |
| Canonical branch version | Exact national/methodology version or revision tested |
| Issue | Legal/factual question being resolved |
| National authority | Applicable U.S. constitutional/Supreme Court authority |
| Circuit/federal authority | Applicable Ninth Circuit or other federal layer |
| State constitutional authority | Applicable California constitutional authority or documented none |
| State statute/regulation | Applicable California primary text or documented none |
| State case law | Applicable California binding/persuasive state authority |
| Contrary/conflicting authority | Material contrary authority or documented none found after adequate research |
| Local dependency | Whether final application depends on locality/facility facts |
| Branch status | Supported / Researched-Unresolved / Gap / Not Applicable |
| Field rule/test | Operational rule or analytical question |
| Verification date | Currency control |
| Reviewer | Human qualification provenance; bootstrap rules apply only at activation |
| Notes | Limitations, open questions, changed-fact triggers, source/research trail |

The compact tables below are the coverage inventory and now show the provisional status/local-dependency result from the existing-research population pass. Detailed branch evidence and limitations are in [QUALIFICATION-EVIDENCE-MAP.md](QUALIFICATION-EVIDENCE-MAP.md).

## Activation-control checklist

These are controls over the completed matrix, not substitutes for branch research.

| Control | Requirement | Current state |
| --- | --- | --- |
| CA-GATE-01 | Every canonical scenario and encounter family mapped | **Met** — all 73 current rows mapped and cross-checked against the evidence map |
| CA-GATE-02 | Every material branch has an approved qualification status | **Met substantively** — final adversarial status review completed; CA-GATE-09 separately controls independent-human/bootstrap provenance |
| CA-GATE-03 | No material activation-blocking Gap remains | **Met** — final adversarial review found no new material Gap |
| CA-GATE-04 | Primary legal text and controlling authority have current verification records | **Met for ordinary qualification scope** — fresh sweeps plus final current-source spot checks completed; specialized branches remain labeled |
| CA-GATE-05 | Binding versus persuasive authority is distinguished | **Met** — final hierarchy/posture audit preserves published, unpublished, district, out-of-circuit, QI, and limited-posture distinctions |
| CA-GATE-06 | Contrary authority and meaningful limitations are preserved | **Met** — final adversarial review retained four Researched-Unresolved rows and material contrary/posture limits |
| CA-GATE-07 | State/local rules are not mistaken for constitutional validity | **Met** — authority/delegation/preemption/constitutional/enforcement chain rechecked |
| CA-GATE-08 | Standing scenario can run without importing California-specific law into the national baseline | **Met** — NC-STANDING-01 v1 contamination/changed-fact checks passed; California remains an overlay/crosswalk |
| CA-GATE-09 | Normal path: independent qualified human review completed; bootstrap path: documented Founder exception if no reviewer is reasonably available | **Met via Founder/bootstrap exception** — on 2026-09-30 the Founder attested that the Founder is presently the only Coalition member, no suitably qualified independent human reviewer is reasonably available at this stage, invoked the exception, and accepted accountability; see `../research/CA-GATE-09-FOUNDER-BOOTSTRAP-RECORD.md` |
| CA-GATE-10 | Authorized human activation decision completed | **Met** — Founder approved the completed qualification record and activated California on 2026-09-30; see `../research/CA-GATE-10-CALIFORNIA-ACTIVATION-RECORD.md` |

## CA-F1 — Lawful presence and area classification

| Row key | Required question / coverage | Canonical/method source | Status | Local dependency |
| --- | --- | --- | --- | --- |
| CA-F1.1 | Public access versus forum status | JQ@f6f5a9b functional coverage family | Supported | Yes |
| CA-F1.2 | Traditional, designated, limited, and nonpublic forum analysis where applicable | JQ@f6f5a9b functional coverage family | Supported | Yes |
| CA-F1.3 | Area-specific classification rather than whole-building assumptions | JQ@f6f5a9b functional coverage family | Supported | Yes |
| CA-F1.4 | Hours, restricted areas, and changed access facts | JQ@f6f5a9b functional coverage family | Supported | Yes |

## CA-F2 — Protected activity and recording

| Row key | Required question / coverage | Canonical/method source | Status | Local dependency |
| --- | --- | --- | --- | --- |
| CA-F2.1 | Peaceful observation, photography, video, audio, questioning, criticism, and information gathering, including lawful-vantage/exposed-to-public-view analysis | JQ functional coverage + NC-VANTAGE-01 | Supported | Yes |
| CA-F2.2 | Recording public officials and police | JQ@f6f5a9b functional coverage family | Supported | Yes |
| CA-F2.3 | Privacy/confidential-communication rules and material exceptions | JQ@f6f5a9b functional coverage family | Supported | Yes |
| CA-F2.4 | Credential-neutral treatment of ordinary members of the public | JQ@f6f5a9b functional coverage family | Supported | No |

## CA-F3 — Government restrictions

| Row key | Required question / coverage | Canonical/method source | Status | Local dependency |
| --- | --- | --- | --- | --- |
| CA-F3.1 | Content/viewpoint analysis | JQ@f6f5a9b functional coverage family | Supported | Yes |
| CA-F3.2 | Time/place/manner or applicable forum-specific reasonableness/tailoring tests | JQ@f6f5a9b functional coverage family | Supported | Yes |
| CA-F3.3 | Asserted safety, privacy, security, operational, or confidentiality interests | JQ@f6f5a9b functional coverage family | Supported | Yes |
| CA-F3.4 | Policy/sign/order versus actual legal authority, including conditional-access demands such as `stop recording or leave` and the legality of the underlying exclusion before downstream trespass enforcement | JQ functional coverage + NC-COMPLAINT-01.M | Supported | Yes |
| CA-F3.5 | Delegated authority and state/federal preemption where material | JQ@f6f5a9b functional coverage family | Supported | Yes |

## CA-F4 — Trespass, exclusion, and removal

| Row key | Required question / coverage | Canonical/method source | Status | Local dependency |
| --- | --- | --- | --- | --- |
| CA-F4.1 | Authority to restrict access or order departure | JQ@f6f5a9b functional coverage family | Supported | Yes |
| CA-F4.2 | Applicable trespass/interference statutes | JQ@f6f5a9b functional coverage family | Supported | Yes |
| CA-F4.3 | Public-property/public-agency distinctions | JQ@f6f5a9b functional coverage family | Supported | Yes |
| CA-F4.4 | Disputed property boundary/current location | JQ@f6f5a9b functional coverage family | Supported | Yes |
| CA-F4.5 | Never-entered versus entered-and-left versus currently-remains versus prospective-no-entry notice, including separation of notice from any independent legal duty to identify | JQ functional coverage + NC-COMPLAINT-01.D | Researched-Unresolved | Yes |
| CA-F4.6 | Effect of a later removal order on an initially lawful presence | JQ@f6f5a9b functional coverage family | Supported | Yes |
| CA-F4.7 | Suspension/exclusion process where material | JQ@f6f5a9b functional coverage family | Supported | Yes |

## CA-F5 — Police encounters

| Row key | Required question / coverage | Canonical/method source | Status | Local dependency |
| --- | --- | --- | --- | --- |
| CA-F5.1 | Consensual contact versus detention | JQ@f6f5a9b functional coverage family | Supported | No |
| CA-F5.2 | Reasonable suspicion | JQ@f6f5a9b functional coverage family | Supported | No |
| CA-F5.3 | Allegation/caller reliability and investigation | JQ@f6f5a9b functional coverage family | Supported | Yes |
| CA-F5.4 | Allegation-to-elements analysis rather than reliance on labels such as trespassing/hostile/disruptive | JQ@f6f5a9b functional coverage family | Supported | Yes |
| CA-F5.5 | Immediately available exculpatory evidence and the applicable circuit rule | JQ@f6f5a9b functional coverage family | Supported | No |
| CA-F5.6 | Preservation of whether identified video/evidence was offered, reviewed, or declined | JQ@f6f5a9b functional coverage family | Supported | No |
| CA-F5.7 | Dissipation of reasonable suspicion or probable cause | JQ@f6f5a9b functional coverage family | Supported | No |
| CA-F5.8 | Identification request versus legal duty | JQ@f6f5a9b functional coverage family | Researched-Unresolved | No |
| CA-F5.9 | Frisk/search/seizure issues material to recording devices | JQ@f6f5a9b functional coverage family | Supported | No |
| CA-F5.10 | Arrest/probable cause | JQ@f6f5a9b functional coverage family | Supported | No |
| CA-F5.11 | Fifth Amendment/Miranda distinctions where the encounter tree requires them | JQ@f6f5a9b functional coverage family | Supported | No |

## CA-F6 — Disorder, obstruction, and reaction-based allegations

| Row key | Required question / coverage | Canonical/method source | Status | Local dependency |
| --- | --- | --- | --- | --- |
| CA-F6.1 | Disturbance/noise | JQ@f6f5a9b functional coverage family | Supported | Yes |
| CA-F6.2 | Obstruction/interference | JQ@f6f5a9b functional coverage family | Supported | Yes |
| CA-F6.3 | Fighting words/threats or analogous offenses where material | JQ@f6f5a9b functional coverage family | Supported | Yes |
| CA-F6.4 | Another person's objection or anger versus statutory elements | JQ@f6f5a9b functional coverage family | Supported | No |
| CA-F6.5 | Allegation-to-elements analysis | JQ@f6f5a9b functional coverage family | Supported | No |

## CA-F7 — Public meetings and assemblies

| Row key | Required question / coverage | Canonical/method source | Status | Local dependency |
| --- | --- | --- | --- | --- |
| CA-F7.1 | Attendance/recording/comment rules | JQ@f6f5a9b functional coverage family | Supported | Yes |
| CA-F7.2 | Actual disruption/removal standards | JQ@f6f5a9b functional coverage family | Supported | Yes |
| CA-F7.3 | Assembly/dispersal rules where material | JQ@f6f5a9b functional coverage family | Supported | Yes |

## CA-F8 — Emergency and law-enforcement scenes

| Row key | Required question / coverage | Canonical/method source | Status | Local dependency |
| --- | --- | --- | --- | --- |
| CA-F8.1 | Lawful perimeter/access restrictions | JQ@f6f5a9b functional coverage family | Supported | Yes |
| CA-F8.2 | Interference/obstruction distinctions | JQ@f6f5a9b functional coverage family | Supported | Yes |
| CA-F8.3 | Recording from lawful locations | JQ@f6f5a9b functional coverage family | Supported | Yes |

## CA-F9 — Public records and evidence

| Row key | Required question / coverage | Canonical/method source | Status | Local dependency |
| --- | --- | --- | --- | --- |
| CA-F9.1 | State public-records framework | JQ@f6f5a9b functional coverage family | Supported | No |
| CA-F9.2 | Records-request process relevant to facility investigations | JQ@f6f5a9b functional coverage family | Supported | Yes |
| CA-F9.3 | Preservation/retention distinctions | JQ@f6f5a9b functional coverage family | Supported | Yes |
| CA-F9.4 | Access to policy, incident, dispatch/body-camera/CCTV or analogous evidence subject to applicable exemptions | JQ@f6f5a9b functional coverage family | Supported | Yes |

## CA-F10 — Remedies and retaliation sufficient for field use

| Row key | Required question / coverage | Canonical/method source | Status | Local dependency |
| --- | --- | --- | --- | --- |
| CA-F10.1 | Retaliation principles material to protected activity | JQ@f6f5a9b functional coverage family | Supported | No |
| CA-F10.2 | Preservation/escalation paths needed by the research methodology | JQ@f6f5a9b functional coverage family | Supported | Yes |
| CA-F10.3 | Clear identification of material remedy areas still outside current operational scope | JQ@f6f5a9b functional coverage family | Supported | No |

## CA-F11 — Facility research methodology

| Row key | Required question / coverage | Canonical/method source | Status | Local dependency |
| --- | --- | --- | --- | --- |
| CA-F11.1 | Rule fact separated from constitutional posture | JQ@f6f5a9b functional coverage family | Supported | No |
| CA-F11.2 | Facility versus area versus restriction versus incident versus conclusion | JQ@f6f5a9b functional coverage family | Supported | No |
| CA-F11.3 | Local ordinance/policy/practice treated as evidence to be tested, not self-validating law | JQ@f6f5a9b functional coverage family | Supported | Yes |
| CA-F11.4 | Contrary authority and changed facts preserved | JQ@f6f5a9b functional coverage family | Supported | No |

## NC-COMPLAINT-01 — Complaint-driven police encounter

Canonical version: **v2**. These rows are required in addition to the functional coverage inventory above; overlap is intentional because the scenario must be runnable end-to-end rather than inferred from topic pages.

| Canonical branch ID | Required question | Version | Status | Local dependency |
| --- | --- | --- | --- | --- |
| NC-COMPLAINT-01.A | Was the recorder ever on the disputed property, and what law applies if not? | v2 | Supported | Yes |
| NC-COMPLAINT-01.B | What is the legal effect of entering but leaving when requested? | v2 | Supported | Yes |
| NC-COMPLAINT-01.C | What law governs currently remaining after a request to leave? | v2 | Supported | Yes |
| NC-COMPLAINT-01.D | What is the effect and permissible scope of prospective no-entry notice, and what separate authority governs any claimed duty to identify for that notice? | v2 | Researched-Unresolved | Yes |
| NC-COMPLAINT-01.E | What factual allegations and actual offense elements support initial detention? | v2 | Supported | Yes |
| NC-COMPLAINT-01.F | What caller/tip reliability rule applies? | v2 | Supported | No |
| NC-COMPLAINT-01.G | What binding circuit rule governs offered/known exculpatory evidence? | v2 | Supported | No |
| NC-COMPLAINT-01.H | When can reasonable suspicion or probable cause dissipate? | v2 | Supported | No |
| NC-COMPLAINT-01.I | How does immediately available video affect the continuing detention/arrest analysis? | v2 | Researched-Unresolved | No |
| NC-COMPLAINT-01.J | What First Amendment retaliation rule applies? | v2 | Supported | No |
| NC-COMPLAINT-01.K | What state/local false-report or emergency-call laws apply to knowingly false factual allegations? | v2 | Supported | Yes |
| NC-COMPLAINT-01.L | What records should be preserved/requested after the encounter: 911 audio, CAD/dispatch, body camera, CCTV, incident reports, exclusion notices, complaints, and related evidence? | v2 | Supported | Yes |
| NC-COMPLAINT-01.M | When access is conditioned on stopping recording/speech/observation, was the underlying restriction and resulting exclusion lawful before downstream trespass enforcement is analyzed? | v2 | Supported | Yes |

## NC-VANTAGE-01 — Lawful-vantage observation and recording

Canonical version: **v1**. This scenario is public/private-subject neutral: the applicable authority may differ, but every jurisdiction must be able to analyze ordinary observation/recording from a lawful vantage without collapsing visibility, privacy, property, audio, intrusion, and exclusion into one rule.

| Canonical branch ID | Required question | Version | Status | Local dependency |
| --- | --- | --- | --- | --- |
| NC-VANTAGE-01.A | Is the observer lawfully present at the vantage point, and what authority governs the right to remain there? | v1 | Supported | Yes |
| NC-VANTAGE-01.B | What rules govern ordinary visual observation, photography, or video of people, property, activity, vehicles, or interiors exposed to ordinary view from that lawful vantage? | v1 | Supported | Yes |
| NC-VANTAGE-01.C | How do transparent windows, windshields, doors, or other transparent barriers affect the analysis when the observer does not cross, open, touch, manipulate, or defeat the barrier? | v1 | Supported | Yes |
| NC-VANTAGE-01.D | What law applies when documents, screens, records, identifiers, or other potentially sensitive/confidential information are left visible from the lawful vantage? | v1 | Supported | Yes |
| NC-VANTAGE-01.E | What changes when the observer physically enters, reaches into, touches, moves, opens, manipulates, defeats a barrier/covering, or otherwise intrudes beyond ordinary observation? | v1 | Supported | Yes |
| NC-VANTAGE-01.F | What separate rules apply to technological enhancement, audio capture/confidential communications, voyeuristic/privacy offenses, or other methods that may implicate interests not presented by ordinary unaided visual observation? | v1 | Supported | Yes |
| NC-VANTAGE-01.G | If an owner, employee, official, security worker, or officer demands that observation/recording stop, that the observer move, or that the observer leave, what independent authority supports that restriction or exclusion and what property/forum facts control? | v1 | Supported | Yes |

## Existing-research population result

The first population pass is complete:

1. existing California handbook chapters, Authority Index entries, and sweep ledgers were mapped to every row;
2. existing national, Ninth Circuit, California constitutional, statutory/regulatory, and state-case material was reused without new external research;
3. existing limitations and contrary authority were preserved through authority bundles;
4. every row received a provisional qualification status;
5. **Researched-Unresolved** was kept distinct from incomplete research; and
6. the original 28 Gap rows were deduplicated into 8 substantive research packages; Sweeps 011 through 018 have now closed GAP-01 through GAP-08. No row remains in Gap status; final qualification and activation controls remain.

Current provisional totals:

- **69 Supported**
- **4 Researched-Unresolved**
- **0 Gap**
- **0 Not Applicable**

These numbers do not activate California and are not a completeness score. See [QUALIFICATION-EVIDENCE-MAP.md](QUALIFICATION-EVIDENCE-MAP.md) for branch rationales and [California Final Adversarial Qualification Review](../research/CA-FINAL-ADVERSARIAL-QUALIFICATION-REVIEW.md) for the final substantive gate review.

## Canonical standing-scenario dependency

CA-GATE-08 has now been addressed by `NC-STANDING-01 v1`, the jurisdiction-neutral factual baseline in `docs/national-core/standing-scenario.md`.

California's `standing-scenario.md` is an overlay/crosswalk rather than the national source. `NC-COMPLAINT-01 v2` and `NC-VANTAGE-01 v1` explicitly inherit the neutral baseline.

The final adversarial review confirmed that no California-specific legal conclusion is silently doing factual work in the canonical scenarios.

## Activation transition: county inventory

California county research is downstream of state qualification, not a prerequisite to it.

At activation, the workflow created and validated the complete California county inventory as `CountyCoverageUnit` records. Every county began **Unresearched**; later promotion requires reconciliation against the qualified California framework and the applicable human review.

County coverage is **Unresearched / Researching / Established** and must not be confused with the California Field Guide qualification status. County records inherit the national core, Ninth Circuit/federal layer, and Active California overlay; they store only county/local law, policy, practice, agencies/facilities, enforcement history, records practice, and other local dependencies.

Existing Contra Costa work is therefore preserved as pre-activation development/test material and should be reconciled into the Contra Costa coverage record after California activation rather than used to qualify California by volume.

## Activation result

California was activated on **2026-09-30** after the Founder made the separate CA-GATE-10 human activation decision. The statewide overlay is **Active** and statewide facility-research maturity begins **Unresearched**.

The activation transition created and verified the complete 58-county `CountyCoverageUnit` inventory. County **research completion** is not an activation requirement; every county begins Unresearched unless and until local work is reconciled and reviewed. See [California County Coverage Inventory](COUNTY-COVERAGE-INVENTORY.md).

The four Researched-Unresolved rows remain visible constraints after activation, and the CA-GATE-09 retrospective independent-review obligation remains in force.
