---
type: Product Overview
title: DocLang skill overview
description: Purpose, supported inputs, deliverables, and documentation scope.
sources:
  - id: skill
    resource: /references/skill.txt
    title: DocLang skill instructions
  - id: readme
    resource: /references/extraction-readme.txt
    title: MLX-VLM extraction README used as a section template
---
# DocLang skill overview

The product `doclang-skill` documents the reusable skill named `doclang`. It guides a model to convert visible information from images into DocLang 0.8 XML while retaining wording, reading order, and semantic structure. Supported subjects include scanned pages, screenshots, forms, tables, charts, diagrams, and photographs.[^skill]

The skill contains instructions, focused syntax guidance, synthetic examples, and a Python structural checker. It does not supply a vision model, train a model, or provide a complete extraction application. A host must provide image inspection or reliable OCR and, to run the checker, Python execution.[^skill]

The usual deliverable is one UTF-8 XML document saved as `.dclg`. Chat output uses one XML code block unless raw XML is requested. The skill's image workflow does not create a `.dclx` archive by default.[^skill]

## Documentation scope

The supplied MLX-VLM README determines the themes covered here. Its program-specific model defaults, arguments, call counts, output-file protections, hardware measurements, and historical model results are not general properties of the skill.[^readme]

| README theme | Coverage in this bundle |
|---|---|
| Introduction, files, environment, command example | [Setup and usage](/setup-and-usage.md) |
| Skill execution | [Extraction workflow](/extraction-workflow.md) |
| Automated verification | [Verification](/verification.md) |
| CV structure regression | Image-based structure review in [Verification](/verification.md) |
| Verification environment | The current checker run in [Verification](/verification.md) |
| Model verification and limits | [Limits and troubleshooting](/limits-and-troubleshooting.md) |

The additional [output-format guide](/output-format.md) explains the markup needed to use the skill. All cited source snapshots are included in this bundle. Original repository paths in the [source records](/references/source-records.md) identify provenance; reading this documentation does not require those original paths to exist.

[^skill]: Bundled snapshot of the skill's SKILL.md.
[^readme]: Bundled snapshot of the supplied extraction README; its section structure is the documentation template.
