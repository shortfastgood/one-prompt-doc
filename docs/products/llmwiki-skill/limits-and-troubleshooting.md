---
type: Troubleshooting Guide
title: LLMWiki limits and troubleshooting
description: Tooling boundaries, path conflicts, evidence gaps, and delivery constraints.
sources:
  - id: skill
    resource: references/skill.txt
    title: Skill workflow and scope boundaries
  - id: okf
    resource: references/okf-authoring.txt
    title: Format validity and reference interpretation
  - id: layout
    resource: references/layout-and-examples.txt
    title: Standalone-delivery completeness
---
# LLMWiki limits and troubleshooting

## Context and automation limits

The skill reduces routine reading through indices, selected concepts, and task-specific references. It does not impose a numeric context budget or provide retrieval software. A full product-delivery review may need to inspect the whole bundle. Source copies do not synchronize themselves; the agent locates them by provenance and updates them only within scope.[^skill]

## Common issues

| Situation | Response |
|---|---|
| The project is ambiguous | Establish the intended project; do not use the skill installation directory by default. |
| New knowledge has no product assignment | Ask for a product or Library; absence of an answer is not permission to choose Library. |
| A product slug already represents different material | Resolve the collision rather than merging it. |
| `docs/index.md` contains unrelated content | Preserve it and update only the LLMWiki navigation section. |
| Existing knowledge is in a flat bundle | Resolve the migration or location decision before moving files. |
| A raw Markdown reference fails the concept check | Add valid concept frontmatter or retain it as a non-Markdown source asset with an inventory concept. |
| Leading-slash links fail in a normal Markdown viewer | Use document-relative paths with the correct base; update source metadata paths consistently. |
| A source is ambiguous or contradictory | Qualify the content and ask when uncertainty blocks an accurate update. |
| An export needs Library or another product | Include a scoped, permitted local copy of the necessary knowledge, or report the missing dependency. |
| A concept is stale or superseded | Flag it for review or deprecate it with a replacement link rather than deleting referenced knowledge automatically. |

These responses follow the skill's workflow, OKF interpretation, and delivery checklist.[^skill][^okf][^layout]

## Validity, completeness, and trust

OKF tolerates missing optional fields, unfamiliar types and keys, missing indices, and broken cross-links. An unresolved link is therefore not automatically a malformed bundle. A product can be valid OKF while still missing information required for its intended delivery.[^okf]

Local path resolution does not prove factual accuracy. Verification metadata describes actual confirmation events; it must not be fabricated from the fact that an agent produced valid YAML or a user requested a change. Similarly, copying a directory does not establish that it is self-contained until its required dependencies have been checked.[^okf][^layout]

The source snapshots document the installed skill's targeted OKF v0.2 behavior. They do not include a full upstream specification mirror, and a newer upstream version must not silently change an existing bundle's declared target.[^okf]

[^skill]: Bundled skill instructions for discovery, classification, maintenance, and scope.
[^okf]: Bundled authoring guide's path, conformance, trust, and versioning guidance.
[^layout]: Bundled checklist distinguishing format validity from complete product delivery.
