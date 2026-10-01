---
title: CA-GATE-08 Canonical Standing Scenario Review
jurisdiction: California
review_date: 2026-09-29
status: activation-control-review
control: CA-GATE-08
---

# CA-GATE-08 — Canonical Standing Scenario Review

Issue: #80

## Question

Can the California overlay run the project's standing scenario without importing California-specific law into the national factual baseline?

## Result

**Provisionally met.**

The new canonical source is:

- `docs/national-core/standing-scenario.md`
- ID: `NC-STANDING-01`
- version: `v1`

California now uses:

- `docs/california/standing-scenario.md`

as a jurisdiction overlay/crosswalk rather than as the source of national facts.

This review does not activate California and does not satisfy the independent-human/bootstrap or activation-decision controls.

---

# 1. National baseline contamination check

The canonical national file was reviewed for jurisdiction-specific contamination.

No references were found to:

- California;
- the California Penal Code;
- the California Government Code;
- the Brown Act;
- Ninth Circuit doctrine; or
- California-specific case law.

The national file contains only:

- jurisdiction-neutral starting facts;
- allegation-to-elements methodology;
- identification as a separate legal question;
- lawful-vantage factual assumptions;
- complaint-driven, public-meeting, and emergency/assembly factual variants;
- changed-fact restart rules; and
- the requirement that jurisdiction overlays supply the actual law.

The file does **not** declare that:

- recording is lawful everywhere;
- a person may ignore a later removal order;
- identification can never be required;
- everything visible may always be recorded;
- peaceful observer status creates immunity from valid dispersal/perimeter law; or
- the absence of assumed misconduct prevents later changed facts from creating an offense.

---

# 2. California overlay separation

The California standing page was rewritten as an overlay.

It now:

- explicitly inherits `NC-STANDING-01 v1`;
- maps neutral facts to California Penal Code and Brown Act branches;
- keeps California identification doctrine in California;
- keeps Ninth Circuit recording/police-encounter authority in California;
- preserves the California allegation-to-elements workflow;
- preserves California-specific complaint-driven and lawful-vantage consequences;
- preserves the California public-meeting variant;
- preserves the California assembly/emergency variant; and
- keeps later removal orders as new legal facts rather than retroactive trespass.

The California overlay expressly states:

> National core supplies the facts. California supplies the law.

---

# 3. Existing canonical scenarios now inherit the same baseline

The two existing national scenarios now expressly inherit `NC-STANDING-01 v1`:

- `NC-COMPLAINT-01 v2`
- `NC-VANTAGE-01 v1`

Neither scenario changes version because this change does not alter its branch questions or jurisdictional legal rules; it identifies the common factual source they already presupposed.

If a later national scenario changes a standing fact, that change must be explicit in that scenario.

---

# 4. California qualification-matrix rerun

The matrix was rechecked after canonicalization.

Result remains:

- **69 Supported**
- **4 Researched-Unresolved**
- **0 Gap**
- **0 Not Applicable**

No branch status changed merely because the common facts moved to national core.

The four Researched-Unresolved rows remain:

- `CA-F4.5`
- `CA-F5.8`
- `NC-COMPLAINT-01.D`
- `NC-COMPLAINT-01.I`

Canonicalization did not convert any unresolved legal question into a fact and did not hide any unresolved branch.

---

# 5. Functional-family cross-check

The national standing baseline remains compatible with every required qualification family.

## Lawful presence / area classification

The baseline assumes initial lawful presence only. It leaves later access changes, hours, restricted areas, forum status, screening, and removal authority to the jurisdiction overlay.

## Protected activity / recording

The baseline describes peaceful information gathering as conduct being analyzed, not as a universal legal conclusion. California still supplies recording/privacy/audio/forum doctrine.

## Government restrictions

The baseline does not decide whether a restriction, sign, order, or conditional-access demand is valid. California must still test source, authority, constitutional validity, delegation, and preemption.

## Trespass / removal

The baseline does not decide later refusal/remain/reentry law. California still supplies §§602/602.1 and prospective-exclusion doctrine.

## Police encounters

The baseline does not create a nationwide no-ID rule, no-detention rule, or no-search rule. California/Ninth Circuit doctrine remains necessary.

## Disorder / obstruction

The baseline excludes invented misconduct at the starting point but explicitly restarts analysis if conduct changes. California still supplies §415, §148, §602.1, §422, and related law.

## Meetings / assemblies / emergency scenes

The national facts do not import Brown Act, California dispersal, or California perimeter rules. Those remain overlay questions.

## Records / remedies / methodology

The standing scenario does not import California CPRA or remedy rules.

---

# 6. Changed-fact failure-point test

The following examples were checked to ensure canonicalization did not create hidden legal conclusions.

### Employee says "stop recording or leave"

Result: new fact. National baseline does not decide legality. California overlay routes to restriction/exclusion authority, forum analysis, and derivative-trespass doctrine.

### Police say "you are detained"

Result: new fact. National baseline does not decide reasonable suspicion. California/Ninth Circuit encounter doctrine applies.

### Officer demands ID

Result: national baseline only says ID possession is not assumed. It does not answer legal duty. California identification doctrine applies.

### Public hours end

Result: changed access fact. Initial lawful presence does not persist by assumption.

### Dispersal warning is issued

Result: changed fact. Warning validity/audibility/opportunity and California §§407–409 are separately tested.

### Meeting chair warns/removes speaker

Result: changed fact. California Brown Act / meeting doctrine applies.

### Auditor begins blocking, threatening, shouting over business, or physically interfering

Result: standing assumptions no longer control that conduct. The relevant offense/restriction branch must be rerun.

---

# 7. Gate disposition

**CA-GATE-08 → Provisionally Met**

Reason:

1. a complete jurisdiction-neutral standing baseline now exists;
2. California-specific law has been moved into a California overlay;
3. national scenarios inherit the neutral baseline;
4. matrix statuses remain intact after rerun; and
5. no California-specific legal conclusion is required to understand the national starting facts.

Remaining activation controls after this change:

- CA-GATE-02 — final/adversarial qualification review;
- CA-GATE-09 — independent qualified human review or documented Founder/bootstrap exception;
- CA-GATE-10 — authorized human activation decision.

CA-GATE-04 through CA-GATE-07 remain provisionally supported and should be stress-tested during CA-GATE-02.
