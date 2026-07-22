# Poster Prototype — Walkthrough Manual L0–L14

Realisasi Volume 3 (Reasoning + Planning Engine — prototipe untuk 1 domain
sempit) dan Volume 4 (Critic Engine + Revision Loop) dari Roadmap §14,
untuk domain yang direkomendasikan §16 butir 3: **poster/single-page**
(`domain:poster`).

> **Yang ini bukan.** Ini bukan implementasi engine otomatis yang
> menjalankan model secara live — belum ada infrastruktur untuk itu di
> repo ini. Ini adalah walkthrough yang ditulis manual, artifact-per-artifact,
> untuk membuktikan bahwa skema (`core/schemas/cognition-stack/`) dan aturan
> struktural Cognition Stack (§5) benar-benar bisa dipatuhi end-to-end pada
> kasus nyata — proof of concept sebelum engine sungguhan ditulis.

## Alur File

| File | Lapis | Catatan |
|---|---|---|
| `brief.md` | — | Brief mentah dari user |
| `L00-brief-intake.json` | L0 | |
| `L01-problem-framing.json` | L1 | |
| `L02-audience-model.json` | L2 | |
| `L03-brand-voice.json` | L3 | |
| `L04-message-hierarchy.json` | L4 | |
| `L05-information-architecture.json` | L5 | |
| `L06-visual-strategy.json` | L6 | Mengutip `pattern:modular-grid-for-density` dan `pattern:geometric-primitives-as-universal-vocabulary` dari Knowledge Graph |
| `L07-composition-grid.json` | L7 | |
| `L08-typography.json` | L8 | |
| `L09-color-contrast.json` | L9 (v1) | **Keputusan berisiko**: warna paling jenuh dipakai pada bentuk aksen, bukan judul |
| `L10` | L10 | **Di-skip secara eksplisit** — dicatat di `L14`, bukan diam-diam (§5) |
| `L11-draft-synthesis.json` + `draft-v1.md` | L11 (v1) | |
| `L12-self-critique.json` | L12 (v1) | **GAGAL** — attention path menyimpang dari Message Hierarchy |
| `L13-revision-loop.json` | L13 | Kembali presisi ke **L09**, bukan mengulang dari L11 |
| `L09-color-contrast-r1.json` | L9 (v2) | Warna jenuh dipindah ke judul |
| `L11-draft-synthesis-r1.json` + `draft-v2.md` | L11 (v2) | |
| `L12-self-critique-r1.json` | L12 (v2) | **LOLOS** |
| `L14-final-lock.json` | L14 | Terkunci, dengan skip L10 tercatat |

## Yang Didemonstrasikan

1. **Tidak ada lapis yang dilompati** — setiap artefak mereferensikan
   artefak lapis sebelumnya lewat field `*_ref`.
2. **Skip gate eksplisit, tercatat** — L10 di-skip dengan justifikasi
   tertulis di `L14.skipped_gates`, bukan sekadar tidak ada.
3. **Decision trace** (§6.2) — setiap keputusan visual di `L11` menunjuk
   balik ke lapis yang menjustifikasinya, termasuk ke pattern Knowledge
   Graph via Reference Engine.
4. **Comparative Pattern Matching bukan copying** (§6.3) — `L06`
   mengutip *pola berpikir* dari Swiss Design dan Bauhaus, bukan aset
   visual mereka.
5. **Self-Critique wajib & presisi** — putaran pertama gagal (`pass: false`)
   dengan finding `blocking` yang menunjuk lapis spesifik (`L09`); Revision
   Loop (`L13`) kembali ke **L09 saja**, bukan mengulang seluruh sintesis
   dari nol — sesuai aturan §5 dan tanggung jawab Critic Engine (§10.3).

## Validasi

Setiap file `L*.json` di folder ini valid terhadap skema yang bersesuaian
di `core/schemas/cognition-stack/L{NN}-*.schema.json` (divalidasi dengan
`jsonschema` saat penulisan; lihat riwayat commit).
