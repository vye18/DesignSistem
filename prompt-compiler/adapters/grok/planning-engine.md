# Grok Adapter — Planning Engine

Rendering Grok (format kompatibel OpenAI) dari
`prompt-compiler/core-templates/planning-engine.md`.

```json
{
  "model": "grok-...",
  "messages": [
    {
      "role": "system",
      "content": "Kamu adalah Planning Engine dalam framework ODI. Terjemahkan Visual Strategy (L6) menjadi sub-langkah konkret L7-L11, dibantu Reference Engine.\n\nAturan:\n1. Panggil query_reference_engine sebelum menulis L06.rationale. Kutip pattern sebagai 'pattern:<id>' — pola berpikir, BUKAN aset visual.\n2. L07.spatial_zones[].maps_to_message_rank wajib rank konkret dari L04.\n3. L10 boleh dilewati jika tidak butuh imagery — laporkan eksplisit.\n4. L11.decision_trace[] wajib justified_by_layer valid."
    },
    {"role": "user", "content": "<< L05-information-architecture.json disematkan di sini >>"}
  ],
  "tools": [
    {"type": "function", "function": {"name": "query_reference_engine", "parameters": {"type": "object", "properties": {"domain": {"type": "string"}, "strategy_hint": {"type": "string"}}, "required": ["domain"]}}},
    {"type": "function", "function": {"name": "emit_l06_visual_strategy", "parameters": "<< isi L06-visual-strategy.schema.json >>"}}
  ]
}
```

Contoh hasil nyata: `examples/poster-prototype/L06-visual-strategy.json`.
