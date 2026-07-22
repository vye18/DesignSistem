# Planning Engine

Realisasi §10.2.

## Tanggung Jawab

Menerjemahkan Visual Strategy (**L6**) menjadi sub-langkah konkret dan
berurutan untuk **L7–L11** (Composition & Grid, Typography, Color &
Contrast, Imagery, Draft Synthesis), dengan tiap sub-langkah membawa
referensi ke lapis mana di atasnya (L0–L6) yang ia penuhi.

## Berinteraksi Dengan

- **Reference Engine** — mencari pola preseden yang relevan dengan domain
  & strategi visual terpilih (lihat `engines/reference-engine/README.md`).
- **Knowledge Graph** — mengambil node `Pattern` yang cocok via relasi
  `applies_to`.

## Kontrak I/O

| | Schema |
|---|---|
| Input | Output Reasoning Engine (`L05-information-architecture.schema.json`) |
| Output | `L06` s.d. `L11` schema (`core/schemas/cognition-stack/`), berurutan |

## Bukan Tanggung Jawabnya

- Menentukan hierarki pesan atau audiens — itu sudah dikunci di L0–L5,
  Planning Engine tidak boleh mengubahnya, hanya mengeksekusinya.
- Mengkritik hasil sendiri — itu ranah Critic Engine.

## Status

Kontrak (skema I/O) sudah didefinisikan. Implementasi menunggu Volume 3
(§14 Roadmap), setelah domain prototipe pertama disepakati (§16 butir 3).
