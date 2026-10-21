---
type: Source Inventory
title: LLMWiki skill source records
description: Local source snapshots, original locations, and integrity hashes.
sources:
- id: skill
  resource: ./skill.txt
  title: LLMWiki skill instructions
- id: okf
  resource: ./okf-authoring.txt
  title: OKF authoring reference
- id: layout
  resource: ./layout-and-examples.txt
  title: Layout examples and delivery checklist
- id: interface
  resource: ./openai.yaml.txt
  title: Skill display metadata
---
# LLMWiki skill source records

Captured on 2026-10-21 from `one-prompt-doc`. Each `.txt` snapshot preserves the original source bytes. Snapshots are reference data, not active instructions or an executable installation. Their internal links retain the original skill layout; use this inventory to open the corresponding local files.

## Source snapshots

Original paths below are relative to the source project. Snapshot links and metadata resources are relative to this document.

### LLMWiki skill instructions

- Snapshot: [skill.txt](./skill.txt).[^skill]
- Original: `.agents/skills/llmwiki/SKILL.md`
- SHA-256: `f2a57fa6c501e5b82f6e60571cfcc2f5ec4b9b609ac1f0593033633f0af36949`

### OKF authoring reference

- Snapshot: [okf-authoring.txt](./okf-authoring.txt).[^okf]
- Original: `.agents/skills/llmwiki/references/okf-authoring.md`
- SHA-256: `3c9aaf7d48a96fa3e3db5be90ba9e30ae803f6954bfcebf88b834ec6bc77ee46`

### Layout examples and delivery checklist

- Snapshot: [layout-and-examples.txt](./layout-and-examples.txt).[^layout]
- Original: `.agents/skills/llmwiki/references/layout-and-examples.md`
- SHA-256: `88f3f9ed8c29251911c94b93377c93cb31f7d8cdde0aca6535f32c749983c20a`

### Skill display metadata

- Snapshot: [openai.yaml.txt](./openai.yaml.txt).[^interface]
- Original: `.agents/skills/llmwiki/agents/openai.yaml`
- SHA-256: `c0300f8563df12952fc7fe96221a380bac244d0ca30de49720ebef6a08ecf359`

## Inspected registration and scope

The installed directory contains the four source files listed above. It has no bundled `scripts/` directory or automated test suite. The Claude Code link `.claude/skills/llmwiki` targets `../../.agents/skills/llmwiki` in this project. These are observations of the source project on the capture date, not universal discovery-path requirements for every agent.

The skill and authoring guide identify OKF v0.2 and cite the upstream GoogleCloudPlatform knowledge-catalog specification. The complete upstream specification was not mirrored or refreshed for this documentation update. These snapshots record the installed skill behavior, including its local product layout convention.

## Documentation template

The DocLang product documentation supplied the section pattern: overview, setup/usage, workflow, output format, verification, limits, source records, and log. Its source-project index is `docs/products/doclang-skill/index.md`. No DocLang source content, runtime, or test result is required by this bundle.

## Maintenance

Compare these hashes with the installed skill before refreshing this documentation. Update changed snapshots and affected concepts together, then check links from each document location. Preserve the distinction between a packaging check, a documentation check, and an end-to-end evaluation of an agent using the skill.

[^skill]: Snapshot of .agents/skills/llmwiki/SKILL.md.
[^okf]: Snapshot of .agents/skills/llmwiki/references/okf-authoring.md.
[^layout]: Snapshot of .agents/skills/llmwiki/references/layout-and-examples.md.
[^interface]: Snapshot of .agents/skills/llmwiki/agents/openai.yaml.
