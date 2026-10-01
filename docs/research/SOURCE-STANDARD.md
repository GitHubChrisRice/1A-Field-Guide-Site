# Legal Source and Verification Standard

Every substantive rule in this project should be traceable to authority that a reader can independently verify.

## Authority tiers

### Tier 1 — Primary controlling authority

Preferred whenever available:

- U.S. Constitution;
- California Constitution;
- United States Code;
- California Codes;
- Code of Federal Regulations;
- California Code of Regulations;
- California Rules of Court;
- U.S. Supreme Court opinions;
- Ninth Circuit opinions;
- California Supreme Court opinions;
- published California Courts of Appeal opinions.

### Tier 2 — Primary persuasive authority

Examples:

- federal appellate cases outside the Ninth Circuit;
- federal district-court decisions;
- unpublished dispositions where citation is lawful and useful;
- attorney-general opinions;
- official administrative decisions.

These sources may be informative but must not be described as binding California authority when they are not.

### Tier 3 — Official policy and guidance

Examples:

- agency photography policies;
- courthouse general orders;
- departmental manuals;
- official FAQs;
- DOJ, POST, DMV, USPS, GSA, or other government guidance.

These can establish what an agency says its rule is. They do not override constitutions, statutes, regulations, or controlling cases.

### Tier 4 — Secondary material

Examples:

- treatises;
- law-review articles;
- legal journalism;
- nonprofit legal guides;
- attorney commentary.

Use these for context and research leads. Whenever practical, follow the citation back to primary authority.

### Tier 5 — Incident evidence

Examples:

- audit videos;
- body-camera recordings;
- dispatch audio;
- public-record responses;
- photographs of signs;
- public employee statements;
- news reports about an incident.

These may establish facts or demonstrate how a policy was applied. They are not authority for the meaning of the law.

### Facility and incident evidence workflow

Facility research should preserve the chain between **law, policy, implementation, and enforcement** rather than treating them as interchangeable.

For a facility-specific investigation, record whenever available:

- the specific area and access status;
- the current written policy and its exact version/effective date;
- the authority the agency claims supports that policy;
- posted signs and where they appeared;
- policy adoption/revision records;
- training or staff instructions;
- prior incidents and original source material;
- police/security involvement, the exclusion/removal authority invoked, and any separate offense/detention/arrest authority invoked;
- later CPRA/FOIA records;
- field-verification results;
- later corrections, policy revisions, or adjudicated outcomes.

Chronology matters. A policy adopted after an incident is not evidence that the same policy governed the earlier event.

Incident evidence should preserve provenance: original source, date, whether the material is edited, how it was obtained, and whether a later official record confirms or contradicts it.

Use the facility investigation template in `docs/templates/facility-investigation-template.md`.

### Facility-policy research flags

These flags describe the state of the project's research; they are not adjudications:

- `SUPPORTED-BY-IDENTIFIED-AUTHORITY`
- `AUTHORITY-UNRESOLVED`
- `POTENTIAL-FACIAL-CONFLICT`
- `POTENTIAL-AS-APPLIED-CONFLICT`
- `POTENTIAL-VIEWPOINT-COMPARATOR`
- `POLICY-TO-CRIMINAL-AUTHORITY-GAP`
- `SUPERSEDED-OR-REVISED`

A sign, employee statement, agency policy, or police practice may provide evidence that a restriction exists or was enforced. It does not by itself prove that the restriction is constitutional, statutorily authorized, or criminally enforceable.


## Binding-authority labels

Case entries should use one of these labels:

- `binding-us-supreme-court`
- `binding-ninth-circuit`
- `binding-california-supreme-court`
- `binding-california-court-of-appeal` — identify district when relevant
- `persuasive-federal-district`
- `persuasive-other-circuit`
- `persuasive-other-state`
- `nonprecedential`

Do not reduce this to a generic "case law" label.

## Verification metadata

Every substantive chapter should contain or link to entries with:

```yaml
authority: "California Penal Code § 602.1(b)"
jurisdiction: "California"
source_type: "statute"
binding_level: "statewide-statute"
source_url: "https://leginfo.legislature.ca.gov/..."
last_verified: "2026-09-16"
status: "verified"
```

For cases add:

```yaml
court: "U.S. Court of Appeals for the Ninth Circuit"
decision_date: "YYYY-MM-DD"
precedential: true
```

## Status values

- `verified` — current text/opinion checked against a primary or authoritative source.
- `needs-review` — plausible but not adequately verified.
- `disputed` — authorities or interpretations materially conflict.
- `superseded` — no longer current but retained for history.
- `facility-specific` — applies only to a particular agency/building/category.

Methodology documents may use `project-methodology` in front matter. That label describes the project's research/field procedure; it is **not** a legal-verification status and should not be applied to a substantive rule of law.

## Quoting law

Short operative language may be quoted when wording matters, but the guide should usually summarize the rule and link the full text.

Do not quote only the favorable half of a provision while omitting an adjacent exception that changes the rule.

## Date discipline

Law changes. Every entry should be checked again when:

- the Legislature amends the statute;
- a new controlling case is decided;
- an agency revises its policy;
- a facility changes rules;
- a contributor flags contrary authority.

A reader should always be able to tell when a proposition was last checked.

## Legal-rule format

Whenever practical, write entries in this order:

1. **Field rule** — short, memorable proposition.
2. **Authority** — precise source.
3. **What the authority actually says.**
4. **Why it matters during an audit.**
5. **Limits/exceptions.**
6. **Cases interpreting it.**
7. **Last verified.**

The purpose of the field rule is recall, not simplification at the expense of accuracy.
