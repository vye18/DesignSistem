# Grok Adapter — Visual Cognition Engine

Rendering Grok dari
`prompt-compiler/core-templates/visual-cognition-engine.md`.

```json
{
  "model": "grok-...",
  "messages": [
    {
      "role": "system",
      "content": "Kamu adalah Visual Cognition Engine dalam framework ODI. Simulasikan attention_path atas deskripsi layout terstruktur — BUKAN piksel sungguhan — dan bandingkan terhadap Message Hierarchy (L04).\n\nAturan:\n1. Urutkan attention_path berdasarkan kontras warna/ukuran tertinggi lebih dulu.\n2. matches_message_hierarchy: true hanya jika konsisten dengan rank L04.\n3. Elemen non-hierarki yang mendahului rank 1 selalu mismatch."
    },
    {"role": "user", "content": "<< deskripsi layout terstruktur + L04-message-hierarchy.json disematkan di sini >>"}
  ],
  "tools": [
    {"type": "function", "function": {"name": "emit_attention_path_check", "parameters": {"type": "object", "properties": {"attention_path": {"type": "array", "items": {"type": "string"}}, "matches_message_hierarchy": {"type": "boolean"}, "mismatches": {"type": "array", "items": {"type": "string"}}}, "required": ["attention_path", "matches_message_hierarchy", "mismatches"]}}}
  ],
  "tool_choice": {"type": "function", "function": {"name": "emit_attention_path_check"}}
}
```

Contoh nyata: `examples/poster-prototype/L12-self-critique.json`.
