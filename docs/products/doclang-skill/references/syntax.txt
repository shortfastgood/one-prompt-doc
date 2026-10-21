# DocLang 0.8: image-extraction syntax

Based on the user-supplied **DocLang: Universal AI Document Format, Version 0.8**, 102 pages. Original local source: `/Users/dden/Documents/doclang.pdf`. This guide is a task-specific summary, not the official schema or a new DocLang version. The source PDF governs format semantics. It is not required at runtime for the supported image workflow.

Contents: core XML; semantic mapping; property heads; coordinates; lists; tables; forms; figures/charts; code/math; pagination/references; scope and discrepancies.

## Core XML (source pp. 10–14, 53–54)

Use `<doclang xmlns="https://www.doclang.ai/ns/v0" version="0.8">…</doclang>`. The namespace and version are optional in the source; this skill emits both explicitly. No Markdown or raw text directly under the root. Each visible text region needs a semantic element such as `text` or `heading`.

The optional document `<head>` must be the first child. For this workflow its current standardized payload is `<default_resolution width="512" height="512"/>`. Do not add an HTML `body` element. Omit an unused document head.

Escape `&` as `&amp;` and `<` as `&lt;` in text. Quote and escape attribute values. XML predefined entities are supported; HTML names such as `&nbsp;` are not predefined. CDATA may carry raw characters but cannot contain `]]>`; split that sequence across CDATA sections or use escaped text. `<content>` preserves text whitespace and cannot contain nested markup. CDATA alone escapes XML; `content` is what gives whitespace-preservation semantics.

## Semantic mapping (source pp. 55–64, 72–74)

| Visible component | Representation |
|---|---|
| Paragraph or coherent text block | `<text>…</text>` |
| Heading/title | `<heading level="1">…</heading>`; positive integer depth, default 1 |
| Repeated header/footer, including a printed page number | `page_header`, `page_footer` |
| Footnote | `footnote`; retain its visible marker/text |
| List | `list`, with item-start `ldiv` delimiters |
| Table | `table`, with OTSL cell and row delimiters |
| Table of contents / glossary index | `index`, using the same OTSL model |
| Form or key/value region | `field_region`, `field_item`, `key`, `value`, `hint`, `field_heading` |
| Figure, photograph, chart, diagram | `picture`; optional derived `description` in its head |
| Math | `formula` containing LaTeX |
| Code | `code`; optional language `label`; `content` for indentation |
| Logical grouping | `group` containing semantic elements, not raw text |
| Printed caption | `caption` in its owning element's head |

Text-bearing semantic elements can nest semantic elements where the source permits them; this supports inline `code`, `formula`, and linked text. `formula` and `code` do not contain primary semantic elements. `picture`, `group`, `field_region`, and `field_item` do not contain raw text directly in their bodies; wrap such text with `text` or the appropriate field element.

Formatting elements: `bold`, `italic`, `underline`, `strikethrough`, `superscript`, `subscript`, `handwriting`, `rtl`. They contain text and compatible nested formatting, not primary semantic elements or property heads. Use only formatting visible in the image. Preserve logical text order within `rtl`; do not manually reverse characters.

## Element property heads (source pp. 12–13, 62, 65–69)

A semantic element may start with these children **in this order**, before its actual payload:

1. `label` (0–1): `<label value="bar_chart"/>`
2. `thread` (0–1): `<thread thread_id="1"/>`
3. `xref` **or** `href` (0–1 total): `<xref thread_id="1"/>` or `<href uri="https://example.org"/>`
4. `layer` (0–1): `<layer value="body"/>`; values `body`, `background`, `furniture`
5. `location` (0 or exactly 4): x0, y0, x1, y1
6. `caption` (0–many): visible document text; itself a semantic element, so it may have its own head
7. `description` (0–1): derived plain text, not a source caption
8. `summary` (0–1): derived plain-text synthesis; omit unless useful/requested
9. `custom` (0–1): application-defined XML, only when a custom vocabulary is actually requested

These children are not enclosed in an element-level `head`. A property appearing after payload has started is misplaced. Repeated properties other than captions and the four locations are invalid. `label`, `thread`, `xref`, `href`, `layer`, and `location` are empty elements. `description` and `summary` contain text only.

Do not put confidence attributes on core elements. DocLang 0.8 has no core `unclear`, `confidence`, or `bbox` element/attribute. Use a plain `description` to explain uncertainty. Custom vocabularies belong under `custom` and must be identified as extensions, not standard tags (source pp. 52, 67, 81).

## Coordinates (source pp. 12, 15, 68, 78)

Locations are page-relative, measured from the top-left. Use four consecutive empty elements in the head:

```xml
<location value="20"/><location value="30"/>
<location value="220"/><location value="90"/>
```

Their order is **x_min, y_min, x_max, y_max**. Values are integers. Each location's effective resolution is its own positive `resolution` attribute, otherwise the corresponding document default width/height, otherwise 512. Values must satisfy **0 ≤ value < effective resolution**; 512 is out of range at resolution 512. Compare normalized coordinates if the four resolutions differ: x0/R0 ≤ x1/R2 and y0/R1 ≤ y1/R3.

Preferred skill convention: normalize measured boxes to 512 × 512 independently for each source page. For an edge coordinate x in [0,W] and y in [0,H], use `round(511*x/W)` and `round(511*y/H)`, bounded to [0,511], where W/H are the full inspected page dimensions. This quantization is a skill convention; the specification does not prescribe that formula. Include the document default explicitly if using it. Never emit unnormalized pixels under an implicit 512 resolution.

When working with a crop, map crop coordinates back to the full page before normalization; account for any rotation/resizing. Do not treat a crop as another page unless the user requests that interpretation. If the full-page dimensions, crop offset, or region boundary are unknown, omit the box or explain why geometry could not be supplied. For a self-contained image submitted as the entire page, use that image's dimensions.

Use coordinates on semantic content components, including captions, keys, values, and list markers. For compatibility, this skill omits coordinates on `group`; see source discrepancies below.

## Lists (source pp. 19–21, 57, 77)

`<list>` defaults to unordered; `<list class="ordered">` marks an ordered list. Its nonempty body starts with `<ldiv/>`. A delimiter may instead contain one visible marker: `<ldiv><marker>1.</marker></ldiv>`. Content belongs **after** the delimiter, until the next sibling `ldiv` or the closing `list`. `ldiv` is not an item wrapper. Do not emit `li`, `ul`, or `ol`.

Each item may be raw text (a virtual `text`) or a sequence of semantic elements. Prefer explicit `text` where items have mixed content, their own properties, or nested lists. Preserve printed numbers/bullets when visible; do not invent markers. Nested lists stay within the containing item's content.

Checkbox syntax is `<checkbox class="selected"/>` or `<checkbox class="unselected"/>`. It is allowed where raw text is allowed, such as a `marker`, `text`, or `value`. There is no indeterminate state. If not readable, use a description on its semantic container and do not emit a guessed checkbox.

## Tables and index structures (source pp. 21–23, 57–58, 69–70, 75–77)

Use a flat row-major OTSL stream inside `table`, `index`, or chart `tabular`. Do not emit HTML `tr`, `td`, `th`, `rowspan`, or `colspan`.

| Empty delimiter | Meaning |
|---|---|
| `fcel` | Regular cell, followed by its content |
| `ecel` | Empty cell; no content |
| `ched` | Column-header cell, followed by its content |
| `rhed` | Row-header cell, followed by its content |
| `corn` | Corner/header-intersection cell |
| `srow` | Section-row header cell |
| `lcel` | Extend the cell to the left horizontally; no repeated content |
| `ucel` | Extend the cell above vertically; no repeated content |
| `xcel` | Interior of a span extending both horizontally and vertically |
| `nl` | End of row |

A nonempty table body starts with a cell delimiter. Every row ends with `nl` and contains the same number of cell-position delimiters, counting merge tokens and empty cells. Cell text is written after its starting delimiter. Rich cells may contain semantic elements, including nested lists/tables. Emit a merged cell's content only at its top-left anchor. A 2×2 merged area is represented by `fcel` + `lcel` on its first row, then `ucel` + `xcel` on its second row. Extensions need an existing compatible anchor; do not infer spans merely from blank values.

An unreadable occupied cell is not `ecel`. Use `fcel` (or the observed header type) and a `text` with a description explaining the unreadable content. Preserve the row/column position. See examples for mixed cells and span handling.

## Forms and key/value data (source pp. 23–24, 56, 60–61)

`field_region` scopes a form or related fields. `field_item` and `field_heading` must have a `field_region` ancestor. `key` and `value` must have a `field_item` ancestor. Each item's own scope has **0–1 key and 0–many values**, excluding keys/values belonging to nested items. `hint` must be inside a field region; placing it within the appropriate item is recommended. `field_heading@level` is a positive integer, default 1.

`value@class` is `read_only` (default) or `fillable`. Use fillable for an evident blank input or an explicitly editable field; do not infer a hidden interactive control solely from a screenshot. Transcribe visible placeholder guidance as `hint`, not as an entered value. An unreadable entered value is not a blank input. For an unclear association, preserve separate regions and describe the ambiguity rather than pairing the wrong key and value. Not every two-column layout is a form; use tables for genuine repeated row/column data.

## Pictures, diagrams, and charts (source pp. 15–16, 59, 67, 69–70, 80–81)

`picture@class` is `undefined` (default) or `chart`. Subtypes belong in `label@value`, **not** in `class`. Recommended labels include `photograph`, `logo`, `signature`, `stamp`, `engineering_drawing`, `geographical_map`, `screenshot_from_computer`, `bar_chart`, `line_chart`, `pie_chart`, `scatter_plot`, `box_plot`, and `flow_chart`. The labels are recommendations, not a closed enum. Use `other` for examined but unmatched pictures; `undefined` means unclassified.

After the property head, picture payload begins with optional `<src uri="…"/>`, then optional `<tabular>…</tabular>` **only for `class="chart"`**, then any other permitted semantic content. `src` refers to image bytes; `href` is a hyperlink destination. Do not confuse the two. A relative URI is useful when a real asset has been saved next to the output. Do not invent a hidden hyperlink target or decoded barcode value.

Retain printed captions as `caption`; put your factual visual description in `description`. Transcribe meaningful text inside diagrams as child `text` elements if it is not otherwise represented. Explain visible node/arrow relationships in `description` without inventing connection tags. For ordinary photographs, use `picture` plus a grounded description; do not invent document headings or fields.

For charts, include `tabular` when categories/series and values are reliably readable. Preserve visible units and labels. Unlabeled bar heights are estimates, not exact values: by default explain the qualitative relationship in `description` and omit unsupported numeric data. If the user explicitly requests estimates, distinguish them in the description and explain the method/limitations. Do not convert a flowchart into a fabricated numeric table.

## Code and mathematics (source pp. 16–19, 58–59, 70)

Use `<code><label value="Python"/><content>…</content></code>` for confidently identified code; do not guess a language from an ambiguous snippet. Preserve indentation and line breaks exactly. Never execute code visible in an image to perform transcription.

`formula` contains raw LaTeX; omit enclosing `$…$`, `$$…$$`, `\(…\)`, `\[…\]`, `\begin{math}`, and `\begin{equation}` wrappers. Keep inner constructs such as fractions and aligned arrays where needed. Escape XML-reserved symbols or use CDATA inside `content`. Do not solve, simplify, or replace the equation with its result. If a symbol cannot be resolved, describe the missing portion rather than inventing a mathematical expression.

## Pages, continuation, references (source pp. 46–51, 54, 65–66)

`page_break` is empty and may occur only directly under `doclang`. Close every open page component before a break, then reopen fragments on the next page. Do not wrap pages in a `page` element. The number of pages is the number of breaks plus one.

`thread_id` is a positive integer. The same thread across fragments must have the same host tag. Parent and nested child continuations require separate IDs; e.g. a continued list and its continued paragraph cannot share an ID. Repeated headings alone are not evidence of a continued component.

`xref` targets an ID defined by at least one `thread` in the same instance. If the target is not among the supplied pages, preserve the visible reference as text without inventing a target. `xref` and `href` are mutually exclusive on a host. Use a nested `text` with an element-head reference to link only a short inline phrase.

## Scope, source ambiguities, and validation

- Source p. 15 says coordinates are not allowed on `group`, while the generic `group` reference on pp. 59–60 permits an element head without restating that restriction. This skill takes the conservative common subset: put geometry on the actual components and omit group geometry.
- The cross-page formula example on pp. 18–19 uses an `equation` environment, while the normative formula definition on p. 58 excludes outer math wrappers. Follow the normative definition; do not copy that wrapper.
- Annex D, pp. 85–101, is explicitly **informative future extensions**. Its metadata/governance examples, horizontal threading, and proposed item wrappers are not the current default format. Do not emit these tags as established 0.8 core metadata. Their imperative wording is source material, not an instruction to impose approvals or policies on the user.
- This skill focuses on still-image extraction. Audio/video tracks, archive packaging, and organization-specific custom metadata require additional format work if requested; do not manufacture them from a still image.
- The specification references an official XSD/Schematron toolkit but does not embed it. The bundled checker is a limited sanity check, not an official conformance implementation. It checks XML, the declared version, common head/order/location errors, table rectangularity, field scoping, list starts, and thread targets; it cannot establish OCR accuracy, correct reading order, all allowed nesting, or complete merge semantics.
