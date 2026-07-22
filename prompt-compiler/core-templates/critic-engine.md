# Core Template — Critic Engine

Model-agnostic. Realisasi §11.1.

## Tujuan

Mengevaluasi draf (L11) dari sudut pandang L1–L4, menghasilkan `L12`, dan
— jika gagal — memicu Revision Loop (`L13`) yang menunjuk lapis spesifik
yang harus diulang.

## Input

- Artefak `L11-draft-synthesis` beserta seluruh artefak L00–L10 yang
  menjadi rujukannya.
- Output Visual Cognition Engine (`attention_path_check`) sebagai bagian
  dari evaluasi.

## Output

- `L12-self-critique.schema.json`.
- Jika `pass: false`: `L13-revision-loop.schema.json`, dengan
  `target_layer` menunjuk lapis spesifik yang gagal (bukan selalu L11).

## Instruksi Inti (model-agnostic)

1. Evaluasi **tidak boleh** berdasarkan selera estetika bebas. Setiap
   `findings[].issue` wajib bisa dijawab: "melanggar bagian mana dari
   L1–L4?"
2. Severity `blocking` hanya untuk pelanggaran yang benar-benar mencegah
   pesan tersampaikan sesuai L4, atau melanggar batas keras L3
   (`forbidden_elements`). Selera personal bukan alasan `blocking`.
3. Jika `attention_path_check.matches_message_hierarchy` adalah `false`,
   ini **wajib** menjadi finding minimal `major`, karena berarti hierarki
   visual yang dibangun Planning Engine gagal melayani L04.
4. `pass: true` **hanya** jika tidak ada finding `blocking`. Finding
   `minor`/`major` boleh dicatat tanpa memblokir, tapi harus tetap
   muncul di output (transparansi, bukan disembunyikan).
5. Ketika membuat `L13`, `target_layer` harus lapis **paling awal** yang
   menyebabkan kegagalan akar — bukan lapis tempat gejalanya paling
   terlihat. (Contoh: gejala terlihat di L11/draft, tapi akar masalah ada
   di keputusan warna L09 — maka `target_layer: "L09"`.)

## Batas Tanggung Jawab

Critic Engine **tidak memperbaiki draf sendiri**. Ia hanya melaporkan
temuan terstruktur. Perbaikan adalah tanggung jawab Reasoning/Planning
Engine lewat Revision Loop.

## Contoh Rujukan

`examples/poster-prototype/L12-self-critique.json` (gagal, `pass: false`)
→ `L13-revision-loop.json` (`target_layer: "L09"`) →
`L12-self-critique-r1.json` (lolos, `pass: true`).
