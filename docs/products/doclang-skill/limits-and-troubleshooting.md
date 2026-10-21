---
type: Troubleshooting Guide
title: DocLang skill limits and troubleshooting
description: Model constraints, checker boundaries, and extraction problems.
sources:
  - id: skill
    resource: /references/skill.txt
    title: DocLang skill instructions
  - id: syntax
    resource: /references/syntax.txt
    title: Syntax scope, source ambiguities, and validation limitations
  - id: checker
    resource: /references/checker.py.txt
    title: Structural checker implementation
---
# DocLang skill limits and troubleshooting

## Model and format limits

The skill does not add vision capability. If the host cannot inspect images or obtain reliable OCR, it cannot faithfully perform the conversion. It must state that limitation instead of inventing image content. A capable model can still omit or misread text, so structural success is not proof of faithful extraction.[^skill]

The supported workflow focuses on still images. Archive packaging, audio/video tracks, and organization-specific extensions need additional work if requested. The syntax reference distinguishes current 0.8 syntax from informative future extensions in the source PDF; those future examples are not default core output.[^syntax]

The source PDF is not bundled here. This product bundle documents the installed skill and includes its complete task-specific syntax guide; it is not a replacement for the official format specification or schema.[^syntax]

## Troubleshooting

| Symptom | Response |
|---|---|
| Missing or fabricated words despite valid XML | Recompare the affected region with the image; preserve uncertainty instead of guessing. |
| Wrong column order or flattened structure | Reinspect region boundaries, headings, and logical relationships before serializing again. |
| Unreadable value treated as blank | Keep its occupied position and attach a description of the unreadable content. |
| Unknown checkbox forced to a binary state | Omit the checkbox element and describe the obscured state on its container. |
| Property-order diagnostic | Move properties before payload in the prescribed order; do not add a per-element `head`. |
| List or table delimiter diagnostic | Use item-start `ldiv` and OTSL cell positions, with equal row widths and `nl` row endings. |
| Bounding-box diagnostic | Check four integer coordinates, effective resolution, ordered bounds, and full-page crop mapping. |
| XML parser failure | Check escaping, root/version, nesting, and complete output; do not treat a truncated response as a document. |
| DTD/entity rejection | The checker's image-output subset rejects DTDs and declared entities. |
| Unsupported element | Consult the syntax guide; do not invent a substitute tag or claim official validation. |

The responses above follow the skill's extraction rules and the checker's diagnostics.[^skill][^syntax][^checker]

## What a passing checker does not establish

The checker does not implement the complete XSD/Schematron rules, prove OCR accuracy or correct reading order, validate every allowed nesting relationship, or establish all merge semantics. Its acceptance of an unqualified root also does not override the skill's instruction to emit the namespace explicitly. Run visual comparison as a separate step and describe exactly which validation was performed.[^syntax][^checker]

[^skill]: Bundled skill instructions for evidence handling, uncertainty, and visual review.
[^syntax]: Bundled syntax guide's current-format scope and validation boundaries.
[^checker]: Bundled checker source, including diagnostics and root acceptance behavior.
