# Privacy, Identity, Attribution, and Retention Workflow

Issue: #43

Policy version: `PRIVACY_V1`

This document defines how the Coalition separates identity from research, controls access to restricted working material, sanitizes public artifacts, preserves internal accountability without requiring public identification, and retains sensitive information only while a legitimate purpose remains.

It does not weaken the Field Guide's evidentiary standard. It defines how evidence and identity are handled while that standard is applied.

# Governing principles

1. **Internal accountability does not require public identification.**
2. **Identity is separate from membership, role, research authorship, requester status, and public attribution.**
3. **Research transparency does not mean publishing the internal working record.**
4. **Sensitive access is need-to-know, purpose-limited, and auditable.**
5. **Public release is a sanitization/export decision applied to an exact immutable PublicationCandidateRevision.**
6. **A lawful or useful internal source is not automatically appropriate to republish.**
7. **Research retention does not require indefinite identity retention.**
8. **Private people who are merely incidental receive minimization by default; people who materially participate in an incident may become part of the publishable evidentiary record.**
9. **Publication relevance, not retaliation or viewpoint, governs identification decisions.**
10. **Secrets and credentials should remain outside ordinary research records wherever technically possible.**

# Data classifications

The platform uses these classifications.

## Public

Material intentionally approved for public release.

Examples:

- published Field Guide text;
- public registry entries;
- approved public facility reports;
- public source links;
- public institutional attribution.

Public means intentionally publishable, not merely obtainable somewhere else.

## Coalition

Ordinary authenticated collaboration material that does not require special need-to-know restriction.

Examples may include:

- nonrestricted research queues;
- general methodology discussion;
- nonrestricted source-verification work;
- ordinary division coordination.

Coalition material is not automatically public.

## Restricted

Need-to-know research or investigation material.

Examples:

- unpublished investigation files;
- raw records productions;
- pre-publication evidence;
- incident video not yet privacy-reviewed;
- internal source notes;
- facility research containing sensitive operational or personal details;
- working copies of documents that require redaction before release.

Holding a role in the same jurisdiction does not automatically grant access.

## Identity-restricted

Information whose primary sensitivity is that it identifies or contacts a person whose identity need not be generally exposed.

Examples:

- requester name and contact information;
- private member contact/profile identity beyond what is needed for authentication/administration;
- linkage between a public pseudonym and private account identity;
- identity-verification material if later supported;
- private-person contact information copied from records.

Identity-restricted data requires an explicit operational purpose to access.

## Administrative

Internal governance/security records.

Examples:

- membership application decisions;
- promotion assessments;
- role-grant rationale;
- contribution-credit disputes;
- security/access reviews;
- privacy incident handling;
- audit records.

Administrative does not automatically mean Identity-restricted, but the two may overlap.

## Secret

Credentials or security secrets.

Examples:

- tokens;
- API keys;
- private keys;
- recovery codes;
- authentication secrets.

Secret material should use dedicated secret storage and should not be copied into research submissions, investigation notes, review comments, exports, or audit metadata.

# Identity separation

## Authentication identity

Authentication identity belongs to the account/security layer.

Examples:

- authentication-provider subject;
- login email;
- account-security state.

Authentication identity is private and is not a public attribution source.

Where practical, password material and authentication secrets remain with the identity provider rather than the Coalition database.

## Membership identity

Membership connects an authenticated User to Coalition participation.

It may support:

- role grants;
- contributions;
- submissions;
- reviews;
- promotion requests;
- investigation assignments;
- audit accountability.

Membership identity is internal provenance. It does not imply public naming.

## Public attribution identity

Public attribution is an independent presentation choice.

Supported modes may include:

- institutional;
- division;
- approved pseudonym;
- individual attribution when deliberately enabled.

Default public attribution is institutional/division attribution.

A public display name:

- need not equal login identity;
- need not equal legal identity;
- must not be silently inferred from email, GitHub username, authentication provider, or private profile;
- may be changed prospectively subject to provenance requirements.

Founder, Administrator, requester, contributor, or reviewer identity is not required to appear publicly merely because related material is published.

## Requester identity

Requester identity is separate from the investigation/research record.

An investigation should reference zero or more opaque requester identifiers where requester linkage is operationally necessary.

Example:

```text
requester_refs: [R-0017]
```

not repeated identity text such as:

```text
requested_by: Jane Example <jane@example.com>
```

across notes, tables, exports, or GitHub artifacts.

Requester contact information belongs in an Identity-restricted record separate from ordinary investigation content. Opaque requester references are internal linkage identifiers, not public attribution identifiers.

Researchers should receive only the requester context they actually need.

# Requester privacy

Requester identity is **not visible to ordinary collaborators by default**.

A requester may need to be identified internally to a limited person for purposes such as:

- clarifying the request;
- resolving authenticity or provenance;
- handling a conflict-of-interest question;
- fulfilling an explicitly requested follow-up;
- responding to a privacy/security incident;
- complying with a valid legal/administrative requirement.

Those needs do not imply the full investigation team needs the identity.

Publication must not reveal requester identity unless:

1. disclosure is intentionally requested/authorized by the requester or otherwise independently justified;
2. the identity is materially necessary to the public artifact;
3. the exact PublicationCandidateRevision passes privacy review; and
4. disclosure is consistent with applicable law and project policy.

The normal expectation is that requester identity is unnecessary to publication.

An investigation may have zero, one, or multiple requester references. Collaboration should expose only the opaque requester references unless a participant has a separate operational need to resolve them to Identity-restricted contact records.

# Member privacy and internal provenance

Internal records may preserve stable Membership identifiers for:

- authorship;
- review history;
- contribution credit;
- promotion decisions;
- access grants;
- publication decisions;
- audit history.

The system should avoid copying member email addresses or authentication identifiers into those records.

Where a historical action must remain attributable after a member departs, retain the stable internal provenance reference while minimizing unnecessary profile/contact information.

Departure does not cause public attribution to revert to private identity.

# Private persons in evidence and publication

The Coalition does not intentionally target uninvolved private persons and should minimize unnecessary identification of people who are merely incidental to research, recording, public-records evidence, or facility activity.

The privacy model distinguishes three categories.

## Incidental private person

A private person who is merely present, captured, named, or visible without materially participating in the researched event.

Examples:

- a visitor standing in the background;
- a patron walking through a lobby;
- a name appearing incidentally in a visitor log;
- an uninvolved person visible on surveillance video;
- a private person's contact information included in a government records production without relevance to the research question.

For incidental private people, public artifacts should minimize unnecessary identification, naming, spotlighting, or disclosure when identity adds no material evidentiary value.

Minimization does **not** require automatic face-blurring of every bystander in ordinary scene footage. Where wider footage is materially useful to show the setting, chronology, government response, or credibility of the record, incidental background presence may remain so long as the publication does not unnecessarily identify or focus on those people.

## Material private participant

A private person may become a material participant when they voluntarily and materially participate in the incident or evidentiary chain being documented.

Examples include a person who:

- confronts a researcher;
- attempts to interfere with the recording/research activity being documented;
- makes a material allegation about the researcher or conduct;
- asks government staff or police to intervene;
- supplies materially relevant statements to officials;
- participates in the removal/exclusion sequence;
- becomes a material witness to the government action under investigation;
- otherwise takes conduct necessary to accurately explain how the documented event unfolded.

A material private participant is not automatically entitled under Coalition policy to face-blurring, anonymization, or omission of their observable conduct merely because they are a private citizen.

Mere annoyance, criticism, a momentary objection, or a brief interaction does not automatically make a person's identity materially relevant. The question is whether their participation meaningfully forms part of the incident, government response, allegation, evidentiary chain, or explanation of what occurred.

Their relevant identity, image, statements, and conduct **may** be retained and published when appropriate to accurately document the incident.

Publishing observable conduct or an unedited/materially complete encounter does not create a default obligation to investigate and reveal an otherwise-unknown participant's real-world identity. Naming or separately identifying a person should be no broader than the evidentiary/reporting purpose requires.

The decision must be based on:

- relevance to the documented event;
- evidentiary value;
- accuracy and context;
- legitimate research/reporting purpose;
- privacy/publication review;
- applicable law.

It must **not** be based on:

- punishment for being rude or critical;
- retaliation for objecting to the researcher;
- an invitation for others to contact or harass the person;
- a desire to expose unrelated personal information.

Material participation does not make unrelated personal data relevant.

Home addresses, personal phone numbers, private email addresses, family information, medical information, financial information, credentials, unrelated social-media accounts, account identifiers, or other unrelated sensitive data should ordinarily remain excluded.

## Government actor acting officially

An official's:

- official name;
- official title/role;
- official statements;
- observable official conduct;
- official agency contact information where relevant;

may be part of the governmental record.

Official status does not justify publication of unrelated private data such as home address, family details, personal phone number, medical information, private credentials, or unrelated personal accounts.

# Minors and child-related material

The project's standing field policy already avoids intentionally entering, remaining in, or filming into areas designated for children.

Where a minor nevertheless appears incidentally in evidence, public identification should receive heightened minimization.

A minor should not be identified merely because:

- they are visible in the background;
- they are present with an adult;
- their name appears incidentally in a record;
- an adult participant references them.

If a minor is materially relevant to government conduct, use the least-identifying public presentation that can accurately establish the governmental action unless a substantially stronger public-interest/legal basis supports identification.

# Public records do not waive Coalition privacy review

The fact that personal information appears in:

- a public record;
- a government website;
- a court filing;
- a public meeting video;
- an official report;
- a lawfully obtained records production;

does not automatically mean the Coalition should republish every personal detail.

The publication question remains:

> What information is materially necessary to support the public proposition?

A source can remain internally preserved while the public artifact uses:

- a redacted copy;
- a cropped image;
- an excerpt;
- a paraphrased factual description;
- a source citation without republishing sensitive fields.

# Evidence handling

## Privacy by reference, not duplication

Restricted/Identity-restricted content should be referenced rather than copied into multiple records wherever practical.

Examples:

- investigation notes reference an Evidence object;
- review comments reference the evidence identifier;
- requester linkage uses an opaque requester reference;
- publication candidates derive sanitized content from controlled source objects.

Avoid copying sensitive text into:

- issue titles;
- task names;
- ordinary comments;
- filenames;
- branch names;
- GitHub metadata;
- public URLs;
- email subjects;
- audit summaries.

## Source provenance remains intact

Redaction/sanitization must not destroy the ability to determine:

- what source was reviewed;
- source provenance;
- what proposition it supported;
- what was removed from the public derivative;
- who authorized the public transformation.

The internal original and public derivative are separate objects where needed.

# Sensitive access model

Role authority and sensitive-data access are separate.

A Reviewer may be authorized to make substantive review decisions without being authorized to see every requester identity or every Restricted investigation.

A Division Lead may coordinate work without receiving blanket access to every sensitive source in the division.

Administrator authority is not a universal content-reading entitlement. Administrative access still requires an administrative purpose and follows auditing requirements.

## InvestigationAssignment

Existing InvestigationAssignment is the normal need-to-know grant for Restricted investigation material.

Assignment should specify:

- investigation;
- membership;
- assignment role;
- grantor;
- grant/revoke time.

## SensitiveAccessGrant

For sensitive access not adequately represented by InvestigationAssignment, use a purpose-limited SensitiveAccessGrant.

Conceptual fields:

- `id`;
- `membership_id`;
- `resource_type`, `resource_id`;
- `access_level`;
- `purpose_code`;
- `reason`;
- `granted_by`;
- `granted_at`;
- `expires_at` where appropriate;
- `revoked_by`, `revoked_at` - nullable.

SensitiveAccessGrant does not create substantive research authority.

## Break-glass access

Emergency/exceptional administrative access may be supported when necessary for:

- security response;
- privacy incident containment;
- data recovery;
- a legal/administrative obligation;
- another specifically documented urgent purpose.

Break-glass access:

- must require an explicit reason;
- must be time-limited where practical;
- must create an AuditEvent;
- should trigger post-use review by another authorized administrator when feasible;
- must not become a routine substitute for ordinary assignment.

# Sensitive read auditing

At minimum, audit:

- access to requester identity;
- access to member Identity-restricted records outside ordinary self-service;
- break-glass access;
- Restricted investigation access outside normal assignment;
- bulk export/download of Restricted or Identity-restricted material;
- privacy-sensitive publication decisions;
- creation/revocation of SensitiveAccessGrant;
- material retention overrides/legal holds;
- privacy/security incident actions.

Routine reading of ordinary Coalition material need not create a surveillance-style activity feed.

Sensitive-read audit data is Administrative and not a public contributor activity stream.

# Public publication is a derived artifact

Internal research records are never made public by changing their classification from Restricted to Public.

The publication path is:

```text
Internal research/evidence
        |
Approved research revision
        |
Derived PublicationCandidateRevision
        |
Sanitization / privacy review
        |
Final publication review
        |
Approved for export
        |
Public artifact
```

The public derivative may contain less information than the internal research record while preserving the supported conclusion and provenance chain.

A PublicationCandidateRevision remains a non-public working object while it is under review, even when its payload is drafted for eventual public use. The exported/published artifact becomes Public only after all required privacy and final-publication approvals.

# Privacy publication gate

Any PublicationCandidateRevision that contains or derives from Restricted, Identity-restricted, Administrative, or otherwise privacy-sensitive content must complete privacy/publication-safety review before `approved_for_export`.

The review is attached to the exact immutable PublicationCandidateRevision.

Privacy review asks:

- Is every identifying detail materially necessary?
- Has requester identity leaked into the candidate?
- Has member/private account identity leaked into the candidate?
- Are uninvolved private persons unnecessarily identified?
- If a private person is identified, are they a material participant or otherwise materially relevant?
- Does publication accurately preserve context rather than selectively expose a participant?
- Are unrelated sensitive details excluded?
- Are minors appropriately minimized?
- Is restricted source material being republished when a less-disclosing presentation would establish the same proposition?
- Are filenames safe?
- Are attachment names safe?
- Are URLs/query strings safe?
- Are email headers/signatures safe?
- Are screenshots/crops safe?
- Has EXIF or similar media metadata been removed where appropriate?
- Have document properties/author metadata been checked?
- Are embedded comments/revisions/hidden spreadsheet cells or similar hidden content relevant to the file type checked where practical?
- Does the public source/provenance trail remain understandable after sanitization?

Approval means this exact public candidate may proceed. It does not authorize a different revision. The privacy Review record must identify the governing privacy-policy version, such as `PRIVACY_V1`.

# Sanitization record

Where sensitive material is transformed for public release, retain a SanitizationRecord.

Conceptual fields:

- `id`;
- `publication_candidate_revision_id`;
- `source_refs`;
- `transformation_types` - redact, blur, crop, omit, paraphrase, metadata-strip, replace-with-public-source, or approved extension;
- `visibility_classification` - Administrative or Restricted;
- `privacy_policy_version`;
- `reason`;
- `performed_by`;
- `performed_at`;
- `verified_by` - nullable until checked;
- `verified_at` - nullable;
- `notes`.

A SanitizationRecord explains the privacy transformation; it does not need to publicly disclose the removed information.

For a privacy-sensitive publication that uses a SanitizationRecord, `verified_by` must be completed before export and must identify someone other than `performed_by`. The privacy reviewer may satisfy that verification when otherwise authorized.

# Retention model

`PRIVACY_V1` defines retention categories and lifecycle controls, not arbitrary universal year counts.

Retention must be based on the continuing purpose of the data.

## Long-lived research provenance

Long-term retention is normally justified for:

- published source provenance;
- accepted immutable research revisions;
- publication-candidate history;
- corrections/supersession history;
- authority verification necessary to explain past published conclusions.

Long-lived provenance does not require indefinite retention of requester/member contact information.

## Audit/governance records

Retain enough governance history to explain:

- role grants/revocations;
- promotion decisions;
- contribution awards/reversals;
- substantive review/publication decisions;
- sensitive-access grants;
- material privacy decisions;
- correction/supersession events.

The audit record should identify stable internal actors without unnecessarily duplicating authentication/contact data.

## Restricted raw evidence

Retain raw Restricted evidence only while it has continuing:

- research value;
- evidentiary value;
- correction/provenance value;
- pending-records/claim/litigation preservation value;
- other documented operational/legal purpose.

A published conclusion does not automatically require permanent storage of every raw copy if provenance can be responsibly preserved another way.

## Requester contact information

Requester contact information should normally be eligible for disposition earlier than the research/investigation itself once:

- necessary communication is complete;
- no unresolved authenticity/provenance need requires it;
- no valid hold applies;
- no other documented operational purpose remains.

The opaque requester reference may remain to preserve internal history without retaining the contact detail.

## Authentication/security information

Retain only what is required for:

- active account operation;
- fraud/security investigation;
- necessary account history;
- applicable administrative/security requirements.

Secrets follow secret-management policy rather than ordinary research retention.

# Retention controls

Sensitive entities should support lifecycle metadata such as:

- `retention_class`;
- `retention_basis`;
- `review_after` - nullable;
- `review_trigger` - nullable event such as communication_complete, investigation_closed, publication_complete, account_departed, or hold_released;
- `retain_until` - nullable when a fixed date is actually appropriate;
- `legal_or_preservation_hold`;
- `hold_reason`;
- `disposition_status`;
- `disposed_at` - nullable;
- `disposition_actor` - nullable.

Every sensitive record should have either a documented long-lived retention class or a review date/event trigger. "No fixed numeric period" must not become an undocumented keep-forever default.

A retention review may result in:

- retain;
- minimize;
- anonymize/pseudonymize;
- detach identity/contact layer;
- archive under narrower access;
- dispose;
- hold.

Retention expiration must not silently destroy material under an active preservation/legal hold.

A preservation/legal hold must have a documented basis and should be reviewed or released when that basis ends. A hold must not be used as a generic undocumented keep-forever label.

# Member departure, deactivation, and privacy requests

When a member departs or an account is deactivated:

- authentication access ends;
- active role grants/assignments are revoked or ended as appropriate;
- unnecessary profile/contact fields may be minimized/disposed under policy;
- public attribution remains governed by the chosen attribution mode and publication history;
- historical submissions/reviews/credit/governance events may retain a stable internal Membership reference where necessary for accountability.

The system should not rewrite history to pretend an approved review, contribution, role decision, or publication action never occurred.

Where technically and operationally possible, personal identity/contact data should be separable from that historical provenance.

A privacy/deletion request is evaluated against:

- whether the field is still necessary;
- historical/audit/provenance requirements;
- security/fraud needs;
- preservation/legal holds;
- public artifact correction needs;
- applicable law.

The outcome may therefore be field deletion/minimization rather than deletion of the underlying historical research event.

# Public attribution changes and withdrawal

A member may request a prospective change from individual/pseudonymous public attribution to institutional attribution where technically and editorially practical.

Historical public artifacts need not be silently rewritten in ways that damage provenance, but privacy-sensitive cases should support correction or attribution minimization when justified.

No public attribution change may alter the internal identity of the actual submitter/reviewer in auditable provenance records.

# Export controls

Bulk export of Coalition/Restricted/Identity-restricted/Administrative data is a privileged action separate from ordinary read access.

Exports should:

- honor current authorization;
- exclude Secrets;
- preserve classification labels where possible;
- be auditable;
- use the minimum data necessary for the purpose;
- avoid silently expanding access through exported copies.

# Service principals and integrations

Service principals receive only the minimum sensitive-data capabilities required for their function.

A GitHub/publication integration should consume approved Public PublicationCandidateRevision content rather than receive blanket access to raw Identity-restricted or Restricted investigation data.

Secrets used by integrations must remain in secret storage and never be exported into GitHub artifacts.

# Privacy/security incidents

A suspected accidental disclosure of Restricted, Identity-restricted, Administrative, or Secret material should create an internal privacy/security incident.

The response may include:

1. contain access/publication;
2. preserve necessary evidence of what occurred;
3. identify the exposed data and affected artifacts;
4. rotate/revoke credentials if Secrets were involved;
5. correct/withdraw public artifacts where appropriate;
6. review access/audit history;
7. document remediation and recurrence prevention.

The incident process must not create a second unnecessary disclosure by copying exposed data into broadly visible incident notes.

# Privacy-neutral publication rule

Privacy decisions must not depend on whether the person's conduct or viewpoint is favorable to the Coalition.

For materially comparable participation, apply materially comparable publication/privacy reasoning.

A private person's negative engagement may make their conduct relevant to the documented incident. It does not create a punishment exception to privacy policy.

Conversely, a private person's favorable engagement does not automatically make them anonymous if their identity/conduct is materially necessary to explain the event.

# Required implementation invariants

Where technically practical:

- authentication identity is not used automatically as public attribution;
- public attribution defaults to institutional/division attribution;
- requester identity is Identity-restricted and separate from investigation content;
- Restricted/Identity-restricted access requires need-to-know authorization beyond ordinary role membership;
- Administrator status alone is not blanket sensitive-content read authority;
- break-glass access is reasoned, time-limited where practical, and audited;
- public release uses a derived PublicationCandidateRevision rather than making the internal record Public;
- a pre-export PublicationCandidateRevision remains non-Public while under review;
- privacy approval applies to the exact immutable public candidate revision;
- required privacy review is independent of the preparer/final sanitizer and is performed by an authorized Senior Reviewer or Division Lead with necessary sensitive access under the initial model;
- privacy-sensitive SanitizationRecords require independent verification before export;
- public export cannot bypass required privacy review;
- requester/member identity is not copied into public artifacts through metadata or filenames;
- incidental private persons receive minimization by default;
- material private participants may be published based on relevance/evidentiary purpose, not retaliation;
- unrelated sensitive details remain excluded even when a material participant is identified;
- minors receive heightened minimization;
- lawfully/publicly obtained personal information is still subject to Coalition publication minimization;
- sensitive-read auditing remains Administrative, not public;
- research retention does not require indefinite retention of contact identity;
- preservation/legal holds override ordinary disposition;
- historical provenance can survive member departure without requiring continued public/private contact disclosure;
- service principals cannot use member roles as a shortcut to sensitive access;
- Secrets do not enter ordinary research/publication records.

# Data-model consequences

The Coalition data model should be updated to:

- define the classification meanings in this policy;
- add requester/reference separation;
- add SensitiveAccessGrant;
- add SanitizationRecord;
- add retention lifecycle metadata or a related retention-control entity for sensitive records;
- clarify sensitive-read AuditEvent requirements;
- preserve stable internal provenance without requiring public identity;
- require the privacy review stage on sensitive PublicationCandidateRevisions.

# Decisions intentionally deferred

`PRIVACY_V1` does not yet set universal numeric retention periods.

It also does not decide:

- the identity-verification standard for membership, if any;
- the exact authentication provider;
- jurisdiction-specific statutory privacy/records obligations that may require specialized overrides;
- formal legal-process response procedures;
- a permanent rule for publishing minors in exceptional public-interest circumstances;
- exact UI for privacy settings, retention review, or sensitive-access grants.

Those decisions require deliberate later policy or implementation work rather than inference.
