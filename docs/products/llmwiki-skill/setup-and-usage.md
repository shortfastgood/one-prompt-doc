---
type: User Guide
title: LLMWiki skill setup and usage
description: Skill files, Python requirements, validator commands, and product selection.
sources:
  - id: skill
    resource: references/skill.txt
    title: Skill invocation and classification workflow
  - id: inventory
    resource: references/source-records.md
    title: Inspected skill files and project registration
  - id: okf
    resource: references/okf-authoring.txt
    title: Bundled validator usage and compatibility guidance
  - id: validator
    resource: references/validator/validate.py.txt
    title: Validator command-line interface
generated:
  by: process:llmwiki-documentation-refresh
  at: "2026-11-22T11:09:48Z"
---
# LLMWiki skill setup and usage

## Files and prerequisites

The inspected project installs the skill at `.agents/skills/llmwiki/`. The Claude Code entry `.claude/skills/llmwiki` is a relative symlink to the same directory. The invocation name is `llmwiki`; `llmwiki-skill` is this wiki product's name.[^inventory]

```text
llmwiki/
  SKILL.md
  agents/openai.yaml
  references/
    okf-authoring.md
    layout-and-examples.md
  scripts/
    validate.py
    LICENSE.okf
    tests/test_validate.py
    _vendor/
      __init__.py
      NOTICE.md
      pyyaml/                 # bundled loading modules and MIT license
```

The host needs to read project instructions and source material, edit Markdown/files within its permissions, and inspect paths. Automated validation requires Python 3.9 or later. No pip package, compiled extension, or LibYAML installation is needed. Keep `scripts/_vendor/` beside `validate.py`; copying only the entry script omits its bundled parser. The skill has no command-line wiki initializer.[^skill][^inventory][^okf]

## Run the validator

From the project root, validate one product bundle, not the collection's `docs/` directory:

```bash
python3 .agents/skills/llmwiki/scripts/validate.py docs/products/llmwiki-skill --json
python3 .agents/skills/llmwiki/scripts/validate.py docs/products/llmwiki-skill --strict
```

Substitute the actual skill location and selected bundle. `--json` returns structured findings. `--strict` makes warnings fail the command as well as errors. `--now` accepts a timestamp for reproducible freshness checks. Exit codes are 0 for a pass, 1 for validation errors or strict-mode warnings, and 2 for usage/setup errors. A passing check does not establish factual accuracy or complete product delivery. See [verification](verification.md) for coverage and limits.[^okf][^validator]

If Python is unavailable, check the declared format's rules manually and report that limitation. The v0.3 checker is not proof of v0.2 conformance.[^okf]

## Select the project and wiki

The target is the project the user specifies, not the skill's installation directory. The default is `<project>/docs`. An explicit wiki-path override or an established existing location takes precedence. Read applicable project instructions and inspect existing navigation before writing.[^skill]

Example requests:

> Use $llmwiki to initialize this project's wiki.

> Use $llmwiki to add this documentation to the wiki. The product name is example-product.

> Use $llmwiki to add these general notes to Library.

> Use $llmwiki to update the existing installation concept for example-product from the attached source.

> Use $llmwiki to package example-product as a standalone directory at the specified destination.

## Product classification

Before assigning new knowledge, the skill asks whether it belongs to a product or Library and, if applicable, which product. A product selection already given for the current request or batch answers that question. Pure initialization requires no classification question. An explicit update to an existing concept inherits that concept's product.[^skill]

For mixed input, obtain assignments for its distinct parts. If no answer has been supplied, do not silently assign it to Library. Product slugs use lowercase ASCII letters, digits, and hyphens; `library` is reserved. A name collision requires disambiguation rather than merging unrelated products.[^skill]

## Results

The agent reports the wiki location, selected product, changed files, checks performed, and unresolved questions. File creation does not itself authorize publication, transmission, code execution, or a Git commit.[^skill]

[^skill]: Bundled skill instructions for discovery, classification, initialization, verification, and delivery.
[^inventory]: Source inventory observed when this documentation was prepared.
[^okf]: Bundled authoring guide's validation and compatibility sections.
[^validator]: Captured validator argument handling and exit-code behavior.
