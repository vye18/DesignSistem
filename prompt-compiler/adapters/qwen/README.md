# Qwen Adapter

Realisasi §7.3, §9, §11.1 untuk model keluarga Qwen (Alibaba DashScope /
OpenAI-compatible mode).

## Yang Diterjemahkan Adapter Ini

1. **Format pemanggilan tool** — pada mode OpenAI-compatible, sama seperti
   adapter GPT/Grok (`tools[].function.parameters`). Pada model/deployment
   yang tidak mendukung function-calling penuh, skema disematkan langsung
   sebagai teks JSON Schema di `system` message dengan instruksi eksplisit
   "balas HANYA dengan JSON yang valid terhadap skema ini" — fallback yang
   dibutuhkan karena dukungan tool-calling Qwen bervariasi antar rilis.
2. **Gaya instruksi** — instruksi bernomor, eksplisit, tanpa asumsi model
   sudah familiar dengan konvensi tool-calling tertentu.
3. **Batas konteks** — sama seperti adapter lain.

Logika kognisi **tidak diulang di sini** — tetap di
`prompt-compiler/core-templates/*.md`.

## Status

Lihat `reasoning-engine.md` untuk satu contoh penuh (varian fallback
JSON-in-prompt); tiga engine lain mengikuti pola yang sama.
