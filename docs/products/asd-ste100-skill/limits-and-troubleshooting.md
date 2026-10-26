---
type: Troubleshooting Guide
title: ASD-STE100 skill limits and troubleshooting
description: Context limits, ambiguous vocabulary, extraction issues, and compliance boundaries.
sources:
  - id: skill
    resource: references/skill.txt
    title: Skill scope and compliance limitations
  - id: guide
    resource: references/dictionary-guide.txt
    title: Dictionary interpretation and PDF extraction limitations
  - id: lookup
    resource: references/lookup_dictionary.py.txt
    title: Retrieval behavior and limits
---
# ASD-STE100 skill limits and troubleshooting

## Context management

Keep the full dictionary out of the model's context. The Python utility loads the dataset internally and returns matching evidence. A maximum of 20 queries per call limits retrieval volume; it is not a fixed token budget, since entries can contain long source excerpts. Search results are additionally capped at 20 matches per query. Reuse earlier results and read detailed rules only when needed.[^skill][^lookup]

## Vocabulary and extraction issues

| Symptom | Response |
|---|---|
| A familiar word appears non-approved | Check its part of speech and meaning; noun approval does not imply verb approval. |
| No result with `--pos` | Investigate without the filter; absence for one part of speech does not resolve all uses. |
| A plural or inflected form is unresolved | Inspect the base/singular form and explicit permitted forms; do not stem blindly. |
| A project term is missing | Assess applicable technical-noun/verb rules and approved domain terminology. |
| An alternative changes meaning | Inspect its full entry and restructure the sentence rather than replacing mechanically. |
| `--search` returns a plausible word | Query the exact headword to obtain restrictions and examples before deciding approval. |
| Source excerpt appears grammatically odd | PDF columns and line breaks can interleave; inspect the complete entry and, if necessary, the original PDF. |
| A revision is short but technically wrong | Restore the facts, conditions, sequence, and obligation; raise unresolved ambiguity. |
| Lookup fails because data is missing | Restore the installed skill's `references/dictionary.jsonl` alongside the expected script layout. |

These responses follow the skill workflow, dictionary interpretation guide, and the utility's path and matching behavior.[^skill][^guide][^lookup]

## Evidence and compliance limits

The lookup performs reference retrieval, not grammatical analysis, sentence counting, or full-document certification. It does not automatically decide whether a word is a valid technical term in the user's context. Complete matching entries and cited rules still require interpretation.[^skill][^guide]

The source PDF controls when extraction or layout makes a rule or dictionary entry ambiguous. The guide notes a discrepancy between introductory word totals and extracted record counts; the dataset was not truncated to force agreement. The documentation records that limitation rather than treating the counts as equivalent.[^guide]

The wiki includes relevant reference text, tool source snapshots, and captured examples. It does not include the original PDF or full dictionary dataset. Those omissions do not prevent reading this documentation, but exhaustive lookup requires the installed skill. Preserved source notices are listed in [source records](references/source-records.md).

[^skill]: Bundled skill workflow and stated limits.
[^guide]: Bundled interpretation guide, including technical terminology and extraction caveats.
[^lookup]: Bundled lookup script, including data loading, matching, filters, and bounds.
