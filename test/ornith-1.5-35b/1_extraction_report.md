I'll re-read the reference and the new comparison file (ornith-1.5-35b).

Read 
Completed with input: {
  "path": "/Users/dden/gitroot/one-prompt-doc/test/gpt-6-astra-high/tiger-loop-01.xml"
}

Read 
Completed with input: {
  "path": "/Users/dden/gitroot/one-prompt-doc/test/ornith-1.5-35b/tiger-loop-01.xml"
}

Here's the comparison, restricted to `<text>` content. The reference is `gpt-6-astra-high`; the compared file is `ornith-1.5-35b`. This variant shows the most content-level errors of all the variants so far — several transcription mistakes in the body text.

# `<text>` Content Differences — tiger-loop-01.xml

Reference: `tiger-loop-01.xml`
Compared: `tiger-loop-01.xml`

## 1. Systematic markup difference (affects all shared blocks)

| Reference | ornith-1.5-35b |
|-----------|----------------|
| `Tigerloop<superscript>®</superscript>`, `SPX<superscript>®</superscript>` | bare `Tigerloop®`, `SPX®` — no `<superscript>` element |

## 2. Structural difference: subtitle moved from heading to text

| Reference | ornith |
|-----------|--------|
| `<heading level="2">Automatic de-aerator for liquid bio fuel…</heading>` | `<text>Automatic de-aerator for liquid bio fuel…</text>` — demoted from level-2 heading to a plain text block |

The text content is identical; only the element type changes.

## 3. Word-level content differences in shared text blocks

| # | Location | Reference | ornith-1.5-35b |
|---|----------|-----------|----------------|
| 1 | OFTEC intro | "class D gas oil (**BS 2869**)" | "class D gas oil (**BS 2689**)" — transposed digits (86→68) |
| 2 | Energy-savings paragraph | "new demands on **energy savings**" | "new demands on **energy saving**" (plural → singular) |
| 3 | Pressurized-return paragraph | "the risk **for** leakage" | "the risk **of** leakage" |
| 4 | Pressurized-return paragraph | "By automatically and **continually** de-aerating the fuel" | "By automatically and **continuously** de-aerating the fuel" |
| 5 | "When fuel is drawn" paragraph | "…**air/gas** is automatically released… It is this **air/gas** that causes…" | "…**airgas** is automatically released… It is this **airgas** that causes…" (slash dropped, both occurrences) |
| 6 | Indoor paragraph 3 | "By providing **air/gas** free fuel continuously" | "By providing **airgas** free fuel continuously" (slash dropped) |

All other shared body paragraphs are textually identical (modulo the `®` markup in §1): two-pipe/one-pipe, "constructed externally…", the "automatically and continuously de-aerates" clause, and the cleaning paragraph.

## 4. Text blocks present in reference but MISSING in ornith

ornith captures no product-label lettering and no model/logo captions — its pictures are description-only:

| Reference `<text>` | ornith handling |
|--------------------|-----------------|
| `Tigerloop®` | **missing** (photo description-only) |
| `DE-AERATOR ORIGINAL` (nested) | **missing** |
| `gerloop® Bio` (nested) | **missing** |
| `AB SWEDEN` (nested) | **missing** |
| `Tigerholm` | **missing** |
| `AN SPX BRAND` | **missing** |
| `Tigerloop Bio` (×2 model photos) | **missing** — both model photos are description-only |
| `SPX®` (logo text) | **missing** — logo is description-only |

## 5. Footer merged and un-bolded

| Reference (3 blocks) | ornith |
|----------------------|--------|
| `<bold>Manufactured by</bold>` | merged into plain `Manufactured by SPX Flow Technology Stockholm AB, SWEDEN` (no bold) |
| `<bold>SPX Flow Technology Stockholm AB, SWEDEN</bold>` | (same line, plain) |
| `<bold>www.tigerholm.com</bold>` | plain `www.tigerholm.com` (separate, no bold) |

Content preserved, but the bold markup and the "Manufactured by" split are lost.

## 6. Nested `<description>` inside "observe local codes" text

| Reference | ornith |
|-----------|--------|
| `<text><description>Bold installation notice enclosed in a black rectangular border.</description><bold>When installing…</bold></text>` | `<text><bold>When installing…</bold></text>` — nested `<description>` omitted |

The visible `<bold>` text is identical; only the description is dropped.

## 7. Summary

- **Systematic:** all `®` symbols lose `<superscript>` markup.
- **Transcription errors (6):** `BS 2869`→`BS 2689` (digit transposition), `energy savings`→`energy saving`, `risk for`→`risk of`, `continually`→`continuously`, and `air/gas`→`airgas` (3 occurrences).
- **Structural:** the level-2 subtitle is rendered as a `<text>` block instead of a heading.
- **Missing text:** 8 label/photo/logo `<text>` blocks dropped (product label, two model captions, SPX logo) — same omission pattern as mistral/claude-sonnet-5.5/qwen variants.
- **Footer:** three bold blocks collapsed/merged and un-bolded (like mistral).
- **Notice description:** nested `<description>` omitted (like qwen3.8-flash).
- **Out-of-scope (non-`<text>`):** the two model-photo captions and logo are description-only; the model-comparison table re-splits its cells into 4 columns (adding `<ecel/>` separators); the "Cleaning" heading is `level="3"`; the main product photo is placed after the body paragraphs rather than before the headings.

Note: I'm running as the read-only Ask agent, so I can't write this to a file. The report is provided inline; switch to a write-capable agent if you'd like it saved to a `.md` file.