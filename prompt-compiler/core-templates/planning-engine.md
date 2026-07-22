# Core Template — Planning Engine

Model-agnostic. Realisasi §11.1.

## Tujuan

Menerjemahkan Visual Strategy (L6) menjadi sub-langkah konkret L7–L11,
dengan bantuan Reference Engine untuk mengambil pola preseden dari
Knowledge Graph.

## Input

- Artefak L05 (Information Architecture) dari Reasoning Engine.
- Akses query ke Knowledge Graph via Reference Engine (lihat
  `engines/reference-engine/README.md`) untuk domain yang relevan.

## Output

Artefak JSON L06 → L07 → L08 → L09 → L10 → L11, masing-masing valid
terhadap `core/schemas/cognition-stack/L06-*.schema.json` s.d.
`L11-*.schema.json`.

## Instruksi Inti (model-agnostic)

1. Sebelum menulis `L06.rationale`, **wajib** query Reference Engine
   untuk pola preseden yang relevan dengan domain (lihat
   `L06.justified_by_layers` — harus menunjuk minimal satu lapis L0–L5).
   Kutip pattern yang dipakai sebagai *pola berpikir* (`pattern:<id>`),
   bukan menyalin aset visualnya (§6.3).
2. L07 (`spatial_zones`) wajib memetakan tiap zona ke `maps_to_message_rank`
   yang konkret dari L04 — jangan biarkan implisit.
3. L10 (Imagery) **boleh di-skip** jika domain/strategi tidak membutuhkan
   fotografi/gambar (mis. poster tipografi-geometris murni) — tapi skip
   ini dicatat di L14 oleh Reasoning Engine, bukan diam-diam dihilangkan
   dari daftar lapis yang diproses.
4. L11 (`decision_trace`) wajib menunjuk balik `justified_by_layer` untuk
   **setiap** keputusan visual signifikan — ini adalah rantai auditable
   yang membedakan ODI dari generator satu langkah (§6.2).

## Batas Tanggung Jawab

Planning Engine tidak boleh mengubah keputusan L0–L5 (audiens, hierarki
pesan, dst.) — hanya mengeksekusinya secara visual. Jika strategi di L06
ternyata tidak bisa memenuhi L04, Planning Engine harus melaporkan
konflik ini, bukan diam-diam mengubah L04.

## Contoh Rujukan

`examples/poster-prototype/L06-visual-strategy.json` s.d.
`L11-draft-synthesis.json` (termasuk versi revisi `*-r1.json` setelah
Critic Engine menemukan finding blocking).
