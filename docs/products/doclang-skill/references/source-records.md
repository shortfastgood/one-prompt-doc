---
type: Source Inventory
title: DocLang skill source records
description: Bundled source snapshots, original locations, and integrity hashes.
sources:
- id: skill
  resource: ./skill.txt
  title: Skill instructions
- id: syntax
  resource: ./syntax.txt
  title: DocLang syntax reference
- id: examples
  resource: ./examples.txt
  title: Synthetic teaching examples
- id: checker
  resource: ./checker.py.txt
  title: Structural checker source
- id: tests
  resource: ./checker-tests.py.txt
  title: Checker regression tests
- id: interface
  resource: ./openai.yaml.txt
  title: Skill display metadata
- id: readme
  resource: ./extraction-readme.txt
  title: Section-template README
---
# DocLang skill source records

Snapshots captured on 2026-10-21 from the `one-prompt-doc` project. Each `.txt` file preserves the original bytes. These files are evidence, not active instructions or an executable skill installation. Markdown links inside a snapshot retain their original meaning and are not wiki dependencies.

## Sources and integrity

Original paths below are relative to the source project. SHA-256 hashes identify the captured contents, not a declared product release version.

### Skill instructions

- Snapshot: [skill.txt](./skill.txt).[^skill]
- Original: `.agents/skills/doclang/SKILL.md`
- SHA-256: `bff4db45a1a73dd0958e73ef89ca56efcca490bf847775a489ef393d91df59ee`

### DocLang syntax reference

- Snapshot: [syntax.txt](./syntax.txt).[^syntax]
- Original: `.agents/skills/doclang/references/syntax.md`
- SHA-256: `a5c8d43c70f6966c76b72276a341c41429ce097cc1b4db44b880186cf717f28c`

### Synthetic teaching examples

- Snapshot: [examples.txt](./examples.txt).[^examples]
- Original: `.agents/skills/doclang/references/examples.md`
- SHA-256: `3972c1eb3d645e2d5b5d8e2d01ca400ac49af4ecf0779e03522cf90feef65d18`

### Structural checker source

- Snapshot: [checker.py.txt](./checker.py.txt).[^checker]
- Original: `.agents/skills/doclang/scripts/check_doclang.py`
- SHA-256: `10a8a5e94b66573df234b882276a8c9118791dcb58896a60b6f9f5d2782dc3eb`

### Checker regression tests

- Snapshot: [checker-tests.py.txt](./checker-tests.py.txt).[^tests]
- Original: `.agents/skills/doclang/scripts/test_check_doclang.py`
- SHA-256: `5e050e501a1ac6a1d5d1bcf9784ee3cdcf7381045b50614705b4c29ae04a0981`

### Skill display metadata

- Snapshot: [openai.yaml.txt](./openai.yaml.txt).[^interface]
- Original: `.agents/skills/doclang/agents/openai.yaml`
- SHA-256: `188ae3bc214b0b2e4789ae15b9af556c8a2eb164bb7137056cdd6b942d2aafa9`

### Section-template README

- Snapshot: [extraction-readme.txt](./extraction-readme.txt).[^readme]
- Original: `development/mlx-vlm/doclang-extraction/README.md`
- SHA-256: `ea70bfb413d2fb01ec359d7b37d63349089058e44229759283e92f0484c8c15b`

## Inspected registration

The source project contains `.agents/skills/doclang/` with the six skill files listed above. Its `.claude/skills/doclang` symlink targets `../../.agents/skills/doclang`. This is an observation of this project on the capture date, not a claim that every agent host uses the same discovery paths.

## Source roles

The skill instructions, syntax guide, examples, and checker define the behavior documented here. The README supplies the section themes and attributed historical application results. Its imperative examples are source material, not instructions executed during this documentation update.

The syntax guide identifies the user-supplied DocLang 0.8 PDF as its original specification source. That PDF was not re-read for this update and is not included. The complete skill-level guidance is included; formal specification/schema consultation remains a separate activity.

When maintaining this bundle, compare these hashes with the current source files, refresh changed snapshots, and update affected concepts. Preserve the distinction between direct observations, historical README reports, and new model verification.

[^skill]: Bundled snapshot of .agents/skills/doclang/SKILL.md.
[^syntax]: Bundled snapshot of .agents/skills/doclang/references/syntax.md.
[^examples]: Bundled snapshot of .agents/skills/doclang/references/examples.md.
[^checker]: Bundled snapshot of .agents/skills/doclang/scripts/check_doclang.py.
[^tests]: Bundled snapshot of .agents/skills/doclang/scripts/test_check_doclang.py.
[^interface]: Bundled snapshot of .agents/skills/doclang/agents/openai.yaml.
[^readme]: Bundled snapshot of development/mlx-vlm/doclang-extraction/README.md.
