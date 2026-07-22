# Qwen Adapter — Planning Engine

Rendering Qwen dari `prompt-compiler/core-templates/planning-engine.md`,
varian fallback JSON-in-prompt.

```json
{
  "model": "qwen-...",
  "messages": [
    {
      "role": "system",
      "content": "Kamu adalah Planning Engine dalam framework ODI. Terjemahkan Visual Strategy (L6) menjadi sub-langkah konkret L7-L11.\n\nAturan:\n1. Sebelum menulis L06.rationale, jelaskan dulu pola preseden yang relevan (dari Knowledge Graph) dalam field terpisah 'reference_notes' di luar objek utama, kutip sebagai 'pattern:<id>' — pola berpikir, BUKAN aset visual.\n2. L07.spatial_zones[].maps_to_message_rank wajib rank konkret dari L04.\n3. L10 boleh dilewati jika tidak butuh imagery — laporkan eksplisit.\n4. Balas HANYA dengan satu objek JSON valid terhadap skema berikut:\n<< isi L06-visual-strategy.schema.json >>"
    },
    {"role": "user", "content": "<< L05-information-architecture.json disematkan di sini >>"}
  ],
  "response_format": {"type": "json_object"}
}
```

Jika deployment mendukung tool-calling penuh, pakai bentuk `tools[]`
seperti `adapters/gpt/planning-engine.md` — lebih diutamakan. Contoh
hasil nyata: `examples/poster-prototype/L06-visual-strategy.json`.
