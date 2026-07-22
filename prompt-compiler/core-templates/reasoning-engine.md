# Core Template — Reasoning Engine

Model-agnostic. Realisasi §11.1: definisi generik dari
`core/cognition-stack/` + skema I/O engine, sebelum diterjemahkan adapter
ke dialek model tertentu.

## Tujuan

Menghasilkan artefak L0–L5 secara berurutan dari satu brief mentah,
masing-masing valid terhadap skema di `core/schemas/cognition-stack/`.

## Input

- Brief mentah (teks bebas dari user).
- (Opsional) artefak lapis sebelumnya, jika melanjutkan sesi yang sudah
  berjalan sebagian.

## Output

Satu artefak JSON per lapis, dalam urutan L0 → L1 → L2 → L3 → L4 → L5.
Setiap artefak harus valid terhadap:

```
core/schemas/cognition-stack/L00-brief-intake.schema.json
core/schemas/cognition-stack/L01-problem-framing.schema.json
core/schemas/cognition-stack/L02-audience-model.schema.json
core/schemas/cognition-stack/L03-brand-voice.schema.json
core/schemas/cognition-stack/L04-message-hierarchy.schema.json
core/schemas/cognition-stack/L05-information-architecture.schema.json
```

## Instruksi Inti (model-agnostic)

1. Jangan mulai lapis N+1 sebelum lapis N valid dan lengkap terhadap
   skemanya.
2. Setiap artefak adalah objek terstruktur sesuai skema — dilarang
   menjawab dengan prosa bebas yang "mengandung" informasi yang sama.
3. Jika brief ambigu, catat di `L00.ambiguities` dan
   `L00.clarifications_needed` secara eksplisit — jangan menebak diam-diam
   dan melanjutkan seolah brief sudah jelas.
4. L01 (`communication_problem`) tidak boleh sekadar mengulang
   `stated_request` dari L00 dengan kata lain — ia harus menjawab
   "masalah komunikasi apa yang sesungguhnya," bukan restatement brief.
5. `rejected_framings` (L01) dan `rejected_alternatives` (dipakai lagi di
   L06 oleh Planning Engine) wajib diisi minimal satu — bukti bahwa
   alternatif benar-benar dipertimbangkan, bukan langsung ke satu jawaban.

## Batas Tanggung Jawab

Reasoning Engine berhenti di L05. Tidak boleh membuat keputusan visual
konkret (grid, tipografi, warna) — itu dimulai Planning Engine di L06.

## Contoh Rujukan

Lihat `examples/poster-prototype/L00-brief-intake.json` s.d.
`L05-information-architecture.json` untuk contoh nyata yang valid
terhadap skema di atas.
