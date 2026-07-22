# GPT Adapter — Reasoning Engine

Rendering GPT dari `prompt-compiler/core-templates/reasoning-engine.md`,
dicontohkan untuk brief `examples/poster-prototype/brief.md`, giliran L0.

```json
{
  "model": "gpt-...",
  "messages": [
    {
      "role": "system",
      "content": "Kamu adalah Reasoning Engine dalam framework ODI. Tugasmu: mengubah brief mentah menjadi artefak L0-L5 secara berurutan. Kamu TIDAK boleh membuat keputusan visual konkret — itu ranah Planning Engine.\n\nAturan:\n1. Jangan mulai lapis N+1 sebelum lapis N valid dan lengkap terhadap skemanya.\n2. Jawab HANYA lewat tool call sesuai skema lapis yang sedang dikerjakan.\n3. Jika brief ambigu, isi 'ambiguities' dan 'clarifications_needed' di L0 secara eksplisit. Jangan menebak diam-diam.\n4. 'communication_problem' di L1 harus menjawab masalah komunikasi sesungguhnya, bukan mengulang stated_request.\n5. Isi minimal satu 'rejected_framings' di L1.\nProses satu lapis per giliran; tunggu konfirmasi sebelum lanjut ke lapis berikutnya."
    },
    {
      "role": "user",
      "content": "raw_brief: \"Bikin poster untuk pameran desain grafis mahasiswa akhir tahun, temanya \\\"Bentuk & Fungsi\\\". Informasinya: nama acara, tanggal, lokasi, cara daftar (QR code), dan nama sponsor utama kampus.\""
    }
  ],
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "emit_l00_brief_intake",
        "description": "Emit artefak L0 Brief Intake sesuai core/schemas/cognition-stack/L00-brief-intake.schema.json",
        "strict": true,
        "parameters": "<< isi file skema L00-brief-intake.schema.json apa adanya >>"
      }
    }
  ],
  "tool_choice": {"type": "function", "function": {"name": "emit_l00_brief_intake"}}
}
```

Hasil yang diharapkan: identik secara struktural dengan
`examples/poster-prototype/L00-brief-intake.json`. Giliran L1-L5
mengulang pola yang sama: ganti `tools[].function.name`/`parameters` ke
skema lapis berikutnya, tambahkan artefak lapis sebelumnya ke pesan
`user`.
