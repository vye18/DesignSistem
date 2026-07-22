# Reasoning Engine

Realisasi §10.1.

## Tanggung Jawab

Menegakkan urutan Cognition Stack (§5), mengubah brief mentah menjadi
artefak terstruktur di tiap lapis **L0–L5** (Brief Intake → Problem Framing
→ Audience Model → Brand & Voice → Message Hierarchy → Information
Architecture), dan menghasilkan *decision trace* awal (§6.2).

## Bukan Tanggung Jawabnya

- Memutuskan pilihan visual konkret (grid, tipografi, warna, imagery) — itu
  ranah **Planning Engine**.
- Mengevaluasi draf akhir — itu ranah **Critic Engine**.
- Mensimulasikan jalur perhatian visual — itu ranah **Visual Cognition
  Engine**.

## Kontrak I/O

| | Schema |
|---|---|
| Input | `L00-brief-intake.schema.json` (brief mentah dari user) |
| Output | `L00` s.d. `L05` schema (`core/schemas/cognition-stack/`), berurutan |

Setiap output juga menjadi input bagi lapis berikutnya di engine yang sama,
dan L05 menjadi input Planning Engine.

## Kegagalan yang Harus Dicegah

- **Lapis dilompati** — mis. menyimpulkan Message Hierarchy (L4) tanpa
  Audience Model (L2) yang valid.
- **Artefak berbentuk teks naratif bebas** alih-alih objek terstruktur
  sesuai skema — ini yang membuat engine lain tidak bisa mengonsumsinya.
- **Menebak diam-diam** ketika brief ambigu — `ambiguities[]` di L0 wajib
  diisi eksplisit, bukan diselesaikan sepihak tanpa dicatat.

## Status

Kontrak (skema I/O) sudah didefinisikan. Implementasi (prompt/kode yang
benar-benar menjalankan engine ini lewat model) belum ada — menunggu
Volume 3 (§14 Roadmap).
