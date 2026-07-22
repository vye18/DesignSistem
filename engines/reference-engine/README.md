# Reference Engine

Realisasi §11.2 dan §6.3 (Comparative Pattern Matching).

## Tanggung Jawab

Menjawab: *"preseden mana dari Knowledge Graph yang relevan dengan situasi
saat ini, dan pola berpikir apa yang bisa diambil darinya (bukan
asetnya)?"*

## Alur Kerja

1. Menerima konteks dari Reasoning/Planning Engine (domain, strategi
   visual, kendala brand).
2. Query ke Knowledge Graph untuk node `Pattern`/`CaseStudy` yang cocok
   (via relasi `applies_to`, `observed_in`).
3. Mengembalikan *pattern of reasoning* terstruktur — bukan gambar atau
   teks yang disalin dari studi kasus, melainkan ringkasan prinsip:
   "Sistem X menyelesaikan masalah Y dengan pendekatan Z, karena alasan W."
4. Menandai jika ada relasi `contradicts` yang relevan (trade-off yang
   perlu disadari pengguna).

## Batasan Etis-Struktural (wajib, bukan opsional)

Reference Engine **dilarang secara arsitektural** mengeluarkan aset visual
asli (gambar, logo, tipografi berlisensi) sebagai output langsung — hanya
deskripsi pola dan struktur keputusan. Batasan ini dijaga di level **skema
output** (lihat `core/schemas/knowledge-graph/case-study.schema.json`,
field `media[].usage_note`), bukan sekadar instruksi lunak yang bisa
diabaikan model.

## Kontrak I/O

| | Schema |
|---|---|
| Input | Konteks domain/strategi dari Reasoning/Planning Engine + query ke `knowledge-graph/` |
| Output | Daftar `pattern_of_reasoning` terstruktur, masing-masing merujuk `pattern:*` / `case-study:*` node ids, plus daftar `contradicts` yang relevan |

## Status

Kontrak I/O sudah didefinisikan. **Data untuk dikonsumsi sudah tersedia** —
Knowledge Graph telah di-seed dengan 6 sistem desain (Swiss Design, Apple
HIG, IBM Carbon, Editorial Design, Bauhaus, Material Design), 17 Pattern,
6 CaseStudy, termasuk relasi `contradicts` dan `supersedes` nyata (lihat
`knowledge-graph/README.md`). Implementasi runtime yang benar-benar
menjalankan query ini lewat model menunggu Volume 3+, setelah
Reasoning/Planning Engine punya prototipe kerja.
