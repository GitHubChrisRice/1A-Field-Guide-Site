---
title: Registry Indoor Common-Space Hardening — Four Pilot Facilities
jurisdiction: California
last_verified: 2026-09-23
status: current-registry-method
---

# Registry Indoor Common-Space Hardening — Four Pilot Facilities

## Purpose

This pass applies the project's [Indoor Public Common Spaces](../california/indoor-public-common-spaces.md) doctrine to the four existing Registry pilots.

The objective is to keep three questions separate:

1. **Forum classification** — what constitutional forum category best fits the indoor area?
2. **Privacy/confidentiality responsibility** — what duties remain with the facility, and what duties actually apply to a visitor?
3. **Recording restriction** — what rule, if any, actually limits recording, and has that rule been constitutionally tested?

The project does not infer:

`sensitive information may exist → visitor is responsible for protecting it → recording prohibited`

That chain is invalid without additional legal authority.

## Registry data added

Indoor public/common subareas may now carry an `indoor_common_space` record containing:

- space type;
- privacy context;
- HIPAA posture;
- facility responsibility;
- visitor responsibility;
- recording effect; and
- supporting authority IDs.

Generated facility pages display this separately from forum classification and from Constitution First restriction status.

## Pilot results

### Concord Library

Hardened indoor areas:

- **Ordinary lobby, stacks, reading and service areas** — general shared interior.
- **Self-Service Sunday interior** — purpose-limited interior with conditioned access.

Current privacy posture:

- routine patron/account/screen information may be present;
- HIPAA is **not indicated** by the current facility record;
- the library retains responsibility for safeguarding records and systems subject to laws/policies applicable to the library;
- a lawful visitor does not inherit those confidentiality duties merely by being present;
- privacy concerns can support targeted restrictions, but no general patron-camera prohibition has been established in the current record.

### Walnut Creek Library

Hardened indoor areas:

- **Ordinary lobby, stacks, reading and service areas** — general shared interior.
- **Garage stairs, elevators and connective corridors** — shared public circulation.

Current privacy posture:

- routine patron/account information may be present in the ordinary interior;
- no special privacy risk was identified in the garage circulation record;
- HIPAA is **not indicated**;
- no general patron-camera prohibition is established by the current record;
- any later claimed restriction must be tied to a real privacy/operational interest and tested under the governing forum standard.

### Concord DMV

Hardened indoor areas:

- **Ordinary lobby / waiting** — waiting area.
- **Customer service counters / transaction zones** — public service counter.

Current privacy posture:

- identity, driver, transaction, and system information may be present;
- confidential interaction risk is stronger at the counter than in the waiting area generally;
- HIPAA is **not indicated**;
- DMV remains responsible for safeguarding agency records and systems under law/policy applicable to DMV;
- ordinary visitors do not become custodians of DMV information merely by entering the public lobby;
- a counter-level privacy interest can support a narrower restriction without establishing a branch-wide camera ban.

The knowledge-test device rule remains separately classified as an **activity-specific rule**. It is not generalized to the lobby.

### Concord Police Headquarters

Hardened indoor areas:

- **Ordinary public lobby / Community Service Desk** — lobby.
- **Records counter** — public service counter.

Current privacy posture:

- victim/witness information, protected records, screens, reports, and confidential interactions may be present;
- the records counter presents a stronger privacy context than the lobby generally;
- HIPAA is **not indicated** by the current police-facility record;
- the department retains responsibility for safeguarding protected records and secure operations;
- a lawful visitor does not become the department's confidentiality agent by entering the lobby;
- privacy does not erase the strong officer-recording authorities identified in the record;
- any recording restriction must track the actual protected information/interaction and survive the applicable constitutional analysis.

## HIPAA status of these pilots

None of these four pilot facilities has been established in the Registry as a HIPAA covered-entity context.

Accordingly, the new `hipaa_posture` field is set to `NOT_INDICATED` for the hardened subareas.

That field exists because future facilities—public health clinics, county hospitals, behavioral-health offices, and similar sites—may require a direct HIPAA analysis.

The project will not label a facility `COVERED_ENTITY_CONTEXT` merely because employees use the word "HIPAA."

## Constitution First rule

For indoor privacy disputes, the Registry now preserves this sequence:

`lawful public access → forum → recording/other protected activity → actual exposed information → facility safeguard duty → visitor duty under law that applies directly → claimed restriction → constitutional test → enforcement authority`

A facility's information-security problem is not automatically converted into a citizen's First Amendment restriction.

## What remains unresolved

This hardening pass does not claim:

- that every visible record may lawfully be recorded or published;
- that California Penal Code § 632 can never apply in a public-access interior;
- that every privacy-based camera restriction is invalid;
- that a public-access lobby creates access to employee workspaces or secure areas;
- that the California Speech Clause treatment of the DMV or police lobby is now resolved; or
- that a field visit is unnecessary for current signs, acoustic/privacy layout, screen orientation, counter geometry, or restricted-door boundaries.

Those remain separate, fact-specific issues.
