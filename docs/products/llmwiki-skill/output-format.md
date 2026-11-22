---
type: Format Reference
title: LLMWiki layout and OKF format
description: Bundle boundaries, concept metadata, references, navigation, and history.
sources:
  - id: skill
    resource: references/skill.txt
    title: Product layout convention
  - id: okf
    resource: references/okf-authoring.txt
    title: Skill's OKF v0.3 authoring guide
  - id: layout
    resource: references/layout-and-examples.txt
    title: Index and log examples
generated:
  by: process:llmwiki-documentation-refresh
  at: "2026-11-22T11:09:48Z"
---
# LLMWiki layout and OKF format

## Bundle boundaries

`docs/` is a collection of product bundles, not one large OKF bundle. Each `docs/products/<slug>/` directory has its own root, identity space, and local dependencies. The collection index is outside those bundles. Product filenames and subdirectories are producer choices, rather than a fixed OKF topic taxonomy.[^skill]

## Concepts and metadata

A non-reserved Markdown file is a concept when its frontmatter has a nonempty string `type`. Markdown without frontmatter or without `type` is ordinary documentation, not a concept; validators warn without making the bundle non-conformant. The filenames `index.md` and `log.md` are reserved at every level and are never concepts. Non-Markdown files are assets. Dot-prefixed files and directories are outside the bundle.[^okf]

Frontmatter must start on the first line with exactly `---`, end at the next exact `---` line, and parse as a YAML 1.2 core-schema mapping. Do not duplicate keys or use custom YAML tags. Quote timestamps and values that resemble numbers or booleans, and avoid re-serializing unchanged values. Any frontmatter in ordinary Markdown must also parse as a mapping. Preserve unknown types and keys at all nesting levels; prefer `x-<producer>-<name>` for new custom keys. The body uses CommonMark, GFM tables, and footnotes, with no universally required headings.[^okf]

A minimal illustrative concept is:

```markdown
---
type: Concept
title: Example subject
description: A concise description of the subject.
---
# Example subject

Replace this illustrative body with supported knowledge before adding a real concept.
```

An imported Markdown source can remain ordinary documentation without being converted into a concept. This product keeps its source snapshots as `.txt` assets to preserve their original bytes and distinguish them from authored concepts. The [source inventory](references/source-records.md) maps those snapshots to the installed files.[^okf]

## Sources, footnotes, and trust

Each `sources` entry needs a `resource`. A stable `id` joins a claim's Markdown footnote label to its source; a corresponding footnote definition explains the reference. Footnotes may appear literally in viewers without footnote support. Keep source IDs stable when rearranging the list.[^okf]

Generation and verification are separate. If `generated` is present, it needs an accurate producer identity in `by`; `at` records the last meaningful content change. Formatting, whitespace, and link repairs do not advance it. Each `verified` event needs `by` and `at`; a single mapping is accepted as a one-item list. Only events at or after `generated.at`, or events when `generated` is absent, establish the current trust tier. Earlier events remain history. No current event means unverified; current nonhuman events mean machine-confirmed; a current `human:` event means human-reviewed. A format check is not factual or human verification.[^okf]

Actors use `<producer>/<version>` or `<scheme>:<identity>`, including `human:`, `team:`, and `process:`. Only `human:` establishes human-reviewed trust; a team name does not identify an individual reviewer. Do not invent identities, dates, or verification events.[^okf]

`status` can be draft, stable, or deprecated; omission means stable. Preserve unknown status values and exclude them from filters to current knowledge. For a deprecated concept with a known replacement, use `superseded_by`; retain a deprecated stub at the old path when renaming.[^okf]

Timestamp fields accept RFC 3339 datetimes with offsets or dates interpreted as midnight UTC. Prefer datetimes for generation and verification comparisons. A datetime without an offset is invalid. Only `stale_after` determines freshness: it is an absolute instant, not a duration, and a nonempty value that cannot be parsed must never count as fresh. Staleness prompts review rather than deletion; omit an unknown review date.[^okf]

Nulls, empty strings, and empty lists in optional fields are treated as absent. A single item is accepted where a list is expected, including tags, sources, verification events, and parameters. A scalar tag containing commas is one tag, not several. Ignore incomplete family entries and report them without rejecting the bundle.[^okf]

## Paths and navigation

Relative links resolve from the containing document. For example, a concept at the product root can reference `references/skill.txt`, while `references/source-records.md` uses `./skill.txt` for that same file. This bundle uses relative paths for navigation and source metadata so ordinary Markdown viewers can resolve them.

OKF also supports leading-slash paths interpreted from the bundle root. The skill prefers relative body links for GitHub rendering and `/`-rooted metadata paths for clarity, but both forms are valid and existing working links are preserved. This documentation bundle retains its existing relative-link convention. Percent-encode spaces and reserved characters, respect path case, and do not read local targets outside the bundle. Standard inline and reference-style Markdown links are supported; `[[wikilinks]]` are not OKF links.[^okf]

These resolution rules apply to `resource`, `sources[].resource`, `computation`, `executor.resource`, `attester.resource`, and `superseded_by`; a path-valued bundle license follows them too. A source resource can instead describe a population or scope. A path field resolving to a concept forms a graph edge. For v0.2, earlier, or unversioned input only, an unresolved metadata path without `/` may be retried from the bundle root.[^okf]

Indices use headings and descriptive links. Only the bundle-root index may have frontmatter, including `okf_version: "0.3"`, title, description, license, and extension keys. Preserve it during navigation updates; it does not apply to individual concepts. Nested indices and logs have no frontmatter. Logs group entries under `YYYY-MM-DD` headings, newest first. Indices and logs are optional under OKF, while this skill maintains them for discovery and history.[^okf][^layout]

## Specialized concepts

An Attested Computation is a separate concept with `type: Attested Computation` and required `runtime`. Parameters require name and type; `required` defaults to false. The computation comes from the `computation` file path when present, otherwise the first fenced code block in a section headed `Computation` at any ATX heading level. Prefer one definition. Missing content is not attestable, and a value must not be labeled attested without runtime, a deterministic attester, and successful run evidence. Maintaining documentation does not authorize executing or rewriting its sanctioned computation.[^okf]

[^skill]: Bundled skill instructions distinguishing the collection from product bundles.
[^okf]: Bundled OKF v0.3 authoring guide and compatibility rules.
[^layout]: Bundled layout examples for navigation and date-grouped history.
