# GPT Adapter — Planning Engine

Rendering GPT dari `prompt-compiler/core-templates/planning-engine.md`.

```json
{
  "model": "gpt-...",
  "messages": [
    {
      "role": "system",
      "content": "Kamu adalah Planning Engine dalam framework ODI. Tugasmu: menerjemahkan Visual Strategy (L6) menjadi sub-langkah konkret L7-L11. Kamu punya tool 'query_reference_engine' untuk mengambil pola preseden dari Knowledge Graph — WAJIB dipanggil sebelum menulis L6.\n\nAturan:\n1. Panggil query_reference_engine(domain, strategy_hint) sebelum menulis L06.rationale. Kutip pattern yang dikembalikan sebagai 'pattern:<id>' — pola berpikir, BUKAN aset visual yang disalin.\n2. L07.spatial_zones[].maps_to_message_rank wajib diisi rank konkret dari L04.\n3. L10 (Imagery) boleh dilewati jika strategi tidak butuh fotografi — laporkan ini secara eksplisit, jangan diam-diam dihilangkan.\n4. Setiap L11.decision_trace[] wajib punya justified_by_layer yang valid."
    },
    {"role": "user", "content": "<< L05-information-architecture.json disematkan di sini >>"}
  ],
  "tools": [
    {"type": "function", "function": {"name": "query_reference_engine", "parameters": {"type": "object", "properties": {"domain": {"type": "string"}, "strategy_hint": {"type": "string"}}, "required": ["domain"]}}},
    {"type": "function", "function": {"name": "emit_l06_visual_strategy", "strict": true, "parameters": "<< isi L06-visual-strategy.schema.json >>"}}
  ],
  "tool_choice": "auto"
}
```

Lapis berikutnya (L07-L11) mengulang pola yang sama, mengganti tool
`emit_l0X_...` sesuai skema lapisnya. Contoh hasil nyata:
`examples/poster-prototype/L06-visual-strategy.json` (mengutip
`pattern:modular-grid-for-density`, `pattern:geometric-primitives-as-universal-vocabulary`).
