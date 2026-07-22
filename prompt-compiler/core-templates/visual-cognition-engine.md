# Core Template — Visual Cognition Engine

Model-agnostic. Realisasi §11.1 dan §6.1.

## Tujuan

Mensimulasikan jalur perhatian visual (`attention_path`) atas deskripsi
layout terstruktur (bukan piksel — batasan v0.1, §15), dibandingkan
terhadap Message Hierarchy target (L04).

## Input

- Deskripsi layout terstruktur: posisi relatif, ukuran relatif, dan
  kontras (warna/berat visual) tiap elemen — bukan gambar mentah.
- `L04-message-hierarchy.schema.json` sebagai target pembanding.

## Output

Objek `attention_path_check` (dikonsumsi Critic Engine sebagai bagian dari
`L12-self-critique.schema.json`):

```json
{
  "attention_path": ["elemen-1", "elemen-2", "..."],
  "matches_message_hierarchy": true,
  "mismatches": []
}
```

## Instruksi Inti (model-agnostic)

1. Urutkan `attention_path` berdasarkan heuristik perseptual yang mapan:
   kontras warna/ukuran tertinggi menarik mata lebih dulu (Gutenberg
   Diagram, Z/F-pattern, Gestalt proximity) — bukan berdasarkan urutan
   yang "seharusnya" menurut L04.
2. `matches_message_hierarchy` adalah `true` hanya jika urutan
   `attention_path` konsisten dengan urutan `rank` di L04 untuk elemen
   yang termasuk dalam Message Hierarchy.
3. Elemen yang **tidak** ada di L04 (mis. elemen dekoratif) tetap boleh
   masuk `attention_path` — dan justru harus ditandai sebagai `mismatch`
   jika elemen non-message itu menarik mata lebih dulu daripada elemen
   rank 1.
4. Jangan menyimpulkan "cukup dekat" sebagai match. Jika ada elemen
   non-hierarki yang mendahului rank 1, itu **selalu** mismatch, sekecil
   apa pun selisih kontrasnya — deteksi ini yang membedakan simulasi dari
   sekadar checklist "sudah pakai grid."

## Keterbatasan v0.1

Simulasi berbasis heuristik perseptual, bukan model vision berbasis
piksel. Lihat §15 (Future Expansion).

## Contoh Rujukan

`examples/poster-prototype/L12-self-critique.json` — `attention_path`
menempatkan `bentuk-geometris-aksen` (bukan bagian L04) sebelum
`judul-acara` (rank 1) → `matches_message_hierarchy: false`.
