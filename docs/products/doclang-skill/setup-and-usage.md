---
type: User Guide
title: DocLang skill setup and usage
description: Skill files, prerequisites, invocation examples, and checker commands.
sources:
  - id: skill
    resource: /references/skill.txt
    title: DocLang skill instructions
  - id: checker
    resource: /references/checker.py.txt
    title: Bundled structural checker source
  - id: inventory
    resource: /references/source-records.md
    title: Inspected skill file inventory and project registration
---
# DocLang skill setup and usage

## Files and prerequisites

The inspected project stores the skill under `.agents/skills/doclang/`. Its Claude Code entry, `.claude/skills/doclang`, is a relative symlink to the same directory. The skill's name remains `doclang`; `doclang-skill` is the wiki product name.[^inventory]

```text
doclang/
  SKILL.md
  agents/openai.yaml
  references/syntax.md
  references/examples.md
  scripts/check_doclang.py
  scripts/test_check_doclang.py
```

The host needs access to the image pixels or reliable OCR, adequate context for the selected references and input, and sufficient output allowance for the resulting XML. Python is used for the bundled checker; its implementation uses only the standard library. The skill itself does not require MLX-VLM, an LM Studio server, a particular model provider, or Apple Silicon.[^skill][^checker]

## Example requests

With the skill available to the coding agent, attach or identify the images and request, for example:

> Use $doclang to convert the attached scanned page to output.dclg. Preserve the wording, reading order, and visible structure.

For multiple pages, state the order if filenames or attachment order do not establish it. For XML-only output, request raw XML explicitly. Ask for coordinates only when they serve the task; the skill can omit geometry when measurements are unreliable.[^skill]

The original PDF specification is not loaded by default. The agent reads the relevant parts of `references/syntax.md` and consults corresponding examples. This keeps routine context use focused.[^skill]

## Structural check

From a project root with the skill installed in the inspected location:

```sh
python3 .agents/skills/doclang/scripts/check_doclang.py output.dclg
```

For a different installation, substitute the actual skill directory. This command checks an existing XML file; it does not perform image extraction or write corrected XML. The checker reads UTF-8 input. It exits with `0` when its checks pass, `1` for structural errors, or `2` for input/argument errors. Structural diagnostics go to standard error.[^checker]

These commands refer to an installed skill, not to executable files in this documentation bundle. The bundle retains source text for inspection; see [source records](/references/source-records.md).

## Output handling

Use `.dclg` for the skill's normal file workflow. The checker accepts a file path without enforcing an extension. Output naming, persistence, and overwrite protection belong to the host application; the skill does not supply a file-publishing implementation.[^skill][^checker]

[^skill]: Bundled skill instructions, including inspection, serialization, and verification.
[^checker]: Bundled check_doclang.py source, including its command-line entry point.
[^inventory]: Source inventory inspected when this bundle was created.
