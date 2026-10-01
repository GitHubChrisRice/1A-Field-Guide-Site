# Controlled GitHub Publication Integration

Issue: #45

This document defines the initial GitHub export boundary for the 1A Field Guide Coalition. It turns an approved, immutable `PublicationCandidateRevision` into a controlled repository-preparation action without giving ordinary Coalition members repository access and without allowing the integration itself to make the final publication/merge decision.

`GitHubChrisRice/1A-Field-Guide-Site` is the intended authoritative **public source repository** after the repository split defined in [Public/Private Repository Split](PUBLIC_PRIVATE_REPOSITORY_SPLIT.md). Its protected `main` branch holds reviewed public source; generated site output is published separately from that source branch. The private `GitHubChrisRice/1A-Field-Guide` repository remains the internal research/workspace repository.

Coalition approval authorizes **preparation for public-source repository review**; it does not authorize a merge.

## Governing principles

1. **Coalition approval and repository authority remain separate.**
2. **The integration identity is a service principal, not a Coalition member or reviewer.**
3. **The integration receives only an already-approved public derivative, never broad access to Restricted or Identity-restricted working material.**
4. **GitHub metadata is treated as potentially public even when the source repository is private.**
5. **Every export is tied to one exact immutable `PublicationCandidateRevision` and its approved content hash.**
6. **The service principal never supplies substantive, privacy, final-publication, qualification, or promotion approval.**
7. **Repository merge remains a separate human-controlled act.**
8. **A failed or partial GitHub operation never changes the underlying research approval.**
9. **Manual changes after export create a new review question; they do not silently inherit the candidate's prior approval.**
10. **No shared human credential, general-purpose personal access token, or public-site deployment credential is reused for Coalition export.**

## Boundary in the publication pipeline

```text
Approved research revision(s)
        |
Derived immutable PublicationCandidateRevision
        |
Required privacy/publication-safety review
        |
Final publication approval
        |
PublicationCandidate = approved_for_export
        |
Human-authorized export request
        |
Controlled GitHub preparation
        |
Draft repository artifact
        |
Human repository review
        |
Human merge decision
        |
Authoritative source merge
        |
Separate site/publication deployment
```

Each arrow is a distinct transition. In particular:

- `approved_for_export` does not create a GitHub artifact;
- GitHub preparation does not make a pull request ready for merge;
- a passing CI build does not supply substantive approval;
- a repository merge is not the same event as successful public-site deployment; and
- a site deployment does not retroactively validate an unapproved repository change.

## Export preconditions

The backend may create a GitHub export request only when all of the following are true for the exact current `PublicationCandidateRevision`:

- the candidate status is `approved_for_export`;
- `approved_revision_id` equals the revision being exported;
- the immutable revision content hash still matches the approved hash;
- all required final-publication review stages are satisfied;
- privacy/publication-safety review is satisfied when required by `PRIVACY_V1`;
- any required `SanitizationRecord` has been independently verified;
- the candidate has not been withdrawn, rejected, or superseded;
- unresolved dependency/correction flags that block publication have been cleared;
- the target repository, base branch, and target paths are allowlisted;
- all GitHub-visible title/body/branch/filename metadata has passed the same public-safety checks as the payload;
- the requesting human has authority to trigger controlled GitHub preparation under the Coalition permission model; and
- an idempotent export for the same candidate revision is not already active or completed.

An export job rechecks these conditions at execution time. Authorization at request time alone is not sufficient if state changes before execution.

## Human authorization to trigger export

The initial permission model remains:

- Administrator: may trigger controlled GitHub preparation;
- Division Lead: only when separately delegated that capability for the applicable scope;
- Founder: no inherent export permission merely from Founder status;
- Senior Reviewer/Reviewer/Researcher/Contributor/Member: no export-trigger permission merely from those roles.

The trigger decision is operational. It does not replace the substantive reviewers who approved the exact `PublicationCandidateRevision`.

The requesting human and the service principal are separately recorded:

```text
requested_by_membership_id -> human authorization
service_principal_id       -> non-human GitHub execution identity
```

## Service identity and credentials

### Preferred identity

Use a dedicated GitHub App or equivalently isolated GitHub integration identity created only for Coalition export.

Do not use:

- the Founder's personal GitHub credential;
- another maintainer's personal token;
- a broad classic PAT;
- the credential used to publish the generated public site;
- a credential shared with unrelated automation; or
- a credential stored in a Coalition research record.

The Coalition database stores only a `credential_reference` pointing to secret storage.

### Installation scope

The integration should be installed on the minimum repository set needed for its current phase. A future expansion to additional authoritative repositories requires a new explicit repository allowlist entry and audit event.

### Credential lifetime

Prefer short-lived installation/access tokens minted from the integration identity. Long-lived private keys or app secrets remain in secret storage and are never copied into job payloads, logs, publication candidates, or audit summaries.

### Service-principal capabilities

The Coalition-side `ServicePrincipal.allowed_capabilities` must independently restrict what the backend is permitted to request from GitHub. GitHub repository permissions are a second ceiling, not a substitute for Coalition-side allowlisting.

The export worker must not expose a generic "call GitHub API" capability. It exposes named operations such as:

- create approved issue;
- create export branch from approved base SHA;
- write approved files to export branch;
- open draft pull request;
- read export branch/PR state for reconciliation.

There is no `merge pull request`, `update default branch`, `delete repository`, `manage secrets`, `manage workflows`, or `change repository settings` operation in the export worker.

## Two deployment phases

### Phase 1 — issue-only preparation

Phase 1 is the safe default when the authoritative default branch cannot be technically protected from the integration identity.

GitHub permissions should be limited to the smallest set needed to create/read approved issues. The integration receives **no Contents write permission** and therefore cannot create or update repository branches or files.

Issue export is appropriate for:

- an approved implementation task;
- an approved research follow-up;
- a correction task that still requires repository work;
- a human-readable publication-preparation ticket; or
- another explicitly approved public-safe tracking artifact.

Issue export is not a way to dump internal research into GitHub. The issue title, body, labels, filenames, links, and attachments must themselves be safe for the GitHub boundary.

### Phase 2 — branch + draft pull request preparation

Phase 2 may be enabled only after the authoritative repository has a technically enforceable default-branch protection that prevents the integration identity from directly updating or merging the authoritative branch.

The intended GitHub repository permission set is narrowly bounded to the functions needed to:

- read repository metadata/content;
- create/update the integration's export branches;
- create/update draft pull requests; and
- optionally create issues if Phase 1 remains supported.

The integration must not receive repository administration, Actions administration, secrets, environments, deployments, organization administration, or equivalent unrelated permissions.

Because GitHub's contents permission is repository-wide rather than a branch-specific application permission, **default-branch protection is part of the security boundary** for Phase 2. Application code that merely promises not to push to `main` is not enough.

### Current repository architecture prerequisite

The project has chosen a public/private repository split rather than paying to make the private research repository the authoritative publication target.

The intended steady state is:

- `GitHubChrisRice/1A-Field-Guide` — **private internal workspace** for investigations, unpublished/raw evidence, requester or member-sensitive material, internal Coalition operations, and pre-publication work;
- `GitHubChrisRice/1A-Field-Guide-Site` `main` — **public authoritative source** containing only deliberately publishable Field Guide source, public Registry material, public methodology, licensing/origin notices, and build configuration;
- `GitHubChrisRice/1A-Field-Guide-Site` `gh-pages` — **generated website output** served by GitHub Pages.

Because the authoritative source repository is public, GitHub Free can provide the branch/ruleset protection needed for Phase 2. The blocker is therefore configuration/migration, not a paid-plan requirement.

At the time of this design, `1A-Field-Guide-Site/main` still contains generated site output and the current integration connection cannot create refs in that repository. Phase 2 must remain disabled until a human repository operator has:

1. preserved the current generated site on a deployment branch such as `gh-pages`;
2. configured GitHub Pages to serve that deployment branch/workflow;
3. migrated reviewed public source to `main`;
4. configured branch protection/rulesets on `main` that exclude the export integration from direct update/merge bypass; and
5. verified the live site and repository checks after the migration.

Until those prerequisites are complete, issue-only preparation remains the production-safe automated mode.

## Default-branch protection requirements for Phase 2

Before enabling branch/PR export, the repository operator should verify protections equivalent to:

- authoritative branch updates occur through pull requests;
- the export integration is **not** a bypass actor for that branch;
- the export integration cannot directly push to the authoritative branch;
- required build/validation checks must pass before merge where supported;
- force pushes to the authoritative branch are blocked;
- deletion of the authoritative branch is blocked; and
- the final merge remains available only to separately authorized human repository operators.

If repository administrators can bypass the protections, that is repository-governance authority, not Coalition-role authority, and should remain limited to the small human operator set.

## RepositoryExport record

A durable export record links Coalition approval to the external repository artifact.

Conceptual fields:

- `id`;
- `publication_candidate_revision_id`;
- `approved_content_hash`;
- `export_mode` - `ISSUE`, `BRANCH_DRAFT_PR`, or approved extension;
- `target_repository`;
- `target_base_ref`;
- `target_path_allowlist`;
- `requested_by_membership_id`;
- `service_principal_id`;
- `status`;
- `request_correlation_id`;
- `base_sha_at_start` - nullable for issue-only export;
- `branch_ref` - nullable;
- `head_sha` - nullable;
- `issue_number` - nullable;
- `pull_request_number` - nullable;
- `external_url` - nullable;
- `attempt_count`;
- `last_error_code` - nullable;
- `created_at`, `updated_at`;
- `completed_at` - nullable.

Initial statuses:

- `REQUESTED`;
- `VALIDATING`;
- `PREPARING`;
- `ISSUE_CREATED`;
- `BRANCH_CREATED`;
- `DRAFT_PR_CREATED`;
- `WAITING_HUMAN_REPOSITORY_DECISION`;
- `DIVERGED`;
- `FAILED_RETRYABLE`;
- `FAILED_FINAL`;
- `MERGED`;
- `PUBLISHED`;
- `WITHDRAWN`;
- `SUPERSEDED`.

A `RepositoryExport` is an operational/audit mapping. It does not become the source of substantive truth.

`PublicationCandidate.status = exported` means only that the exact approved revision has been successfully emitted to a controlled external preparation artifact and its external reference has been recorded. It does **not** mean the repository change was merged or that the public artifact was published. `RepositoryExport` and `PublicationEvent` carry those later `MERGED` and `PUBLISHED` transitions.

## Idempotency

The uniqueness key for normal export is:

```text
(target_repository,
 publication_candidate_revision_id,
 approved_content_hash,
 export_mode)
```

Retrying a network failure must not create duplicate issues, branches, or pull requests when the prior operation may actually have succeeded.

The worker should:

1. look for an existing active/completed `RepositoryExport`;
2. reconcile any recorded external reference with GitHub;
3. create only the missing transition;
4. record the resulting external identifier immediately; and
5. use a correlation/idempotency token in safe metadata where the GitHub operation supports it.

A new substantive PublicationCandidateRevision creates a new export identity rather than overwriting the old approved revision.

## Public-safe naming conventions

GitHub branch names, issue titles, pull-request titles, commit messages, labels, and filenames must not contain:

- requester names or contact information;
- member email/login identity unless independently selected for public attribution;
- investigation-only identifiers that reveal sensitive associations;
- private-person names unless the exact publication candidate deliberately approves that identification;
- raw records-request tracking strings when they expose personal information;
- secret/token fragments; or
- arbitrary unsanitized user-entered text.

Recommended branch pattern:

```text
coalition/export/pc-<opaque-public-safe-id>-r<revision>
```

Recommended automated commit message:

```text
Prepare publication candidate <public-safe-id> revision <n>
```

The opaque ID must itself be safe to expose.

## Export payload generation

The export worker receives only the exact approved derived payload and the minimum public-safe metadata required for the requested operation.

It should not query or receive:

- `RequesterIdentity`;
- member authentication profiles;
- unrelated investigation records;
- raw Restricted attachments;
- sensitive-access audit logs; or
- secret storage.

When repository content must be generated from structured candidate data, prefer deterministic rendering so the output can be reproduced and compared against the approved candidate hash.

## Branch + draft PR workflow

For Phase 2:

1. Revalidate the exact candidate revision and trigger authority.
2. Read and record the current authoritative base SHA.
3. Create a new export branch from that SHA using the safe branch convention.
4. Write only allowlisted paths represented by the approved candidate.
5. Record every created commit SHA.
6. Re-read the branch and verify that the resulting content matches the expected approved export.
7. Open a **draft** pull request.
8. Record the PR number/URL and move the export to `WAITING_HUMAN_REPOSITORY_DECISION`.
9. Allow normal repository CI/validation to run.
10. Do not mark the PR ready, approve it, enable auto-merge, or merge it from the export service.

The PR body should include only public-safe/export-safe information, such as:

- the publication target;
- the candidate public-safe ID/revision;
- a concise sanitized change summary;
- the fact that Coalition publication review is complete for the exported revision;
- the approved content hash or shortened integrity reference where useful;
- the paths changed; and
- a statement that repository merge remains a separate human decision.

Do not copy private review comments, member identities, requester information, or sensitive evidence provenance into the PR body.

## Issue-only workflow

For Phase 1 or an approved issue-export target:

1. Revalidate candidate/export approval.
2. Render an issue title/body from an approved public-safe template.
3. Check the rendered metadata for privacy/secret leakage.
4. Search the recorded export mapping for an existing issue.
5. Create the issue.
6. Record the issue reference immediately.
7. Mark the export `ISSUE_CREATED` or the applicable waiting state.
8. Do not convert issue creation into repository/publication approval.

A human repository operator may later implement the issue through the normal repository workflow.

## GitHub-side human edits and divergence

The approved candidate authorizes an exact derived payload.

If a human or another automation changes the export branch after the service has verified it, the branch becomes **diverged** from the approved export unless the change is a deterministic rendering-only transformation that the system can prove does not change public meaning.

Divergence handling:

- record the unexpected head SHA and actor where available;
- mark the `RepositoryExport` `DIVERGED`;
- do not silently overwrite the human change;
- do not claim the prior final-publication approval covers the modified content;
- route the changed content back through PublicationCandidateRevision review when substantive;
- prefer a new approved revision/export over force-pushing history after review has begun.

A repository operator may still possess technical power to merge divergent content. If that occurs, the Coalition records the merge accurately as a repository event but marks the publication linkage nonconforming and opens a correction/reconciliation path. Audit history must reflect what actually happened rather than rewriting the prior approval.

## Base-branch movement and conflicts

A base branch changing after export does not automatically invalidate the candidate's substantive approval.

If GitHub can merge the unchanged approved payload cleanly, ordinary repository merge mechanics may proceed.

If conflict resolution or rebasing changes the public meaning/content:

- create a new PublicationCandidateRevision;
- repeat the affected final/privacy review;
- export the new revision.

Do not let a conflict-resolution edit inherit an old content hash.

## Webhooks and reconciliation

The integration should use signed GitHub webhooks, or a deliberately approved polling fallback, to reconcile external state.

Useful events include:

- issue created/closed;
- pull request opened/edited/closed/merged;
- branch/head updates;
- check/run status where used for operational visibility.

Webhook handling must:

- verify the GitHub webhook signature;
- be idempotent;
- map the event to an existing `RepositoryExport`;
- reject repository/installation IDs outside the allowlist;
- record the external actor separately from the Coalition service principal;
- never treat a GitHub review as a substitute for required Coalition substantive review; and
- never let an external event grant Coalition roles or permissions.

## Merge and publication states

Repository merge and public deployment are separate events.

### Merge

When the authoritative repository reports the PR merged:

- record the merge commit SHA;
- record the GitHub actor who performed the merge;
- add a `PublicationEvent(action=merged)`;
- mark the RepositoryExport `MERGED`;
- preserve the exact candidate revision/hash that was supposed to be merged; and
- verify divergence status before claiming a conforming publication linkage.

### Published

If a later deployment workflow publishes the merged source to a public site or artifact:

- record that as a distinct `PublicationEvent(action=published)`;
- record the deployment/public artifact reference where practical;
- mark the RepositoryExport `PUBLISHED` only after that publication transition is confirmed.

A failed deployment leaves the source merged but not yet confirmed published.

## Withdrawal and supersession

Before merge, a candidate may be withdrawn or superseded.

The integration may:

- close or annotate its own draft PR/issue where policy allows;
- mark the export `WITHDRAWN` or `SUPERSEDED`; and
- preserve the external artifact/audit history.

It must not delete history merely to make an obsolete export disappear.

After merge/publication, correction uses the normal correction/supersession workflow rather than rewriting the old PublicationEvent.

## Failure handling

Failures are classified at least as:

- authorization/state failure;
- privacy/sanitization failure;
- repository allowlist failure;
- credential/authentication failure;
- rate-limit/transient GitHub failure;
- branch/path conflict;
- external divergence;
- validation/CI failure;
- permanent GitHub policy/permission failure.

Retryable failures may be retried idempotently.

A failure never:

- changes the candidate's substantive approval;
- awards contribution credit;
- changes a role grant;
- makes the work public; or
- authorizes a broader credential.

## PublicationEvent extensions

The existing `PublicationEvent` remains the immutable event stream for publication transitions. Add or support actions sufficient to record attempted export accurately:

- `export_requested`;
- `export_validation_failed`;
- `issue_created`;
- `branch_created`;
- `draft_pr_created`;
- `export_failed`;
- `diverged`;
- `reconciled`;
- `merged`;
- `published`;
- `withdrawn`;
- `corrected`.

`PublicationEvent` records what happened. `RepositoryExport.status` records the current operational state.

## Audit requirements

At minimum record:

- human export request;
- exact PublicationCandidateRevision and approved hash;
- authorization decision;
- service principal used;
- target repository/base/path allowlist;
- export mode;
- external issue/branch/PR references;
- commit/base/head SHAs;
- each failed/retried operation;
- detected divergence;
- human GitHub merge actor;
- merge commit;
- public deployment confirmation where applicable;
- withdrawal/supersession; and
- credential/allowlist/configuration changes for the integration.

Do not place:

- credentials;
- raw webhook secrets;
- raw private candidate payloads;
- requester contact details; or
- unrelated sensitive evidence

inside general audit summaries.

## Security separation from site deployment

After the repository split, public source and generated output may live in the same public repository but on different branches with different authority boundaries.

The Coalition export integration targets only protected public-source `main`. The site deployment workflow builds from merged `main` and publishes generated output to `gh-pages` (or an equivalent Pages deployment target). The exporter must not receive deployment authority merely because both targets are in one repository.

```text
PRIVATE 1A-Field-Guide
approved PublicationCandidateRevision
        |
controlled export service principal
        |
PUBLIC 1A-Field-Guide-Site / protected main
        |
human merge
        |
build/deployment workflow
        |
gh-pages / GitHub Pages
```

Where separate credentials are used, they must remain separate. Where GitHub Actions can use an ephemeral workflow token for deployment, scope that token only to the deployment operation. Compromise or revocation of the export identity must not imply permission to alter deployed site output directly, and deployment authority must not grant access to private research records.

## Implementation sequence

### Stage A — data/control plane

Implement:

- `RepositoryExport`;
- expanded PublicationEvent actions;
- repository/base/path allowlists;
- export-trigger authorization;
- service-principal capability allowlist;
- idempotent export state machine;
- audit logging; and
- candidate/hash/privacy precondition checks.

No GitHub write credential is needed to test this stage.

### Stage B — issue-only GitHub integration

Create the dedicated GitHub integration with issue-only minimum permissions.

Implement:

- issue export template;
- privacy-safe metadata rendering;
- issue idempotency/reconciliation;
- signed webhook validation or approved polling;
- external reference/audit capture.

This is the first production-capable automated GitHub mode under the current repository constraints.

### Stage C — protected branch/draft-PR integration

Only after the repository operator verifies the authoritative branch protection prerequisite:

- grant the integration the additional minimum contents/PR permissions;
- enable branch + draft PR export;
- enforce branch prefix and path allowlists;
- verify output hashes;
- reconcile PR/head state;
- detect divergence;
- confirm that the integration cannot directly update/merge the authoritative branch.

### Stage D — deployment reconciliation

Optionally reconcile the existing site-build/publish workflow so a conforming source merge can later be marked `published` after successful public deployment.

## Required invariants

Where technically practical:

- only `approved_for_export` exact immutable candidate revisions may enter export;
- an export worker cannot create substantive approval;
- an export worker cannot change role/qualification state;
- an export worker receives no requester/member private identity by default;
- GitHub-visible metadata is public-safe;
- export is idempotent;
- target repositories, bases, and paths are allowlisted;
- the integration cannot call arbitrary GitHub APIs;
- the integration cannot inherit site-deployment authority merely because source and generated output share a public repository;
- Phase 2 remains disabled until default-branch protection against the integration is verified;
- Phase 2 opens draft PRs only;
- the integration never marks its PR ready, approves it, enables auto-merge, or merges it;
- a changed approved payload requires a new immutable candidate revision/review;
- external divergence is detected and recorded, not silently overwritten;
- merge actor and merge SHA are captured separately from the export service;
- merged and published are separate states;
- failure/retry history is retained;
- no repository event grants Coalition authority.

## Decisions intentionally deferred

This design does not decide:

- the specific cloud/secret manager used;
- the final Coalition application/database technology;
- whether the repository will later move to an organization account or different GitHub plan;
- whether issue-only export remains enabled after Phase 2;
- exact user-interface layout for export operators;
- whether additional authoritative repositories are added;
- whether a future governance model gives any Coalition role direct repository merge authority; or
- whether GitHub remains the authoritative publication source permanently.

Any change that would let automation or ordinary Coalition roles directly merge authoritative content is a governance/security change, not an implementation detail.
