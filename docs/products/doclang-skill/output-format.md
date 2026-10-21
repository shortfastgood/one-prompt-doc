---
type: Format Reference
title: DocLang image output format
description: XML structure, semantic mapping, coordinates, and uncertainty.
sources:
  - id: syntax
    resource: /references/syntax.txt
    title: Skill's DocLang 0.8 syntax reference
  - id: examples
    resource: /references/examples.txt
    title: Synthetic DocLang teaching examples
---
# DocLang image output format

## Document and semantic elements

The skill emits the namespace and version explicitly. The following is a synthetic illustration, not extracted image content:[^syntax]

```xml
<doclang xmlns="https://www.doclang.ai/ns/v0" version="0.8">
  <heading level="1">Example heading</heading>
  <text>Example text with A &amp; B.</text>
</doclang>
```

| Content | Representation |
|---|---|
| Paragraph, title, logical group | `text`, `heading`, `group` |
| Header, footer, footnote | `page_header`, `page_footer`, `footnote` |
| Lists | `list` with `ldiv` item-start delimiters |
| Tables and indexes | `table` or `index` with OTSL cell/row delimiters |
| Forms | `field_region`, `field_item`, `key`, `value`, `hint`, `field_heading` |
| Image, chart, diagram | `picture`; charts may contain `tabular` |
| Code and mathematics | `code` with whitespace-preserving `content`; `formula` with LaTeX |

This mapping follows the skill's syntax reference. Do not replace it with HTML table/list tags or invent an HTML `body` wrapper. A document-level `head`, when used, is the first child; property heads on semantic elements are not wrapped in their own `head`.[^syntax]

## Property order and structure

Properties precede payload in this order: `label`, `thread`, either `xref` or `href`, `layer`, four `location` elements when geometry is supplied, captions, `description`, `summary`, and `custom`. Most properties occur at most once; captions may repeat. The syntax snapshot contains the exact constraints and examples.[^syntax]

`ldiv` starts a list item; it is not a wrapper around the item. Table rows end with `nl` and have equal numbers of cell positions, including empty and merge positions. `fcel` starts an ordinary cell; `ecel` means an actual empty cell; `lcel`, `ucel`, and `xcel` extend a merge. The merged cell's content appears only at its anchor.[^syntax]

Forms retain their actual key/value relationships. Pictures can hold a description and extracted semantic content without a `src`; a `src` must identify a real supplied or created asset. Chart subtypes belong in a label, while the class is `chart`. Only reliably readable numeric values become chart data by default.[^syntax]

## Coordinates, pages, and references

Optional geometry consists of four integer locations ordered x-min, y-min, x-max, y-max, relative to the full page. The skill convention normalizes measured coordinates to 512 × 512 using `round(511*x/W)` and `round(511*y/H)`, bounded to 0–511. Crop offsets and transformations must be mapped back first. Omit unreliable geometry; the skill omits geometry on `group` because its source reference identifies an ambiguity.[^syntax]

Separate actual pages with root-level `page_break`. Continuation uses positive `thread_id` values; fragments sharing a thread must have the same host element type. An `xref` targets an existing thread in the same document. Do not invent targets for unseen pages.[^syntax]

## Unreadable content

Use an element's description to mark an unreadable value or span. For example:[^examples]

```xml
<doclang xmlns="https://www.doclang.ai/ns/v0" version="0.8">
  <text><description>A text region is present, but its characters are unreadable.</description></text>
</doclang>
```

There is no core `unclear`, `bbox`, or `confidence` element/attribute. Checkbox states are selected or unselected; an unknown state is described on the container without emitting a guessed checkbox.[^syntax]

The bundled [syntax snapshot](/references/syntax.txt) and [teaching examples](/references/examples.txt) provide the detailed reference. They are preserved source text, including their original relative references; those references describe the skill's original layout rather than links within this wiki.

[^syntax]: Bundled syntax reference derived by the skill from the user-supplied DocLang 0.8 PDF; it is not an official schema.
[^examples]: Bundled synthetic examples, including their convention for unreadable content.
