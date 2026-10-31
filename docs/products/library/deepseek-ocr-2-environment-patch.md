---
type: Engineering Note
title: Environment / DeepSeek-OCR-2 inconsistency patch
description: Why development/mlx-vlm/deepseek-ocr-2/extractor.py patches two removed transformers symbols at runtime.
tags: [mlx-vlm, deepseek-ocr-2, transformers, compatibility, patch, ImportError]
sources:
  - id: extractor-source
    resource: /references/extractor.py.txt
    title: extractor.py, development/mlx-vlm/deepseek-ocr-2/
  - id: requirements-file
    resource: /references/requirements.txt
    title: requirements.txt for the deepseek-ocr-2 script
status: stable
generated:
  by: process:<author>
  at: 2026-10-30T16:30:00Z
---
# Environment / DeepSeek-OCR-2 inconsistency patch

The script patches two symbols removed from `transformers` 5.x because the
`mlx-community/DeepSeek-OCR-2-bf16` checkpoint ships custom modeling code that
was written for `transformers` 4.46. The mismatch is:

* The checkpoint's `auto_map` routes `AutoConfig` into a torch-based module.
* That module imports two symbols that existed in `transformers` 4.46 but were
  removed in `transformers` 5.x.
* The installed `mlx-vlm` 0.7.8 requires `transformers` 5.x, so importing the
  checkpoint's code fails before any inference can run.

The fix lives in `_patch_missing_transformers_symbols()`, called once at the
start of `main`, before `load`. It is defensive: it only adds an attribute when
the running `transformers` lacks it, so it is harmless on versions that still
export the symbols.

## What it patches and why each is safe

| Symbol | Imported from | Patch action | Why it is safe |
| --- | --- | --- | --- |
| `LlamaFlashAttention2` | `transformers.models.llama.modeling_llama` | Aliased to `LlamaAttention` | Flash-attention 2 is not active on Metal, so the alias never changes behaviour. The symbol only appears in the model's attention registry and is never instantiated on this path. |
| `is_torch_fx_available` | `transformers.utils.import_utils` | Returns `False` when `torch.fx` is absent | It only guards a `torch.fx.wrap` graph-tracing optimization that has no effect on normal inference. |

`is_torch_fx_available` is implemented as a lambda that inspects `torch.fx`, so
it reports the real runtime capability rather than a hard-coded value.

## Why this coupling exists

The environment pinned `transformers` 5.x (via `mlx-vlm` 0.7.8) while the model
checkpoint is still on the `transformers` 4.46 import contract. Rather than
pin `transformers` down to 4.46 — which `mlx-vlm` does not support — the script
keeps the modern runtime and bridges only the two missing symbols at import
time. `torch>=2.5.0` must also be installed because `torch.fx` (and therefore
the patched guard) is only optional inside `transformers`.

This is a compatibility shim for a specific checkpoint-plus-runtime
combination, not a general-purpose library. See
[the extractor overview](/deepseek-ocr-2-extractor.md) for how the script is
invoked.

[^extractor-source]: Source copy kept as [`references/extractor.py.txt`](references/extractor.py.txt), mirroring `development/mlx-vlm/deepseek-ocr-2/extractor.py` at generation time.
[^requirements-file]: Requirements copy kept as [`references/requirements.txt`](references/requirements.txt).
