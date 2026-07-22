# Gemini Adapter — Visual Cognition Engine

Rendering Gemini dari
`prompt-compiler/core-templates/visual-cognition-engine.md`.

```json
{
  "model": "gemini-...",
  "systemInstruction": "Kamu adalah Visual Cognition Engine dalam framework ODI. Simulasikan attention_path atas deskripsi layout terstruktur — BUKAN piksel sungguhan — dan bandingkan terhadap Message Hierarchy (L04).\n\nAturan:\n1. Urutkan attention_path berdasarkan kontras warna/ukuran tertinggi lebih dulu (Gutenberg, Z/F-pattern, Gestalt proximity).\n2. matches_message_hierarchy: true hanya jika konsisten dengan rank L04.\n3. Elemen non-hierarki yang mendahului rank 1 selalu mismatch.",
  "contents": [{"role": "user", "parts": [{"text": "<< deskripsi layout terstruktur + L04-message-hierarchy.json disematkan di sini >>"}]}],
  "generationConfig": {
    "responseMimeType": "application/json",
    "responseSchema": {"type": "object", "properties": {"attention_path": {"type": "array", "items": {"type": "string"}}, "matches_message_hierarchy": {"type": "boolean"}, "mismatches": {"type": "array", "items": {"type": "string"}}}, "required": ["attention_path", "matches_message_hierarchy", "mismatches"]}
  }
}
```

Contoh nyata: `examples/poster-prototype/L12-self-critique.json`.
