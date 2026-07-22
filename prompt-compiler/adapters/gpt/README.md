# GPT Adapter

Realisasi §7.3, §9, §11.1 untuk model keluarga GPT (OpenAI Chat Completions
/ Responses API).

## Yang Diterjemahkan Adapter Ini

1. **Format pemanggilan tool** — skema di `core/schemas/cognition-stack/`
   dibind sebagai `tools[].function.parameters` (JSON Schema, dengan
   `strict: true` bila tersedia) sehingga output lapis divalidasi oleh
   provider sebelum sampai ke aplikasi, bukan hanya lewat instruksi teks.
2. **Gaya instruksi** — GPT merespons konsisten pada instruksi terstruktur
   sebagai daftar bernomor di `system` message, dengan pemisahan eksplisit
   antara "instructions" dan "input data" (bukan XML-tag seperti Claude).
3. **Batas konteks** — sama seperti adapter lain: hanya artefak lapis
   relevan yang disertakan per panggilan (lihat `core-templates/*.md`).

Logika kognisi **tidak diulang di sini** — tetap didefinisikan sekali di
`prompt-compiler/core-templates/*.md`.

## Pola Umum per Engine

```json
{
  "model": "gpt-...",
  "messages": [
    {"role": "system", "content": "<instruksi dari core-templates/*.md, dirender sebagai daftar bernomor>"},
    {"role": "user", "content": "<artefak lapis sebelumnya, sebagai JSON>"}
  ],
  "tools": [
    {"type": "function", "function": {"name": "emit_l0X_...", "strict": true, "parameters": "<isi $id skema lapis ini>"}}
  ],
  "tool_choice": {"type": "function", "function": {"name": "emit_l0X_..."}}
}
```

## Status

Kerangka pembungkus siap. Rendering konkret per-engine mengikuti pola di
atas, memakai isi instruksi identik dengan `core-templates/*.md` dan
`adapters/claude/*.md` sebagai rujukan konten — lihat
`reasoning-engine.md` di folder ini untuk satu contoh penuh; tiga engine
lain (planning, critic, visual-cognition) mengikuti pola pembungkus yang
sama persis, hanya `tools[].function.name` dan `parameters` yang berganti
sesuai skema lapisnya.
