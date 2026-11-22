---
type: Source Inventory
title: LLMWiki skill source records
description: Current skill snapshots, original locations, licenses, integrity hashes, and test evidence.
sources:
  - id: skill
    resource: ./skill.txt
    title: "LLMWiki skill instructions"
  - id: okf
    resource: ./okf-authoring.txt
    title: "OKF v0.3 authoring reference"
  - id: layout
    resource: ./layout-and-examples.txt
    title: "Layout examples and delivery checklist"
  - id: interface
    resource: ./openai.yaml.txt
    title: "Skill display metadata"
  - id: validator
    resource: ./validator/validate.py.txt
    title: "Bundled OKF validator implementation"
  - id: validator-tests
    resource: ./validator/tests/test_validate.py.txt
    title: "Validator regression tests"
  - id: vendor-notice
    resource: ./validator/_vendor/NOTICE.md.txt
    title: "Bundled-source versions and local adaptations"
  - id: okf-license
    resource: ./validator/LICENSE.okf.txt
    title: "Upstream validator Apache 2.0 license"
  - id: pyyaml-license
    resource: ./validator/_vendor/pyyaml/LICENSE.txt
    title: "PyYAML MIT license"
  - id: vendor-vendor---init---py
    resource: ./validator/_vendor/__init__.py.txt
    title: "Bundled parser source _vendor/__init__.py"
  - id: vendor-vendor-pyyaml---init---py
    resource: ./validator/_vendor/pyyaml/__init__.py.txt
    title: "Bundled parser source _vendor/pyyaml/__init__.py"
  - id: vendor-vendor-pyyaml-composer-py
    resource: ./validator/_vendor/pyyaml/composer.py.txt
    title: "Bundled parser source _vendor/pyyaml/composer.py"
  - id: vendor-vendor-pyyaml-constructor-py
    resource: ./validator/_vendor/pyyaml/constructor.py.txt
    title: "Bundled parser source _vendor/pyyaml/constructor.py"
  - id: vendor-vendor-pyyaml-error-py
    resource: ./validator/_vendor/pyyaml/error.py.txt
    title: "Bundled parser source _vendor/pyyaml/error.py"
  - id: vendor-vendor-pyyaml-events-py
    resource: ./validator/_vendor/pyyaml/events.py.txt
    title: "Bundled parser source _vendor/pyyaml/events.py"
  - id: vendor-vendor-pyyaml-loader-py
    resource: ./validator/_vendor/pyyaml/loader.py.txt
    title: "Bundled parser source _vendor/pyyaml/loader.py"
  - id: vendor-vendor-pyyaml-nodes-py
    resource: ./validator/_vendor/pyyaml/nodes.py.txt
    title: "Bundled parser source _vendor/pyyaml/nodes.py"
  - id: vendor-vendor-pyyaml-parser-py
    resource: ./validator/_vendor/pyyaml/parser.py.txt
    title: "Bundled parser source _vendor/pyyaml/parser.py"
  - id: vendor-vendor-pyyaml-reader-py
    resource: ./validator/_vendor/pyyaml/reader.py.txt
    title: "Bundled parser source _vendor/pyyaml/reader.py"
  - id: vendor-vendor-pyyaml-resolver-py
    resource: ./validator/_vendor/pyyaml/resolver.py.txt
    title: "Bundled parser source _vendor/pyyaml/resolver.py"
  - id: vendor-vendor-pyyaml-scanner-py
    resource: ./validator/_vendor/pyyaml/scanner.py.txt
    title: "Bundled parser source _vendor/pyyaml/scanner.py"
  - id: vendor-vendor-pyyaml-tokens-py
    resource: ./validator/_vendor/pyyaml/tokens.py.txt
    title: "Bundled parser source _vendor/pyyaml/tokens.py"
  - id: run
    resource: ./verification-run.txt
    title: "Captured validator tests and packaging check"
generated:
  by: process:llmwiki-documentation-refresh
  at: "2026-11-22T11:09:48Z"
---
# LLMWiki skill source records

Captured on 2026-11-22 from the installed `.agents/skills/llmwiki/` directory in `one-prompt-doc`. The 22 source snapshots below preserve the original file bytes, including the validator, its test suite, the bundled YAML loading modules, and their licenses. The separate verification record captures this documentation refresh's test run.

Snapshots are reference data, not active instructions or an executable installation. Their `.txt` suffixes preserve the distinction from authored concepts. Internal imports and links retain the original installation layout; use the mapping below to locate each snapshot. Keep parser modules and license notices together when reconstructing or distributing the implementation.

## Source snapshots

Original paths are relative to `.agents/skills/llmwiki/`. Snapshot links are relative to this document.

| Original file | Snapshot | SHA-256 |
|---|---|---|
| `SKILL.md` | [skill.txt](./skill.txt)[^skill] | `184c0c723f032202cbe3084c9b996ddbe6f50fe10063a558a49fba329c820315` |
| `references/okf-authoring.md` | [okf-authoring.txt](./okf-authoring.txt)[^okf] | `78dd798529269a6c07d6a24af093f19b69c8f2490ee65101b72ddc14cb75b637` |
| `references/layout-and-examples.md` | [layout-and-examples.txt](./layout-and-examples.txt)[^layout] | `2a4869c066181d5b88ac257a66b685b7b0a093dbf00a777963aa8e6f4c1e2957` |
| `agents/openai.yaml` | [openai.yaml.txt](./openai.yaml.txt)[^interface] | `c0300f8563df12952fc7fe96221a380bac244d0ca30de49720ebef6a08ecf359` |
| `scripts/validate.py` | [validator/validate.py.txt](./validator/validate.py.txt)[^validator] | `8fd56835edb410b3aa20adfc6e4bdb89a6d666c867c5d7039d59020c9b792e32` |
| `scripts/tests/test_validate.py` | [validator/tests/test_validate.py.txt](./validator/tests/test_validate.py.txt)[^validator-tests] | `0e3f2594425016e0c7cee445f05484c9818ee0fd845e3196b2fbcfa23bcaf638` |
| `scripts/_vendor/NOTICE.md` | [validator/_vendor/NOTICE.md.txt](./validator/_vendor/NOTICE.md.txt)[^vendor-notice] | `ed3b456aebc842c38fc2e90029c74043b2ee192f8f6e04bd167eb1111ca85a95` |
| `scripts/LICENSE.okf` | [validator/LICENSE.okf.txt](./validator/LICENSE.okf.txt)[^okf-license] | `8c6db340475136df3c1201d458fa5755698eace76e510471ecc9d857d6083dac` |
| `scripts/_vendor/pyyaml/LICENSE` | [validator/_vendor/pyyaml/LICENSE.txt](./validator/_vendor/pyyaml/LICENSE.txt)[^pyyaml-license] | `8d3928f9dc4490fd635707cb88eb26bd764102a7282954307d3e5167a577e8a4` |
| `scripts/_vendor/__init__.py` | [validator/_vendor/__init__.py.txt](./validator/_vendor/__init__.py.txt)[^vendor-vendor---init---py] | `4a293975b0d9e8136fde997521d32a7d6aab54eed657a7a683961772169bbf4c` |
| `scripts/_vendor/pyyaml/__init__.py` | [validator/_vendor/pyyaml/__init__.py.txt](./validator/_vendor/pyyaml/__init__.py.txt)[^vendor-vendor-pyyaml---init---py] | `5ae8ebe6c5bb5722dff7e656abdb0ebd47005bb96964ad878bc4dfc3c324dd01` |
| `scripts/_vendor/pyyaml/composer.py` | [validator/_vendor/pyyaml/composer.py.txt](./validator/_vendor/pyyaml/composer.py.txt)[^vendor-vendor-pyyaml-composer-py] | `fcaa37d16afa783594794a5ab94193dcb720f503c19ce3d59539c8311189f453` |
| `scripts/_vendor/pyyaml/constructor.py` | [validator/_vendor/pyyaml/constructor.py.txt](./validator/_vendor/pyyaml/constructor.py.txt)[^vendor-vendor-pyyaml-constructor-py] | `90d8247da78b524c10618fd0e857f54f3d97570fe91b5c5513d024ef3faf88b0` |
| `scripts/_vendor/pyyaml/error.py` | [validator/_vendor/pyyaml/error.py.txt](./validator/_vendor/pyyaml/error.py.txt)[^vendor-vendor-pyyaml-error-py] | `021f73fada072546c4f63f8cf18a7181244ce4280b09cc15cc980b2d1176171a` |
| `scripts/_vendor/pyyaml/events.py` | [validator/_vendor/pyyaml/events.py.txt](./validator/_vendor/pyyaml/events.py.txt)[^vendor-vendor-pyyaml-events-py] | `e74fd392c810884e2ea7e94aa3f57e9c1cbeb402319083d0c58e6a0e1282787c` |
| `scripts/_vendor/pyyaml/loader.py` | [validator/_vendor/pyyaml/loader.py.txt](./validator/_vendor/pyyaml/loader.py.txt)[^vendor-vendor-pyyaml-loader-py] | `5156becc8aa6905482218abf3e04869b835226db4763645fff3438fdbd5f1cdd` |
| `scripts/_vendor/pyyaml/nodes.py` | [validator/_vendor/pyyaml/nodes.py.txt](./validator/_vendor/pyyaml/nodes.py.txt)[^vendor-vendor-pyyaml-nodes-py] | `80f28d8fca4a09d87677882bde021820d9cf39a3b11a12405226211919cf13ce` |
| `scripts/_vendor/pyyaml/parser.py` | [validator/_vendor/pyyaml/parser.py.txt](./validator/_vendor/pyyaml/parser.py.txt)[^vendor-vendor-pyyaml-parser-py] | `8a55a9e6fbe0a07146cef3990c8b45a068c3e83e369e1959ad9ca30306b4a09a` |
| `scripts/_vendor/pyyaml/reader.py` | [validator/_vendor/pyyaml/reader.py.txt](./validator/_vendor/pyyaml/reader.py.txt)[^vendor-vendor-pyyaml-reader-py] | `d1d9b38ab3a20c6e17a38d519ee412ecaf6b918df18c78956ac7c330d4ea08dc` |
| `scripts/_vendor/pyyaml/resolver.py` | [validator/_vendor/pyyaml/resolver.py.txt](./validator/_vendor/pyyaml/resolver.py.txt)[^vendor-vendor-pyyaml-resolver-py] | `f4bf9561f9b89961f1503d558385fbae30d12bfed565de9bf76c33abb63620a6` |
| `scripts/_vendor/pyyaml/scanner.py` | [validator/_vendor/pyyaml/scanner.py.txt](./validator/_vendor/pyyaml/scanner.py.txt)[^vendor-vendor-pyyaml-scanner-py] | `60433788b652690c17710460da5d91e0c753d3318fd85f5e1e42862a71f25906` |
| `scripts/_vendor/pyyaml/tokens.py` | [validator/_vendor/pyyaml/tokens.py.txt](./validator/_vendor/pyyaml/tokens.py.txt)[^vendor-vendor-pyyaml-tokens-py] | `953408cd2570f0c83dc2fe39f7e4e388e41eeb05738aa69196a5f6ffcf6ba79e` |
| Captured run evidence | [verification-run.txt](./verification-run.txt)[^run] | `dca73259219cd30bb7831aafbbfc4673c2469c893e2e25ab633dd3316be14514` |

## Inspected registration and scope

The installed skill contains 22 files. The Claude Code link `.claude/skills/llmwiki` targets `../../.agents/skills/llmwiki` in this project. These are observations on the capture date, not universal discovery-path requirements for every agent.

The skill targets OKF v0.3 for new bundles and includes explicit compatibility and migration guidance for older declarations. The canonical specification is in `open-knowledge-format/open-knowledge-format`. The authoring guide is included locally; the complete upstream specification is not mirrored in this bundle.[^skill][^okf]

The validator derives from upstream OKF commit `c4df7bab129884a19673c7098dd8a5c55bf06c86`. Its bundled parser uses eleven unchanged PyYAML 6.0.3 loading modules plus a local loading-only interface. The upstream validator is Apache-2.0 licensed; the parser is MIT licensed. The notices describe local YAML 1.2 scalar handling, multiline preservation, malformed-input reporting, and bundle-boundary checks. Python 3.9+ and its standard library are sufficient at runtime; no separately installed YAML package is needed.[^vendor-notice][^okf-license][^pyyaml-license]

## Verification evidence

The captured run records Python 3.9.6, 17 passing validator tests with site-packages disabled, and a successful skill packaging check. It is implementation evidence, not a human verification event or an end-to-end evaluation of an agent maintaining a wiki.[^run]

## Documentation template

The DocLang product documentation supplied the original section pattern: overview, setup/usage, workflow, output format, verification, limits, source records, and log. No DocLang source content, runtime, or test result is required by this bundle.

## Maintenance

Compare these hashes with the installed skill before refreshing this documentation. Update changed snapshots and affected concepts together, retain source licenses, then check links from each document location. Rerun the bundled validator tests after implementation changes. Preserve the distinction between a packaging check, a documentation check, and an end-to-end evaluation of an agent using the skill.

[^skill]: Snapshot of `.agents/skills/llmwiki/SKILL.md`.
[^okf]: Snapshot of `.agents/skills/llmwiki/references/okf-authoring.md`.
[^layout]: Snapshot of `.agents/skills/llmwiki/references/layout-and-examples.md`.
[^interface]: Snapshot of `.agents/skills/llmwiki/agents/openai.yaml`.
[^validator]: Snapshot of `.agents/skills/llmwiki/scripts/validate.py`.
[^validator-tests]: Snapshot of `.agents/skills/llmwiki/scripts/tests/test_validate.py`.
[^vendor-notice]: Snapshot of `.agents/skills/llmwiki/scripts/_vendor/NOTICE.md`.
[^okf-license]: Snapshot of `.agents/skills/llmwiki/scripts/LICENSE.okf`.
[^pyyaml-license]: Snapshot of `.agents/skills/llmwiki/scripts/_vendor/pyyaml/LICENSE`.
[^vendor-vendor---init---py]: Snapshot of `.agents/skills/llmwiki/scripts/_vendor/__init__.py`.
[^vendor-vendor-pyyaml---init---py]: Snapshot of `.agents/skills/llmwiki/scripts/_vendor/pyyaml/__init__.py`.
[^vendor-vendor-pyyaml-composer-py]: Snapshot of `.agents/skills/llmwiki/scripts/_vendor/pyyaml/composer.py`.
[^vendor-vendor-pyyaml-constructor-py]: Snapshot of `.agents/skills/llmwiki/scripts/_vendor/pyyaml/constructor.py`.
[^vendor-vendor-pyyaml-error-py]: Snapshot of `.agents/skills/llmwiki/scripts/_vendor/pyyaml/error.py`.
[^vendor-vendor-pyyaml-events-py]: Snapshot of `.agents/skills/llmwiki/scripts/_vendor/pyyaml/events.py`.
[^vendor-vendor-pyyaml-loader-py]: Snapshot of `.agents/skills/llmwiki/scripts/_vendor/pyyaml/loader.py`.
[^vendor-vendor-pyyaml-nodes-py]: Snapshot of `.agents/skills/llmwiki/scripts/_vendor/pyyaml/nodes.py`.
[^vendor-vendor-pyyaml-parser-py]: Snapshot of `.agents/skills/llmwiki/scripts/_vendor/pyyaml/parser.py`.
[^vendor-vendor-pyyaml-reader-py]: Snapshot of `.agents/skills/llmwiki/scripts/_vendor/pyyaml/reader.py`.
[^vendor-vendor-pyyaml-resolver-py]: Snapshot of `.agents/skills/llmwiki/scripts/_vendor/pyyaml/resolver.py`.
[^vendor-vendor-pyyaml-scanner-py]: Snapshot of `.agents/skills/llmwiki/scripts/_vendor/pyyaml/scanner.py`.
[^vendor-vendor-pyyaml-tokens-py]: Snapshot of `.agents/skills/llmwiki/scripts/_vendor/pyyaml/tokens.py`.
[^run]: Captured 2026-11-22 test and packaging run.
