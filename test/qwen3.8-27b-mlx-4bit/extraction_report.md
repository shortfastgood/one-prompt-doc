I'll re-read the reference and the new comparison file (qwen3.8-27b-mlx-4bit).

Read 
Completed with input: {
  "path": "/Users/dden/gitroot/one-prompt-doc/test/gpt-6-astra-high/tiger-loop-01.xml"
}

Read 
Completed with input: {
  "path": "/Users/dden/gitroot/one-prompt-doc/test/qwen3.8-27b-mlx-4bit/tiger-loop-01.xml"
}

Here's the comparison, restricted to `<text>` content. The reference is `gpt-6-astra-high`; the compared file is `qwen3.8-27b-mlx-4bit`. This variant diverges heavily — it adds `<location>`/`<head>`/`<default_resolution>` geometry (out of scope for text) and makes several content, structural, and markup changes inside `<text>`.

# `<text>` Content Differences — tiger-loop-01.xml

Reference: `tiger-loop-01.xml`
Compared: `tiger-loop-01.xml`

## 1. Systematic markup difference (affects all shared blocks)

| Reference | qwen3.8-27b-mlx-4bit |
|-----------|----------------------|
| `Tigerloop<superscript>®</superscript>`, `SPX<superscript>®</superscript>`, etc. | bare `Tigerloop®`, `SPX®`, `gerloop® Bio` — no `<superscript>` element |

Every shared block renders the trademark as a bare `®` instead of wrapping it in `<superscript>`.

## 2. Word-level content differences in shared text blocks

| # | Location | Reference | qwen3.8-27b-mlx-4bit |
|---|----------|-----------|----------------------|
| 1 | OFTEC intro paragraph | "…OFTEC Product Standard OPS 23 **,** the Tigerloop® Bio models are compatible not only…" | "…OFTEC Product Standard OPS 23 **.** The Tigerloop® Bio models are compatible not only…" (comma → period; "the" → "The") |
| 2 | Main photograph label | `Tigerloop®` | `igerloop` — leading "T" reported lost in reflection |

All other shared body paragraphs are textually identical (modulo the `®` markup in §1), including the 4th paragraph ("fuel burner", "continually de-aerating"), the two-pipe/one-pipe paragraph, the three indoor paragraphs, and the cleaning paragraph.

## 3. Nested / product-label text blocks — mismatches and an empty block

| Reference `<text>` | qwen `<text>` |
|--------------------|---------------|
| `gerloop<superscript>®</superscript> Bio` | `gerloop® Bio` (bare `®`, otherwise same) |
| `AB SWEDEN` (one block) | split into **two** blocks: one description-only **empty** text (no visible content) + one reading `AB, SWEDEN` (added comma) |
| — | the nested `<text>` wrappers for DE-AERATOR / gerloop / AB lines carry `<description>` only, matching the reference structure |

The `DE-AERATOR ORIGINAL`, `Tigerholm`, and `AN SPX BRAND` label lines match.

## 4. Text blocks present in reference but MISSING / merged in qwen

| Reference `<text>` | qwen handling |
|--------------------|---------------|
| `Tigerloop Bio` (**×2**, one per model photo) | merged into a **single** `Tigerloop® Bio` caption on one combined picture |
| `SPX<superscript>®</superscript>` (logo text) | **omitted** — logo picture is description-only, no `<text>` |
| 3 separate footer bold blocks (`Manufactured by` / company / `www.tigerholm.com`) | collapsed into **one** `<text>` with a single `<bold>` and line breaks between the three lines |

## 5. Nested `<description>` inside the "observe local codes" text

| Reference | qwen |
|-----------|------|
| `<description>Bold installation notice enclosed in a black rectangular border.</description>` | `<description>Printed in bold inside a rectangular box with a heavy black border.</description>` |

The visible `<bold>` text ("When installing Tigerloop® Bio always observe local codes and ordinances!") is identical; only the description wording differs.

## 6. Summary

- **Systematic:** all `®` symbols lose their `<superscript>` markup.
- **Content changes:** 2 — OFTEC paragraph "OPS 23, the" → "OPS 23. The"; photo label "Tigerloop®" → "igerloop" (leading T dropped).
- **Label mismatches:** the `AB SWEDEN` line is split into an empty description-only text + `AB, SWEDEN` (added comma); `gerloop® Bio` keeps bare `®`.
- **Missing / merged text:** the two `Tigerloop Bio` model captions merge into one; the `SPX®` logo text is dropped; the three footer bold blocks collapse into one.
- **Notice description:** reworded; bold text unchanged.
- **Out-of-scope (non-`<text>`):** qwen adds `<head><default_resolution/>`, and `<location>` boxes on virtually every element; headings "Technical data", "Suitable for Indoor Installation", and "Models" are `level="1"` (vs `level="2"` in the reference); the table thread quotes are straight `"` — none of these are inside `<text>`.

Note: I'm running as the read-only Ask agent, so I can't write this to a file. The report is provided inline; switch to a write-capable agent if you'd like it saved to a `.md` file.