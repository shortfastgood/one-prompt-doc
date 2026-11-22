---
type: Verification Guide
title: LLMWiki skill verification
description: Validator scope, the 17-test result, documentation checks, and behavioral review scenarios.
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
  - id: okf
    resource: references/okf-authoring.txt
    title: Validation requirements and limitations
  - id: validator
    resource: references/validator/validate.py.txt
    title: Bundled validator implementation
  - id: tests
    resource: references/validator/tests/test_validate.py.txt
    title: Validator regression suite
  - id: run
    resource: references/verification-run.txt
    title: Captured 2026-11-22 validator test and skill packaging run
generated:
  by: process:llmwiki-documentation-refresh
  at: "2026-11-22T11:09:48Z"
---
# LLMWiki skill verification

## Available validation

The installed skill includes `scripts/validate.py`, its bundled pure-Python YAML parser, and `scripts/tests/test_validate.py`. Run it with Python 3.9+; no pip package or LibYAML installation is required. It checks OKF v0.3 structure and field shapes, including duplicate YAML keys, concept classification, reserved files, provenance references, lifecycle metadata, computation contracts, and supported local paths.[^skill][^validator][^inventory]

The loader uses YAML 1.2 core scalar resolution and preserves multiline scalar endings. Errors identify conformance failures, warnings identify issues such as non-concept Markdown or malformed fields, and informational findings include stale content and verifications older than generation. `--strict` fails on warnings as well as errors. An intentional ordinary Markdown file may therefore fail strict mode while the bundle remains conformant.[^validator][^okf]

The checker is not a complete Markdown parser or dependency audit. Separately review reference-style links, images, footnote definitions, navigation, and all dependencies needed for product delivery. Passing it does not verify factual accuracy, execute computations, or establish human review. For an older declared format, consult that version's rules rather than treating this checker as proof of conformance.[^okf][^layout]

## Run the regression suite

From the project root:

```bash
python3 -S -B -m unittest discover -s .agents/skills/llmwiki/scripts/tests -v
```

The suite has 17 tests. They cover execution with site-packages disabled, read-only bundle handling, nested and flow YAML, quoted and multiline values, aliases, YAML 1.2 scalar types, duplicate and malformed input, non-concept warnings, reserved files, freshness and verification dates, path resolution, legacy fallback, deprecation, source attribution, computation headings, hidden paths, escaping symlinks, and missing bundle errors. They test the validator implementation, not an end-to-end agent invocation.[^tests][^run]

## Verification performed for this update

| Item | Observation |
|---|---|
| Date | 2026-11-22, Europe/Zurich |
| Source project | `one-prompt-doc` |
| Python | 3.9.6 |
| Validator regression suite | 17 tests passed with `-S -B`; captured output is included in the bundle |
| Skill packaging check | Existing skill-creator `quick_validate.py` reported “Skill is valid!” |
| Packaging check scope | Skill metadata and packaging checks, not an end-to-end behavior test |
| Documentation checks | Strict v0.3 validation of 9 Markdown files; 0 errors, 0 warnings; local paths, source footnotes, and snapshot hashes checked separately |
| Model benchmark or agent scenario suite | Not run |
| Product export artifact | Not requested or created |

The [captured run](references/verification-run.txt) records the test command, Python version, packaging command, output, and successful exit. The packaging validator belongs to local skill-authoring tooling; the OKF validator and its tests are bundled with LLMWiki. This update does not certify every future agent invocation or other wiki products.[^run]

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
| Meaning changed after a human review | Retain the old event as history and report the reduced current trust tier. |
| Renamed v0.3 concept | Retain a deprecated stub at the old path with `superseded_by`. |
| Missing local link | Report it separately from basic OKF validity. |
| Export depending on a sibling product | Resolve required dependencies locally or report incomplete delivery. |
| Escaping symlink | Exclude it from a claimed standalone package; do not dereference it into the delivery. |

[^skill]: Bundled skill instructions for classification, preservation, maintenance, and verification.
[^layout]: Bundled standalone-product delivery checklist.
[^inventory]: Current source inventory of instructions, references, validator, tests, parser modules, and licenses.
[^okf]: Bundled authoring guide's validation and compatibility sections.
[^validator]: Captured bundled validator source, including local YAML and path adaptations.
[^tests]: Captured validator regression tests.
[^run]: Captured test and packaging-check output from 2026-11-22.
