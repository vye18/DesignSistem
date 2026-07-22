# Gemini Adapter

Realisasi §7.3, §9, §11.1 untuk model keluarga Gemini (Google GenAI API).

## Yang Diterjemahkan Adapter Ini

1. **Format pemanggilan tool** — skema di `core/schemas/cognition-stack/`
   dibind sebagai `responseSchema` (structured output mode) atau
   `tools[].functionDeclarations[].parameters`, tergantung apakah panggilan
   memakai `generateContent` mode JSON langsung atau function-calling.
2. **Gaya instruksi** — instruksi ditempatkan di `systemInstruction`,
   dipisah jelas dari `contents` (data/riwayat artefak lapis sebelumnya).
3. **Batas konteks** — sama seperti adapter lain: hanya artefak lapis
   relevan yang disertakan.

Logika kognisi **tidak diulang di sini** — tetap di
`prompt-compiler/core-templates/*.md`.

## Pola Umum per Engine

```json
{
  "model": "gemini-...",
  "systemInstruction": "<instruksi dari core-templates/*.md>",
  "contents": [{"role": "user", "parts": [{"text": "<artefak lapis sebelumnya, sebagai JSON>"}]}],
  "generationConfig": {
    "responseMimeType": "application/json",
    "responseSchema": "<< isi $id skema lapis ini >>"
  }
}
```

## Status

Kerangka pembungkus siap. Lihat `reasoning-engine.md` untuk satu contoh
penuh; tiga engine lain mengikuti pola pembungkus yang sama, hanya
`responseSchema` yang berganti sesuai skema lapisnya.
