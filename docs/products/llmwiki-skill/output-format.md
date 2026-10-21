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
    title: Skill's OKF v0.2 authoring guide
  - id: layout
    resource: references/layout-and-examples.txt
    title: Index and log examples
---
# LLMWiki layout and OKF format

## Bundle boundaries

`docs/` is a collection of product bundles, not one large OKF bundle. Each `docs/products/<slug>/` directory has its own root, identity space, and local dependencies. The collection index is outside those bundles. Product filenames and subdirectories are producer choices, rather than a fixed OKF topic taxonomy.[^skill]

## Concepts and metadata

Every Markdown file inside a bundle is a concept except the reserved filenames `index.md` and `log.md`, which are reserved at every level. A concept needs parseable YAML frontmatter and a nonempty `type`. Titles, descriptions, tags, provenance, and lifecycle information are optional format fields, though they can make the wiki more useful. Unknown types and extra fields must be preserved.[^okf]

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

Markdown source copies placed in `references/` still need valid concept frontmatter. Alternatively, preserve raw source text in a non-Markdown asset, such as `.txt`, and describe it in a source-inventory concept. This product uses that second pattern.[^okf]

## Sources, footnotes, and trust

Each `sources` entry needs a `resource`. A stable `id` joins a claim's Markdown footnote label to its source; a corresponding footnote definition explains the reference. Footnotes may appear literally in viewers without footnote support. Keep source IDs stable when rearranging the list.[^okf]

Generation and verification are separate. If `generated` is present, it needs an accurate producer identity in `by`; `at` records a meaningful content change. `verified` records confirmation events and can be a list or a single mapping. A format check is not human verification of the content. Do not invent identities, dates, or verification events.[^okf]

`status` can be draft, stable, or deprecated; omission means stable. `stale_after` is an absolute datetime, not a duration. Timestamp-valued metadata uses ISO 8601 datetimes with explicit offsets. Staleness should prompt review rather than automatic deletion.[^okf]

## Paths and navigation

Relative links resolve from the containing document. For example, a concept at the product root can reference `references/skill.txt`, while `references/source-records.md` uses `./skill.txt` for that same file. This bundle uses relative paths for navigation and source metadata so ordinary Markdown viewers can resolve them.

OKF also supports leading-slash paths interpreted from the bundle root. They require that OKF interpretation; ordinary Markdown viewers can interpret them differently. The installed skill's examples use that supported form, while this bundle follows the user's relative-link preference.[^okf]

Indices use headings and descriptive links. Only the bundle-root index may carry the version frontmatter `okf_version: "0.2"`; nested indices have no frontmatter. Logs group entries under `YYYY-MM-DD` headings, newest first. The format makes indices and logs optional, while this skill maintains them for navigation and history.[^okf][^layout]

## Specialized concepts

An Attested Computation is a separate concept with `type: Attested Computation` and a required `runtime`. The authoring reference describes parameters, inline/file computations, executors, and deterministic attesters. Maintaining such documentation does not authorize running the computation or rewriting its sanctioned definition.[^okf]

[^skill]: Bundled skill instructions distinguishing the collection from product bundles.
[^okf]: Bundled OKF authoring guide; these notes document the skill's targeted v0.2 behavior.
[^layout]: Bundled layout examples for navigation and date-grouped history.
