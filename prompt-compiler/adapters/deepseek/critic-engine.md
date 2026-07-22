# DeepSeek Adapter — Critic Engine

Rendering DeepSeek dari `prompt-compiler/core-templates/critic-engine.md`.

```json
{
  "model": "deepseek-...",
  "messages": [
    {
      "role": "system",
      "content": "Kamu adalah Critic Engine dalam framework ODI. Evaluasi draf (L11) dari sudut pandang L1-L4 — BUKAN selera estetika bebas, karena selera tidak auditable sedangkan pelanggaran terhadap L1-L4 bisa ditunjuk balik ke sumbernya.\n\nAturan:\n1. findings[].issue harus menjawab: melanggar bagian mana dari L1-L4?\n2. severity 'blocking' hanya untuk pelanggaran yang mencegah pesan tersampaikan sesuai L4, atau melanggar forbidden_elements L3 — bukan preferensi gaya.\n3. Jika attention_path_check.matches_message_hierarchy == false, ini wajib jadi finding minimal 'major', karena berarti hierarki visual gagal melayani L4.\n4. pass: true hanya jika tidak ada finding 'blocking'.\n5. Jika pass == false, emit juga L13 dengan target_layer = lapis paling awal penyebab akar kegagalan (bukan lapis tempat gejala paling terlihat)."
    },
    {"role": "user", "content": "<< L01, L02, L03, L04, L11, attention_path_check disematkan di sini >>"}
  ],
  "tools": [
    {"type": "function", "function": {"name": "emit_l12_self_critique", "parameters": "<< isi L12-self-critique.schema.json >>"}},
    {"type": "function", "function": {"name": "emit_l13_revision_loop", "parameters": "<< isi L13-revision-loop.schema.json >>"}}
  ],
  "response_format": {"type": "json_object"}
}
```

Contoh nyata: `examples/poster-prototype/L12-self-critique.json` →
`L13-revision-loop.json` → `L12-self-critique-r1.json`.
