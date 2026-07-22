# Knowledge Graph

Realisasi §8. Markdown adalah *source of truth* yang dapat dibaca dan
diedit manusia; `edges/edges.jsonl` dan `index/graph.db` adalah artefak
turunan yang **di-generate**, bukan diedit manual.

```
knowledge-graph/
├── nodes/
│   ├── principles/*.md      (frontmatter sesuai core/schemas/knowledge-graph/principle.schema.json)
│   ├── patterns/*.md         (→ pattern.schema.json)
│   ├── case-studies/*.md     (→ case-study.schema.json)
│   ├── systems/*.md          (→ system.schema.json)
│   ├── domains/*.md          (→ domain.schema.json)
│   └── benchmarks/*.md       (→ benchmark.schema.json)
├── edges/
│   └── edges.jsonl           (satu baris per edge, → edge.schema.json)
├── build_graph.py             (compile nodes+edges → index/graph.db; validasi referensial)
└── index/
    └── (graph.db — generated, tidak di-commit; lihat .gitignore)
```

Jalankan `python3 knowledge-graph/build_graph.py` dari root repo untuk
memvalidasi dan mengompilasi graph. Skrip gagal (`exit 1`) jika ada node
yatim referensial (edge menunjuk id yang tidak ada) atau id duplikat.

## Mengapa Graph, Bukan Folder Datar (§8.1)

Dengan target 5000 markdown, 10.000 gambar, 500 studi kasus, dan 100
benchmark, folder datar gagal di dua hal: (1) relasi lintas-dokumen (mis.
satu prinsip whitespace dipakai di 40 studi kasus dari 6 sistem berbeda)
tidak bisa direpresentasikan sebagai path folder; (2) pencarian pola
membutuhkan query relasional, bukan file listing.

## Tipe Node (§8.2) → Skema

| Node | Skema |
|---|---|
| Principle | `core/schemas/knowledge-graph/principle.schema.json` |
| Pattern | `core/schemas/knowledge-graph/pattern.schema.json` |
| CaseStudy | `core/schemas/knowledge-graph/case-study.schema.json` |
| System | `core/schemas/knowledge-graph/system.schema.json` |
| Engine | `core/schemas/knowledge-graph/engine.schema.json` |
| Benchmark | `core/schemas/knowledge-graph/benchmark.schema.json` |
| Domain | `core/schemas/knowledge-graph/domain.schema.json` |

## Tipe Relasi (§8.3)

```
Principle  --justifies-->      Pattern
Pattern    --observed_in-->    CaseStudy
CaseStudy  --belongs_to-->     System
Pattern    --applies_to-->     Domain
Benchmark  --tests-->          Principle | Pattern
Engine     --implements-->     Principle | Pattern
CaseStudy  --contradicts-->    CaseStudy
Pattern    --supersedes-->     Pattern
```

`contradicts` wajib direpresentasikan eksplisit ketika ada — desain penuh
trade-off, dan graph ODI tidak berpura-pura ada satu jawaban benar tunggal.

## QA Struktural Sebelum Node Masuk Graph (§12.1)

Setiap node baru dari kontribusi terbuka wajib lolos:

1. **Traceability check** — terhubung ke minimal satu `Principle` yang
   sudah ada (tidak boleh node yatim).
2. **Non-duplication check** — jika pola serupa sudah ada, harus jadi
   relasi `supersedes`, bukan duplikat baru.
3. **Copyright/asset check** — gambar di `CaseStudy` hanya untuk analisis
   pola dengan atribusi, bukan reproduksi utuh karya berlisensi.

Lihat `contrib/CONTRIBUTING.md` untuk proses lengkap.

## Seed Data (Volume 2)

Graph sudah diisi seed awal hasil reverse-engineering 6 sistem desain
(§14 Volume 2): Swiss Design, Apple HIG, IBM Carbon, Editorial Design,
Bauhaus, Material Design. Per build terakhir:

| Tipe | Jumlah |
|---|---|
| Principle | 15 |
| System | 6 |
| Pattern | 17 |
| CaseStudy | 6 |
| Domain | 7 |
| Benchmark | 4 (seed awal, kategori L02/L04/L07/L12) |
| Edge | 90 |

Termasuk satu relasi `contradicts` nyata (densitas informasi enterprise
dashboard vs napas visual editorial layout) dan satu relasi `supersedes`
nyata (elevation/flat menggantikan skeuomorfisme realistis) — keduanya
diwajibkan §8.3 sebagai bukti graph tidak menyembunyikan trade-off atau
evolusi pola.

## Status Format Penyimpanan (§16 butir 2)

**Divalidasi dengan data seed nyata, masih draft untuk dikunci final oleh
maintainer.** Format Markdown+JSONL terbukti bekerja untuk 55 node/90 edge
tanpa referensi rusak (`build_graph.py` menegakkan integritas referensial
di setiap build). SQLite dipakai untuk `index/graph.db` — pilihan ini
belum final, tapi sudah divalidasi sebagai baseline yang berfungsi.
