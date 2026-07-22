# Gemini Adapter — Planning Engine

Rendering Gemini dari `prompt-compiler/core-templates/planning-engine.md`.

```json
{
  "model": "gemini-...",
  "systemInstruction": "Kamu adalah Planning Engine dalam framework ODI. Tugasmu: menerjemahkan Visual Strategy (L6) menjadi sub-langkah konkret L7-L11, dibantu Reference Engine untuk pola preseden dari Knowledge Graph.\n\nAturan:\n1. Query Reference Engine (via functionDeclarations 'query_reference_engine') sebelum menulis L06.rationale. Kutip pattern sebagai 'pattern:<id>' — pola berpikir, BUKAN aset visual.\n2. L07.spatial_zones[].maps_to_message_rank wajib rank konkret dari L04.\n3. L10 boleh dilewati jika tidak butuh imagery — laporkan eksplisit.\n4. L11.decision_trace[] wajib justified_by_layer valid.",
  "tools": [
    {"functionDeclarations": [{"name": "query_reference_engine", "parameters": {"type": "object", "properties": {"domain": {"type": "string"}, "strategy_hint": {"type": "string"}}, "required": ["domain"]}}]}
  ],
  "contents": [{"role": "user", "parts": [{"text": "<< L05-information-architecture.json disematkan di sini >>"}]}],
  "generationConfig": {"responseMimeType": "application/json", "responseSchema": "<< isi L06-visual-strategy.schema.json >>"}
}
```

Lapis berikutnya (L07-L11) mengulang pola, mengganti `responseSchema`
sesuai skema lapisnya. Contoh hasil nyata:
`examples/poster-prototype/L06-visual-strategy.json`.
