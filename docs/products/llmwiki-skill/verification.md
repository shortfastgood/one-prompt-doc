---
type: Verification Guide
title: LLMWiki skill verification
description: Structural checks, observed validation, and behavioral review scenarios.
sources:
  - id: skill
    resource: references/skill.txt
    title: Required verification and delivery checks
  - id: layout
    resource: references/layout-and-examples.txt
    title: Standalone delivery checks
  - id: inventory
    resource: references/source-records.md
    title: Inspected files and source integrity records
---
# LLMWiki skill verification

## Available validation

The installed skill has no bundled executable or automated regression suite. Its verification procedure asks the host to use available tools and review the relevant OKF rules. Do not reuse the DocLang template's checker commands or test counts for this product.[^skill][^inventory]

For changed concepts, parse YAML when a parser is available and check required frontmatter, reserved filenames, navigation entries, source/footnote correspondence, date-grouped history, and local reference targets. Preserve optional and unfamiliar metadata. For delivery, inspect the complete product and all required dependencies rather than only the changed pages.[^skill][^layout]

## Verification performed for this update

| Item | Observation |
|---|---|
| Date | 2026-10-21, Europe/Zurich |
| Source project | `one-prompt-doc` |
| Skill packaging check | Existing skill-creator `quick_validate.py` reported “Skill is valid!” |
| Packaging check scope | Skill metadata and packaging checks, not an end-to-end behavior test |
| Documentation checks | YAML parsing, concept/index/log structure, relative local paths, source footnotes, and snapshot hashes |
| Model benchmark or agent scenario suite | Not run |
| Product export artifact | Not requested or created |

The packaging validator belongs to the local skill-authoring tooling, not to LLMWiki. This documentation update checks its own bundle; it does not establish that every future agent invocation will follow all instructions or certify all existing wiki products.

## Behavioral review scenarios

The following expectations come from the skill and are useful when evaluating it. They are a review checklist, not newly executed automated tests.[^skill][^layout]

| Scenario | Expected behavior |
|---|---|
| Empty project | Create only collection and Library root indices. |
| Repeated initialization | Leave existing initialized content unchanged. |
| Unassigned new knowledge | Ask product-or-Library classification and wait. |
| Explicit product or existing-concept update | Use the supplied or inherited product without asking again. |
| Existing unrelated documentation | Preserve it; resolve path or migration conflicts before restructuring. |
| Updated concept | Reconcile content, preserve unknown metadata, update affected navigation/history. |
| Missing local link | Report it separately from basic OKF validity. |
| Export depending on a sibling product | Resolve required dependencies locally or report incomplete delivery. |
| Escaping symlink | Exclude it from a claimed standalone package; do not dereference it into the delivery. |

[^skill]: Bundled skill instructions for classification, preservation, maintenance, and verification.
[^layout]: Bundled standalone-product delivery checklist.
[^inventory]: Captured inventory establishing that the installed skill contains instructions and references only.
