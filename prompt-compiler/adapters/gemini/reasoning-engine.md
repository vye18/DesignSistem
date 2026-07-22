# Gemini Adapter — Reasoning Engine

Rendering Gemini dari `prompt-compiler/core-templates/reasoning-engine.md`,
giliran L0, brief `examples/poster-prototype/brief.md`.

```json
{
  "model": "gemini-...",
  "systemInstruction": "Kamu adalah Reasoning Engine dalam framework ODI. Tugasmu: mengubah brief mentah menjadi artefak L0-L5 secara berurutan. Kamu TIDAK boleh membuat keputusan visual konkret — itu ranah Planning Engine.\n\nAturan:\n1. Jangan mulai lapis N+1 sebelum lapis N valid dan lengkap terhadap skemanya.\n2. Jawab HANYA sesuai responseSchema yang aktif untuk lapis ini.\n3. Jika brief ambigu, isi 'ambiguities' dan 'clarifications_needed' di L0 secara eksplisit. Jangan menebak diam-diam.\n4. 'communication_problem' di L1 harus menjawab masalah komunikasi sesungguhnya, bukan mengulang stated_request.\n5. Isi minimal satu 'rejected_framings' di L1.\nProses satu lapis per giliran.",
  "contents": [
    {
      "role": "user",
      "parts": [{"text": "raw_brief: \"Bikin poster untuk pameran desain grafis mahasiswa akhir tahun, temanya \\\"Bentuk & Fungsi\\\". Informasinya: nama acara, tanggal, lokasi, cara daftar (QR code), dan nama sponsor utama kampus.\""}]
    }
  ],
  "generationConfig": {
    "responseMimeType": "application/json",
    "responseSchema": "<< isi file skema L00-brief-intake.schema.json apa adanya >>"
  }
}
```

Hasil yang diharapkan: identik secara struktural dengan
`examples/poster-prototype/L00-brief-intake.json`. Giliran L1-L5
mengulang pola yang sama: ganti `responseSchema` ke skema lapis berikutnya,
tambahkan artefak lapis sebelumnya ke `contents`.
