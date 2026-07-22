# Prompt Compiler

Realisasi §9 (arsitektur) dan §11.1.

## Apa Ini Bukan

Bukan kumpulan prompt siap pakai. Menambah dukungan model baru berarti
menulis satu adapter baru, bukan menulis ulang logika 14 lapis kognisi.

## Apa Ini

Lapisan penerjemah yang mengambil tiga input dan menyusun instruksi konkret
untuk model:

1. Definisi generik dari `core/cognition-stack/` (apa yang harus dicapai
   di suatu lapis).
2. Skema I/O dari engine terkait (`core/schemas/`).
3. Konteks runtime: model target, panjang konteks tersedia, gaya instruksi
   yang optimal untuk model tersebut (mis. Claude merespons baik pada
   XML-tag terstruktur; model lain mungkin lebih baik dengan JSON schema
   eksplisit).

```
prompt-compiler/
├── core-templates/     # instruksi generik, model-agnostic — satu per engine
└── adapters/
    ├── claude/          # format tool-call, gaya instruksi Claude
    ├── gpt/
    ├── gemini/
    ├── grok/
    ├── qwen/
    └── deepseek/
```

Setiap adapter hanya bertanggung jawab atas: (a) format pemanggilan
tool/function spesifik model, (b) batas panjang konteks, (c) gaya instruksi
paling efektif untuk model tersebut. **Logika kognisi ODI sendiri tidak
boleh ditulis ulang per-model.**

## Target Skala (§11.1)

Hingga 200 varian prompt compiler (engine × model × domain) tanpa
duplikasi logika — dicapai dengan memisahkan template inti (model-agnostic)
dari transformasi adapter (tipis, spesifik model).

## Status

**`core-templates/` lengkap** untuk keempat engine (Reasoning, Planning,
Critic, Visual Cognition) — instruksi model-agnostic yang mengoperasionalkan
kontrak di `engines/*/README.md` menjadi langkah konkret, masing-masing
merujuk contoh nyata di `examples/poster-prototype/`.

**`adapters/claude/` lengkap** — rendering Claude (XML-tag + tool-use
dengan `input_schema` dibind langsung dari `core/schemas/cognition-stack/`)
untuk keempat engine yang sama, sesuai prioritas §11.1 (Claude sebagai
*native execution environment*).

**`adapters/gpt|gemini|grok|qwen|deepseek/` — kerangka + 1 contoh penuh
per model** (engine Reasoning). Masing-masing punya `README.md` yang
menjelaskan konvensi binding skema spesifik model itu (tool-calling
OpenAI-compatible untuk GPT/Grok/DeepSeek, `responseSchema` untuk Gemini,
fallback JSON-in-prompt untuk Qwen), dan `reasoning-engine.md` sebagai
rendering nyata. Tiga engine lain (Planning, Critic, Visual Cognition)
per model mengikuti pola pembungkus identik — dicatat sebagai pekerjaan
mekanis lanjutan, bukan keputusan desain baru, sehingga tidak diulang
manual satu-satu di v0.1 ini.
