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
│   └── benchmarks/*.md       (→ benchmark.schema.json)
├── edges/
│   └── edges.jsonl           (satu baris per edge, → edge.schema.json)
└── index/
    └── (graph.db — generated, tidak di-commit; lihat .gitignore)
```

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

## Status Format Penyimpanan (§16 butir 2)

**Draft.** Format Markdown+JSONL ini adalah usulan awal dan perlu divalidasi
dengan data seed nyata (Volume 2, §14) sebelum dikunci sebagai format
final. `index/graph.db` akan dibangun dari `nodes/` + `edges/edges.jsonl`
saat build time (SQLite atau graph-lib — implementasi belum dipilih).
