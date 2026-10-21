---
type: Product Overview
title: LLMWiki skill overview
description: Purpose, supported tasks, and documentation scope.
sources:
  - id: skill
    resource: references/skill.txt
    title: LLMWiki skill instructions
---
# LLMWiki skill overview

The product `llmwiki-skill` documents the reusable skill named `llmwiki`. It guides an agent to initialize and maintain a project-local knowledge wiki, add or revise knowledge, review the wiki structure, and package one product's knowledge independently. The default wiki location is the selected project's `docs/` directory.[^skill]

## Purpose and scope

Each product, including the virtual product **Library**, occupies its own Open Knowledge Format (OKF) bundle. Library holds general knowledge when the user selects it. It is not an automatic destination for knowledge whose owner is unknown. A product's required knowledge and assets stay within that product's bundle so other products need not be included in its delivery.[^skill]

The installed skill targets OKF v0.2. Its product directory arrangement is a local convention built around OKF bundles, not an additional requirement imposed by the format. It preserves existing documents and custom metadata rather than automatically converting every file in `docs/`.[^skill]

The skill supplies instructions and supporting references. It has no bundled executable, database, background synchronization service, or dedicated test suite. The host agent performs file operations and checks using its available tools; the inspected inventory is recorded in [source records](references/source-records.md).

## Documentation structure

This bundle follows the DocLang documentation's section pattern. The extraction workflow becomes wiki maintenance, and the output-format topic covers OKF layout and metadata. Setup, verification, limits, and source records retain their corresponding roles. No DocLang behavior or test result is attributed to LLMWiki.

Start with [setup and usage](setup-and-usage.md), then consult [wiki maintenance](wiki-workflow.md) and [layout and format](output-format.md). The supporting source snapshots are included locally, so this documentation can be delivered without the other wiki products.

[^skill]: Bundled snapshot of the installed LLMWiki SKILL.md.
