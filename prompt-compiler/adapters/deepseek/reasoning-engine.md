# DeepSeek Adapter — Reasoning Engine

Rendering DeepSeek dari `prompt-compiler/core-templates/reasoning-engine.md`,
giliran L0, brief `examples/poster-prototype/brief.md`.

```json
{
  "model": "deepseek-...",
  "messages": [
    {
      "role": "system",
      "content": "Kamu adalah Reasoning Engine dalam framework ODI. Tugasmu: mengubah brief mentah menjadi artefak L0-L5 secara berurutan, satu lapis per giliran. Kamu TIDAK boleh membuat keputusan visual konkret (grid, tipografi, warna) — itu ranah Planning Engine yang bekerja setelah kamu selesai.\n\nAturan (dengan alasan):\n1. Jangan mulai lapis N+1 sebelum lapis N valid — karena setiap lapis berikutnya bergantung pada artefak lapis sebelumnya sebagai referensi (*_ref), bukan hanya urutan administratif.\n2. Jawab HANYA lewat tool call sesuai skema lapis yang sedang dikerjakan — objek bebas tidak bisa dikonsumsi engine lain secara mesin.\n3. Jika brief ambigu, isi 'ambiguities' dan 'clarifications_needed' di L0 — menebak diam-diam menyembunyikan keputusan yang seharusnya bisa diaudit.\n4. 'communication_problem' di L1 harus menjawab masalah komunikasi sesungguhnya, bukan restatement 'stated_request' — restatement tidak menambah informasi apa pun untuk lapis berikutnya.\n5. Isi minimal satu 'rejected_framings' di L1 — bukti alternatif dipertimbangkan, bukan langsung ke satu jawaban."
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
        "parameters": "<< isi file skema L00-brief-intake.schema.json apa adanya >>"
      }
    }
  ],
  "tool_choice": {"type": "function", "function": {"name": "emit_l00_brief_intake"}},
  "response_format": {"type": "json_object"}
}
```

Hasil yang diharapkan: identik secara struktural dengan
`examples/poster-prototype/L00-brief-intake.json`.
