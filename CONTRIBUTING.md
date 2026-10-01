# Contributing to 1A Field Guide

This project is intended to become a reliable public legal-reference project, not a collection of anecdotes or slogans. Contributions are welcome, but substantive legal claims need traceable support.

## What you can contribute

Useful contributions include:

- statutes, regulations, court rules, and constitutional provisions;
- binding and persuasive cases;
- official agency policies and facility rules;
- corrections to existing summaries;
- updates when law or policy changes;
- public-records results that clarify how an agency applies a rule;
- real-world audit case studies with enough documentation to verify what happened;
- facility-specific research for California public agencies and federal facilities in California.

## Evidence standard

For legal propositions, prefer sources in this order:

1. Official constitution, statute, regulation, court rule, or published judicial opinion.
2. Official government guidance or policy.
3. Reputable legal research source reproducing primary authority.
4. Secondary commentary only for explanation or leads.

A video, social-media post, news article, forum post, or verbal statement by a public employee may be evidence that an event occurred, but it is not authority for what the law means.

## Required information for a new legal entry

A proposed legal entry should identify:

- the exact authority;
- jurisdiction;
- court or issuing body where applicable;
- date decided/enacted/current version;
- direct source URL;
- whether the authority is binding in California;
- the narrow proposition it supports;
- important limitations or contrary authority;
- date the source was last verified.

Use the templates in `docs/templates/` where possible.

## Case submissions

A case submission should not simply say that an auditor "won" or an agency "lost." Explain what legal issue was actually decided.

For litigation, distinguish among:

- complaint/allegations;
- temporary restraining order or preliminary injunction;
- motion to dismiss;
- summary judgment;
- trial judgment;
- appellate decision;
- settlement;
- unpublished/nonprecedential disposition.

A settlement does not itself establish that a court held the challenged conduct unconstitutional.

## Real-world audit reports

When contributing an incident or audit:

- separate observed facts from legal conclusions;
- provide dates, the specific facility area, access status, and public hours where relevant;
- link original, preferably unedited source material where lawful and appropriate;
- identify the exact written policy, sign, employee instruction, or claimed rule involved;
- identify the statute, regulation, ordinance, order, or other authority the agency or officer actually invoked;
- distinguish a policy violation from separate exclusion/removal authority and separate detention/citation/arrest authority, if any;
- document materially comparable treatment when viewpoint/selective enforcement is relevant;
- identify records obtained before and after the visit through CPRA/FOIA;
- preserve policy version/effective-date chronology;
- redact or avoid unnecessary personal information about private individuals;
- note any later correction to the initial interpretation.

For facility investigations, use `docs/templates/facility-investigation-template.md` and the methodology in `docs/california/facility-investigation-methodology.md`.

The purpose is to document government conduct, not to identify or embarrass uninvolved members of the public.

## Writing style

- State the rule before commentary.
- Avoid inflammatory labels.
- Avoid claiming an issue is "settled" unless the authority supports that characterization.
- Explain uncertainty rather than hiding it.
- Distinguish what an officer or agency **may ask** from what a person is **legally required** to do.
- Distinguish whether conduct gives an officer a reason to **investigate**, **detain**, **search**, or **arrest**.
- Do not generalize rules governing one type of property to every government facility.


## Project governance and work tracking

GitHub Issues and Pull Requests are the planning, execution, review, and continuation record for repository work. Durable research or architecture invariants belong in the document that owns them or, when necessary, in `docs/DECISIONS.md`. Do not maintain Markdown roadmaps, status snapshots, review registers, or mirrors of GitHub work state.

Work from an authorized Issue or explicit owner-directed task. Begin routine implementation on a descriptive branch from current `main`; do not make routine implementation changes directly on `main`. Keep PRs focused and link them to the Issue they implement.

Merged source is the accepted working implementation. An open Issue, submission, investigation note, automated result, PR, or repeated suggestion is not authoritative Field Guide content merely because it exists.

The nationwide Coalition architecture and its durable boundaries are defined in `docs/COALITION_ARCHITECTURE.md`. Agents and contributors must not silently change legal conclusions, research standards, publication criteria, privacy boundaries, permission models, jurisdiction activation requirements, or organizational governance to complete implementation. Surface genuine conflicts for human decision.

### Contribution and publication boundary

Coalition submissions are proposals. They must pass the applicable validation and review path before becoming publication candidates. Reviews attach to immutable submitted revisions, and approval of research remains separate from final publication approval. The detailed workflow is defined in `docs/RESEARCH_SUBMISSION_WORKFLOW.md`. Contribution points may support promotion eligibility but never confer authority, activate a jurisdiction, or approve publication. Credit values, anti-gaming rules, scope-aware eligibility, calibration, and promotion routing are defined in `docs/CONTRIBUTION_PROMOTION_WORKFLOW.md`.

Ordinary coalition participation does not require GitHub access. A platform integration may prepare GitHub Issues or draft Pull Requests from approved work, but repository publication and merge remain separate human-controlled actions unless governance is deliberately changed later.

### Privacy

Preserve internal provenance needed for accountability while minimizing unnecessary public personal information. Do not expose private requester/member identity, contact information, unpublished investigation material, credentials, tokens, or restricted working material in public artifacts. Public attribution may be institutional or division-based where appropriate.

The detailed classification, requester-isolation, private-person/material-participant, sensitive-access, publication-sanitization, audit, and retention rules are defined in `docs/PRIVACY_ATTRIBUTION_RETENTION.md`.

## Pull requests

Keep pull requests focused. A PR changing one doctrine or facility chapter is easier to review than a PR changing the entire handbook.

When changing a legal proposition, include the primary authority in the PR description and explain why the change is needed.

## Corrections

If you believe the guide is dangerously or materially wrong, open an issue even if you do not yet have a complete replacement draft. Include enough source material for the claim to be investigated.

## Licensing contributions

The handbook and documentation are licensed under the **Creative Commons Attribution-ShareAlike 4.0 International Public License (CC BY-SA 4.0)**. See [`LICENSE.md`](LICENSE.md).

By submitting a contribution to the handbook or documentation and allowing it to be merged, you agree that your contribution may be distributed under CC BY-SA 4.0 as part of this project, unless you clearly identify different licensing terms before the contribution is accepted.

Do not submit third-party material unless the project may lawfully use it. Statutes, judicial opinions, government materials, quotations, images, policies, and other third-party material may have a legal status different from the project's original writing and are not automatically relicensed under CC BY-SA 4.0 merely because they are cited or included.

Original executable tooling and helper scripts expressly covered by [`LICENSE-SOFTWARE.md`](LICENSE-SOFTWARE.md) are licensed under the MIT License. By submitting code intended for those covered files and allowing it to be merged, you agree that the contribution may be distributed under that software license unless different terms are clearly identified and accepted before merge.
