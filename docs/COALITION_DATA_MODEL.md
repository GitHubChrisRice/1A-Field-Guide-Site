# Coalition Data Model and Permission Matrix

Issue: #39

This document defines the implementation-neutral data model and least-privilege authorization model for the Coalition platform. It refines the boundaries in [Coalition Architecture](COALITION_ARCHITECTURE.md) without changing them.

## Design principles

1. **Identity is not authority.** A user account, coalition membership, role grant, public profile, and GitHub identity are separate concepts.
2. **Roles are scoped grants, not a single global rank.** A member may hold different responsibilities in different jurisdictions.
3. **Points are evidence of contribution, not permissions.** No point total creates a role grant.
4. **Submission is not publication.** Research records retain disposition and review history separately from published artifacts.
5. **Sensitive access is need-to-know.** Investigation assignment and explicit administrative authority control restricted working material.
6. **Public attribution is separable from internal provenance.** Internal accountability does not require public disclosure of a person's identity.
7. **Authorization is server-enforced and auditable.** UI hiding is never the security boundary.
8. **Destructive or authority-changing actions require stronger permission than ordinary editing.**

## Core entities

Names below are conceptual. Storage technology and exact field types are implementation decisions.

### User

Authentication identity.

Minimum fields:

- `id`
- `auth_subject` - stable identifier from the authentication provider
- `email` - private; verification state stored separately or alongside it
- `account_status` - invited, pending, active, suspended, disabled
- `created_at`, `updated_at`, `last_login_at`

A User is not automatically a coalition member.

Authentication secrets and password material should remain with the identity provider rather than the Coalition database where possible.

### Membership

Coalition relationship for a User.

Minimum fields:

- `id`
- `user_id`
- `membership_status` - applicant, approved, inactive, suspended, departed
- `joined_at`, `ended_at`
- `public_attribution_mode` - institutional by default; pseudonymous/individual only when deliberately supported
- `public_display_name` - nullable and never required to equal legal/authentication identity
- `internal_notes_classification` - if administrative notes are supported

Membership status does not itself grant research review or publication authority.

### RequesterIdentity

Identity-restricted contact/linkage record for a person who requests or initiates research without requiring that identity to be copied into investigation content.

Minimum fields:

- `id`
- `opaque_requester_ref` - stable internal reference suitable for use in investigation records
- `contact_fields` - minimum contact information actually required
- `verification/provenance_notes` - nullable and Identity-restricted
- `created_at`, `updated_at`
- `retention_class`, `retention_basis`
- `review_after`, `retain_until` - nullable
- `review_trigger` - nullable event-based retention review trigger
- `legal_or_preservation_hold`
- `disposition_status`, `disposed_at` - nullable

Requester identity is separate from Investigation. Ordinary collaborators use the opaque reference and do not receive the underlying identity by default.

### Jurisdiction

A legal/geographic scope.

Minimum fields:

- `id`
- `kind` - federal, circuit, state, district, local, or other approved type
- `code` - stable machine identifier
- `name`
- `parent_jurisdiction_id` - nullable
- `qualification_status` - Inactive, Field Guide Development, Active
- `facility_research_status` - nullable until Active; then Unresearched, Researching, or Established
- `qualification_changed_at`
- `qualification_changed_by`
- `facility_research_status_changed_at` - nullable
- `facility_research_status_changed_by` - nullable
- `is_publicly_listed`

All 50 states and the District of Columbia may exist before activation. Federal circuits are an applicable legal dimension and must not be modeled merely as state children.

Field Guide/division qualification is human-controlled; computed readiness may inform but never write `qualification_status` automatically. `facility_research_status` must remain null until qualification is Active. Activating a jurisdiction initializes facility research at Unresearched; later facility-research maturity does not alter qualification.

County and county-equivalent inventory records are **not** modeled as independently qualified child Jurisdictions merely to obtain geographic coverage. Use `CountyCoverageUnit` for the complete inherited county-level research inventory defined below. A future local jurisdiction that genuinely requires its own legal qualification model would need an explicit governance/schema decision rather than silently reusing county coverage.

### CountyCoverageUnit

Inherited county-level research coverage beneath an Active state.

Minimum fields:

- `id`
- `state_jurisdiction_id`
- `stable_geographic_code` - authoritative stable county/county-equivalent identifier where available
- `name`
- `unit_type` - county, county-equivalent, or approved extension
- `coverage_status` - Unresearched, Researching, Established
- `coverage_status_changed_at`
- `coverage_status_changed_by`
- `inventory_verified_at`
- `inventory_source_ref`
- `notes` - nullable
- `is_publicly_listed`

A CountyCoverageUnit inherits the national core, applicable federal/circuit layer, and parent state's Active overlay. It does not receive a separate `qualification_status`.

CountyCoverageUnit is a geographic/research index rather than a universal legal-parent relationship. Municipalities, special districts, state agencies, federal facilities, and other entities retain their actual governing authority even when geographically associated with a county unit. A resource may reference multiple CountyCoverageUnits when its geographic scope crosses county boundaries.

State activation creates or validates the complete CountyCoverageUnit inventory. New county records begin Unresearched unless reconciled existing work supports a later human-reviewed coverage status. County research stores only local dependencies and applications rather than duplicating national/state doctrine.

### Division

Operational organization attached to an activated or developing jurisdiction.

Minimum fields:

- `id`
- `jurisdiction_id`
- `operational_status`
- `created_at`
- `activated_at` - nullable

A Jurisdiction may exist without a Division. An Active Division requires the separate qualification workflow defined by the jurisdiction-lifecycle design.

### RoleDefinition

Controlled vocabulary describing a type of responsibility.

Initial role concepts:

- Member
- Contributor
- Researcher
- Reviewer
- Senior Reviewer
- Division Lead
- Administrator
- Founder

`Founder` is a project-origin governance role outside the points/merit ladder. It is not a numeric rank above Administrator and does not inherit every Administrator, Reviewer, or Division Lead permission. Its exceptional authorities are explicit founding/bootstrap actions defined by governance policy.

Minimum fields:

- `id`
- `code`
- `name`
- `description`
- `is_system_role`

Role names describe responsibility; permissions are defined by policy rather than inferred from numeric rank.

### RoleGrant

Assignment of a role to a Membership within a scope.

Minimum fields:

- `id`
- `membership_id`
- `role_definition_id`
- `scope_type` - global, jurisdiction, division, investigation, or other deliberately approved scope
- `scope_id` - nullable only for global scope
- `granted_by`
- `granted_at`
- `expires_at` - nullable
- `revoked_by`, `revoked_at` - nullable
- `reason` - auditable administrative rationale
- `grant_origin` - normal_promotion, scope_extension, bootstrap/founding, administrative, or approved extension

A promotion creates or changes RoleGrants only after human approval. Points cannot write RoleGrants.

### Contribution

Append-oriented ledger entry for accepted or otherwise recognized substantive work.

Minimum fields:

- `id`
- `membership_id`
- `jurisdiction_id` - nullable only for truly project-wide work
- `contribution_class` - verification, standard research, substantive research, major integrated research, review, or approved extension
- `credit_rule_code` - stable rule identifier for the applicable credit tier
- `credit_policy_version`
- `credit_points`
- `source_entity_type`, `source_entity_id` - the submission/review/etc. that generated the credit
- `source_revision_id` - nullable where the source has no immutable revision
- `credit_scope_basis` - direct jurisdiction, applicable national core, applicable circuit/federal layer, or project-wide methodology
- `credit_applicability_refs` - explicit national/circuit/jurisdiction/methodology applicability references used for target-scope eligibility
- `status` - pending, accepted, reversed
- `recommended_by` - nullable
- `awarded_by`
- `awarded_at`
- `reversal_of_id` - nullable
- `reason`
- `created_at`

Contribution history is a ledger. Point changes are represented by reversal/replacement records rather than silently rewriting history. Accepted work later becoming obsolete does not by itself reverse credit. Detailed credit classes, anti-gaming controls, and promotion use are defined in [Contribution Credit and Promotion Workflow](CONTRIBUTION_PROMOTION_WORKFLOW.md).

### PromotionRequest

Request for additional scoped responsibility.

Minimum fields:

- `id`
- `membership_id`
- `requested_role_definition_id`
- `requested_scope_type`, `requested_scope_id`
- `request_kind` - normal_promotion or scope_extension
- `eligibility_snapshot` - frozen contribution/breadth/current-role facts at request time
- `eligibility_policy_version`
- `status` - submitted, under_review, approved, deferred, declined, withdrawn
- `requested_at`
- `recommended_by` - nullable until the required recommendation exists
- `recommended_at` - nullable
- `decided_by`, `decided_at` - nullable
- `decision_reason` - nullable

Eligibility permits a normal promotion or scope-extension request to enter human assessment; approval is a separate Administrator decision under the initial governance model and may create a scoped RoleGrant.

### PromotionAssessment

Structured internal assessment supporting a PromotionRequest.

Minimum fields:

- `id`
- `promotion_request_id`
- `assessor_membership_id`
- `assessment_type` - eligibility verification, research competency, review calibration, scope knowledge, privacy/reliability, leadership, overall recommendation, or approved extension
- `result` - pass, needs_work, recommend, defer, oppose, abstain
- `evidence_refs`
- `comments`
- `created_at`
- `superseded_by_assessment_id` - nullable

PromotionAssessment records are internal governance material. Calibration assessments do not create formal Review decisions or review points. Detailed promotion criteria and routing are defined in [Contribution Credit and Promotion Workflow](CONTRIBUTION_PROMOTION_WORKFLOW.md).

### ResearchSubmission

Structured proposal entering the research pipeline.

Minimum fields:

- `id`
- `submitted_by_membership_id`
- `jurisdiction_id`
- `submission_type` - legal authority, jurisdiction-overlay branch, facility research, records result, correction, investigation evidence, or approved extension
- `title`
- `status` - draft, submitted, validation_failed, in_review, changes_requested, approved, rejected, withdrawn, superseded
- `current_revision_id` - nullable until a submitted revision exists
- `approved_revision_id` - nullable until a specific revision is approved
- `supersedes_submission_id` - nullable
- `visibility_classification`
- `created_at`, `updated_at`

The ResearchSubmission is the workflow container. Schema-versioned substantive content lives in ResearchSubmissionRevision. Mutable draft storage is an implementation detail and is not a reviewed artifact until an immutable revision is created.

Approval makes the exact `approved_revision_id` eligible for later publication processing; it does not itself make the submission authoritative published content.

Detailed submission requirements, revision semantics, review routing, and publication-candidate boundaries are defined in [Structured Research Submission and Review Workflow](RESEARCH_SUBMISSION_WORKFLOW.md).

### ResearchSubmissionRevision

Immutable reviewed version of a ResearchSubmission.

Minimum fields:

- `id`
- `research_submission_id`
- `revision_number`
- `schema_version`
- `canonical_branch_refs` - zero or more immutable `{branch_id, branch_version}` references where applicable
- `structured_payload`
- `visibility_classification`
- `created_by_membership_id`
- `created_at`, `submitted_at`
- `content_hash` or equivalent integrity reference where practical
- `supersedes_revision_id` - nullable

Review decisions attach to the exact immutable revision reviewed. A substantive edit produces a new revision and invalidates any review approvals affected by that change.

### Review

A review action on a ResearchSubmission or other reviewable entity.

Minimum fields:

- `id`
- `reviewable_type`, `reviewable_id` - must identify the exact immutable review target, such as a ResearchSubmissionRevision or PublicationCandidateRevision
- `reviewer_membership_id`
- `review_stage` - research, source verification, doctrinal/evidentiary, privacy, final publication, or approved extension
- `governing_policy_version` - nullable generally; required for privacy/publication-safety review (for example `PRIVACY_V1`)
- `decision` - approve, request_changes, reject, abstain
- `comments`
- `created_at`
- `superseded_by_review_id` - nullable

Required stages, routing, independence, recusal, and elevated-impact rules are defined in [Structured Research Submission and Review Workflow](RESEARCH_SUBMISSION_WORKFLOW.md). The data model must not assume that one review is universally sufficient.

### PublicationCandidate

Workflow container for a derived artifact proposed for public/authoritative publication after one or more research revisions have been approved.

Minimum fields:

- `id`
- `target_type`
- `target_identifier`
- `status` - prepared, in_final_review, approved_for_export, changes_requested, rejected, superseded, exported
- `current_revision_id`
- `approved_revision_id` - nullable
- `supersedes_publication_candidate_id` - nullable
- `prepared_by`, `prepared_at`

A PublicationCandidate is separate from the internal submission so privacy sanitization, synthesis, formatting, and dependency resolution do not mutate the accepted research record. Exact supporting-revision provenance belongs to each immutable PublicationCandidateRevision. A pre-export candidate remains non-Public while under review even when its payload is drafted for eventual public release.

### PublicationCandidateRevision

Immutable version of the derived publication artifact.

Minimum fields:

- `id`
- `publication_candidate_id`
- `revision_number`
- `source_submission_revision_ids` - exact immutable research revisions supporting this publication revision
- `derived_public_payload`
- `visibility_classification`
- `dependency_refs` - canonical/jurisdiction/facility/publication dependencies affected by this exact revision
- `content_hash` or equivalent integrity reference where practical
- `created_by`, `created_at`
- `supersedes_revision_id` - nullable

Final-publication review attaches to the exact PublicationCandidateRevision reviewed. Substantive changes create a new revision and require new final-publication approval.

### Investigation

Restricted working container for facility/incident investigative work.

Minimum fields:

- `id`
- `jurisdiction_id`
- `facility_id` - nullable where not facility-specific
- `requester_refs` - zero or more opaque RequesterIdentity references; never embeds requester contact data
- `title`
- `status`
- `visibility_classification`
- `created_by_membership_id`
- `created_at`, `closed_at`
- `publication_summary_id` - nullable

Private investigation content is not made accessible merely by holding a research role in the same state.

### InvestigationAssignment

Need-to-know access grant.

Minimum fields:

- `id`
- `investigation_id`
- `membership_id`
- `assignment_role` - contributor, researcher, reviewer, lead, or approved extension
- `granted_by`, `granted_at`
- `revoked_by`, `revoked_at` - nullable

### SensitiveAccessGrant

Purpose-limited authorization for Restricted, Identity-restricted, or Administrative material not adequately covered by ordinary InvestigationAssignment.

Minimum fields:

- `id`
- `membership_id`
- `resource_type`, `resource_id`
- `access_level`
- `purpose_code`
- `reason`
- `granted_by`, `granted_at`
- `expires_at` - nullable
- `revoked_by`, `revoked_at` - nullable

SensitiveAccessGrant does not create substantive research/review authority.

### SanitizationRecord

Audit/provenance record describing privacy transformations applied to an immutable PublicationCandidateRevision.

Minimum fields:

- `id`
- `publication_candidate_revision_id`
- `source_refs`
- `transformation_types` - redact, blur, crop, omit, paraphrase, metadata_strip, replace_with_public_source, or approved extension
- `visibility_classification` - Administrative or Restricted
- `privacy_policy_version`
- `reason`
- `performed_by`, `performed_at`
- `verified_by`, `verified_at` - nullable
- `notes`

Sanitization records explain the transformation without requiring the removed content itself to become public.

### RetentionControl

Lifecycle metadata for a sensitive object when retention cannot be represented directly on the source entity.

Minimum fields:

- `id`
- `resource_type`, `resource_id`
- `retention_class`
- `retention_basis`
- `review_after` - nullable
- `review_trigger` - nullable event-based retention review trigger
- `retain_until` - nullable
- `legal_or_preservation_hold`
- `hold_reason` - nullable
- `disposition_status`
- `disposed_at`, `disposition_actor` - nullable

Detailed privacy, access, sanitization, and retention rules are defined in [Privacy, Identity, Attribution, and Retention Workflow](PRIVACY_ATTRIBUTION_RETENTION.md).

### PublicationEvent

Immutable record of a publication transition or attempted transition.

Minimum fields:

- `id`
- `source_type`, `source_id`
- `publication_target`
- `action` - prepared, approved_for_export, export_requested, export_validation_failed, issue_created, branch_created, draft_pr_created, export_failed, diverged, reconciled, merged, published, withdrawn, corrected
- `performed_by` - human membership or service principal
- `external_reference` - nullable GitHub/public artifact reference
- `created_at`
- `metadata`

PublicationEvents record what happened; they do not themselves authorize the next action.

### RepositoryExport

Operational mapping from one exact approved PublicationCandidateRevision to one controlled external repository-preparation attempt.

Minimum fields:

- `id`
- `publication_candidate_revision_id`
- `approved_content_hash`
- `export_mode` - ISSUE, BRANCH_DRAFT_PR, or approved extension
- `target_repository`
- `target_base_ref`
- `target_path_allowlist`
- `requested_by_membership_id`
- `service_principal_id`
- `status`
- `request_correlation_id`
- `base_sha_at_start` - nullable
- `branch_ref` - nullable
- `head_sha` - nullable
- `issue_number` - nullable
- `pull_request_number` - nullable
- `external_url` - nullable
- `attempt_count`
- `last_error_code` - nullable
- `created_at`, `updated_at`, `completed_at` - completed_at nullable

RepositoryExport is operational state, not substantive authority. It must remain tied to the exact approved revision/hash and follows the controls in [Controlled GitHub Publication Integration](GITHUB_PUBLICATION_INTEGRATION.md).

### ServicePrincipal

Non-human system identity, including future GitHub integration.

Minimum fields:

- `id`
- `name`
- `purpose`
- `status`
- `credential_reference` - reference to secret storage, never the secret itself
- `allowed_capabilities`

Service principals receive only the capabilities required for their function and cannot inherit member roles.

### AuditEvent

Append-oriented security/governance audit record.

Minimum fields:

- `id`
- `actor_type`, `actor_id`
- `action`
- `target_type`, `target_id`
- `occurred_at`
- `request/correlation_id`
- `result`
- `reason_or_metadata`

At minimum, audit role grants/revocations, promotion decisions, contribution awards/reversals, investigation access changes, lifecycle changes, review decisions, privacy-sensitive reads where practical, and publication/GitHub actions.

Audit logs are administrative records and must not become a second public activity feed.

## Relationship summary

```text
User 1---0..1 Membership
Membership 1---* RoleGrant *---1 RoleDefinition
RoleGrant *---scope---> Jurisdiction / Division / Investigation / Global

Jurisdiction 1---0..1 Division
State Jurisdiction 1---* CountyCoverageUnit
Jurisdiction 1---* ResearchSubmission
Jurisdiction 1---* Investigation

Membership 1---* Contribution
Membership 1---* PromotionRequest
PromotionRequest 1---0..* PromotionAssessment
Membership 1---* ResearchSubmission
Membership 1---* Review

Investigation 1---* InvestigationAssignment *---1 Membership
Membership 1---0..* SensitiveAccessGrant
RequesterIdentity 0..*---0..* Investigation (via opaque requester refs)
PublicationCandidateRevision 1---0..* SanitizationRecord
RetentionControl *---1 sensitive resource

ResearchSubmission 1---0..* ResearchSubmissionRevision
ResearchSubmissionRevision 1---0..* Review
ResearchSubmissionRevision 0..*---0..* PublicationCandidateRevision
PublicationCandidate 1---1..* PublicationCandidateRevision
PublicationCandidateRevision 1---0..* Review
PublicationCandidate 1---0..* PublicationEvent
PublicationCandidateRevision 1---0..* RepositoryExport
RepositoryExport *---1 ServicePrincipal

ServicePrincipal 1---* AuditEvent
Membership 1---* AuditEvent
```

Facility, source, evidence, records-request, and publication-content entities already implied by the Field Guide methodology should be related to these entities rather than collapsed into Membership or Investigation. Their detailed schemas belong to the structured-research issue.

## Authorization model

Every protected operation evaluates:

`authenticated identity + active membership + active role grants + scope + resource classification + assignment + action`

A higher-sounding role does not automatically bypass resource classification or scope.

### Baseline permission matrix

Legend: **R** read, **C** create, **E** edit, **V** substantive review/decision, **A** administer/authority-changing. All permissions are limited to the role's granted scope unless explicitly marked global.

| Capability | Member | Contributor | Researcher | Reviewer | Senior Reviewer | Division Lead | Administrator |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Read public Field Guide/registry | R | R | R | R | R | R | R |
| Read own private profile/contribution history | R | R | R | R | R | R | R |
| Edit own non-authority profile fields | E | E | E | E | E | E | E |
| Create research submission | C | C | C | C | C | C | C |
| Edit own draft / changes-requested submission | E | E | E | E | E | E | E |
| Read nonrestricted submissions in scope | - | R | R | R | R | R | R |
| Perform substantive research work in scope | - | C/E | C/E | C/E | C/E | C/E | C/E |
| Submit review decision | - | - | - | V | V | V | - |
| Perform senior/final delegated review | - | - | - | - | V | V | - |
| Perform privacy/publication-safety review | - | - | - | - | V/authorized access | V/authorized access | - |
| Recommend contribution credit | - | - | - | V | V | V | - |
| Award/reverse contribution credit | - | - | - | - | V | V | A |
| Request own promotion | C | C | C | C | C | C | C |
| Recommend promotion | - | - | - | V | V | V | - |
| Decide promotion / create resulting RoleGrant | - | - | - | - | - | - | A |
| Recommend Field Guide qualification change | - | - | - | V | V | V | V |
| Change Field Guide qualification | - | - | - | - | - | - | A |
| Update facility-research maturity after activation | - | - | - | - | V | V | A |
| Manage scoped division assignments | - | - | - | - | - | A | A |
| Access restricted investigation | assigned only | assigned only | assigned only | assigned only | assigned only | assigned/need-to-know | A/need-to-know |
| Manage investigation assignments | - | - | - | - | - | scoped A | A |
| Approve publication candidate | - | - | - | - | V | V | - |
| Trigger controlled GitHub preparation | - | - | - | - | - | only if separately delegated | A |
| Merge/publish to authoritative repository | - | - | - | - | - | - | separate repository authority |
| Manage global roles/security policy | - | - | - | - | - | - | A |

This matrix is a ceiling for initial implementation, not a mandate to expose every listed capability immediately.

**Founder is intentionally not represented as a broad superuser column in this baseline matrix.** Founder is an additive governance role whose ordinary research, review, administrative, sensitive-access, and repository capabilities come from the member's other active grants or external repository authority. The Founder role itself authorizes only explicitly defined founding/bootstrap actions, including:

- establishing the first Administrator and issuing auditable bootstrap/founding RoleGrants needed to initialize governance;
- making a Founder/bootstrap jurisdiction-activation decision when the independent-review path is unavailable and every requirement in `JURISDICTION_QUALIFICATION.md` is satisfied; and
- recording those actions as founding/bootstrap governance events.

Founder does not by itself authorize substantive review decisions, unrestricted Restricted/Identity-restricted access, contribution-credit self-awards, ordinary self-promotion, or repository merge access.

### Important permission rules

#### Self-service does not imply self-approval

A person cannot satisfy a required independent review of their own submission. The workflow design may require multiple reviewers for particular material.

The Founder/bootstrap jurisdiction-activation exception does not convert self-review into independent review. It expressly records that the independent-review requirement could not be met because no qualified independent human was reasonably available, and it applies only through the documented qualification exception.

#### Scope does not automatically cascade everywhere

A state-scoped role may apply to ordinary research in that state but does not automatically reveal restricted investigations, private identities, administrative notes, or secrets.

Circuit/federal authority may intersect multiple states. Authorization must evaluate the resource's explicit jurisdictional scopes rather than pretending circuit authority belongs to one state.

#### Division Lead is not Administrator

A Division Lead can manage delegated operations within their division but cannot:

- activate their own jurisdiction;
- alter national standards;
- grant global roles;
- change global security/privacy policy;
- access unrelated restricted investigations;
- obtain repository credentials by virtue of the role.

#### Administrator is not automatic publication authorship

Administrative access exists to operate the platform. It does not convert administrative action into substantive legal review or eliminate required independent review stages. An Administrator who also performs substantive review must hold a separate active Reviewer, Senior Reviewer, or Division Lead grant in the applicable scope; the Administrator role alone cannot submit or satisfy substantive review/publication approval.

Administrator status is also not blanket permission to read Restricted or Identity-restricted content. Sensitive access still requires an operational purpose, applicable assignment or SensitiveAccessGrant, and required auditing.

#### Repository authority remains external

The Coalition authorization model records who may prepare or approve a publication candidate. Actual GitHub merge authority is separately controlled by repository credentials/settings. Initially, coalition members receive none merely from their Coalition role.

## Data classifications

Initial classifications:

- **Public** - intentionally published material.
- **Coalition** - authenticated-member material safe for ordinary internal collaboration.
- **Restricted** - investigation working material, unpublished sensitive evidence, or scoped internal research.
- **Identity-restricted** - requester/member contact or identity-bearing records not needed for ordinary research.
- **Administrative** - membership decisions, internal notes, security/audit records, role administration.
- **Secret** - credentials, tokens, signing material; stored outside ordinary application records wherever possible.

Authorization checks use both role/scope and classification. Export/publication code must default-deny non-Public fields. Classification meanings, requester isolation, material-private-participant handling, sensitive-access rules, and retention lifecycle are defined in [Privacy, Identity, Attribution, and Retention Workflow](PRIVACY_ATTRIBUTION_RETENTION.md).

## Public identity separation

The platform should expose a public attribution object rather than directly rendering User or Membership identity.

A publication can therefore be attributed to, for example:

- `California Division`;
- `1A Field Guide Coalition`;
- a deliberately chosen public pseudonym/display name where later policy permits.

Internal records still retain submitter and reviewer provenance. Changing public attribution does not rewrite internal history.

## Required invariants for implementation

Database constraints and service-layer authorization should enforce, where technically practical:

- points cannot create/update RoleGrants;
- contribution awards/reversals cannot be self-awarded;
- contribution points must match the recorded credit-rule code and credit-policy version;
- normal promotion/scope-extension eligibility uses a frozen policy-versioned snapshot;
- target-scope points use recorded credit applicability rather than ad hoc promotion-time reclassification;
- Division Lead recommendation cannot create the resulting RoleGrant;
- final normal promotion approval is Administrator-only under the initial model;
- the candidate cannot make their own final promotion decision;
- Administrator status alone does not satisfy substantive contribution-credit or promotion recommendation requirements;
- only an authorized human decision can approve a PromotionRequest;
- readiness metrics cannot directly write `qualification_status`;
- normal jurisdiction activation preserves the independent qualified-human review requirement;
- a Founder/bootstrap activation may bypass only that independent-review requirement, must preserve all other qualification requirements, must be explicitly marked `founding/bootstrap`, and must generate an AuditEvent;
- AI/automation/service principals cannot satisfy the independent-human-review requirement or create a Founder/bootstrap activation decision;
- later availability of an independent reviewer does not automatically deactivate a bootstrap-activated jurisdiction, but should queue retrospective review;
- `facility_research_status` remains null until `qualification_status` is Active;
- state activation creates or validates the complete CountyCoverageUnit inventory;
- CountyCoverageUnit records do not carry independent Field Guide qualification status and begin Unresearched unless reconciled prior work supports a later human-reviewed coverage status;
- activation initializes facility research at Unresearched; facility activity cannot itself qualify or activate a jurisdiction;
- a submission status change to approved does not create a public artifact by itself;
- reviewable_type/reviewable_id reference the exact immutable revision being reviewed;
- substantive revision changes invalidate affected review approvals;
- each PublicationCandidateRevision retains exact provenance to its supporting ResearchSubmissionRevisions;
- final-publication approvals reference immutable PublicationCandidateRevisions;
- restricted/identity-restricted records require explicit purpose-limited authorization beyond ordinary membership/role status;
- requester identity remains separate from Investigation and is referenced through zero or more opaque requester references;
- opaque requester references remain internal and are not public attribution identifiers;
- sensitive-access grants do not create substantive review/publication authority;
- privacy-sensitive public release occurs only through a derived immutable PublicationCandidateRevision;
- required privacy review applies to that exact PublicationCandidateRevision, records the governing privacy-policy version, and is performed independently from the final preparer/sanitizer by an authorized Senior Reviewer or Division Lead with necessary sensitive access under the initial model;
- sensitive publication transforms retain SanitizationRecord provenance and privacy-policy version;
- privacy-sensitive SanitizationRecords require independent verification before export;
- incidental private persons are minimized by default while material private participants may be published for documented evidentiary relevance rather than retaliation;
- unrelated sensitive personal information remains excluded even when a material participant is identified;
- minors receive heightened minimization;
- sensitive-read/bulk-export/break-glass access generates Administrative AuditEvents where required;
- research retention does not require indefinite retention of requester/member contact information;
- sensitive records require a documented long-lived retention class or a retention review date/event trigger rather than an undocumented keep-forever default;
- active preservation/legal holds prevent ordinary disposition;
- role grants cannot exceed the grantor's delegated authority;
- revoked/expired grants stop authorizing new actions;
- publication exports exclude non-Public data unless an explicit sanitization/review step permits a derived public field;
- service credentials are never stored in contribution/submission/publication payloads;
- material authority-changing actions generate AuditEvents.

## Decisions intentionally deferred

Issue #39 does **not** decide:

- contribution credit values, promotion eligibility floors, calibration, and promotion routing are defined by #41 in `docs/CONTRIBUTION_PROMOTION_WORKFLOW.md`;
- exact Field Guide qualification criteria, activation review procedure, and facility-research maturity thresholds (#40);
- detailed structured submission/review rules are defined by #42 in `docs/RESEARCH_SUBMISSION_WORKFLOW.md`;
- detailed privacy, attribution, sensitive-access, and lifecycle retention rules are defined by #43 in `docs/PRIVACY_ATTRIBUTION_RETENTION.md`;
- UI design for the nationwide shell (#44);
- controlled GitHub export mechanics are defined by #45 in `docs/GITHUB_PUBLICATION_INTEGRATION.md`; future credential/provider implementation choices remain implementation details;
- whether future governance delegates final repository merge authority beyond the current operator.

Those decisions must not be inferred from this schema.
