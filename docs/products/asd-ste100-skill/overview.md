---
type: Product Overview
title: ASD-STE100 skill overview
description: Purpose, task scope, and documentation structure.
sources:
  - id: skill
    resource: references/skill.txt
    title: ASD-STE100 skill instructions
---
# ASD-STE100 skill overview

The wiki product `asd-set100-skill` documents the installed skill named `asd-ste100`. The standard and invocation name use **STE**, for Simplified Technical English. The skill targets **ASD-STE100 Issue 9, January 2025**; it does not silently substitute a different edition.[^skill]

## Purpose and scope

The skill helps a model draft, revise, or review English technical documentation, and answer specific rule or vocabulary questions. It distinguishes procedural writing, descriptive writing, and safety instructions. It preserves technical meaning while applying the supplied rules and dictionary; it is not intended for generic simplification or unrelated writing.[^skill]

The product consists of instructions, a complete rule checklist, detailed rule extracts, a dictionary interpretation guide, an indexed dictionary, and a Python lookup utility with regression tests. The utility retrieves evidence. It does not analyze an entire document's grammar or certify compliance.[^skill]

## Documentation structure

This bundle follows the DocLang skill documentation's organization, adapting its extraction and format topics to technical writing:

| Documentation theme | Coverage here |
|---|---|
| Purpose and supported tasks | This overview |
| Installation layout, prerequisites, example requests | [Setup and usage](setup-and-usage.md) |
| Skill execution | [Writing and review workflow](writing-workflow.md) |
| Output and reference interpretation | [Rules and dictionary](rules-and-dictionary.md) |
| Automated verification and verification environment | [Verification](verification.md) |
| Model/tool limits and troubleshooting | [Limits and troubleshooting](limits-and-troubleshooting.md) |
| Provenance and maintenance | [Source records](references/source-records.md) |

The DocLang product supplies the section pattern only; none of its extraction behavior or test results applies here. This documentation is independently readable from its local references. Running dictionary queries still requires the installed skill and its full dictionary, as explained in setup and usage.

[^skill]: Bundled snapshot of the ASD-STE100 SKILL.md.
