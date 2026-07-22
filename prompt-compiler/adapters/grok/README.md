# Grok Adapter

Realisasi §7.3, §9, §11.1 untuk model keluarga Grok (xAI API — kompatibel
format OpenAI Chat Completions).

## Yang Diterjemahkan Adapter Ini

1. **Format pemanggilan tool** — sama seperti adapter GPT: skema
   `core/schemas/cognition-stack/` dibind sebagai
   `tools[].function.parameters` (JSON Schema).
2. **Gaya instruksi** — instruksi bernomor di `system` message, konsisten
   dengan konvensi API kompatibel-OpenAI.
3. **Batas konteks** — sama seperti adapter lain.

Logika kognisi **tidak diulang di sini** — tetap di
`prompt-compiler/core-templates/*.md`. Karena Grok API kompatibel dengan
format OpenAI, rendering adapter ini secara struktural identik dengan
`adapters/gpt/`, hanya field `model` yang berbeda (`grok-...`).

## Status

Lihat `reasoning-engine.md` untuk satu contoh penuh; tiga engine lain
mengikuti pola yang sama seperti `adapters/gpt/`.
