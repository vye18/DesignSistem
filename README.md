# Open Design Intelligence (ODI)

**Specification v0.1 — Foundational Blueprint.** Status: Draft · Volume 1 ·
Architecture-First.

ODI adalah kerangka kognisi desain (*design cognition framework*) yang
mengajarkan model bahasa untuk berpikir seperti seorang Senior Art
Director — bukan seperti generator gambar/teks yang langsung melompat dari
brief ke output. Lihat spesifikasi lengkap di
[`docs/spec/odi-spec-v0.1.md`](docs/spec/odi-spec-v0.1.md).

> Repositori ini merealisasikan **struktur** blueprint v0.1: direktori,
> skema data, dan kontrak antar-engine. Sesuai spec, Volume 1 **sengaja**
> tidak berisi modul konten aktual, prompt eksekusi siap pakai, atau
> implementasi kode engine — itu dimulai di Volume 2+ (lihat Roadmap di
> bawah), setelah kontrak §16 dikunci oleh maintainer.

## Prinsip Inti

- **Framework, bukan prompt tunggal** — engine yang saling bergantung.
- **Model-agnostic** — Claude, GPT, Gemini, Grok, Qwen, DeepSeek lewat
  lapisan adapter (`prompt-compiler/adapters/`).
- **Open, tapi terkurasi** — kontribusi terbuka lewat pipeline QA ketat
  (`contrib/CONTRIBUTING.md`).
- **Scalable by construction** — dirancang untuk 5–10 ribu dokumen sejak
  v0.1, bukan "direfactor nanti."

Rincian filosofis lengkap: `core/manifesto/manifesto.md`.

## Struktur Direktori

```
open-design-intelligence/
├── docs/spec/                    # Spesifikasi v0.1 verbatim (source of truth naratif)
├── core/
│   ├── manifesto/                 # Vision, Mission, Manifesto, Core Philosophy (§2-4)
│   ├── cognition-stack/           # Definisi L0-L14 (§5) — model-agnostic
│   └── schemas/                   # JSON Schema per lapis kognisi & per tipe node graph (§8.2, §16)
├── engines/
│   ├── reasoning-engine/          # L0-L5 (§10.1)
│   ├── planning-engine/           # L6-L11 (§10.2)
│   ├── critic-engine/             # L12 (§10.3)
│   ├── visual-cognition-engine/   # simulasi perhatian visual (§10.4)
│   └── reference-engine/          # preseden desain, pattern-of-reasoning (§11.2)
├── knowledge-graph/                # Nodes + edges (§8)
├── prompt-compiler/                 # Template inti + adapter per model (§9, §11.1)
├── benchmarks/                      # Kategori per lapis kognisi L0-L14 (§12.2)
├── case-studies/                    # Staging area sebelum masuk knowledge-graph (raw intake)
├── contrib/                          # Panduan kontribusi & QA gate (§12.1)
└── versions/                         # Snapshot versi tiga-lapis (§13)
```

Setiap folder di atas punya `README.md` sendiri yang menjelaskan tanggung
jawab, kontrak I/O, dan status implementasinya.

## Cognition Stack — Ringkasan

14 lapis kognisi berurutan, dari brief mentah sampai draf terkunci (detail
lengkap: `core/cognition-stack/README.md`):

```
L0 Brief Intake → L1 Problem Framing → L2 Audience Model → L3 Brand & Voice
→ L4 Message Hierarchy → L5 Information Architecture → L6 Visual Strategy
→ L7 Composition & Grid → L8 Typography → L9 Color & Contrast → L10 Imagery
→ L11 Draft Synthesis → L12 Self-Critique → L13 Revision Loop → L14 Final Lock
```

Tidak boleh loncat lapis; L12 (Self-Critique) wajib; skip gate harus
dicatat eksplisit di `L14`, tidak diam-diam.

## Status Kontrak §16 (Kontrak Terbuka untuk Volume Berikutnya)

Tiga hal yang harus dikunci maintainer sebelum Volume 3 (implementasi
engine) dimulai:

1. ✅ **Draft tersedia** — Skema JSON per lapis kognisi L0–L14:
   `core/schemas/cognition-stack/`.
2. 🟡 **Divalidasi dengan data seed nyata, menunggu sign-off final** —
   Format Markdown+JSONL sudah diuji dengan 55 node/90 edge hasil seeding
   Volume 2 (`knowledge-graph/build_graph.py` menegakkan integritas
   referensial). Lihat `knowledge-graph/README.md`.
3. 🟡 **Direkomendasikan, dipakai sebagai domain seed terluas** —
   **poster/single-page**, sesuai saran spec. Domain lain (dashboard-ui,
   mobile-app, editorial-layout, dst.) sudah ikut di-seed di Volume 2 agar
   Reference Engine punya cakupan lintas-domain, tapi domain prototipe
   *pertama* untuk Volume 3 tetap direkomendasikan poster/single-page.

## Volume 2 — Reference Engine + Knowledge Graph Seed (§14)

**Sudah di-seed.** 6 sistem desain di-reverse-engineer menjadi node
Pattern/CaseStudy nyata: Swiss Design, Apple HIG, IBM Carbon, Editorial
Design, Bauhaus, Material Design. Rincian isi graph dan cara build:
`knowledge-graph/README.md`. Termasuk contoh nyata relasi `contradicts`
(trade-off densitas vs whitespace) dan `supersedes` (evolusi pola
skeuomorfisme → elevation/flat), sesuai kewajiban §8.3.

Belum dikerjakan di Volume 2: implementasi Reference Engine yang benar-benar
menjalankan query terhadap graph ini secara runtime (baru kontrak I/O-nya
yang ada, di `engines/reference-engine/README.md`) — itu bagian dari
Volume 3+ setelah Reasoning/Planning Engine punya prototipe kerja.

## Roadmap (§14)

| Volume | Fokus | Status |
|---|---|---|
| 1 (repo ini) | Blueprint & kontrak dasar — struktur, skema, kontrak antar-engine | Struktur di-scaffold |
| 2 | Reference Engine + Knowledge Graph Seed — reverse-engineering 5-10 sistem desain | Graph di-seed (6 sistem); implementasi runtime Reference Engine belum |
| 3 | Reasoning + Planning Engine — prototipe untuk 1 domain sempit | Belum dimulai |
| 4 | Critic Engine + Visual Cognition Engine — self-critique loop end-to-end | Belum dimulai |
| 5 | Prompt Compiler multi-model — Claude dulu, lalu GPT/Gemini/dst. | Belum dimulai |
| 6+ | Scale-out — ekspansi domain, kontributor, QA pipeline otomatis | Belum dimulai |

## Future Expansion (§15, diakui terbuka)

Vision model berbasis piksel sungguhan, Reference Engine multi-modal
(video/motion), personalization layer, cross-domain trade-off resolver
formal, governance model untuk 50+ kontributor.

## Kontribusi

Lihat `contrib/CONTRIBUTING.md` untuk QA gate (traceability,
non-duplication, copyright/asset check) sebelum node baru masuk
`knowledge-graph/`.
