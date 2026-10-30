I'll re-read the reference and the new comparison file (qwen3.8-flash-next-4bit-high).

Read 
Completed with input: {
  "path": "/Users/dden/gitroot/one-prompt-doc/test/gpt-6-astra-high/tiger-loop-01.xml"
}

Read 
Completed with input: {
  "path": "/Users/dden/gitroot/one-prompt-doc/test/qwen3.8-flash-next-4bit-high/tiger-loop-01.xml"
}

Here's the comparison, restricted to `<text>` content. The reference is `gpt-6-astra-high`; the compared file is `qwen3.8-flash-next-4bit-high`. This variant diverges more than the gemini/claude variants — it has word-level content changes **and** a systematic markup difference.

# `<text>` Content Differences — tiger-loop-01.xml

Reference: `tiger-loop-01.xml`
Compared: `tiger-loop-01.xml`

## 1. Systematic markup difference (affects all text blocks)

Every trademark symbol is rendered differently:

| Reference | qwen3.8-flash-next-4bit |
|-----------|-------------------------|
| `Tigerloop<superscript>®</superscript>` / `SPX<superscript>®</superscript>` | plain `Tigerloop®` / `SPX®` (bare `®`, no `<superscript>` element) |

This appears in every shared block. The visible characters are equivalent, but the `<superscript>` markup the reference preserves is dropped throughout qwen's output.

## 2. Word-level content differences in shared text blocks

Two genuine content changes in the 4th body paragraph ("pressurized return line…"):

| # | Location | Reference | qwen3.8-flash-next-4bit |
|---|----------|-----------|-------------------------|
| 1 | 4th body paragraph | "…drawn from the tank to the fuel **burner**." | "…drawn from the tank to the fuel **pump**." |
| 2 | 4th body paragraph | "By automatically and **continually** de-aerating the fuel…" | "By automatically and **continuously** de-aerating the fuel…" |

All other shared body paragraphs are textually identical (modulo the `®` markup in §1): OFTEC/OPS 23 intro, energy-savings, two-pipe vs one-pipe, "constructed externally…", "When fuel is drawn…", and "automatically and continuously de-aerates" (indoor para 3), plus the cleaning paragraph.

## 3. Text blocks present in reference but MISSING in qwen

qwen omits the product-label lettering and all model/logo captions, using description-only `<picture>` elements:

| Reference `<text>` content | Context |
|----------------------------|---------|
| `Tigerloop®` | Main photograph label |
| `DE-AERATOR ORIGINAL` (nested `<text>`+`<description>`) | Product label |
| `gerloop® Bio` (nested) | Product name curving out of view |
| `AB SWEDEN` (nested) | Small label lettering |
| `Tigerholm` | Label text |
| `AN SPX BRAND` | Label text |
| `Tigerloop Bio` (×2) | Two model photographs |
| `SPX®` | Logo text |

## 4. Merged / reformatted footer

The three separate footer blocks are collapsed into one:

| Reference (3 blocks) | qwen (1 block) |
|----------------------|----------------|
| `<bold>Manufactured by</bold>` | merged into a single `<text><bold>Manufactured by`<br>`SPX Flow Technology Stockholm AB, SWEDEN`<br>`www.tigerholm.com</bold></text>` |
| `<bold>SPX Flow Technology Stockholm AB, SWEDEN</bold>` | (same, joined) |
| `<bold>www.tigerholm.com</bold>` | (same, joined) |

Content is preserved but the three-line split and block structure are lost.

## 5. Nested `<description>` inside the "observe local codes" text

| Reference | qwen |
|-----------|------|
| `<text><description>Bold installation notice enclosed in a black rectangular border.</description><bold>When installing…</bold></text>` | `<text><bold>When installing…</bold></text>` — nested `<description>` omitted |

The visible `<bold>` text is identical; only the description is dropped.

## 6. Summary

- **Systematic:** all `®` symbols lose their `<superscript>` markup in qwen.
- **Content changes:** 2 in the 4th body paragraph — `burner`→`pump` and `continually`→`continuously`.
- **Missing text:** 8 label/photo/logo `<text>` blocks (same omission pattern as mistral and claude-sonnet-5.5).
- **Footer:** three separate bold blocks merged into one (mistral also merged; qwen keeps them bold).
- **Notice description:** nested `<description>` dropped (also seen in mistral; gemini/claude kept a variant).
- Out-of-scope (non-`<text>`): the Technical-data table uses `<rhed/>` instead of `<fcel/>` and the thread quotes are straight `"` — not inside `<text>`.

Note: I'm running as the read-only Ask agent, so I can't write this to a file. The report is provided inline; switch to a write-capable agent if you'd like it saved to a `.md` file.