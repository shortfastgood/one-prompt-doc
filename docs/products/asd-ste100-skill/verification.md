---
type: Verification Guide
title: ASD-STE100 skill verification
description: Regression tests, observed results, and document-review checks.
sources:
  - id: tests
    resource: references/test_lookup_dictionary.py.txt
    title: Dictionary regression test source
  - id: run
    resource: references/verification-run.txt
    title: Captured test command and output
  - id: examples
    resource: references/lookup-examples.json
    title: Captured lookup command outputs
  - id: skill
    resource: references/skill.txt
    title: Document-review requirements and compliance boundary
---
# ASD-STE100 skill verification

## Automated verification

From the project root with the skill installed:

```sh
python3 -B -m unittest discover \
  -s .agents/skills/asd-ste100/scripts -p 'test_lookup_dictionary.py' -v
```

The nine existing tests cover part-of-speech-dependent approval, case and explicit forms, multi-word/qualified entries, line-wrapped headwords, unresolved words, bounded search, retained restrictions, record uniqueness/source evidence, and entries affected by nonsequential PDF text order. They use the real dictionary and Python's standard library.[^tests]

## Verification environment and result

| Item | Observed value |
|---|---|
| Verification date | 2026-10-21, Europe/Zurich |
| Working project | `one-prompt-doc` |
| Interpreter | `python3`, Python 3.9.6 |
| Result | 9 tests ran; all passed |
| Supporting evidence | Captured test output and source hashes |
| Separate model benchmark | Not run for this documentation update |
| Full-document STE assessment | Not performed by the test suite |

The recorded run is available as [verification-run.txt](references/verification-run.txt). The documented example commands were also executed successfully; their JSON results are retained locally. No result from the DocLang template was reused as verification of this product.[^run][^examples]

## Document review

For an actual writing task, compare the revision with its source and technical context. Check that facts, units, sequence, conditions, obligations, and hazard severity are unchanged. Review applicable rules, count words using STE conventions, and check vocabulary in context, including newly introduced terms and multi-word expressions. Track terminology across sections.[^skill]

Report findings with rule numbers or dictionary printed-page evidence. Separate confirmed problems from domain-dependent terms and unresolved questions. Passing the retrieval tests establishes behavior covered by those tests; it does not establish that a model's document is fully compliant.[^skill]

[^tests]: Bundled regression test source.
[^run]: Actual command, interpreter version, and output captured during this update.
[^examples]: Actual dictionary queries captured during this update.
[^skill]: Skill instructions for preserving meaning, reviewing rules, and qualifying conclusions.
