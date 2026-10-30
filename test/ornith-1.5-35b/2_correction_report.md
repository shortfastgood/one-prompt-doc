The tagged files are the same pair as my last comparison. Let me re-read both fresh in case their contents changed.

Read 
Completed with input: {
  "path": "/Users/dden/gitroot/one-prompt-doc/test/gpt-6-astra-high/tiger-loop-01.xml"
}

Read 
Completed with input: {
  "path": "/Users/dden/gitroot/one-prompt-doc/test/ornith-1.5-35b/tiger-loop-01.xml"
}

The `ornith-1.5-35b` file has changed since my last read of this pair. The reference is `gpt-6-astra-high`. Compared to the previous ornith version, several transcription errors were corrected, but a new one appeared.

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
| `<heading level="2">Automatic de-aerator for liquid bio fuel…</heading>` | `<text>Automatic de-aerator for liquid bio fuel…</text>` — demoted from a level-2 heading to a plain text block |

Content identical; only the element type changes.

## 3. Word-level content differences in shared text blocks

| # | Location | Reference | ornith-1.5-35b |
|---|----------|-----------|----------------|
| 1 | Pressurized-return paragraph | "the risk **for** leakage" | "the risk **of** leakage" |
| 2 | Pressurized-return paragraph | "By automatically and **continually** de-aerating the fuel" | "By automatically and **continuously** de-aerating the fuel" |
| 3 | Indoor paragraph 3 | "By providing air/gas free fuel continuously to the burner" | "By providing **the** air/gas free fuel continuously to the burner" (extra "the" — **new** this version) |

**Corrected since the previous ornith read** (now matching the reference, so no longer differences):
- `BS 2869` (was `BS 2689`)
- `energy savings` (was `energy saving`)
- `air/gas` in the "When fuel is drawn" paragraph (was `airgas`, ×2)

All remaining shared body paragraphs are textually identical (modulo the `®` markup in §1): two-pipe/one-pipe, "constructed externally…", and the cleaning paragraph.

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
- **Content differences now 3:** `risk for`→`risk of`, `continually`→`continuously`, and a **new** extra "the" in "By providing **the** air/gas free fuel…" (indoor para 3).
- **Corrected vs previous ornith read:** `BS 2689`→`BS 2869`, `energy saving`→`energy savings`, and `airgas`→`air/gas` (×2) now all match the reference.
- **Structural:** the level-2 subtitle is rendered as a `<text>` block.
- **Missing text:** 8 label/photo/logo `<text>` blocks dropped (product label, two model captions, SPX logo).
- **Footer:** three bold blocks collapsed/merged and un-bolded.
- **Notice description:** nested `<description>` omitted.
- **Out-of-scope (non-`<text>`):** the model-comparison table re-splits its cells into 4 columns with added `<ecel/>` separators (and the OFCERT last cell now reads `S138 2004 T1` with a space); the "Cleaning" heading is `level="3"`; the main product photo is placed after the body paragraphs rather than before the headings.

Note: I'm running as the read-only Ask agent, so I can't write this to a file. The report is provided inline; switch to a write-capable agent if you'd like it saved to a `.md` file.