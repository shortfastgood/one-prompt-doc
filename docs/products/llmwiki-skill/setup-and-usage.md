---
type: User Guide
title: LLMWiki skill setup and usage
description: Skill files, project selection, classification, and example requests.
sources:
  - id: skill
    resource: references/skill.txt
    title: Skill invocation and classification workflow
  - id: inventory
    resource: references/source-records.md
    title: Inspected skill files and project registration
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
```

The host needs to read project instructions and source material, edit Markdown/files within its permissions, and inspect paths. A YAML parser is useful for validation when available; the skill does not require a particular language or install dependencies automatically. It does not include a command-line initializer or validator.[^skill][^inventory]

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
