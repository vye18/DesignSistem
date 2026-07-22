# Qwen Adapter — Reasoning Engine

Rendering Qwen dari `prompt-compiler/core-templates/reasoning-engine.md`,
varian fallback JSON-in-prompt (dipakai ketika tool-calling penuh tidak
tersedia), giliran L0, brief `examples/poster-prototype/brief.md`.

```json
{
  "model": "qwen-...",
  "messages": [
    {
      "role": "system",
      "content": "Kamu adalah Reasoning Engine dalam framework ODI. Tugasmu: mengubah brief mentah menjadi artefak L0-L5 secara berurutan. Kamu TIDAK boleh membuat keputusan visual konkret — itu ranah Planning Engine.\n\nAturan:\n1. Jangan mulai lapis N+1 sebelum lapis N valid dan lengkap terhadap skemanya.\n2. Balas HANYA dengan satu objek JSON valid terhadap skema berikut, tanpa teks lain di luar JSON:\n<< isi file skema L00-brief-intake.schema.json apa adanya >>\n3. Jika brief ambigu, isi 'ambiguities' dan 'clarifications_needed' secara eksplisit. Jangan menebak diam-diam.\n4. Proses satu lapis per giliran."
    },
    {
      "role": "user",
      "content": "raw_brief: \"Bikin poster untuk pameran desain grafis mahasiswa akhir tahun, temanya \\\"Bentuk & Fungsi\\\". Informasinya: nama acara, tanggal, lokasi, cara daftar (QR code), dan nama sponsor utama kampus.\""
    }
  ],
  "response_format": {"type": "json_object"}
}
```

Jika deployment Qwen yang dipakai mendukung tool-calling penuh
(OpenAI-compatible mode), pakai bentuk `tools[]` yang sama seperti
`adapters/gpt/reasoning-engine.md` — lebih diutamakan karena validasi
struktural terjadi di sisi provider, bukan hanya lewat instruksi prompt.

Hasil yang diharapkan: identik secara struktural dengan
`examples/poster-prototype/L00-brief-intake.json`.
