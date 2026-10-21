---
type: Reference Guide
title: ASD-STE100 rules and dictionary
description: Writing-rule coverage, vocabulary interpretation, and lookup output.
sources:
  - id: rules
    resource: references/rules.txt
    title: Issue 9 rule checklist
  - id: guide
    resource: references/dictionary-guide.txt
    title: Dictionary interpretation and data provenance
  - id: lookup
    resource: references/lookup_dictionary.py.txt
    title: Lookup output implementation
  - id: examples
    resource: references/lookup-examples.json
    title: Captured dictionary command outputs
---
# ASD-STE100 rules and dictionary

## Writing-rule coverage

The skill covers nine sections. The table provides orientation; the local extracts contain the detailed conditions and examples.[^rules]

| Section | Main coverage | Detailed reference |
|---|---|---|
| 1. Words | Approved vocabulary, meaning, part of speech, technical nouns/verbs, spelling | [Words](references/rules/01-words.txt) |
| 2. Multi-word nouns | Noun length and clarification of longer technical nouns | [Multi-word nouns](references/rules/02-multi-word-nouns.txt) |
| 3. Verbs | Permitted forms, tenses, and active voice | [Verbs](references/rules/03-verbs.txt) |
| 4. Sentences | Clear structure, lists, connectors, articles | [Sentences](references/rules/04-sentences.txt) |
| 5. Procedural writing | Commands, conditions, sentence length, notes | [Procedural writing](references/rules/05-procedural-writing.txt) |
| 6. Descriptive writing | Gradual explanation, sentence and paragraph structure | [Descriptive writing](references/rules/06-descriptive-writing.txt) |
| 7. Safety instructions | Risk identification, command/condition, consequence | [Safety instructions](references/rules/07-safety-instructions.txt) |
| 8. Punctuation and word count | Permitted punctuation and STE counting conventions | [Punctuation and counting](references/rules/08-punctuation-and-word-count.txt) |
| 9. Writing practices | Restructuring, appropriate vocabulary, consistency, recommendations | [Writing practices](references/rules/09-writing-practices.txt) |

Procedural sentences have a maximum of 20 words; descriptive sentences have a maximum of 25. Descriptive paragraphs have one topic and no more than six sentences. These limits require STE counting conventions: a whitespace count is insufficient. Section 8 treats, for example, numbers with units, qualifying identifiers, quoted text, parenthesized text, and hyphenated words specially. The active-voice rule allows a descriptive passive only when the agent is unknown. Read the detailed sections before applying exceptions.[^rules]

## Dictionary interpretation

Approval attaches to a word, its part of speech, its meaning, and its permitted form. Uppercase source headwords indicate approved entries; they do not instruct the writer to uppercase ordinary prose. Read the complete entry, including restrictions and examples. Suggested alternatives are not unconditional replacements.[^guide]

Countable plurals require inspection of the singular entry and any restrictions. Explicit aliases retrieve listed forms, but the utility performs no general stemming or grammatical analysis. Check multi-word expressions as well as individual words. A missing entry or a non-approved entry can require technical-term analysis rather than an automatic pass/fail.[^guide]

## Retrieval output

Exact mode returns a JSON array with one result per retained query. Each result has `query`, `status`, and `entries`. The status is `found` or `unresolved`. Entries include `word`, `part_of_speech`, `approved`, `aliases`, and `excerpts`; each excerpt retains its printed page, physical PDF page, and source text. Search mode returns `status: index_only`, `total_matches`, `truncated`, and up to 20 concise `matches` per query.[^lookup][^guide]

The documented commands produced these observations on 2026-10-21. Their full evidence is in the [captured outputs](references/lookup-examples.json).[^examples]

| Query | Observed result |
|---|---|
| `check` | Both an approved noun entry and a non-approved verb entry |
| `make sure` | Approved verb entry found |
| `removed` | Alias retrieves the approved `REMOVE` verb entry |
| `--pos v test` | Non-approved verb entry found |
| `--search accord` | One index match; full entry still needed for interpretation |
| `unlisted-project-widget` | `unresolved`, with an empty entries array |

These are retrieval observations, not approval of every possible sentence containing the queried words.

## Dataset counts

The dictionary guide reports 2,196 extracted word-and-part-of-speech records: 878 marked approved and 1,318 marked non-approved. The source introduction reports 875 approved and 1,274 non-approved words. The guide explicitly identifies these as different counts and does not claim they have been reconciled. Do not equate an extraction-record count with the source's word total.[^guide]

[^rules]: Bundled Issue 9 checklist; detailed source sections are linked in the table.
[^guide]: Bundled dictionary guide, including record structure and count discrepancies.
[^lookup]: Bundled Python lookup implementation.
[^examples]: Captured outputs from actual commands run while preparing this documentation.
