# Benchmarks

Realisasi §12.2. Dikategorikan per **lapis kognisi** (L0–L14) sejak awal —
bukan daftar datar — agar penambahan benchmark ke-101 dst. tidak
menciptakan kekacauan navigasi (target skala §12.2: 100 benchmark
terkategori di v0.1).

```
benchmarks/
├── L00-brief-intake/
├── L01-problem-framing/
├── ...
└── L14-final-lock/
```

Setiap file benchmark mengikuti `core/schemas/knowledge-graph/benchmark.schema.json`
dan disimpan di subfolder lapis yang sesuai (`category_layer`). Domain
diletakkan sebagai field, bukan sub-folder tambahan, supaya satu benchmark
tidak perlu dipindah folder jika domainnya diperluas.

## Tiga Tipe (§12.2)

1. **Regression** — kasus uji lama yang dulu lolos Critic Engine harus
   tetap lolos.
2. **Adversarial** — brief yang sengaja ambigu/kontradiktif, memastikan
   Reasoning Engine meminta klarifikasi struktural, bukan diam-diam
   menebak.
3. **Cross-model** — benchmark yang sama dijalankan lewat adapter berbeda
   untuk memastikan logika inti (bukan hanya kualitas satu model) yang
   diuji.

## Status

Struktur folder per-lapis sudah dibuat, masih kosong. Isi benchmark
menunggu Volume 3–4 (§14 Roadmap), setelah Reasoning/Planning/Critic Engine
punya prototipe kerja untuk domain pertama.
