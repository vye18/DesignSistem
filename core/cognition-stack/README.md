# Cognition Stack (L0–L14)

> Realisasi §5 dan §6 dari `docs/spec/odi-spec-v0.1.md`. Definisi di sini
> murni struktural/model-agnostic — tidak ada logic model spesifik. Logic
> eksekusi ada di `engines/`; skema JSON konkret per lapis ada di
> `core/schemas/cognition-stack/`.

## Aturan Struktural Kunci

1. **Tidak boleh loncat lapis.** Lapis N+1 tidak boleh dimulai sebelum
   artefak lapis N valid terhadap skemanya.
2. **Setiap lapis menghasilkan artefak terstruktur, bukan opini/narasi
   bebas.** Lihat `core/schemas/cognition-stack/L{NN}-*.schema.json`.
3. **L12 (Self-Critique) wajib**, minimal satu putaran, sebelum draf
   dianggap final.
4. **Gate boleh di-skip secara eksplisit** (mis. iterasi cepat/low-stakes),
   tapi skip harus tercatat di artefak `L14` sebagai keputusan sadar
   (`skipped_gates[]` dengan alasan) — tidak boleh diam-diam.

Stack ini adalah kontrak antara Reasoning Engine (menegakkan urutan) dan
Planning Engine (menyusun sub-langkah eksekusi per lapis).

## Daftar Lapis

| Lapis | Nama | Pertanyaan Inti | Dihasilkan oleh | Skema |
|---|---|---|---|---|
| L0 | Brief Intake | Apa yang diminta vs apa yang tersirat? | Reasoning Engine | `L00-brief-intake.schema.json` |
| L1 | Problem Framing | Apa masalah komunikasi sesungguhnya? | Reasoning Engine | `L01-problem-framing.schema.json` |
| L2 | Audience Model | Siapa yang melihat, dalam kondisi apa? | Reasoning Engine | `L02-audience-model.schema.json` |
| L3 | Brand & Voice | Batasan identitas apa yang tak boleh dilanggar? | Reasoning Engine | `L03-brand-voice.schema.json` |
| L4 | Message Hierarchy | Apa yang dibaca pertama/kedua/ketiga? | Reasoning Engine | `L04-message-hierarchy.schema.json` |
| L5 | Information Architecture | Bagaimana konten dikelompokkan & diurutkan? | Reasoning Engine | `L05-information-architecture.schema.json` |
| L6 | Visual Strategy | Pendekatan besar apa, dan mengapa? | Planning Engine | `L06-visual-strategy.schema.json` |
| L7 | Composition & Grid | Bagaimana ruang dibagi agar hierarki L4 terjadi? | Planning Engine | `L07-composition-grid.schema.json` |
| L8 | Typography | Sistem huruf apa yang mendukung L3 & L4? | Planning Engine | `L08-typography.schema.json` |
| L9 | Color & Contrast | Apa yang membawa mata, apa yang diam? | Planning Engine | `L09-color-contrast.schema.json` |
| L10 | Imagery/Photography | Peran gambar: bukti, suasana, atau navigasi? | Planning Engine | `L10-imagery.schema.json` |
| L11 | Draft Synthesis | Menyatukan L6–L10 menjadi satu draf konkret | Planning Engine | `L11-draft-synthesis.schema.json` |
| L12 | Self-Critique | Draf diserang dari sudut pandang L1–L4 | Critic Engine + Visual Cognition Engine | `L12-self-critique.schema.json` |
| L13 | Revision Loop | Kembali ke lapis yang gagal | Reasoning/Planning Engine | `L13-revision-loop.schema.json` |
| L14 | Final Lock | Draf disahkan hanya jika lolos semua gate relevan | Reasoning Engine | `L14-final-lock.schema.json` |

## Mental Model (§6)

Tiga proses paralel yang saling mengoreksi, dipetakan ke engine:

- **Perceptual Simulation** (§6.1) → Visual Cognition Engine. Simulasi
  jalur perhatian mata (attention path), dibandingkan terhadap L4.
- **Intentional Reasoning** (§6.2) → seluruh engine, via `decision_trace`
  di setiap artefak: rantai "keputusan X ada karena kebutuhan Y di lapis Z."
- **Comparative Pattern Matching** (§6.3) → Reference Engine. Mengambil
  *pattern of reasoning*, bukan aset visual literal.

## Status

Draft — skema field-per-field di `core/schemas/cognition-stack/` adalah
kandidat lock untuk memenuhi §16 butir 1. Belum di-*sign-off* oleh
maintainer; terbuka untuk revisi sebelum Volume 2 dimulai.
