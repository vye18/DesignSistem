# DeepSeek Adapter

Realisasi §7.3, §9, §11.1 untuk model keluarga DeepSeek (API kompatibel
format OpenAI Chat Completions, dengan dukungan `response_format: json_object`).

## Yang Diterjemahkan Adapter Ini

1. **Format pemanggilan tool** — DeepSeek mendukung function-calling
   bergaya OpenAI; skema `core/schemas/cognition-stack/` dibind sebagai
   `tools[].function.parameters`, sama seperti adapter GPT/Grok.
2. **Gaya instruksi** — instruksi bernomor di `system` message. DeepSeek
   dilaporkan merespons baik pada instruksi yang menyertakan alasan
   ("kenapa" aturan ini ada), bukan hanya daftar imperatif — jadi rationale
   singkat dari `core-templates/*.md` disertakan, tidak dipangkas.
3. **Batas konteks** — sama seperti adapter lain.

Logika kognisi **tidak diulang di sini** — tetap di
`prompt-compiler/core-templates/*.md`.

## Status

Lihat `reasoning-engine.md` untuk satu contoh penuh; tiga engine lain
mengikuti pola yang sama seperti `adapters/gpt/`.
