# GPT Adapter — Visual Cognition Engine

Rendering GPT dari
`prompt-compiler/core-templates/visual-cognition-engine.md`.

```json
{
  "model": "gpt-...",
  "messages": [
    {
      "role": "system",
      "content": "Kamu adalah Visual Cognition Engine dalam framework ODI. Simulasikan jalur perhatian visual (attention_path) atas deskripsi layout terstruktur — BUKAN piksel sungguhan — dan bandingkan terhadap Message Hierarchy (L04).\n\nAturan:\n1. Urutkan attention_path berdasarkan kontras warna/ukuran tertinggi menarik mata lebih dulu (Gutenberg, Z/F-pattern, Gestalt proximity), bukan urutan 'seharusnya' menurut L04.\n2. matches_message_hierarchy: true hanya jika urutan attention_path konsisten dengan rank di L04.\n3. Elemen non-hierarki yang mendahului rank 1 SELALU dicatat sebagai mismatch."
    },
    {"role": "user", "content": "<< deskripsi layout terstruktur (draft-v1.md) + L04-message-hierarchy.json disematkan di sini >>"}
  ],
  "tools": [
    {"type": "function", "function": {"name": "emit_attention_path_check", "strict": true, "parameters": {"type": "object", "properties": {"attention_path": {"type": "array", "items": {"type": "string"}}, "matches_message_hierarchy": {"type": "boolean"}, "mismatches": {"type": "array", "items": {"type": "string"}}}, "required": ["attention_path", "matches_message_hierarchy", "mismatches"]}}}
  ],
  "tool_choice": {"type": "function", "function": {"name": "emit_attention_path_check"}}
}
```

Contoh nyata: `examples/poster-prototype/L12-self-critique.json` —
`bentuk-geometris-aksen` (bukan bagian L04) mendahului `judul-acara`
(rank 1) → `matches_message_hierarchy: false`.
