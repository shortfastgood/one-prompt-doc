---
type: Source Inventory
title: ASD-STE100 skill source records
description: Source snapshots, original paths, integrity hashes, and captured run
  evidence.
sources:
- id: skill
  resource: ./skill.txt
  title: Skill instructions
- id: rules
  resource: ./rules.txt
  title: Complete rule checklist
- id: guide
  resource: ./dictionary-guide.txt
  title: Dictionary interpretation guide
- id: lookup
  resource: ./lookup_dictionary.py.txt
  title: Dictionary lookup implementation
- id: tests
  resource: ./test_lookup_dictionary.py.txt
  title: Dictionary regression tests
- id: interface
  resource: ./openai.yaml.txt
  title: Skill display metadata
- id: notice
  resource: ./source-notice.txt
  title: Preserved source notice
- id: rule-01
  resource: ./rules/01-words.txt
  title: Detailed rule section 01
- id: rule-02
  resource: ./rules/02-multi-word-nouns.txt
  title: Detailed rule section 02
- id: rule-03
  resource: ./rules/03-verbs.txt
  title: Detailed rule section 03
- id: rule-04
  resource: ./rules/04-sentences.txt
  title: Detailed rule section 04
- id: rule-05
  resource: ./rules/05-procedural-writing.txt
  title: Detailed rule section 05
- id: rule-06
  resource: ./rules/06-descriptive-writing.txt
  title: Detailed rule section 06
- id: rule-07
  resource: ./rules/07-safety-instructions.txt
  title: Detailed rule section 07
- id: rule-08
  resource: ./rules/08-punctuation-and-word-count.txt
  title: Detailed rule section 08
- id: rule-09
  resource: ./rules/09-writing-practices.txt
  title: Detailed rule section 09
- id: run
  resource: ./verification-run.txt
  title: Captured verification run
- id: examples
  resource: ./lookup-examples.json
  title: Captured dictionary command outputs
- id: inventory
  resource: ./dictionary-inventory.json
  title: Dictionary fingerprint and observed counts
---
# ASD-STE100 skill source records

Captured on 2026-10-21 from `one-prompt-doc`. Source snapshots preserve the original bytes, with Markdown and Python source stored as `.txt` evidence. They are reference material, not active agent instructions or executable installation files. Their internal relative links retain the original skill layout; use the inventory below to find the corresponding local snapshot.

## Source snapshots and evidence

Original source paths are relative to the source project. Every snapshot link and frontmatter resource below is relative to this document.

### Skill instructions

- Snapshot: [skill.txt](./skill.txt).[^skill]
- Original: `.agents/skills/asd-ste100/SKILL.md`
- SHA-256: `c676f682b701da3c098715845c5c3dc5a61c32fc5872af5ea9d6aa9f5e4a3081`

### Complete rule checklist

- Snapshot: [rules.txt](./rules.txt).[^rules]
- Original: `.agents/skills/asd-ste100/references/rules.md`
- SHA-256: `5e31488f5cd7ce6608199c8e73ce93da5052345980506d90d0339fae753b0b6f`

### Dictionary interpretation guide

- Snapshot: [dictionary-guide.txt](./dictionary-guide.txt).[^guide]
- Original: `.agents/skills/asd-ste100/references/dictionary-guide.md`
- SHA-256: `2b075cdaf90faa7d5313254ffca7381a15340d920d099028d62b59590a32ce4f`

### Dictionary lookup implementation

- Snapshot: [lookup_dictionary.py.txt](./lookup_dictionary.py.txt).[^lookup]
- Original: `.agents/skills/asd-ste100/scripts/lookup_dictionary.py`
- SHA-256: `f8b520337a5e603a6a7c68faf05cd5f260aac9799c76a6143108fda301484073`

### Dictionary regression tests

- Snapshot: [test_lookup_dictionary.py.txt](./test_lookup_dictionary.py.txt).[^tests]
- Original: `.agents/skills/asd-ste100/scripts/test_lookup_dictionary.py`
- SHA-256: `c7391d46196bdfeb3b0f4212ea3f0b1aa72fa8f83cdb422bb739139cb945c60d`

### Skill display metadata

- Snapshot: [openai.yaml.txt](./openai.yaml.txt).[^interface]
- Original: `.agents/skills/asd-ste100/agents/openai.yaml`
- SHA-256: `ca6fcd895e541b8af8be37132f17d1b16c78e3fa48fce607c7b2d07b3eaa87d1`

### Preserved source notice

- Snapshot: [source-notice.txt](./source-notice.txt).[^notice]
- Original: `.agents/skills/asd-ste100/references/source-notice.txt`
- SHA-256: `8495724c3c8668bb60ac8a3da343263eb4ef82ba5990bfc3a41cc4808c87d63a`

### Detailed rule section 01

- Snapshot: [rules/01-words.txt](./rules/01-words.txt).[^rule-01]
- Original: `.agents/skills/asd-ste100/references/rules/01-words.md`
- SHA-256: `1bf89e7f515829e2e0fbc36786450ea53781f342f906751f38468ea5b57141ea`

### Detailed rule section 02

- Snapshot: [rules/02-multi-word-nouns.txt](./rules/02-multi-word-nouns.txt).[^rule-02]
- Original: `.agents/skills/asd-ste100/references/rules/02-multi-word-nouns.md`
- SHA-256: `95ed581c0b6bea4d8035827efe40fdb723e88365fbfe1099cab4b2c950c4aaa1`

### Detailed rule section 03

- Snapshot: [rules/03-verbs.txt](./rules/03-verbs.txt).[^rule-03]
- Original: `.agents/skills/asd-ste100/references/rules/03-verbs.md`
- SHA-256: `a30718761fb5913c954f577e154823570bc836fd910e32b2ce36108ebd75c79e`

### Detailed rule section 04

- Snapshot: [rules/04-sentences.txt](./rules/04-sentences.txt).[^rule-04]
- Original: `.agents/skills/asd-ste100/references/rules/04-sentences.md`
- SHA-256: `a14a668ddc4b5af3d678f7ba99dc2fd668e4918419f3ebb5f4a87384b00fbfc5`

### Detailed rule section 05

- Snapshot: [rules/05-procedural-writing.txt](./rules/05-procedural-writing.txt).[^rule-05]
- Original: `.agents/skills/asd-ste100/references/rules/05-procedural-writing.md`
- SHA-256: `f1705f370971d418ae4e18a7950d538b8c8e954fd75fd2ab8657d1a4479ebcac`

### Detailed rule section 06

- Snapshot: [rules/06-descriptive-writing.txt](./rules/06-descriptive-writing.txt).[^rule-06]
- Original: `.agents/skills/asd-ste100/references/rules/06-descriptive-writing.md`
- SHA-256: `399d40140562a03905aa04631e0055e70940fd08942a502d6592c3be29c40f4b`

### Detailed rule section 07

- Snapshot: [rules/07-safety-instructions.txt](./rules/07-safety-instructions.txt).[^rule-07]
- Original: `.agents/skills/asd-ste100/references/rules/07-safety-instructions.md`
- SHA-256: `562a2807f31bb9ef4504c38e9d0b5d3d8026d0caca0bfe02b195c031291785ce`

### Detailed rule section 08

- Snapshot: [rules/08-punctuation-and-word-count.txt](./rules/08-punctuation-and-word-count.txt).[^rule-08]
- Original: `.agents/skills/asd-ste100/references/rules/08-punctuation-and-word-count.md`
- SHA-256: `14f054d263120ab6afbc1d088e223822fd7a8265538601c9f0d18c4f33c6a44e`

### Detailed rule section 09

- Snapshot: [rules/09-writing-practices.txt](./rules/09-writing-practices.txt).[^rule-09]
- Original: `.agents/skills/asd-ste100/references/rules/09-writing-practices.md`
- SHA-256: `5707a658e86269a3e687575912f5389e2e6ffc8a0870246e4a1edcc48368530a`

### Captured verification run

- Snapshot: [verification-run.txt](./verification-run.txt).[^run]
- Origin: Generated during this documentation update.
- SHA-256: `95d607eaa4f02c636a899d6a922e9c393d2f7335d462c6bb8ffcaf4e40315f9e`

### Captured dictionary command outputs

- Snapshot: [lookup-examples.json](./lookup-examples.json).[^examples]
- Origin: Generated during this documentation update.
- SHA-256: `91543e0068bb922dd963b763cf43c3564d58cfe66f8c6535ef176e6976bd59f5`

### Dictionary fingerprint and observed counts

- Snapshot: [dictionary-inventory.json](./dictionary-inventory.json).[^inventory]
- Origin: Generated during this documentation update.
- SHA-256: `85e3d2b2584d53a7a07c9d39e6421db1381f65fa5317b409024c91fc3b1c1013`

## Installed skill and source boundaries

The inspected project contains `.agents/skills/asd-ste100/`. The Claude Code link `.claude/skills/asd-ste100` targets `../../.agents/skills/asd-ste100`. The skill is named `asd-ste100`; the wiki product is named `asd-set100-skill` as requested.

The full `dictionary.jsonl` is not duplicated into this documentation. Its hash, byte length, and directly observed counts are recorded in the local dictionary inventory. The lookup source and test source snapshots depend on that dataset when used as executable code; this bundle documents their behavior rather than installing them.

The installed references identify the user-supplied ASD-STE100 Issue 9 PDF as their original source. The PDF was not re-read for this update and is not included. Its preserved notice accompanies the extracts; source notices remain reference data, separate from repository code licensing.

## Documentation template

The DocLang skill documentation supplied the section pattern: overview, setup/usage, workflow, format/reference details, verification, limits, and source records. No DocLang content, model results, or skill runtime is required to read this product bundle. Its template index was `docs/products/doclang-skill/index.md` in the source project.

## Maintenance

Compare the recorded hashes with the installed source files before refreshing this documentation. Update affected concepts and snapshots together, and record a new test run when claiming new verification. Keep historical verification dates and dataset counts distinct from a new observation.

[^skill]: Skill instructions; source path or generated origin and integrity hash are recorded above.
[^rules]: Complete rule checklist; source path or generated origin and integrity hash are recorded above.
[^guide]: Dictionary interpretation guide; source path or generated origin and integrity hash are recorded above.
[^lookup]: Dictionary lookup implementation; source path or generated origin and integrity hash are recorded above.
[^tests]: Dictionary regression tests; source path or generated origin and integrity hash are recorded above.
[^interface]: Skill display metadata; source path or generated origin and integrity hash are recorded above.
[^notice]: Preserved source notice; source path or generated origin and integrity hash are recorded above.
[^rule-01]: Detailed rule section 01; source path or generated origin and integrity hash are recorded above.
[^rule-02]: Detailed rule section 02; source path or generated origin and integrity hash are recorded above.
[^rule-03]: Detailed rule section 03; source path or generated origin and integrity hash are recorded above.
[^rule-04]: Detailed rule section 04; source path or generated origin and integrity hash are recorded above.
[^rule-05]: Detailed rule section 05; source path or generated origin and integrity hash are recorded above.
[^rule-06]: Detailed rule section 06; source path or generated origin and integrity hash are recorded above.
[^rule-07]: Detailed rule section 07; source path or generated origin and integrity hash are recorded above.
[^rule-08]: Detailed rule section 08; source path or generated origin and integrity hash are recorded above.
[^rule-09]: Detailed rule section 09; source path or generated origin and integrity hash are recorded above.
[^run]: Captured verification run; source path or generated origin and integrity hash are recorded above.
[^examples]: Captured dictionary command outputs; source path or generated origin and integrity hash are recorded above.
[^inventory]: Dictionary fingerprint and observed counts; source path or generated origin and integrity hash are recorded above.
