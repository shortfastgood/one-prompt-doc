I'll read both files to compare them.

Read 
Completed with input: {
  "path": "/Users/dden/gitroot/one-prompt-doc/test/gpt-6-astra-high/tiger-loop-01.xml"
}

Read 
Completed with input: {
  "path": "/Users/dden/gitroot/one-prompt-doc/test/output/tiger-loop-01.md"
}

I've read both files. The XML is DocLang v0.8; the MD is a coordinate-annotated markdown rendering of the same page. Here is the semantic comparison, focused on the plan text, plus a sequence check.

## Sequence check — same order?

**Yes, the overall sequence is identical.** Both traverse the page in three blocks:

1. **Upper portion**: product photo → title → subtitle → 4 intro paragraphs
2. **Lower-left column**: Technical data → table → Models → 2 images → model table → Cleaning → cleaning text
3. **Lower-right column**: "Suitable for Indoor Installation" → 3 paragraphs → install notice → SPX logo → "Manufactured by / SPX Flow Technology / www"

The coordinate `y`-values in the MD confirm the ordering (e.g., install notice `y≈829` → SPX logo `y≈892` → "Manufactured by" `y≈940`), matching the XML group order. No reordering or dropped/moved sections.

## Plan-text differences

The **body prose is verbatim identical** across all 4 intro paragraphs and the 3 right-column paragraphs — no wording, spelling, or punctuation drift in the running text. The differences are all **structural/formatting** and a few **minor spacing artifacts**:

| # | What | XML (source) | MD (output) | Type |
|---|------|-------------|-------------|------|
| 1 | **Photo text labels lost** | `<picture>` carries 7 text labels: `Tigerloop®`, `DE-AERATOR ORIGINAL`, `…gerloop® Bio`, `…AB SWEDEN`, `Tigerholm`, `AN SPX BRAND` | Single `image` ref, no extracted text | Content dropped |
| 2 | **Model-image text lost** | Each model `<picture>` has description + `Tigerloop Bio` text | Bare `image` refs, no text | Content dropped |
| 3 | **SPX logo text lost** | `<picture label="logo">` with `SPX®` text | Bare `image` ref | Content dropped |
| 4 | **Heading levels collapsed** | `<heading level="1">` *Tigerloop Bio* + `<heading level="2">` *de-aerator…* | Both rendered as `##` | Hierarchy lost (H1→`##`) |
| 5 | **® rendering** | `<superscript>®</superscript>` | `\( ^{®} \)` (escaped math) + **double space**: `Tigerloop \( ^{®} \)  Bio` | Formatting + spacing artifact |
| 6 | **Bold lost** | Install notice and `Manufactured by` / `SPX Flow Technology…` / `www.tigerholm.com` are `<bold>` | Plain text | Formatting lost |
| 7 | **Temperature spacing** | `70° C` (space) | `70°C` (no space) | Minor text diff |
| 8 | **Model-name spacing** | `Tigerloop Bio: TOB110I` (single space) | `Tigerloop Bio:  TOB110I` (double space) | Minor text diff |
| 9 | **"Manufactured by" block merged** | 3 separate `<text>` elements | 1 `<|ref|>text<|/ref|>` with 3 lines | Structure change (semantically equal) |

## Summary

- **Sequence: consistent** — no reordering.
- **Plan text (prose): semantically identical** — all paragraphs match word-for-word; the only textual deltas are cosmetic spacing (`70° C`→`70°C`, double spaces around model names/`®`).
- **Real information loss is confined to image-embedded text**: the product-photo labels (`DE-AERATOR ORIGINAL`, `Tigerholm`, `AN SPX BRAND`, partial `…gerloop® Bio` / `…AB SWEDEN`), the two model-image labels (`Tigerloop Bio`), and the `SPX®` logo text are not carried into the MD. If those labels matter, that's the gap to close — the running plan text itself is faithful.

Note that items 1–3 are likely *expected* behavior for this MD format (it uses `image` refs rather than inlining extracted text), so they may be acceptable depending on whether the MD pipeline is meant to preserve image text. Want me to flag which of these are "intended" vs "genuine regressions"?