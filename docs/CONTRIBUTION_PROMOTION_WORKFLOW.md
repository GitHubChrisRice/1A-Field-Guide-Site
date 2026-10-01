# Contribution Credit and Promotion Workflow

Issue: #41

This document defines how accepted Coalition work becomes contribution credit, how credit supports promotion eligibility, and how additional role authority is granted.

The system is designed to recognize useful, trustworthy work without turning legal research into a contest for volume, preferred outcomes, or public rank.

## Governing principles

1. **Points record accepted contribution; they do not create authority.**
2. **Quality and trust gates matter more than totals.** A threshold only makes a member eligible to request promotion.
3. **Outcomes are neutral.** Research supporting a government restriction, contradicting it, correcting the Coalition, or concluding Researched-Unresolved may receive the same credit when the work is equally rigorous.
4. **Credit is scoped.** Work in one jurisdiction does not automatically establish competence in another.
5. **Accepted work is the unit of credit, not clicks, words, citations, uploads, comments, or raw activity.**
6. **Review authority must be demonstrated before it is granted.**
7. **Promotion is a human trust decision with an audit trail.**
8. **Administrator is not a merit rank.** Points can never unlock administrative/platform authority.
9. **There is no public leaderboard by default.** Contribution credit exists to support internal recognition, eligibility, and governance.

## Role progression

The normal contributor/trust progression is:

```text
Member
  |
Contributor
  |
Researcher
  |
Reviewer
  |
Senior Reviewer
  |
Division Lead
```

`Administrator` is separate from this ladder.

Administrator is a platform/governance role granted through a separate authority decision. A person can be an Administrator without being a substantive reviewer, and a substantive reviewer does not become an Administrator through points or promotion.

Roles remain scoped grants under the Coalition data model. A member may therefore hold different roles in different jurisdictions.

## What contribution points mean

Contribution points are an internal ledger summary of work that the Coalition accepted or separately recognized as useful.

They may be used to answer questions such as:

- Has this person contributed enough accepted work to request additional responsibility?
- Has this person demonstrated work in the jurisdiction where they seek a scoped role?
- Has this person contributed across enough types of work to show breadth?
- Has this person performed enough accepted review work to be considered for Senior Reviewer?

They do **not** answer:

- Is this person legally correct in every dispute?
- Should this person automatically be trusted with restricted investigations?
- Should this person be allowed to publish?
- Should this person lead a division?
- Is this person "better" than another contributor?
- Is a jurisdiction ready for activation?

Points are evidence, not authority.

# Contribution ledger

Each credit award is represented by a `Contribution` ledger entry tied to the work that generated it.

The ledger is append-oriented. Awards, reversals, and replacement awards remain historically traceable.

## Contribution fields

The existing Contribution entity should support at least:

- `id`;
- `membership_id`;
- `jurisdiction_id` - nullable only for truly project-wide work;
- `contribution_class`;
- `credit_rule_code` - stable rule identifying the applicable credit class/review tier;
- `credit_policy_version`;
- `credit_points`;
- `source_entity_type`, `source_entity_id`;
- `source_revision_id` - where an immutable revision exists;
- `credit_scope_basis` - direct jurisdiction, applicable national core, applicable circuit/federal layer, or project-wide methodology;
- `credit_applicability_refs` - explicit national/circuit/jurisdiction/methodology applicability references used for target-scope eligibility;
- `status` - pending, accepted, reversed;
- `recommended_by` - nullable;
- `awarded_by`;
- `awarded_at`;
- `reversal_of_id` - nullable;
- `reason`;
- `created_at`.

The source entity should normally be an approved ResearchSubmissionRevision, a completed Review, an accepted correction, or another explicitly approved contribution source.

No credit is created merely because a record exists.

# Credit classes

Initial author/research credit uses a small fixed scale.

Every award records a stable `credit_rule_code` and `credit_policy_version`. Implementations should validate the awarded points against the schedule for that policy version rather than accepting arbitrary numbers.

The initial credit schedule uses `credit_policy_version = CREDIT_V1` with these rule codes:

| Rule code | Credit |
| --- | ---: |
| RESEARCH_VERIFY | 1 |
| RESEARCH_STANDARD | 2 |
| RESEARCH_SUBSTANTIVE | 3 |
| RESEARCH_MAJOR | 5 |
| REVIEW_SOURCE_OR_RESEARCH | 1 |
| REVIEW_DOCTRINAL_OR_FINAL | 2 |
| REVIEW_ELEVATED_ADDITIONAL | 3 |

## 1 point — Verification

Use for accepted work that materially improves confidence or currency without independently resolving a substantial research question.

Examples:

- verifying current primary statutory/regulatory text;
- confirming case later history or precedential status;
- verifying a policy version/effective date;
- checking source provenance;
- documenting a material source correction;
- independently verifying evidence when independent verification was requested or substantively useful.

Pure formatting, spelling, or cosmetic edits normally receive no contribution points unless they correct a material ambiguity or source error.

## 2 points — Standard research result

Use for a discrete accepted research/evidence result that adds useful substance.

Examples:

- a narrowly supported legal proposition;
- a useful public-records result with provenance and supported propositions;
- a material evidence package;
- a discrete facility-policy/authority finding;
- a meaningful update to an existing authority record;
- a well-supported Researched-Unresolved or Gap result.

The direction of the result does not affect the points.

## 3 points — Substantive research result

Use for accepted work requiring meaningful synthesis, analysis, or correction.

Examples:

- a jurisdiction-overlay branch resolution;
- a material facility analysis;
- a significant legal correction;
- a multi-source records result that changes the investigation;
- a substantive contrary-authority package;
- a material dependency update;
- a developed facility research component that applies multiple authority layers.

## 5 points — Major integrated research package

Use sparingly for accepted work that integrates several substantial components into one coherent research product.

Examples:

- a complete multi-source facility investigation or system sweep;
- a major jurisdiction-overlay research package spanning multiple related branches;
- a major correction requiring dependency analysis across several published conclusions;
- a canonical scenario/decision-tree research package that materially advances the national framework.

"Large" means substantively integrated and consequential, not simply long.

## One author-credit classification per accepted research unit

An accepted research revision receives one primary author/research credit classification for each contributor whose material work is documented.

The following do not multiply points by themselves:

- number of sources;
- number of pages;
- number of citations;
- number of canonical branches referenced;
- number of form sections;
- number of files uploaded;
- number of revisions required before acceptance.

If one submission intentionally combines several genuinely independent research products, the reviewer may require them to be separated into independently reviewable units before credit is assigned.

# Review credit

Formal review is itself meaningful contribution work.

A completed Review may receive credit when the review is substantive, within scope, and satisfies the workflow standard.

Initial review credit:

| Review contribution | Points |
| --- | ---: |
| Source-verification or ordinary research review | 1 |
| Doctrinal/evidentiary or final-publication review | 2 |
| Additional elevated-impact substantive review | 3 |

If the same reviewer legitimately satisfies multiple stages on the **same immutable revision**, they receive the highest applicable single review credit, not the sum of every stage.

This prevents review-stage multiplication from becoming a points strategy.

An Approve decision is not required for review credit. A rigorous Request Changes or Reject may be creditable when the review work itself was useful and properly performed. An Abstain may be creditable only when it contains substantive analysis that materially advances the review despite the reviewer declining the decision. A conflict-only recusal is good governance but does not normally earn points by itself.

A superficial approval is not automatically creditable merely because it is a Review record.

# Corrections and self-correction

Corrections are valuable work and must not be disfavored.

A correction is credited according to the same 1/2/3/5 research scale based on substantive value.

## Correcting someone else's or institutional work

A contributor may receive full appropriate credit for:

- finding a material factual error;
- locating controlling contrary authority;
- identifying superseded law/policy;
- correcting an overbroad field rule;
- discovering a privacy/provenance defect;
- documenting that a prior conclusion should become unresolved.

## Correcting one's own prior work

Good-faith self-correction is expected and should not be punished.

However, fixing one's own previously accepted error does not normally create a second full credit event merely for repairing the same work. Additional credit may be appropriate when the correction required substantial new research or produced a genuinely new accepted contribution beyond the repair itself.

This avoids both disincentivizing honesty and creating an error-then-correct points strategy.

# Results that receive equal treatment

For equal-quality work, contribution credit must not depend on whether the result:

- supports an auditor's initial theory;
- supports the government's legal position;
- finds a restriction likely invalid;
- finds a restriction supported;
- identifies contrary authority;
- shows an incident narrative was inaccurate;
- documents no violation;
- concludes Researched-Unresolved;
- identifies a material Gap;
- results in a correction to Coalition content.

The project rewards reliable research, not ideological direction.

# When credit is awarded

Research credit is normally eligible only after the exact ResearchSubmissionRevision has been Approved under the required review workflow.

Review credit is eligible after the Review record is completed and its quality is accepted for credit by an authorized awarder.

Publication is **not** required before contribution credit may be awarded. Useful accepted research can remain internal, unresolved, superseded later, or be withheld from public release for privacy reasons and still have been a real contribution.

# Credit recommendation and award authority

Under the initial permission model:

- Reviewer, Senior Reviewer, or Division Lead may recommend contribution credit where they are authorized to assess the work;
- Senior Reviewer or Division Lead may award/reverse credit within their delegated scope;
- Administrator may perform the administrative award/reversal action based on the substantive workflow, but Administrator status alone is not recommendation authority;
- no person may award or reverse **their own** contribution credit;
- the award/reversal must identify the source work and reason.

Administrator status alone does not transform an Administrator into the substantive reviewer of the work. When an Administrator awards credit based on substantive acceptance, the underlying research/review disposition must already come from the authorized substantive workflow.

# Credit-policy version changes

Changing the credit schedule requires a new `CREDIT_*` version. Changing promotion eligibility floors or competency-count rules requires a new `PROMOTION_*` version.

Existing historical awards keep the value and rule under which they were issued unless governance deliberately approves an audited migration. A new schedule does not silently recalculate old contributions.

Already-granted roles are not automatically revoked or downgraded because a later policy version raises an eligibility floor. Role maintenance/review remains a separate governance decision.

If a migration is ever required, use explicit adjustment/reversal/replacement records so the before/after totals remain explainable.

# No silent point editing

Once accepted, a Contribution ledger entry is not silently edited to change its point value.

If an award was wrong:

1. create a reversal referencing the original entry;
2. record the reason;
3. create a replacement award when appropriate.

This preserves the historical audit trail.

# Credit reconsideration and correction

A member may request reconsideration when they believe a credit award contains a factual error in:

- contributor attribution;
- credit rule/classification;
- point value under the recorded policy version;
- scope/applicability references; or
- duplicate/reversal status.

Where practical, a different authorized Senior Reviewer or Division Lead should examine the request. Reconsideration does not rewrite the original ledger entry. The outcome is no change, or an audited reversal/replacement.

A credit reconsideration does not reopen the underlying legal/research conclusion unless the research workflow independently requires correction.

# Legacy / pre-platform work

Substantive work completed before the Coalition portal or contribution ledger exists may receive retrospective credit only when:

- the specific source artifact/work is identifiable;
- the contributor's material role can be documented;
- the work can be evaluated against the applicable current or explicitly approved historical standard;
- an authorized awarder assigns a normal credit rule and applicability record; and
- the award is marked as retrospective/legacy in its reason/audit metadata.

Do not grant bulk points for vague assertions of prior participation, years of service, repository ownership, founding status, or project administration.

Bootstrap/founding RoleGrants do not create Contribution points. Historical research may be credited on its own merits separately.

# When points are not reversed

Points generally remain when accepted work later becomes obsolete because:

- law changes;
- policy changes;
- stronger authority is later discovered;
- a facility changes configuration;
- a good-faith interpretation is later narrowed;
- a later correction supersedes the accepted work.

The contribution still occurred and passed the standards in effect at the time.

A later substantive correction can itself receive credit.

# When points may be reversed

Reversal is appropriate when the **credit award itself** was invalid, including:

- duplicate credit for the same work;
- wrong contributor attribution;
- arithmetic/classification error;
- credit issued without the required acceptance/review;
- fabricated or intentionally falsified source/evidence;
- plagiarism or deliberate misrepresentation that invalidates the credited work;
- other documented integrity failure directly defeating the basis for the award.

Ordinary good-faith research disagreement is not an integrity failure.

# Anti-gaming rules

## No activity points

Do not award points for:

- account age;
- logins;
- comments;
- reactions;
- issue count;
- raw submissions;
- raw records requests;
- raw uploads;
- word count;
- citation count;
- facility count;
- time spent;
- number of revisions after Changes Requested.

## No fragmentation multiplier

Closely related work that would ordinarily be one research product does not generate extra credit merely because it was split into many submissions.

Reviewers/awarders may group related submissions into a single credit unit when fragmentation would otherwise inflate points.

## Duplicate work

Duplicate or near-duplicate work receives no additional credit unless it adds documented value such as:

- requested independent verification;
- later history;
- a new primary source;
- a material correction;
- contrary authority;
- a distinct jurisdictional application.

## No double author/reviewer credit on the same revision

A contributor cannot receive both author credit and formal reviewer credit for the same submitted revision because the workflow already prohibits self-review.

## No stage stacking

A reviewer who performs several review stages on one revision receives only the highest applicable review-credit amount for that revision.

## No preferred-result bonus

Do not increase credit because a submission exposes misconduct, supports a popular legal theory, produces a dramatic incident, or reaches another preferred outcome.

## Reciprocal-pattern review

The system may flag unusually concentrated reciprocal credit/review patterns for administrative audit.

A flag is not itself proof of misconduct and does not automatically remove credit.

# Co-authored work

Multiple people may receive credit from one accepted research product when the internal record documents each person's material contribution.

Credit is not automatically divided as a zero-sum pool, because meaningful collaboration should not penalize participants.

However:

- merely being listed as a collaborator is insufficient;
- each credited member needs a documented contribution basis;
- identical full credit must not be copied to participants whose work was nominal;
- the award reason should briefly state the person's contribution.

# Scope-aware points

Promotion is scoped, so eligibility uses both total accepted contribution and target-scope contribution.

## Total points

All valid Contribution ledger points credited to the member.

## Target-scope points

Points demonstrating competence applicable to the requested role scope.

For a state role, target-scope points may include:

- direct work in that state;
- national/canonical work explicitly recorded as applicable to that state;
- applicable federal-circuit/federal-layer work explicitly linked to that state;
- project-wide methodology work explicitly recorded as target-scope-relevant.

Points from an unrelated state's unique law do not automatically count as target-state points merely because they count toward the member's total.

Scope applicability is recorded when credit is awarded or corrected, not invented during promotion review. Applicability references may identify national/core scope, a federal circuit, a jurisdiction, or project-wide methodology. Circuit applicability must be resolved through the project's explicit legal-applicability mapping rather than pretending circuits are parent jurisdictions of states.

If an applicability record is wrong, correct it through the audited credit/reversal process rather than silently reclassifying points for one candidate.

The eligibility snapshot must record how target-scope points were calculated from those existing applicability records.

# Initial promotion eligibility floors

These are **eligibility floors, not automatic promotion thresholds**.

Meeting them only permits a normal promotion request to enter human assessment. These values use `eligibility_policy_version = PROMOTION_V1` and may be changed prospectively through a new policy version after experience shows whether they are too permissive or too restrictive.

| Requested role | Total points | Target-scope points | Additional minimum evidence |
| --- | ---: | ---: | --- |
| Contributor | 5 | 3 | At least 2 accepted credited research/verification events; at least 1 direct-scope event |
| Researcher | 15 | 10 | At least 4 accepted research events across at least 2 submission/research functions; at least 2 direct-scope research events |
| Reviewer | 30 | 20 | At least 6 accepted substantive research events; at least 3 direct-scope substantive research events; plus 2 passed review-calibration exercises |
| Senior Reviewer | 60 | 40 | Current Reviewer role plus at least 10 distinct completed review matters that satisfied the workflow, including doctrinal/evidentiary review on at least 4 distinct targets, 2 complex/disputed/correction matters, at least 4 direct-scope review matters, and doctrinal/evidentiary review on at least 2 direct-scope targets |
| Division Lead | 100 | 70 | Current Senior Reviewer role in/for the scope; at least 15 distinct completed review matters; at least 6 direct-scope review matters, including doctrinal/evidentiary or final-publication review on at least 3 direct-scope targets; at least 5 senior-level review/assessment matters completed after the Senior Reviewer grant, including 2 elevated-impact/final-publication or comparable senior-level matters; breadth across jurisdiction-overlay and facility/records work; and a leadership assessment |

A "substantive research event" for Reviewer eligibility normally means a distinct accepted 2-, 3-, or 5-point research unit. Verification-only volume cannot by itself create Reviewer eligibility.

For promotion experience counts, a **review matter** means a distinct immutable ResearchSubmissionRevision or PublicationCandidateRevision reviewed by the member. Performing multiple review stages on the same immutable target counts as one review matter for volume/breadth thresholds, even though the individual Review records remain preserved. Where the table requires a particular review type, the target must actually include that stage.

For a state or local role, a **direct-scope** event is work materially grounded in that jurisdiction's own constitution, statutes/regulations, cases, ordinances, records, facilities, or enforcement evidence. National or circuit work may count toward target-scope points when applicable, but does not satisfy the direct-jurisdiction evidence floor merely because it applies there.

For a federal, circuit, national-methodology, or other non-state scope, "direct-scope" is interpreted against that requested scope rather than forcing state-specific work.

This direct-scope floor prevents transferable national/circuit credit from standing in for jurisdiction-specific competence while still recognizing that reusable federal work legitimately applies across jurisdictions.

Administrator has no point threshold because it is not part of the promotion ladder.

# Review calibration before Reviewer authority

A Researcher seeking Reviewer status must demonstrate review judgment before receiving authority to approve other people's work.

A **review-calibration exercise** is not a formal Review decision and does not affect the underlying submission.

The candidate is given an already-dispositioned research revision they are authorized to access, or a specially prepared/sanitized calibration fixture, and independently identifies:

- the proposition being reviewed;
- source sufficiency;
- binding/persuasive posture where applicable;
- overbreadth or unsupported inference;
- contrary authority/evidence;
- uncertainty;
- appropriate disposition: approve / changes needed / reject / abstain;
- reasons for that disposition.

An authorized Senior Reviewer or Division Lead evaluates the calibration against the actual review record and methodology.

Reviewer eligibility requires two passed calibration exercises. At least one must involve a non-routine problem such as:

- contrary authority;
- a correction;
- Researched-Unresolved;
- a source that supports one proposition but not another;
- an allegation/evidence distinction;
- a procedural-posture trap.

Calibration exercises generate PromotionAssessment records, not formal Reviews and not review points.

# Promotion competency gates

Points establish contribution volume/breadth. Promotion assessment establishes trust for the requested authority.

The promotion reviewer must consider criteria appropriate to the requested role.

## Contributor

Evidence should show the member can:

- submit useful work;
- follow basic source/provenance requirements;
- respond to review feedback;
- work within privacy/classification boundaries.

## Researcher

Evidence should additionally show the member can:

- formulate a narrow research question;
- distinguish authority, policy, evidence, and conclusion;
- preserve uncertainty;
- find and disclose contrary material;
- apply the standing methodology consistently.

## Reviewer

Evidence should additionally show the member can:

- evaluate someone else's work independently;
- detect overreading and unsupported conclusions;
- distinguish binding/persuasive authority and procedural posture;
- handle contrary evidence neutrally;
- request specific remediable changes;
- abstain/recuse when appropriate.

## Senior Reviewer

Evidence should additionally show the member can:

- review high-impact or disputed work;
- calibrate other reviewers;
- identify downstream dependency/correction effects;
- preserve national standards under local pressure;
- handle publication-level caveats and uncertainty;
- demonstrate consistent judgment across multiple matters.

## Division Lead

Evidence should additionally show the member can:

- coordinate work without lowering research standards;
- assign/prioritize work fairly;
- manage scoped access responsibly;
- recognize when questions require escalation beyond the division;
- recommend promotions based on evidence rather than loyalty or viewpoint;
- support corrections to their own division's work;
- maintain jurisdiction-specific breadth;
- separate leadership authority from publication/legal conclusions.

# PromotionAssessment

Promotion decisions should be supported by structured assessments rather than a single unexplained yes/no.

Conceptual fields:

- `id`;
- `promotion_request_id`;
- `assessor_membership_id`;
- `assessment_type` - eligibility verification, research competency, review calibration, scope knowledge, privacy/reliability, leadership, overall recommendation, or approved extension;
- `result` - pass, needs_work, recommend, defer, oppose, abstain;
- `evidence_refs`;
- `comments`;
- `created_at`;
- `superseded_by_assessment_id` - nullable.

Assessments are internal governance records, not a public scorecard.

# Normal promotion workflow

```text
Eligibility floor met
        |
Member submits PromotionRequest
        |
Eligibility snapshot frozen
        |
Required competency/calibration assessments
        |
Promotion recommendation
        |
Administrator final decision
        |
If approved: scoped RoleGrant created
        |
AuditEvent
```

## 1. Eligibility calculation

The system calculates an eligibility snapshot containing:

- total accepted points;
- target-scope points and their basis;
- accepted contribution counts/types;
- distinct immutable review-matter counts/types where applicable;
- current active role grants and the grant dates needed for role-stage evidence;
- direct-scope event/review counts required by the requested role;
- calibration/assessment prerequisites;
- relevant contribution reversals and documented quality/integrity assessments;
- requested role and scope.

The snapshot is evidence, not the decision.

## 2. Promotion request

Once the normal eligibility floor is met, the member may submit a PromotionRequest for the next role in the normal ladder within a specified scope.

The member may explain why they are ready, but self-description cannot substitute for the objective ledger and assessment record.

For a member's initial progression, normal promotion is sequential:

`Member -> Contributor -> Researcher -> Reviewer -> Senior Reviewer -> Division Lead`.

Skipping a rung in that initial progression requires an explicit bootstrap/exception authority described below and is not triggered by points.

## Scope extension for an already-trusted member

Because roles are scoped, an experienced reviewer should not have to repeat every generic rung merely to work in another jurisdiction.

A member who already holds an active substantive role may request the **same or a lower substantive role in an additional scope** through a scope-extension request.

Scope extension:

- never automatically copies a role to another jurisdiction;
- still requires the target role's target-scope point floor;
- still requires current target-scope knowledge/competency assessment;
- may reuse already-passed generic review calibration when the methodology has not materially changed;
- requires a substantive recommendation appropriate to the requested role;
- requires the same Administrator final RoleGrant decision under the initial model;
- is recorded as a scoped RoleGrant decision, not as fictional re-promotion through every lower rung.

A request for a **higher** role than the member already holds remains a normal promotion and must satisfy that higher role's requirements.

If the requested same-role extension has prerequisites that can only be earned while holding a lower substantive role in the new scope, the member first receives/requests that lower scope extension and builds the required direct-scope experience. For example, a Senior Reviewer in one state may extend as Reviewer in a new state, perform the required state-scoped review work, and then seek Senior Reviewer authority there.

This permits national/circuit/state expertise to transfer where genuinely applicable without pretending that expertise in one state's unique law automatically proves competence in another.

## 3. Recommendation

Under the initial model, division/substantive leaders **recommend** promotions; they do not create their own or another member's authority grant.

Minimum recommendation routing:

- Contributor: recommendation by Reviewer, Senior Reviewer, or Division Lead in/applicable to scope;
- Researcher: recommendation by Reviewer, Senior Reviewer, or Division Lead in/applicable to scope;
- Reviewer: recommendation by Senior Reviewer or Division Lead after calibration requirements;
- Senior Reviewer: recommendation by Division Lead or, where no appropriate Division Lead exists, by another qualified Senior Reviewer outside the candidate's authorship chain;
- Division Lead: recommendation by a qualified Senior Reviewer or existing Division Lead who is not the candidate.

The recommender cannot be the candidate.

Administrator may manage the workflow and final decision but Administrator status alone does not count as the substantive recommendation when a substantive recommender is required. An Administrator who also holds the required substantive role acts through that separate scoped RoleGrant.

## 4. Final decision

Under the **initial governance model**, only Administrator authority creates the promotion decision/RoleGrant. The candidate cannot make their own final promotion decision; an Administrator candidate must be decided by another authorized Administrator or use an explicit founding/bootstrap path where applicable.

This resolves the prior data-model ambiguity: Division Leads may recommend scoped promotions but do not independently grant Coalition role authority.

A future governance change may deliberately delegate final promotion authority, but implementation must not infer that delegation from division autonomy.

Final decisions:

- Approved;
- Deferred;
- Declined.

Approved creates the specific scoped RoleGrant.

Deferred/Declined must record a reason tied to the eligibility/competency/trust criteria rather than viewpoint or personal preference.

A declined or deferred request does not delete the member's contributions or permanently prevent a later request.

# Promotion neutrality

Promotion may not be conditioned on:

- reaching pro-auditor legal conclusions;
- reaching pro-government legal conclusions;
- political viewpoint;
- willingness to provoke confrontations;
- number of dramatic incidents;
- public popularity;
- social-media audience;
- public disclosure of identity when the project's attribution rules allow privacy.

Relevant considerations are research quality, judgment, reliability, privacy/security handling, review competence, scope knowledge, and leadership behavior tied to Coalition responsibilities.

# Quality and integrity concerns

Points alone do not override current evidence that the requested authority would be unsafe or unreliable.

Promotion assessment may consider documented patterns such as:

- repeated material source misrepresentation;
- undisclosed contrary authority after correction;
- repeated failure to distinguish allegations from established facts;
- misuse of restricted information;
- attempts to bypass review;
- falsified evidence;
- retaliatory or viewpoint-based review behavior;
- improper self-credit or reciprocal-credit manipulation.

A concern must be evidence-based and documented. Disagreement over a good-faith legal interpretation is not by itself an integrity violation.

# Point recency and legal change

Points do not decay merely because time passes.

Promotion reviewers may nevertheless require current competency evidence when:

- the target jurisdiction's law has materially changed;
- the member has not worked in the scope for a long period;
- the requested role involves current review authority;
- prior credited work predates major methodology revisions.

The remedy is current assessment/research evidence, not silent deletion of historical contribution credit.

# Role maintenance is separate

This issue defines promotion, not automatic demotion or role-expiration policy.

The existing RoleGrant model permits expiration/revocation where later governance authorizes it, but points are not automatically decremented and roles are not automatically removed because a point total changes.

Any future maintenance/renewal policy must be explicit.

# Founder, bootstrap, and founding appointments

The normal promotion ladder cannot create the first Reviewers, Senior Reviewers, Division Leads, or Administrators because nobody initially exists to assess the next person.

**Founder** is a separate project-origin governance role, not a points-based rank and not a rung in the Member -> Division Lead progression. The Founder role itself may remain permanent as provenance/governance authority. It does not automatically create substantive review competence, unrestricted sensitive access, or repository authority.

The initial repository/platform owner acting as Founder, or an existing Administrator once one exists, may make a **bootstrap/founding RoleGrant** when necessary to establish the initial governance structure. The first Administrator is established through the Founder's explicit founding authority rather than through the points ladder.

Bootstrap grants:

- require an explicit `bootstrap`/founding reason;
- are not earned automatically by points;
- must identify the scope;
- generate an AuditEvent;
- do not fabricate Contribution points;
- must be distinguishable from normal promotion grants.

A bootstrap substantive RoleGrant is different from the permanent Founder role. Once enough qualified people exist for the normal workflow, bootstrap substantive grants should be reviewed and either ratified under ordinary competency expectations, narrowed, replaced, or revoked as appropriate. The existence of the permanent Founder role does not make a bootstrap Researcher/Reviewer/Division Lead grant permanently exempt from review.

Bootstrap authority is an initialization mechanism, not a general shortcut around promotion standards.

Jurisdiction activation has a related but separate founding exception. When no independent qualified human reviewer is reasonably available, the Founder may make a documented bootstrap activation decision under the requirements in [Jurisdiction Qualification and Field Guide Overlay Model](JURISDICTION_QUALIFICATION.md). That exception does not award points, create a promotion, or falsely count the Founder or an AI/service principal as an independent reviewer.

# Public display

Contribution points are private/internal by default.

A member may see:

- their own ledger;
- total points;
- target-scope eligibility calculations;
- promotion requirements/status.

Authorized reviewers/leadership may see the contribution information necessary for credit and promotion decisions.

The public site may show published contributions or role attribution under the project's privacy rules, but a public points leaderboard or public numerical ranking requires a deliberate later governance decision.

# Audit requirements

At minimum audit:

- credit recommendation;
- credit award;
- credit reconsideration;
- retrospective/legacy credit award;
- credit reversal/replacement;
- eligibility snapshot generation;
- PromotionRequest submission;
- PromotionAssessment;
- promotion recommendation;
- final promotion decision;
- RoleGrant creation/revocation related to promotion;
- bootstrap/founding RoleGrant;
- Founder/bootstrap jurisdiction activation decision.

The audit record must identify actor, target member, source work/request, scope, outcome, timestamp, and reason.

# Required implementation invariants

Where technically practical:

- points never create or modify RoleGrants;
- points never change research/publication state;
- only accepted/recognized work can receive credit;
- awarded points must match the recorded credit-rule code and credit-policy version;
- promotion eligibility snapshots record the applicable promotion-policy version;
- the same work cannot be multiplied through fragmentation or review-stage stacking;
- promotion review-volume thresholds count distinct immutable review targets, not raw Review-record count;
- a member cannot award/reverse their own credit;
- correction/contrary/unresolved outcomes are creditable on equal terms;
- contribution direction does not affect point value;
- target-scope eligibility is calculated from credit-time recorded applicability references, not reclassified ad hoc during promotion;
- direct-jurisdiction evidence floors cannot be satisfied solely by inherited national/circuit applicability;
- circuit-derived applicability uses explicit circuit-to-jurisdiction applicability mapping rather than jurisdiction parentage;
- scope extension never automatically copies authority across jurisdictions;
- Review calibration does not create a formal Review decision;
- Administrator is excluded from the points-based merit ladder;
- normal promotion is sequential;
- Division Lead recommendation does not create the RoleGrant;
- final promotion approval is Administrator-only under the initial model;
- bootstrap grants are explicitly marked and audited;
- Founder/bootstrap jurisdiction activations are explicitly marked and audited and cannot be created by automation;
- no automated process approves promotion.

# Data-model consequences

The Coalition data model should be updated to:

- refine Contribution fields for fixed credit classes, scope basis, immutable source revision, recommendation, and reversal;
- add PromotionAssessment;
- make the normal promotion workflow point to a frozen eligibility snapshot;
- align the permission matrix so Division Leads recommend rather than decide promotions;
- preserve Administrator as final initial promotion authority;
- preserve no-self-award and no-self-promotion-decision invariants.

# Decisions intentionally deferred

This design does not decide:

- public gamification/badges beyond the default no-leaderboard rule;
- future delegation of final promotion authority away from Administrator;
- role renewal/expiration/demotion policy;
- detailed UI for the contribution ledger or promotion request;
- privacy/retention rules owned by #43;
- GitHub integration mechanics owned by #45.

Those choices require separate deliberate governance changes.
