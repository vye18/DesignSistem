# Visual Cognition Engine

Realisasi §10.4 dan §6.1 (Perceptual Simulation).

## Tanggung Jawab

Simulasi jalur perhatian visual atas draf/komposisi, menghasilkan
*attention path* yang dibandingkan terhadap Message Hierarchy target (L4).
Berdasarkan heuristik perseptual yang mapan secara empiris:

- Gutenberg Diagram
- Z-pattern (layout sederhana)
- F-pattern (teks padat)
- Prinsip Gestalt (pengelompokan)

Jika urutan perhatian yang disimulasikan tidak cocok dengan urutan pesan
yang diinginkan di L4, ini adalah **cacat desain** yang harus diperbaiki di
L7–L9 (Composition/Typography/Color), bukan ditambal di tahap akhir.

## Kontrak I/O

| | Schema |
|---|---|
| Input | Deskripsi layout terstruktur — posisi, ukuran relatif, kontras (bukan piksel mentah di v0.1) + `L04-message-hierarchy.schema.json` sebagai target pembanding |
| Output | Objek `attention_path_check` yang dikonsumsi Critic Engine sebagai bagian dari `L12-self-critique.schema.json` |

## Keterbatasan v0.1 (diakui secara eksplisit, §15)

Engine ini bekerja di atas **deskripsi layout terstruktur**, bukan model
computer vision yang memproses piksel sungguhan. Integrasi vision model
nyata adalah item Future Expansion, di luar cakupan v0.1.

## Status

Kontrak I/O sudah didefinisikan. Implementasi menunggu Volume 4 (§14
Roadmap), bersamaan dengan Critic Engine.
