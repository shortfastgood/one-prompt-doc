---
type: User Guide
title: ASD-STE100 skill setup and usage
description: Installed files, prerequisites, invocation, and lookup commands.
sources:
  - id: skill
    resource: references/skill.txt
    title: Skill instructions and dictionary invocation
  - id: lookup
    resource: references/lookup_dictionary.py.txt
    title: Dictionary lookup implementation
  - id: inventory
    resource: references/source-records.md
    title: Inspected project registration and source inventory
---
# ASD-STE100 skill setup and usage

## Files and prerequisites

The inspected project installs the skill at `.agents/skills/asd-ste100/`. Its Claude Code entry, `.claude/skills/asd-ste100`, is a relative symlink to the same directory. The wiki product slug does not rename the installed skill.[^inventory]

```text
asd-ste100/
  SKILL.md
  agents/openai.yaml
  references/
    rules.md
    rules/                         # nine detailed rule sections
    dictionary-guide.md
    dictionary.jsonl
    source-notice.txt
  scripts/
    lookup_dictionary.py
    test_lookup_dictionary.py
```

The lookup utility uses Python 3's standard library and the dictionary at `references/dictionary.jsonl`, resolved relative to the script. It does not need the original PDF for normal queries. The host must make the skill files and the user's technical text available to the model. No model provider or GPU runtime is selected by this skill.[^skill][^lookup]

## Example requests

> Use $asd-ste100 to revise this maintenance procedure against ASD-STE100 Issue 9. Preserve the sequence, conditions, quantities, units, and hazard severity.

> Use $asd-ste100 to review this technical description. Identify confirmed findings with rule numbers or dictionary printed-page references, and list unresolved terminology separately.

> Use $asd-ste100 to investigate whether “test” is permitted as a verb in this sentence.

Supply relevant technical context, approved domain terminology, and any mandated wording. The skill asks for clarification when missing context materially affects a safe, accurate rewrite.[^skill]

## Dictionary commands

From the project root with the installed skill:

```sh
python3 .agents/skills/asd-ste100/scripts/lookup_dictionary.py 'check' 'make sure' 'removed'
python3 .agents/skills/asd-ste100/scripts/lookup_dictionary.py --pos v 'test'
python3 .agents/skills/asd-ste100/scripts/lookup_dictionary.py --search 'accord'
```

Use the actual installation path in another project. At most 20 query arguments are accepted per call. Quote multi-word expressions as one argument. The `--pos` choices are `n`, `v`, `adj`, `adv`, `prep`, `pron`, `conj`, `art`, and `prefix`. Search produces an index for discovery; retrieve a selected headword in exact mode before interpreting approval.[^lookup]

The utility prints JSON to standard output and does not change the input text or write a revised document. A normal unresolved lookup is a successful utility execution with `status: unresolved`, not a command failure. Invalid arguments produce an argparse error. There is no full-document lint or automatic rewrite command.[^lookup]

If Python is unavailable, the skill permits a targeted search for the exact `word` field and inspection of only the matching records. Do not load the full JSONL file into model context.[^skill]

These commands refer to an installed skill. The source snapshots in this wiki are for documentation and inspection, not an executable installation.

[^skill]: Bundled skill instructions, including context requirements and lookup fallback.
[^lookup]: Bundled lookup script source, including argument parsing and JSON output.
[^inventory]: Source locations and Claude Code registration inspected for this documentation.
