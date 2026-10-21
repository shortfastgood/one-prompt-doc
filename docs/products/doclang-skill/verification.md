---
type: Verification Guide
title: DocLang skill verification
description: Automated checks, visual regression guidance, and recorded verification environment.
sources:
  - id: tests
    resource: /references/checker-tests.py.txt
    title: Existing checker regression tests
  - id: checker
    resource: /references/checker.py.txt
    title: Structural checker implementation
  - id: skill
    resource: /references/skill.txt
    title: Required source-image comparison
  - id: readme
    resource: /references/extraction-readme.txt
    title: Historical application verification reported in the template README
---
# DocLang skill verification

## Automated verification

From the project root with the skill installed:

```sh
python3 -B -m unittest discover \
  -s .agents/skills/doclang/scripts -p 'test_check_doclang.py' -v
```

The existing suite contains 10 tests. It checks nine XML teaching examples and exercises XML/document boundaries, property ordering, coordinate bounds, tables, lists, field scopes, thread references, chart-class requirements, and rejection of unsupported core constructs. It uses the bundled checker and Python's standard library, without a vision model or GPU.[^tests][^checker]

## Verification environment and result

The following was directly observed while preparing this documentation, rather than copied from the template's historical results:

| Item | Observed value |
|---|---|
| Verification date | 2026-10-21, Europe/Zurich |
| Working project | `one-prompt-doc` |
| Interpreter | `python3`, Python 3.9.6 |
| Command | The unittest command above |
| Result | 10 tests ran; all passed |
| Model inference | Not run for this documentation update |
| Official XSD/Schematron validation | Not run |

This records checker regression coverage, not factual verification of every statement or a model-quality benchmark. The source hashes in [source records](/references/source-records.md) identify the inspected implementation and tests.

## Image comparison and structure regression

For an extraction, compare the generated document against the actual image after structural validation. Check exact wording and punctuation, reading order, heading levels, group boundaries, table dimensions/merges, field associations, checkbox states, captions, and omitted or invented material.[^skill]

The supplied README includes a CV-specific regression with explicit expectations for heading levels, employment and education groups, and list membership. Those counts describe one fixture, not rules for arbitrary CVs or documents. A suitable future regression should derive its expectations from its own source image.[^readme]

For the README's CV example, hierarchy checks passed while a punctuation transcription error remained. That is historical evidence reported by the application documentation, not a new model run or an accuracy guarantee for this skill.[^readme]

## Application tests are separate

The README reports MLX-VLM CLI tests and model runs on a specified machine and model revision. It also warns that the CLI test file retained a former module import after a directory move. This wiki update did not change or rerun that application suite. Its model-call, hardware, memory, and timing results should not be attributed to the reusable skill.[^readme]

[^tests]: Bundled snapshot of test_check_doclang.py.
[^checker]: Bundled checker source; it is a limited structural check.
[^skill]: Bundled skill's region-by-region visual verification requirements.
[^readme]: Bundled README snapshot; application-specific results are historical reports only.
