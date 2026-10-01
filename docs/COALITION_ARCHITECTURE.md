# Coalition Architecture

This document records durable boundaries for the nationwide 1A Field Guide Coalition platform. Implementation details may evolve, but changes to these boundaries require deliberate review.

## Purpose

The Coalition is a standards-governed research network supporting the 1A Field Guide. California is the reference implementation for research rigor; nationwide expansion must preserve or strengthen that standard.

The platform separates contribution from publication. Members may submit research without receiving repository access or authority to publish Field Guide conclusions.

## Jurisdiction model

The platform represents:

- Federal/national material;
- federal judicial circuits as an applicable legal dimension;
- all 50 states and the District of Columbia from inception;
- subordinate regional/local organization where useful;
- facility-specific records and investigations.

Jurisdiction readiness has two separate dimensions that must not be collapsed into one status.

### Field Guide and division qualification

A state or other jurisdiction intended to support facility analysis may be:

1. **Inactive** - no qualified jurisdiction-specific Field Guide exists yet.
2. **Field Guide Development** - the jurisdiction's legal/doctrinal framework is being built or reviewed against Coalition standards.
3. **Active** - the Field Guide has passed human qualification and is approved for use as the analytical framework for facility research. The corresponding division may operate under Coalition standards.

A jurisdiction may be publicly represented while Inactive. Contributors may research and develop its Field Guide, but Coalition facility conclusions must not be generated against an unqualified framework.

Qualification is a human decision. Coverage metrics, contribution points, or automated completeness checks may support review but never activate a jurisdiction automatically.

Independent qualified human review is the normal activation path. During bootstrap governance, when no independent qualified human reviewer is reasonably available, the Founder may use the documented founding/bootstrap activation exception defined in [Jurisdiction Qualification and Field Guide Overlay Model](JURISDICTION_QUALIFICATION.md). A bootstrap activation does not pretend that independent review occurred; it records the exception and the Founder assumes responsibility for the activation decision.

### Facility-research maturity

Facility-research status applies only after the jurisdiction is Active and its Field Guide is qualified:

1. **Unresearched** - the qualified framework exists, but no facility research program has materially begun.
2. **Researching** - facility investigations or registry analysis are underway using the qualified Field Guide.
3. **Established** - a meaningful facility-research body exists and is maintained as continuing work.

Facility-research maturity describes application of the qualified framework; it does not qualify the Field Guide itself and does not confer organizational authority.

### County/county-equivalent coverage

Formal county research coverage begins **after** the parent state Field Guide is Active. Pre-activation county/facility work may still exist as development or test material under the jurisdiction-qualification rules, but it does not receive county coverage maturity until it is reconciled against the qualified state framework. Counties and county-equivalents are not independently activated miniature state Field Guides.

As part of state activation, the system creates or validates a complete inventory of the state's counties/county-equivalents. Each coverage unit inherits the national core, applicable federal/circuit layer, and Active state overlay, then tracks only the local law, policy, agency/facility, enforcement, records-practice, and other local dependencies that vary below the state layer.

County coverage uses **Unresearched / Researching / Established** as research-coverage labels, not qualification statuses. Existing pre-activation work may seed a county record only after it is reconciled against the newly qualified state framework.

A CountyCoverageUnit is a geographic/research index, **not a claim that every municipality, special district, state agency, federal facility, or other entity within its boundaries is legally subordinate to county government**. Local authority must still be traced to the actual governing entity. Cross-county entities or facilities may reference more than one coverage unit where necessary.

California is the reference pattern: establish the legal/research framework first, then use that framework to measure county/local law, facility policies, access conditions, enforcement evidence, and resulting findings.

Nationwide expansion uses a canonical Field Guide structure rather than independent state wikis. National methodology and nationally controlling authority are reused; applicable circuit, state, and local authority are layered onto the canonical scenario and encounter decision trees. Qualification measures whether the jurisdiction-specific overlay can run those trees without material research gaps. See [Jurisdiction Qualification and Field Guide Overlay Model](JURISDICTION_QUALIFICATION.md).

## Member progression

Member roles and jurisdiction scope are separate. Initial role concepts are:

- Member;
- Contributor;
- Researcher;
- Reviewer;
- Senior Reviewer;
- Division Lead;
- Administrator;
- Founder.

Roles represent trust and responsibility. Contribution points represent accepted work. A point threshold may establish eligibility to request promotion but must never grant authority automatically.

The normal merit/trust progression is Member -> Contributor -> Researcher -> Reviewer -> Senior Reviewer -> Division Lead. Administrator is a separate platform/governance appointment, not a points-based top rung.

**Founder** is also separate from the merit ladder. It records project-origin governance authority and is not earned through points or normal promotion. Founder is not a universal superuser and does not automatically supply substantive Reviewer competence, unrestricted sensitive-data access, or repository credentials. Its exceptional authority is limited to deliberately documented founding/bootstrap actions, including establishing initial governance and, when the normal independent-review path is unavailable, making a bootstrap jurisdiction-activation decision under the qualification rules. The permanent Founder role is distinct from temporary or reviewable bootstrap substantive RoleGrants.

A person may contribute to multiple jurisdictions without leading them. Leadership requires demonstrated jurisdiction-specific work and human approval. Initial credit values, scope-aware eligibility floors, review calibration, and promotion routing are defined in [Contribution Credit and Promotion Workflow](CONTRIBUTION_PROMOTION_WORKFLOW.md).

## Contribution model

Points should reward accepted, useful work rather than raw activity. Eligible work may include authoritative-source research, facility research, public-records results, corrections, source verification, substantive peer review, and other approved contributions.

The system should reward accurate contrary findings and well-supported uncertainty as strongly as findings favorable to a contributor's initial theory. Incentives must not depend on reaching a preferred legal or factual conclusion.

Each accepted contribution should retain provenance sufficient to identify its submitter internally, review history, disposition, jurisdiction, and relationship to published material.

Contribution credit is an internal ledger rather than a public ranking system by default. Credit must not reward fragmentation, submission volume, dramatic outcomes, or viewpoint alignment.

## Research pipeline

The authoritative publication path is:

`submission -> validation -> research review -> applicable doctrinal/evidentiary review -> approval -> publication candidate -> final publication decision`

Rejected, returned, unresolved, or superseded work remains distinguishable from authoritative Field Guide content.

Structured submissions should require the fields needed by the applicable methodology. Software may validate completeness and consistency, but automated validation does not supply substantive approval. The type-specific schemas, immutable-revision model, review stages, independence rules, and publication-candidate boundary are defined in [Structured Research Submission and Review Workflow](RESEARCH_SUBMISSION_WORKFLOW.md).

## GitHub boundary

Coalition membership does not imply GitHub access.

For the initial system, members submit through the Coalition platform. Only an exact immutable `PublicationCandidateRevision` that has completed all required publication/privacy review may become eligible for controlled GitHub preparation. Repository publication and merge remain separate human-controlled actions.

The GitHub integration runs as a dedicated least-privilege service principal. It receives only the approved public derivative and public-safe metadata needed for the requested export operation; it does not inherit Coalition roles, obtain broad investigation access, or reuse a human maintainer/public-site deployment credential.

The initial deployment is phased. Issue-only preparation may operate with no Contents write permission. Branch + draft-Pull-Request preparation is enabled only after the authoritative branch is technically protected from direct update/merge by the integration identity. The export service never marks its PR ready, approves it, enables auto-merge, or merges it.

Detailed preconditions, service-principal boundaries, export state, divergence handling, audit requirements, and repository-split prerequisites are defined in [Controlled GitHub Publication Integration](GITHUB_PUBLICATION_INTEGRATION.md) and [Public/Private Repository Split](PUBLIC_PRIVATE_REPOSITORY_SPLIT.md).

The platform must not expose repository credentials or broad GitHub permissions to ordinary members.

The intended repository boundary is explicit: `1A-Field-Guide` remains private for internal research/workflow material, while `1A-Field-Guide-Site` becomes the public authoritative-source repository after migration. Generated website output belongs on a deployment branch such as `gh-pages`, not on the authoritative public-source `main` branch.

## Research integrity

A government policy is evidence that the government claims or applies a rule; it is not by itself proof that the rule is constitutional.

Facility research must distinguish the facility, specific area, access status, restriction, source, claimed authority, applicable doctrine, evidence of enforcement, and resulting finding.

Legal and factual propositions must preserve authority level, jurisdiction, binding/persuasive status where applicable, verification date, limitations, contrary authority, and unresolved questions.

`Unresolved` is an acceptable conclusion.

## Privacy and attribution

Public identity and internal accountability are separate.

The system may retain internal authorship, review, and audit records while public materials use institutional or division attribution. Member/requester identity, contact information, unpublished investigative material, credentials, and other restricted information must not be exposed merely because related research is published.

Founder or administrator identity is not required to be part of public-facing attribution.

Requester identity is Identity-restricted and should be separated from ordinary investigation content. Public release uses a sanitized PublicationCandidateRevision rather than exposing the internal working record.

For private persons appearing in incident evidence, the project distinguishes incidental people from material participants. Incidental private people are minimized by default. A person who voluntarily becomes materially involved in the documented incident may have relevant identity, statements, image, and conduct retained or published when necessary to accurately document the event; this is an evidentiary decision, not a retaliation exception, and unrelated sensitive personal information remains excluded.

Detailed rules are defined in [Privacy, Identity, Attribution, and Retention Workflow](PRIVACY_ATTRIBUTION_RETENTION.md).

## Division autonomy

Active divisions may coordinate local research, prioritize facility work, recommend promotions, and perform delegated review within their scope.

Division autonomy does not include authority to lower national research, sourcing, evidentiary, privacy, or publication standards.

## Human decision boundaries

Implementation agents and automated systems must not silently change:

- legal conclusions or authority classifications;
- research/evidence standards;
- publication criteria;
- privacy or attribution boundaries;
- role permissions or promotion authority;
- Field Guide qualification or division activation requirements;
- organizational governance.

When implementation exposes a genuine question in one of these areas, record the question for human decision rather than inventing a rule.
