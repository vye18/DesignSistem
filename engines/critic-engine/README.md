# Critic Engine

Realisasi §10.3.

## Tanggung Jawab

Mengevaluasi draf (**L11**) dari sudut pandang lapis-lapis awal, bukan dari
selera estetika bebas. Pertanyaan wajib yang diajukan Critic Engine:

1. Apakah hierarki visual benar-benar cocok dengan Message Hierarchy (L4)?
   — dicek silang dengan output Visual Cognition Engine (`attention_path`).
2. Apakah ada elemen yang melanggar batas Brand & Voice (L3)?
3. Apakah Audience Model (L2) benar-benar terlayani (mis. kontras cukup
   untuk konteks pembacaan yang disebutkan)?

## Kontrak I/O

| | Schema |
|---|---|
| Input | `L11-draft-synthesis.schema.json` + output Visual Cognition Engine |
| Output | `L12-self-critique.schema.json` |

Setiap `findings[]` di output **wajib** menunjuk balik ke `layer_ref`
spesifik (L0–L11) yang gagal — ini yang memungkinkan Revision Loop (L13)
presisi kembali ke lapis yang gagal, bukan mengulang semua dari L11 secara
membabi buta.

## Aturan

- `pass: true` hanya jika tidak ada finding berseverity `blocking`.
- Critic Engine tidak boleh memperbaiki draf sendiri — ia hanya melaporkan
  temuan. Perbaikan adalah tanggung jawab Reasoning/Planning Engine lewat
  Revision Loop.

## Status

Kontrak (skema I/O) sudah didefinisikan. Implementasi menunggu Volume 4
(§14 Roadmap).
