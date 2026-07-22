# Contributing to ODI

Realisasi §12.1 (QA Struktural) dan §9.2 (dependency principle: kontributor
studi kasus tidak perlu memahami internal engine).

## Prasyarat Membaca

1. `docs/spec/odi-spec-v0.1.md` — spesifikasi lengkap.
2. `core/manifesto/manifesto.md` — filosofi yang menjustifikasi setiap
   keputusan struktural.
3. `core/cognition-stack/README.md` — jika kontribusi menyentuh engine
   atau skema lapis kognisi.

## Jenis Kontribusi

### 1. Menambah Node ke Knowledge Graph (Principle / Pattern / CaseStudy)

Wajib lolos tiga gate sebelum masuk `knowledge-graph/nodes/`:

- **Traceability check** — node baru harus terhubung ke minimal satu
  `Principle` yang sudah ada (via `justified_by` atau relasi setara). Node
  yatim ditolak.
- **Non-duplication check** — cek dulu apakah pola serupa sudah ada. Jika
  ya, ajukan sebagai revisi + relasi `supersedes`, bukan node duplikat.
- **Copyright/asset check** — gambar di `CaseStudy` hanya untuk analisis
  pola dengan atribusi jelas, bukan reproduksi utuh karya berlisensi.

Setiap node baru harus valid terhadap skema JSON yang sesuai di
`core/schemas/knowledge-graph/`.

Alur: taruh draf di `case-studies/raw/` dulu → review → jika lolos, pindah
ke `knowledge-graph/nodes/<tipe>/` dan tambahkan edge terkait ke
`knowledge-graph/edges/edges.jsonl`.

**Ketiga gate di atas ditegakkan otomatis** oleh
`knowledge-graph/qa_check.py` (dijalankan CI di setiap PR yang menyentuh
`knowledge-graph/`, `core/schemas/`, atau `examples/` — lihat
`.github/workflows/knowledge-graph-qa.yml`). Jalankan secara lokal sebelum
membuka PR:

```
pip install jsonschema PyYAML
python3 knowledge-graph/qa_check.py
python3 knowledge-graph/build_graph.py
```

`qa_check.py` menolak PR jika: node tidak valid terhadap skema, edge
menunjuk id yang tidak ada, atau `justified_by`/`pattern_ids` kosong
(node yatim) — termasuk mendeteksi drift antara frontmatter node dan
`edges.jsonl` (mis. lupa menambah edge setelah mengubah frontmatter).

### 2. Menambah/Mengubah Engine

Setiap engine baru harus bisa menjawab: **"pilar mana (§4) yang
menjustifikasi keberadaanmu?"** Jika tidak ada jawaban, diusulkan ditolak
sebagai dekorasi.

Perubahan pada skema I/O suatu engine (`core/schemas/`) yang mengubah
`required` fields adalah perubahan **MAJOR** (§13) dan perlu didiskusikan
sebelum PR, karena memutus kontrak dengan engine lain yang bergantung
padanya.

### 3. Menambah Benchmark

Taruh di `benchmarks/L{NN}-*/` sesuai lapis kognisi yang diuji, dengan
`type` salah satu dari `regression | adversarial | cross-model` (lihat
`core/schemas/knowledge-graph/benchmark.schema.json`).

## Yang Ditolak Otomatis

- Node tanpa keterhubungan ke Principle (node yatim).
- Kontribusi yang menyertakan aset visual berlisensi tanpa atribusi/izin.
- Engine/module baru tanpa jawaban jelas atas uji pilar (§4).
- Skip gate kognisi (§5) yang tidak dicatat secara eksplisit di
  `L14-final-lock` (`skipped_gates[]`).

## Governance

Proses maintainer/reviewer formal untuk kontribusi berskala besar (50+
kontributor) belum didefinisikan — ini item terbuka di §15 (Future
Expansion). Untuk saat ini, PR direview oleh maintainer repo secara manual.
