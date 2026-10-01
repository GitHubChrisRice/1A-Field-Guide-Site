# Structured Research Submission and Review Workflow

Issue: #42

This document defines the contributor-facing research pipeline for the 1A Field Guide Coalition. It translates the existing California research standard into structured submissions that can be validated, reviewed, corrected, credited, and prepared for publication without giving ordinary contributors direct publication authority.

It does not replace the substantive methodology in the Field Guide. It defines how work enters and moves through that methodology.

## Governing principle

A submission is a **proposal or evidence package**, not authoritative Field Guide content.

The publication path is:

```text
Draft
  |
Submit immutable revision
  |
Automated validation
  |
Human research/source review
  |
Applicable doctrinal/evidentiary/privacy review
  |
Approved research revision
  |
Publication candidate
  |
Final publication approval
  |
Controlled export / GitHub preparation
  |
Repository publication / merge
```

Each boundary is real. No earlier state silently implies a later one.

In particular:

- validation does not mean the proposition is legally correct;
- review approval does not publish the work;
- contribution credit does not publish the work;
- publication-candidate approval does not itself merge a repository change; and
- repository credentials remain separate from Coalition roles.

## Contributor experience

The ordinary contributor should not need to understand GitHub.

A contributor should be able to:

1. choose a contribution type;
2. complete a structured form appropriate to that type;
3. attach or cite the supporting sources/evidence;
4. save a private or scoped draft;
5. submit a fixed revision for review;
6. receive validation errors or reviewer requests for changes;
7. create a new revision addressing those requests;
8. see the disposition and review history of their work;
9. receive contribution credit when work is accepted under the later points policy; and
10. see whether accepted work was later published, superseded, corrected, or remained internal.

The contributor does not choose whether their own work is authoritative.

## Submission lifecycle

The existing `ResearchSubmission.status` values are interpreted as follows.

### Draft

Editable working state owned by the submitter.

A Draft:

- may be incomplete;
- has no review effect;
- cannot satisfy qualification or publication requirements;
- may contain scoped/private working notes;
- may be withdrawn without preserving every intermediate edit as a review artifact.

### Submitted

The contributor has declared a specific revision ready for validation and review.

Submitting creates an immutable `ResearchSubmissionRevision`. Later edits occur in a new working revision; they do not change the submitted revision underneath existing review decisions.

### Validation Failed

Automated or deterministic checks found a defect that prevents substantive review.

Examples:

- required field missing;
- invalid jurisdiction identifier;
- malformed or missing source reference;
- required date/version omitted;
- facility submission missing the specific area being analyzed;
- correction missing the target being corrected;
- restricted evidence submitted into a public-only field;
- submission references a superseded canonical branch without acknowledging it.

Validation Failed does **not** mean the legal proposition is wrong.

The contributor may correct the draft and submit a new revision.

### In Review

The submitted revision passed validation and is undergoing required human review.

The exact stages depend on submission type and impact.

### Changes Requested

A reviewer identified a remediable issue.

The reviewer must state what needs to change and why. The contributor responds through a new revision.

The prior revision and review remain in history.

### Approved

All review stages required for the research submission itself have been satisfied for that exact revision.

Approved means:

> the submission's `approved_revision_id` points to this exact revision, which is accepted as Coalition research input and may be used by later qualified workflows.

Approved does **not** mean:

- already published;
- automatically authoritative everywhere;
- automatically incorporated into a jurisdiction's qualification matrix;
- automatically awarded a particular point value;
- automatically safe for public release; or
- automatically merged to GitHub.

### Rejected

The submission is not accepted in its current proposition or evidentiary form.

A rejection should preserve a reason such as:

- unsupported proposition;
- materially unreliable source;
- duplicated work with no added value;
- irreconcilable factual defect;
- legal conclusion exceeds authority;
- privacy/safety problem that cannot be cured;
- outside project scope.

Rejection is not a penalty for reaching a result the project dislikes.

### Withdrawn

The submitter voluntarily stops review. Existing audit/review history remains where required for accountability.

### Superseded

A later accepted revision/submission replaces this one for the relevant proposition or evidentiary purpose.

Superseded does not mean deleted or historically nonexistent.

### Changes after approval

Once a ResearchSubmission has an Approved revision, later substantive research should normally enter as a new submission that supersedes or corrects the approved work rather than reopening and rewriting the accepted submission history.

The approved revision remains the historical record of what was accepted at that time.

## Immutable submission revisions

### ResearchSubmissionRevision

Human review attaches to an immutable revision, never to a moving draft.

Minimum conceptual fields:

- `id`;
- `research_submission_id`;
- `revision_number`;
- `schema_version`;
- `canonical_branch_refs` - zero or more immutable `{branch_id, branch_version}` references where applicable;
- `structured_payload`;
- `visibility_classification`;
- `created_by_membership_id`;
- `created_at`;
- `submitted_at`;
- `content_hash` or equivalent integrity reference where practical;
- `supersedes_revision_id` - nullable.

A review decision must record the exact `ResearchSubmissionRevision.id` reviewed.

Any substantive change after a review decision requires a new revision. Prior substantive approvals become stale by default. An authorized reviewer may explicitly re-affirm an unaffected stage for the new revision, but the system must record that carry-forward decision rather than silently assuming the old approval still applies.

Clerical metadata may be corrected without restarting substantive review only when the system can prove the correction did not change the reviewed proposition, evidence, classification, or publication content. Such corrections remain auditable.

## Common submission fields

Every submission type should capture, where applicable:

- submission type;
- jurisdiction and scope;
- title / short description;
- research question or proposition;
- canonical scenario/encounter branch affected;
- canonical branch version;
- source/evidence references;
- narrow statement of what each source supports;
- limitations / contrary evidence or authority;
- unresolved questions;
- verification/retrieval date;
- visibility classification;
- related facility/investigation/publication records;
- whether the work corrects or supersedes existing material;
- submitter notes for reviewers.

A contributor must not be required to manufacture a legal conclusion when the correct result is uncertainty.

## Source references

A source reference should preserve enough metadata to verify what was reviewed.

Minimum conceptual fields:

- source type;
- title/identifier;
- issuing body / court / agency / record custodian where applicable;
- jurisdiction;
- direct source location;
- decision/adoption/effective/version date where applicable;
- retrieval/verification date;
- authority level and binding/persuasive posture where applicable;
- preserved-copy/evidence reference where appropriate and lawful;
- visibility classification;
- proposition(s) the source supports;
- limitations on what the source proves.

A source may support one proposition without supporting another.

For example:

- a statute may prove the statutory elements;
- an agency policy may prove what the agency says its rule is;
- a body-camera video may prove observable encounter facts;
- none of those sources, by their existence alone, proves that a challenged restriction is constitutional.

## Submission types

### 1. Legal authority / proposition

Use for constitutions, statutes, regulations, court rules/orders, judicial opinions, and legal propositions derived from them.

Required structured content:

- exact authority/citation;
- jurisdiction;
- issuing court/body;
- date/version;
- precedential status where applicable;
- binding/persuasive posture for the jurisdiction at issue;
- procedural posture for cases;
- narrow proposition supported;
- facts/material predicates that limit the proposition;
- later history / amendment / supersession where known;
- contrary or limiting authority;
- affected canonical branch(es);
- proposed field rule, if any;
- unresolved questions;
- primary source.

A legal-authority submission must distinguish:

- allegations from findings;
- dicta from holding where material;
- procedural rulings from merits rulings;
- qualified-immunity analysis from a definitive merits rule;
- settlement from adjudication.

### 2. Jurisdiction-overlay branch

Use to resolve or update a canonical scenario/encounter branch for a federal circuit, state, or other approved legal jurisdiction.

Required structured content:

- canonical branch ID and version;
- issue/question answered;
- national authority inherited;
- applicable circuit/federal authority;
- state constitutional authority;
- state statute/regulation;
- state appellate authority;
- contrary/conflicting authority;
- local dependency, if any;
- proposed branch status: Supported / Researched-Unresolved / Gap / Not Applicable;
- proposed field rule/test;
- verification dates;
- explicit explanation for Researched-Unresolved or Not Applicable.

The contributor proposes branch status. Qualification reviewers decide whether it satisfies the jurisdiction qualification standard.

A Gap is valid research output. The system must not reward a contributor for hiding it.

### 3. Facility research

Use for a facility, specific area, restriction, access question, policy, or systematic facility sweep.

Required structured content should preserve the functions in the facility-investigation methodology:

- facility and controlling agency;
- specific area/subarea;
- research question;
- access status/public hours;
- ownership/control/boundary evidence where material;
- applicable qualified jurisdiction overlay;
- forum/activity classification analysis;
- current policy and provenance;
- claimed legal authority;
- implementation/signage;
- prior incidents/enforcement;
- exclusion/removal authority;
- detention/citation/arrest authority where implicated;
- records research;
- field verification, if any;
- post-visit evidence, if any;
- verified facts;
- official policy;
- controlling law;
- legal analysis;
- unresolved questions;
- research flags/classifications;
- source/evidence manifest.

A facility submission may not collapse:

`facility = area = policy = criminal authority = constitutional conclusion`.

Those remain separate propositions.

Before a jurisdiction is Active, real facility material may be submitted only as development/test-fixture research under the qualification rules. It cannot become a qualified public facility conclusion and does not advance facility-research maturity.

### 4. Public-records result

Use for CPRA, FOIA, or analogous official-record responses and productions.

Required structured content:

- requesting jurisdiction/agency;
- request date;
- request text or stable request reference;
- response/determination dates;
- records requested;
- records produced;
- records withheld/partially withheld;
- exemptions/privileges asserted, if any;
- appeal/follow-up status where applicable;
- source files/evidence references;
- provenance and chain sufficient to show the record came from the responding agency;
- proposition each produced record supports;
- privacy/redaction concerns;
- relationship to an existing investigation, authority question, or facility entry.

A records result proves what the production/response establishes. It does not automatically prove that an agency's legal interpretation in the response is correct.

### 5. Correction

Use when existing Coalition material may be inaccurate, stale, overstated, incompletely sourced, or materially misleading.

Required structured content:

- exact target being corrected;
- current published/internal proposition;
- proposed corrected proposition;
- reason for correction;
- new or newly discovered authority/evidence;
- affected canonical branches, jurisdictions, facility conclusions, and publication artifacts where known;
- whether the problem is legal, factual, source/version, privacy, attribution, or other;
- urgency/impact flag;
- whether the contributor recommends dependent material be temporarily suspended pending review.

A contributor may submit a correction without having a complete replacement answer when the existing material is materially unsafe or wrong. Such a submission may be routed for expedited human review before full replacement research is complete. A contributor's suspension recommendation does not itself change published material; withdrawal, warning, or temporary-status action requires the authority that already governs the affected publication.

Corrections never silently erase prior provenance.

### 6. Investigation evidence

Use for evidence that may support or contradict an investigation without itself asserting a full facility/legal conclusion.

Examples:

- video/audio;
- photographs;
- signage;
- CAD/dispatch;
- body-camera footage;
- incident report;
- exclusion notice;
- correspondence;
- preserved GIS/property evidence;
- contemporaneous notes;
- official meeting video/minutes.

Required structured content:

- investigation/facility relationship;
- evidence type;
- source/provenance;
- date/time or time range;
- exact area/context;
- authenticity/provenance notes;
- what is directly observable;
- what is inferred rather than directly shown;
- privacy/identity classification;
- preservation reference;
- limitations or missing context.

Evidence submission must not convert an allegation into a fact merely because the allegation appears in an official report.

## Submission types versus contribution credit

The later contribution-points policy may credit accepted:

- research submissions;
- source verification;
- corrections;
- substantive reviews;
- other approved work.

Formal review work is represented by the `Review` record itself and does not require reviewers to create artificial ResearchSubmissions merely to receive credit.

A Contributor or Researcher who does not hold Reviewer authority may still perform useful source-verification research by submitting the verified source, updated authority, correction, or other appropriate ResearchSubmission. That work may later receive contribution credit, but it does **not** satisfy a required formal Source Verification review stage. Only an authorized reviewer may record the review decision that satisfies that stage.

# Validation

Validation occurs before substantive human review.

## Deterministic validation may check

- required fields;
- schema version;
- valid jurisdiction/scope identifiers;
- valid canonical branch ID/version when required;
- source URL/reference shape;
- required date/version fields;
- duplicate exact source identifiers;
- required relationship to facility/investigation/correction target;
- allowed status values;
- visibility/classification compatibility;
- whether restricted data is being placed into a public field;
- whether the current user may submit in the requested scope;
- whether a superseded branch/version requires rebase or acknowledgement;
- basic internal consistency, such as an appellate case date preceding the claimed decision date.

## Validation must not decide

Automation must not decide:

- whether a constitutional restriction is lawful;
- whether a case truly controls the proposition;
- whether facts satisfy reasonable suspicion or probable cause;
- whether a facility is a particular forum merely from its name/type;
- whether a government interest is sufficient;
- whether a legal issue is genuinely settled;
- whether contrary authority is immaterial;
- whether an unresolved issue should be forced into a definitive result;
- whether a jurisdiction should activate;
- whether a submission deserves publication.

Automated tools may flag these questions for review.

## Duplicate and related work

The system should detect likely duplicates and related work without blocking legitimate independent verification.

A submission can add value by:

- updating a stale source;
- identifying later history;
- adding contrary authority;
- correcting a proposition;
- applying an existing rule to a new jurisdiction;
- independently verifying a high-impact source;
- contributing new facility evidence.

"Already researched" is not by itself a reason to discard a correction or contrary source.

# Human review stages

Reviews are explicit records tied to a specific immutable revision.

The initial review-stage vocabulary is:

1. **Research review**
2. **Source verification**
3. **Doctrinal/evidentiary review**
4. **Privacy/publication-safety review**
5. **Final publication review**

Not every submission needs every stage.

## Research review

Checks whether the submission actually answers the stated research question and follows the applicable methodology.

Typical questions:

- Is the proposition narrow enough?
- Are facts separated from conclusions?
- Is the jurisdiction/scope correct?
- Are relevant contrary sources acknowledged?
- Is uncertainty preserved?
- Does the facility analysis keep area/policy/enforcement questions separate?

Performed by a Reviewer or higher substantive review role within scope.

## Source verification

Checks that the cited or attached source is what the submission says it is.

Typical questions:

- Is this the official/current text?
- Is the case citation and later history correct?
- Does the record come from the claimed agency/source?
- Does the cited page/section actually support the proposition?
- Is the policy version the one that applied at the relevant time?

Source verification does not itself approve the legal conclusion.

## Doctrinal/evidentiary review

Checks the substantive inference from authority/evidence.

For legal material:

- correct controlling/persuasive classification;
- correct procedural posture;
- no overreading;
- federal/state authority relationship handled correctly;
- constitutional validity not inferred merely from policy/statute existence;
- contrary authority and unresolved questions treated accurately.

For factual/investigative material:

- direct observation separated from inference;
- reliability/provenance assessed;
- allegations not converted into established facts;
- comparator facts actually comparable;
- chronology preserved;
- legal assessment uses law applicable to the relevant time.

A Reviewer may perform this stage when authorized in scope. Higher-impact material may require Senior Reviewer or Division Lead involvement as described below.

## Privacy/publication-safety review

Required when the candidate contains or derives from Restricted, Identity-restricted, or other material that could expose:

- requester/member identity;
- unnecessary private-person information;
- unpublished sensitive evidence;
- security-sensitive details not appropriate for publication;
- confidential or legally restricted records;
- credentials or secret material.

Submission-level privacy review may classify or restrict internal material, but it does not by itself authorize public release.

When the question is whether material may appear publicly, the privacy/publication-safety decision must review the exact PublicationCandidateRevision proposed for release. That review does not rewrite the underlying evidence record.

Access to Restricted or Identity-restricted material still requires the applicable assignment/need-to-know authorization; holding a Reviewer role alone does not grant that access.

Detailed privacy/retention rules are defined in [Privacy, Identity, Attribution, and Retention Workflow](PRIVACY_ATTRIBUTION_RETENTION.md). Under PRIVACY_V1, required publication privacy review is performed by an authorized Senior Reviewer or Division Lead with the necessary sensitive-access authorization, and must be independent of the person who prepared the final candidate revision or final privacy-sensitive sanitization.

## Final publication review

Checks the **derived PublicationCandidate**, not merely the internal submission.

It asks:

- Does the public artifact accurately reflect the approved revision?
- Were required caveats/limitations preserved?
- Was private/restricted material excluded or properly transformed?
- Are source links/references appropriate?
- Does the artifact overstate the accepted proposition?
- Does it create a conflict with other published Field Guide material that must be resolved first?

Only Senior Reviewers or Division Leads with applicable substantive authority may satisfy final publication approval under the current permission matrix. Administrator status alone is not substantive publication review authority.

# Review routing by submission type

Minimum routing:

| Submission type | Research | Source verification | Doctrinal/evidentiary | Privacy | Final publication |
| --- | --- | --- | --- | --- | --- |
| Legal authority/proposition | Required | Required | Required | If needed | Required if published |
| Jurisdiction-overlay branch | Required | Required | Required | If needed | Required if published |
| Facility research | Required | Required for material sources | Required for findings | If needed | Required if published |
| Public-records result | Required | Required | Required if a legal/factual inference is drawn | Usually when records contain nonpublic/private data | Required if published |
| Correction | Required | Required for replacement sources | Same level needed for affected proposition | If needed | Required for public correction |
| Investigation evidence | Required | Required/provenance review | Required if an inference/classification is attached | Often required | Required only for public use |

A stage may be marked Not Applicable only with a recorded reason.

# Reviewer independence and conflicts

## Self-review prohibition

The submitter cannot satisfy a required review stage for their own submission or revision.

A reviewer who materially co-authored the submitted proposition is treated as an author for independence purposes.

## Conflict/recusal

A reviewer must abstain/recuse from a stage when a reasonable reviewer could not independently evaluate the work because of a material conflict.

Examples can include:

- reviewer is the subject of the investigation;
- reviewer personally participated in the incident being evaluated in a way that makes them a material witness;
- reviewer is evaluating their own prior disputed conclusion;
- reviewer has a direct personal or organizational interest in the outcome that cannot be managed through disclosure;
- reviewer lacks the jurisdictional/substantive scope needed for the review.

Recusal is not an adverse mark.

The workflow should record abstention/recusal without forcing a false approve/reject decision.

## Multiple stages by one reviewer

A qualified independent reviewer may satisfy more than one review stage for an ordinary submission where the stages are within their scope and no policy requires separation.

Higher-impact work must receive additional independent scrutiny.

# Elevated-impact routing

A submission receives elevated-impact routing when it would materially:

- change a canonical national scenario, encounter branch, or research methodology;
- change a national, circuit, or state legal proposition with downstream dependency effects;
- resolve or alter a jurisdiction-qualification branch;
- publish a material conclusion that a government restriction or enforcement action is constitutionally/statutorily supported, invalid, strongly contradicted by controlling authority, or otherwise resolves a significant disputed legal question;
- reverse or materially narrow a previously published legal/facility conclusion;
- expose or derive from significant Restricted or Identity-restricted evidence;
- create an unresolved conflict among published Field Guide propositions; or
- otherwise create a substantial dependency/correction impact.

Elevated-impact routing requires:

1. ordinary required stages;
2. at least one **additional** independent substantive review by a Senior Reviewer or appropriately scoped Division Lead who did not satisfy the primary doctrinal/evidentiary review stage; and
3. final publication review by an authorized Senior Reviewer or Division Lead who did not author the submitted revision.

At least two different qualified humans must therefore participate in the substantive review of elevated-impact work. The final-publication reviewer may also be one of those substantive reviewers if otherwise authorized and independent.

This does not mean elevated-impact work must reach a conservative or government-favorable conclusion. It means the consequences justify stronger review.

National methodology/governance changes remain subject to the separate human decision boundaries in `AGENTS.md` and `COALITION_ARCHITECTURE.md`.

# Review decisions

For each stage, the reviewer records one of:

### Approve

The exact revision satisfies the stage.

### Request changes

The revision may be acceptable after identified remediable changes.

The decision must explain the defect sufficiently for the contributor to respond.

### Reject

The revision cannot satisfy the stage without changing its fundamental proposition/evidentiary basis, is outside scope, or is materially unreliable.

### Abstain

The reviewer does not decide the stage because of conflict, insufficient expertise/scope, or another recorded reason.

Abstain never counts as approval.

# Disagreement and contrary conclusions

Review is not a vote for the preferred outcome.

A reviewer must not reject work merely because it:

- undermines an existing Coalition conclusion;
- supports a government restriction;
- shows an auditor/contributor was legally mistaken;
- identifies a factual problem with a popular incident narrative;
- concludes the issue is unresolved.

Where qualified reviewers disagree materially:

1. preserve both analyses;
2. identify the exact disputed proposition;
3. identify which authority/fact drives the disagreement;
4. seek additional scoped review when the disagreement affects publication or qualification;
5. publish uncertainty or competing authority when that is the most accurate result.

Do not manufacture consensus by deleting contrary evidence.

# Publication candidates

Approved research revisions may be transformed into one or more `PublicationCandidate` records.

A PublicationCandidate is the proposed public/authoritative artifact. It is separate from the internal submission so that sanitization, synthesis, formatting, and dependency resolution can occur without mutating the accepted research record.

Minimum conceptual fields for the PublicationCandidate workflow container:

- `id`;
- `target_type` - Field Guide chapter, authority index, jurisdiction matrix, registry entry, facility report, correction notice, or approved extension;
- `target_identifier`;
- `status` - prepared, in_final_review, approved_for_export, changes_requested, rejected, superseded, exported;
- `current_revision_id`;
- `approved_revision_id` - nullable;
- `prepared_by`;
- `prepared_at`;
- `supersedes_publication_candidate_id` - nullable;
- dependency/impact references.

Each PublicationCandidateRevision must retain links back to every research revision materially supporting that exact public version.

`exported` means the approved revision has been handed to a controlled external preparation artifact with a recorded external reference. It does not mean the repository change was merged or that the public artifact was published; those are later repository/publication transitions.

### PublicationCandidateRevision

Final-publication review attaches to an immutable PublicationCandidateRevision.

Minimum conceptual fields:

- `id`;
- `publication_candidate_id`;
- `revision_number`;
- `source_submission_revision_ids` - exact immutable research revisions supporting this publication revision;
- `derived_public_payload`;
- `visibility_classification` - internal working-access classification; the candidate remains non-Public until the approved export/publication transition;
- `dependency_refs` - canonical/jurisdiction/facility/publication dependencies affected by this exact revision;
- `content_hash` or equivalent integrity reference where practical;
- `created_by`, `created_at`;
- `supersedes_revision_id` - nullable.

A single approved research submission may support multiple publication candidates. Multiple approved submissions may be synthesized into one publication candidate.

## PublicationCandidate changes

Before export, a substantive change after final publication approval creates a new PublicationCandidateRevision, clears/invalidates the prior export approval for the current candidate, and returns it to final review.

After a PublicationCandidate has been exported/published, substantive changes should ordinarily be represented by a new superseding/correction PublicationCandidate so the previously published artifact and its approval history remain traceable.

Formatting-only or deterministic rendering changes may retain approval only when the system can prove the public meaning/content is unchanged and preserve an audit record of that determination.

# Corrections and dependency impact

When an accepted correction or new authority changes a proposition with dependent content, the system should identify affected:

- canonical branches;
- jurisdiction-overlay branches;
- qualification matrices;
- facility analyses;
- registry conclusions;
- publication candidates;
- published artifacts.

Dependency flags do not automatically rewrite legal conclusions.

A reviewer must decide whether dependent material:

- remains valid;
- requires re-verification;
- requires correction;
- should be temporarily marked unresolved;
- should be withdrawn/superseded.

Historical versions and correction provenance remain preserved.

# Privacy boundary

Submission visibility and publication visibility are separate.

Internal records may retain:

- submitter identity;
- reviewer identity;
- requester identity where operationally necessary;
- unpublished evidence;
- investigation notes;
- restricted source material.

Public artifacts must default to excluding non-Public fields unless a deliberate sanitization/transformation step creates an approved public derivative.

The system must never treat "approved research" as permission to expose the submitter's or requester's private identity.

# Audit requirements

At minimum, create auditable records for:

- submission;
- immutable revision creation;
- validation result;
- review assignment;
- review decision;
- recusal/abstention;
- changes requested;
- approval/rejection/withdrawal/supersession;
- publication-candidate creation;
- final publication approval;
- export/GitHub preparation;
- correction/supersession of published work.

Audit history is not a public contributor leaderboard.

# Contribution-credit handoff

Issue #41 will define point values and promotion eligibility.

This workflow establishes only these boundaries for that later design:

- credit is tied to accepted/dispositioned work, not raw clicks or submission volume;
- a ResearchSubmission, Review, source-verification action, or correction can be a credit source;
- rejected spam/duplicative low-value activity must not become a points strategy;
- accurate contrary findings, corrections, and Researched-Unresolved outcomes are eligible for meaningful credit;
- no credit event changes permissions or publication state by itself;
- reversals/adjustments preserve history rather than silently rewriting prior credit.

# Required implementation invariants

Where technically practical, implementation must enforce:

- reviews reference immutable revisions;
- substantive edits invalidate affected review approvals;
- a submitter cannot approve their own required review stage;
- an abstention cannot satisfy a required stage;
- automation cannot create substantive approval;
- approval does not create a public artifact;
- publication candidates retain provenance to supporting revisions;
- final-publication approval applies to a specific immutable PublicationCandidateRevision;
- restricted/private source material does not flow into public output without explicit sanitization/review;
- a policy/source proves only propositions it can actually support;
- publication cannot bypass the qualification restriction on pre-Active facility conclusions;
- contributor points cannot affect submission/review/publication state;
- Administrator role alone cannot satisfy substantive review;
- repository merge authority remains external to Coalition review roles.

# Relationship to current repository contributions

Direct GitHub Pull Requests from trusted repository maintainers may continue during development, but they should follow the same substantive evidence and review principles.

The future Coalition portal is the ordinary-member path. Once implemented, ordinary members should not need repository access to contribute.

After the repository split, `GitHubChrisRice/1A-Field-Guide-Site` protected `main` is the authoritative public-source repository, while `GitHubChrisRice/1A-Field-Guide` remains the private internal research/workspace repository. Generated website output is deployed separately from authoritative source, normally to `gh-pages` or an equivalent Pages deployment target.

Controlled export from an approved PublicationCandidateRevision into GitHub is defined in [Controlled GitHub Publication Integration](GITHUB_PUBLICATION_INTEGRATION.md). Under that design, issue-only preparation remains available during migration; branch + draft-PR automation begins only after the public authoritative `main` branch is technically protected and never includes service-principal merge authority. See [Public/Private Repository Split](PUBLIC_PRIVATE_REPOSITORY_SPLIT.md).

# Decisions intentionally deferred

This workflow does not decide:

- contribution point values or promotion thresholds (#41);
- detailed identity verification, retention, and privacy policy (#43);
- national UI design (#44);
- final database technology;
- whether any future role receives direct repository merge authority.

Those decisions must not be inferred from this workflow.
