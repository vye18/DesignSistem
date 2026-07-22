# Core Schemas

Realisasi §8.2 (tipe node graph), §16 butir 1 (skema per lapis kognisi), dan
kontrak I/O antar-engine (§9.3).

```
core/schemas/
├── cognition-stack/     # Skema artefak L0-L14 — kontrak Reasoning ↔ Planning ↔ Critic ↔ Visual Cognition Engine
└── knowledge-graph/     # Skema tipe node (§8.2) dan edge (§8.3)
```

## Status

**Draft — kandidat lock, belum di-*sign-off*.** Sesuai §16, tiga hal harus
dikunci sebelum Volume 2 (Reference Engine + Knowledge Graph Seed) dimulai:

1. ✅ *(draft)* Skema objek data per lapis kognisi L0–L14 — ada di
   `cognition-stack/`.
2. 🟡 *(sebagian draft)* Format penyimpanan Knowledge Graph — skema node/edge
   ada di `knowledge-graph/`, tapi format final (Markdown+JSONL vs
   alternatif) baru divalidasi setelah ada data seed nyata (Volume 2).
3. ⬜ Domain pertama untuk prototipe — direkomendasikan **poster/single-page**
   (lihat README root), belum diputuskan final oleh maintainer.

## Aturan Versi Skema

- Perubahan pada field wajib (`required`) di skema manapun adalah perubahan
  **MAJOR** terhadap spec (§13) — memutus kontrak antar-engine yang ada.
- Penambahan field opsional adalah **MINOR**.
- Setiap skema mendeklarasikan `$id` sendiri; engine memvalidasi artefak
  yang diterima/dikirim terhadap `$id` yang relevan, bukan berasumsi bentuk
  implisit.

## Prinsip Dependency (§9.2)

`core/schemas` tidak bergantung pada modul lain di repo ini. `engines/*`
bergantung padanya (via referensi `$id`), tidak sebaliknya.
