# DeepSeek Adapter — Visual Cognition Engine

Rendering DeepSeek dari
`prompt-compiler/core-templates/visual-cognition-engine.md`.

```json
{
  "model": "deepseek-...",
  "messages": [
    {
      "role": "system",
      "content": "Kamu adalah Visual Cognition Engine dalam framework ODI. Simulasikan attention_path atas deskripsi layout terstruktur — BUKAN piksel sungguhan (batasan v0.1) — dan bandingkan terhadap Message Hierarchy (L04).\n\nAturan:\n1. Urutkan attention_path berdasarkan kontras warna/ukuran tertinggi lebih dulu (Gutenberg, Z/F-pattern, Gestalt proximity) — bukan urutan 'seharusnya' menurut L04, karena tujuan simulasi ini justru mendeteksi ketika keduanya berbeda.\n2. matches_message_hierarchy: true hanya jika urutan konsisten dengan rank L04.\n3. Elemen non-hierarki yang mendahului rank 1 selalu dicatat sebagai mismatch, sekecil apa pun selisih kontrasnya."
    },
    {"role": "user", "content": "<< deskripsi layout terstruktur + L04-message-hierarchy.json disematkan di sini >>"}
  ],
  "tools": [
    {"type": "function", "function": {"name": "emit_attention_path_check", "parameters": {"type": "object", "properties": {"attention_path": {"type": "array", "items": {"type": "string"}}, "matches_message_hierarchy": {"type": "boolean"}, "mismatches": {"type": "array", "items": {"type": "string"}}}, "required": ["attention_path", "matches_message_hierarchy", "mismatches"]}}}
  ],
  "response_format": {"type": "json_object"}
}
```

Contoh nyata: `examples/poster-prototype/L12-self-critique.json`.
