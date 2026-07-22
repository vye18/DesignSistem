# Open Design Intelligence (ODI)
## Specification v0.1 — Foundational Blueprint

Status: Draft · Volume 1 · Architecture-First

> Dokumen ini adalah salinan verbatim dari spesifikasi v0.1 yang menjadi
> sumber kebenaran arsitektural repositori ini. Jangan mengedit isi naratif
> di file ini secara langsung — perubahan pada spec mengikuti proses
> versioning di `versions/` (lihat §13 di bawah, dan `versions/README.md`).
> Realisasi teknis tiap bagian ada di `core/`, `engines/`, `knowledge-graph/`,
> `prompt-compiler/`, `benchmarks/`, dan `contrib/`.

Catatan pembacaan. Dokumen ini adalah blueprint, bukan implementasi. Tidak ada
prompt siap pakai, tidak ada template modul di sini. Tujuannya adalah
mendefinisikan struktur berpikir yang akan menjadi kerangka rujukan sebelum
satu baris modul pun ditulis. Setiap keputusan arsitektur di bawah ini diuji
dengan satu pertanyaan tunggal: "Apakah struktur ini masih masuk akal ketika
proyek ini punya 5000 markdown, 10.000 gambar, 500 studi kasus, dan 50
contributor?" Jika jawabannya tidak, bagian itu ditolak dan dirancang ulang
sebelum masuk dokumen ini.

## 0. Ringkasan Eksekutif

Open Design Intelligence (ODI) adalah kerangka kognisi desain (design
cognition framework) yang mengajarkan model bahasa untuk berpikir seperti
seorang Senior Art Director — bukan seperti generator gambar/teks yang
langsung melompat dari brief ke output.

Masalah inti yang ingin diselesaikan ODI bukan "AI tidak bisa membuat desain
bagus." Masalahnya lebih dalam: AI tidak memiliki proses berpikir desain yang
terurut, dapat diaudit, dan dapat dikritik ulang. AI generatif hari ini
menyatukan riset, strategi, dan eksekusi visual dalam satu langkah generasi,
sehingga hasilnya statistically-average alih-alih decision-driven.

ODI membalik urutan itu dengan memaksa adanya lapisan kognisi eksplisit —
sebuah rantai keputusan yang dapat ditelusuri — di antara brief dan output
visual/kode/deskripsi desain.

ODI dirancang sebagai:

- Framework, bukan prompt tunggal. Ia terdiri dari mesin-mesin (engines) yang
  saling bergantung.
- Model-agnostic. Harus bisa dijalankan oleh Claude, GPT, Gemini, Grok, Qwen,
  DeepSeek, dst., lewat lapisan adapter.
- Open, tapi terkurasi. Kontribusi terbuka, tapi masuk lewat pipeline QA yang
  ketat (lihat §12).
- Scalable by construction. Struktur direktori, skema data, dan graph relasi
  dirancang untuk beban 5–10 ribu dokumen sejak versi 0.1, bukan "akan
  direfactor nanti."

## 1. Vision

Dalam lima tahun, ketika sebuah AI menghasilkan desain, seharusnya kita bisa
bertanya "kenapa," dan AI itu bisa menjawab dengan alasan yang sama seperti
yang akan diberikan seorang Art Director senior — bukan dengan deskripsi
permukaan seperti "karena ini terlihat modern."

ODI ingin menjadi lapisan kognisi standar yang duduk di atas model AI apa
pun, sehingga kemampuan "berpikir desain" tidak terikat pada satu vendor
model, melainkan menjadi portable reasoning layer — mirip bagaimana HTTP
menjadi lapisan standar di atas jaringan fisik yang berbeda-beda.

## 2. Mission

- Mendekomposisi proses berpikir desainer profesional menjadi tahapan
  kognitif yang eksplisit dan dapat diinstruksikan ke AI (lihat §5, Design
  Cognition Stack).
- Membangun reasoning engine yang memaksa AI melalui tahapan tersebut secara
  berurutan, dengan kemampuan berhenti, mengevaluasi, dan mengulang
  (self-critique loop).
- Mendokumentasikan pola berpikir di balik sistem desain kelas dunia (Swiss
  Design, Apple HIG, IBM Carbon, editorial design, dst.) — bukan meniru
  output visualnya, melainkan mengekstrak decision logic-nya (lihat §6,
  Reference Engine).
- Menyediakan format modul, skema data, dan graph pengetahuan yang cukup
  general untuk menampung ribuan studi kasus dan puluhan design engine
  tambahan tanpa perombakan struktural.
- Menjaga agar seluruh keluaran framework dapat diaudit: setiap keputusan
  desain yang direkomendasikan AI harus bisa ditelusuri kembali ke prinsip
  kognitif atau referensi yang mendasarinya.

## 3. Manifesto

Desain adalah keputusan, bukan dekorasi. Setiap elemen visual adalah jawaban
atas sebuah pertanyaan yang lebih dulu diajukan. AI yang tidak bertanya,
tidak sedang mendesain — ia sedang menebak.

Generic bukan netral, generic adalah default kegagalan. Ketika AI tidak
diberi kerangka berpikir, ia jatuh ke pola statistik paling umum. ODI ada
untuk mencegah keruntuhan itu.

Rasa (taste) bisa distrukturkan, walau tidak bisa dijadikan formula tunggal.
ODI tidak berjanji menghasilkan "rumus desain bagus." Ia berjanji
menghasilkan proses yang, jika diikuti dengan disiplin, menyingkirkan
keputusan-keputusan buruk lebih cepat daripada menebak-nebak.

Kritik adalah bagian dari proses, bukan tahap darurat. Sebuah sistem yang
tidak bisa mengkritik hasilnya sendiri bukan sistem desain — ia generator
satu arah.

Referensi tanpa pemahaman adalah plagiat; pemahaman tanpa referensi adalah
spekulasi. ODI mewajibkan keduanya berjalan bersama (lihat §6).

Skala adalah desain, bukan konsekuensi. Arsitektur yang tidak dipikirkan
untuk 10.000 aset sejak awal akan mati di aset ke-500.

## 4. Core Philosophy

ODI berdiri di atas lima pilar teoretis. Ini bukan daftar bacaan — ini adalah
sumber logika yang menjustifikasi setiap engine di §7–§11.

| Pilar | Apa yang diambil | Bagaimana ODI memakainya |
|---|---|---|
| Cognitive Psychology | Load kognitif, chunking, pengenalan pola, memori kerja | Menentukan berapa banyak "keputusan" yang boleh diminta dari AI dalam satu langkah reasoning agar tidak degenerasi menjadi tebakan |
| Visual Perception | Gestalt principles, kontras, hierarki fokus mata, Gutenberg diagram, Z-pattern/F-pattern | Menjadi dasar Visual Cognition Engine (§10) — bukan checklist "gunakan grid," tapi model bagaimana mata benar-benar bergerak |
| Communication Design | Pesan vs medium, semiotika, audiens vs niat | Menjustifikasi tahap "Message" dan "Audience" dalam Design Thinking Framework (§5) sebelum tahap visual apa pun dimulai |
| Information Architecture | Hierarki informasi, taksonomi, findability | Menjadi dasar struktur Knowledge Graph (§8) dan tahap IA dalam cognition stack |
| Systems Thinking & Software Architecture | Dependency graph, modularitas, separation of concerns, versioning | Menjadi dasar seluruh §7 (Architecture), §9 (module structure & dependency), §12 (QA), §13 (versioning) |

Prinsip pengujian filosofis: setiap modul baru yang diusulkan harus bisa
menjawab, "pilar mana yang menjustifikasi keberadaanmu?" Jika tidak ada
jawaban, modul itu adalah dekorasi dan ditolak.

## 5. Design Thinking Framework (Cognition Stack)

Ini adalah jantung filosofis ODI: representasi eksplisit dari alur berpikir
desainer profesional, direstrukturisasi sebagai stack kognitif berlapis —
setiap lapis adalah gerbang (gate) yang harus dilalui sebelum lapis
berikutnya diaktifkan.

```
L0  Brief Intake         → Apa yang sebenarnya diminta, vs apa yang tersirat?
L1  Problem Framing      → Apa masalah komunikasi sesungguhnya (bukan "buat poster")?
L2  Audience Model       → Siapa yang melihat ini, dalam kondisi mental/fisik apa?
L3  Brand & Voice        → Batasan identitas apa yang tidak boleh dilanggar?
L4  Message Hierarchy    → Apa yang harus dibaca pertama, kedua, ketiga?
L5  Information Architecture → Bagaimana konten dikelompokkan & diurutkan?
L6  Visual Strategy      → Pendekatan besar apa (minimal, editorial, bold, dst.) dan mengapa?
L7  Composition & Grid   → Bagaimana ruang dibagi agar hierarki L4 benar-benar terjadi?
L8  Typography           → Sistem huruf apa yang mendukung suara (L3) dan hierarki (L4)?
L9  Color & Contrast     → Apa yang membawa mata, apa yang diam?
L10 Imagery/Photography  → Peran gambar: bukti, suasana, atau navigasi?
L11 Draft Synthesis      → Menyatukan L6–L10 menjadi satu draf konkret
L12 Self-Critique        → Critic Engine menyerang draf dari sudut pandang L1–L4
L13 Revision Loop        → Kembali ke lapis yang gagal, bukan ke L11 secara membabi buta
L14 Final Lock           → Draf disahkan hanya jika lolos semua gate relevan
```

Aturan struktural kunci:

- Tidak boleh loncat lapis. AI tidak boleh mulai membahas tipografi (L8)
  sebelum L4 (hierarki pesan) selesai didefinisikan — ini yang membedakan
  ODI dari prompt biasa yang menyuruh "buatkan desain modern dengan
  tipografi bold."
- Setiap lapis menghasilkan artefak, bukan opini. L2 (Audience Model) harus
  menghasilkan objek terstruktur (lihat skema di §8), bukan kalimat naratif
  seperti "audiensnya anak muda."
- L12 (Self-Critique) bukan opsional. Setiap keluaran wajib melalui Critic
  Engine minimal satu putaran sebelum dianggap final.
- Gate boleh di-skip secara eksplisit, misalnya untuk iterasi cepat/low-stakes,
  tapi skip harus dicatat sebagai keputusan sadar (logged), bukan default
  diam-diam.

Stack ini adalah kontrak antara Reasoning Engine (§7.2) dan Planning Engine
(§7.3): reasoning engine menjamin urutan lapis ditegakkan; planning engine
menjamin setiap lapis punya sub-langkah konkret yang bisa dieksekusi model.

## 6. Design Cognition — Model Mental AI

Bagian ini menjawab pertanyaan filosofis utama: bagaimana "berpikir seperti
Art Director" direpresentasikan secara computable, bukan sekadar naratif?

ODI memodelkan kognisi desain sebagai tiga proses paralel yang saling
mengoreksi:

### 6.1 Perceptual Simulation

Model mensimulasikan bagaimana mata manusia sungguhan akan menjelajahi
komposisi — bukan berdasarkan estetika subjektif, tapi berdasarkan pola
perhatian visual yang sudah mapan secara empiris (Gutenberg Diagram,
Z-pattern untuk layout sederhana, F-pattern untuk teks padat, prinsip
Gestalt untuk pengelompokan). Output-nya adalah peta urutan perhatian
(attention path), yang kemudian dibandingkan dengan Message Hierarchy dari
L4. Jika urutan perhatian yang disimulasikan tidak cocok dengan urutan pesan
yang diinginkan, ini adalah cacat desain yang harus diperbaiki di L7–L9,
bukan di tahap akhir.

### 6.2 Intentional Reasoning

Untuk setiap keputusan visual (pemilihan warna, jenis huruf, kepadatan
whitespace), engine wajib mengaitkannya kembali ke satu atau lebih lapis
L1–L6. Struktur pengait ini disebut decision trace — rantai "keputusan X ada
karena kebutuhan Y di lapis Z." Decision trace inilah yang membuat hasil ODI
auditable, berbeda dari AI generatif biasa yang tidak bisa menjelaskan kenapa
memilih warna tertentu selain "terlihat cocok."

### 6.3 Comparative Pattern Matching (bukan copying)

Model dibolehkan — bahkan diwajibkan — mencari preseden dari Reference
Engine (§6.4 / §11), tapi hanya pola strukturalnya (mis. "Swiss design
menyelesaikan padatnya informasi lewat grid modular yang ketat dan tipografi
netral yang tidak mengganggu"), bukan meniru elemen visual literalnya. ODI
membedakan tegas: pattern of reasoning (boleh diambil) vs visual
asset/style (tidak boleh disalin verbatim).

Ketiga proses ini dijalankan oleh dua engine berbeda dalam arsitektur
(Visual Cognition Engine menangani 6.1, Reasoning Engine menangani 6.2,
Reference Engine mendukung 6.3), dan hasilnya disatukan oleh Planning Engine
sebelum sintesis draf (L11).

## 7. Architecture — Gambaran Sistem

### 7.1 Prinsip Arsitektural

- Separation of concerns ketat: kognisi (reasoning), eksekusi (planning),
  evaluasi (critic), dan persepsi (visual cognition) adalah engine terpisah
  yang berkomunikasi lewat skema data yang terdefinisi, bukan lewat teks
  bebas.
- Model-agnostic melalui adapter: setiap engine dipanggil lewat prompt
  compiler (§9) yang menerjemahkan permintaan generik ke dialek masing-masing
  model (Claude, GPT, Gemini, dll.), sehingga logika inti tidak perlu ditulis
  ulang per model.
- Data lebih penting daripada prompt. Sebagian besar "kepintaran" ODI hidup
  di Knowledge Graph (§8) dan Reference Engine (§11), bukan di satu system
  prompt raksasa. Prompt hanyalah jembatan yang memanggil data terstruktur
  ini.
- Semua yang scalable dipisah dari semua yang stateless. Referensi, studi
  kasus, dan graph pengetahuan bersifat data terpisah yang bisa tumbuh tanpa
  batas; engine bersifat stateless dan hanya membaca data itu saat runtime.

### 7.2 Diagram Sistem Tingkat Tinggi

```
                          ┌───────────────────────────┐
                          │        USER BRIEF         │
                          └─────────────┬─────────────┘
                                        ▼
                          ┌───────────────────────────┐
                          │   INTAKE & FRAMING (L0-L1) │
                          └─────────────┬─────────────┘
                                        ▼
        ┌────────────────────── REASONING ENGINE ──────────────────────┐
        │   Menegakkan urutan Cognition Stack (§5), menghasilkan       │
        │   artefak terstruktur per lapis (Audience Model, Message     │
        │   Hierarchy, dst.)                                           │
        └───────────────┬─────────────────────────┬────────────────────┘
                        ▼                         ▼
          ┌─────────────────────────┐   ┌─────────────────────────┐
          │   REFERENCE ENGINE      │   │  KNOWLEDGE GRAPH (§8)   │
          │  (pola preseden desain) │◄──┤ (relasi konsep, prinsip,│
          │                         │   │  studi kasus, entitas)  │
          └─────────────┬───────────┘   └─────────────┬───────────┘
                        └──────────────┬───────────────┘
                                       ▼
                          ┌───────────────────────────┐
                          │      PLANNING ENGINE       │
                          │ (menyusun sub-langkah      │
                          │  konkret per lapis L6-L11) │
                          └─────────────┬─────────────┘
                                        ▼
                          ┌───────────────────────────┐
                          │  VISUAL COGNITION ENGINE   │
                          │ (simulasi perhatian visual,│
                          │  validasi hierarki)        │
                          └─────────────┬─────────────┘
                                        ▼
                          ┌───────────────────────────┐
                          │        DRAFT (L11)         │
                          └─────────────┬─────────────┘
                                        ▼
                          ┌───────────────────────────┐
                          │       CRITIC ENGINE        │
                          │  (menyerang draf dari      │
                          │   sudut pandang L1-L4)     │
                          └──────┬─────────────┬───────┘
                          lolos ▼             ▼ gagal
                ┌───────────────────┐   ┌───────────────────────┐
                │   FINAL LOCK (L14) │   │  REVISION LOOP (L13)  │
                └───────────────────┘   │  → kembali ke lapis    │
                                        │    yang gagal, bukan   │
                                        │    L11 secara acak     │
                                        └───────────┬───────────┘
                                                    │
                                                    └──► kembali ke Planning Engine
```

Seluruh komunikasi antar-engine dilakukan lewat objek data terstandar
(lihat §8.2), bukan teks naratif bebas — ini yang membuat sistem dapat
diaudit dan dapat diuji unit per unit.

### 7.3 Lapisan Adapter Model (Model-Agnostic Layer)

```
ODI Core (engine logic, schema, knowledge graph)
        │
        ▼
Prompt Compiler (§9) — menerjemahkan permintaan generik
        │
   ┌────┼────┬────────┬────────┬────────┐
   ▼    ▼    ▼         ▼        ▼        ▼
 Claude GPT Gemini    Grok     Qwen   DeepSeek
 Adapter Adapter Adapter    Adapter  Adapter  Adapter
```

Setiap adapter hanya bertanggung jawab atas: (a) format pemanggilan
tool/function spesifik model, (b) batas panjang konteks, (c) gaya instruksi
yang paling efektif untuk model tersebut (mis. Claude merespons baik pada
XML-tag terstruktur, model lain mungkin lebih baik dengan JSON schema
eksplisit). Logika kognisi ODI sendiri tidak boleh ditulis ulang per-model —
hanya cara penyampaiannya yang berbeda.

## 8. Knowledge Graph

### 8.1 Mengapa Graph, Bukan Folder Markdown Datar

Dengan target 5000 markdown, 10.000 gambar, 500 studi kasus, dan 100
benchmark, struktur folder datar akan gagal dalam dua hal: (1) hubungan
lintas-dokumen (mis. "prinsip whitespace ini dipakai di 40 studi kasus dari
6 sistem desain berbeda") tidak bisa direpresentasikan sebagai path folder;
(2) pencarian pola ("tunjukkan semua preseden yang menyelesaikan masalah
densitas informasi lewat grid modular") membutuhkan query relasional, bukan
file listing.

ODI karena itu memodelkan pengetahuannya sebagai graph, dengan folder
markdown hanya sebagai lapisan penyimpanan/tampilan manusiawi di atas graph
tersebut — bukan sumber kebenaran itu sendiri.

### 8.2 Tipe Node

| Tipe Node | Contoh | Keterangan |
|---|---|---|
| Principle | "Kontras menciptakan hierarki fokus" | Unit kognitif paling atomik; berasal dari §4 (pilar teori) |
| Pattern | "Grid modular ketat untuk densitas informasi tinggi" | Pola berpikir hasil reverse-engineering dari suatu sistem desain |
| CaseStudy | "Redesain company profile X" | Studi kasus konkret yang menunjukkan Pattern diterapkan |
| System | "Swiss Design", "IBM Carbon" | Kumpulan pola dari satu tradisi/sistem desain |
| Engine | "Visual Cognition Engine v1" | Referensi ke modul eksekusi (§7) |
| Benchmark | "Uji hierarki fokus pada poster A/B" | Kasus uji terukur untuk QA (§12) |
| Domain | "Poster", "Company Profile", "Dashboard UI" | Konteks aplikasi output |

### 8.3 Tipe Relasi (Edge)

```
Principle  --justifies-->      Pattern
Pattern    --observed_in-->    CaseStudy
CaseStudy  --belongs_to-->     System
Pattern    --applies_to-->     Domain
Benchmark  --tests-->          Principle | Pattern
Engine     --implements-->     Principle | Pattern
CaseStudy  --contradicts-->    CaseStudy   (untuk kasus prinsip yang tegang/trade-off)
Pattern    --supersedes-->     Pattern      (evolusi pola, untuk versioning §13)
```

Relasi contradicts penting secara filosofis: desain penuh trade-off (mis.
"densitas informasi tinggi" vs "napas visual/whitespace"). Graph ODI wajib
merepresentasikan ketegangan ini secara eksplisit, bukan menyembunyikannya —
supaya Reasoning Engine bisa menyajikan trade-off ke pengguna, bukan
berpura-pura ada satu jawaban benar tunggal.

### 8.4 Skema Penyimpanan (usulan awal, model-agnostic terhadap DB)

```
/knowledge-graph/
  nodes/
    principles/*.md      (frontmatter: id, pillar, statement, tags)
    patterns/*.md         (frontmatter: id, source_systems[], domains[], justified_by[])
    case-studies/*.md     (frontmatter: id, pattern_ids[], system_id, media[])
    systems/*.md
    benchmarks/*.md
  edges/
    edges.jsonl           (baris: {from, to, relation, weight, note})
  index/
    graph.db              (index terkompilasi untuk query cepat — SQLite/graph-lib, dibangun dari nodes+edges saat build time)
```

Markdown tetap dipakai sebagai source of truth yang dapat dibaca manusia dan
diedit contributor; edges.jsonl dan graph.db adalah artefak turunan yang
di-generate, bukan diedit manual. Ini menjaga human-editability (penting
untuk open-source) sekaligus machine-queryability (penting untuk engine).

## 9. Module Structure & Dependency Graph

### 9.1 Struktur Direktori Level-Atas

```
open-design-intelligence/
├── core/
│   ├── cognition-stack/         # Definisi L0-L14 (§5), tidak berisi logic model spesifik
│   ├── schemas/                 # JSON Schema untuk setiap artefak antar-engine (§8.2 + object per lapis)
│   └── manifesto/               # §2-§4 dalam bentuk canonical, versioned
├── engines/
│   ├── reasoning-engine/
│   ├── planning-engine/
│   ├── critic-engine/
│   ├── visual-cognition-engine/
│   └── reference-engine/
├── knowledge-graph/              # §8
├── prompt-compiler/
│   ├── core-templates/           # instruksi generik, model-agnostic
│   └── adapters/
│       ├── claude/
│       ├── gpt/
│       ├── gemini/
│       ├── grok/
│       ├── qwen/
│       └── deepseek/
├── benchmarks/                   # §12
├── case-studies/                 # data mentah sebelum masuk knowledge-graph
├── contrib/                      # panduan & template kontribusi
└── versions/                     # snapshot versi (§13)
```

### 9.2 Prinsip Dependency

Aturan dependency searah, tidak melingkar:

```
core/schemas  ◄────────────────┐
     ▲                          │
     │                          │
core/cognition-stack            │
     ▲                          │
     │                          │
engines/*  ──depends_on──► core/schemas, core/cognition-stack
     │
     ▼
prompt-compiler ──depends_on──► engines/* (hanya interface publiknya, bukan internal)
     │
     ▼
adapters/*   ──depends_on──► prompt-compiler/core-templates
```

knowledge-graph tidak bergantung pada engine apa pun — ia adalah data murni
yang bisa dikembangkan independen oleh contributor riset, sementara engines
bergantung padanya (via query interface, §9.3). Ini krusial untuk skala:
kontributor yang menambahkan studi kasus ke-501 tidak boleh perlu memahami
internal Reasoning Engine.

### 9.3 Interface Antar-Engine (kontrak, bukan implementasi)

Setiap engine mengekspos hanya:

- Input schema (objek terstruktur, lihat §8.2 gaya)
- Output schema

Tidak ada shared mutable state — semua komunikasi lewat objek yang di-pass
eksplisit (mendukung penggantian satu engine tanpa merombak yang lain —
penting ketika nanti ada 50 design engine tambahan).

## 10. Reasoning Engine, Planning Engine, Critic Engine, Visual Cognition Engine

### 10.1 Reasoning Engine

Tanggung jawab: menegakkan urutan Cognition Stack (§5), mengubah brief
mentah menjadi artefak terstruktur di tiap lapis L0–L5 (Problem Framing →
Audience Model → Brand & Voice → Message Hierarchy), dan menghasilkan
decision trace awal (§6.2). Bukan tanggung jawabnya: memutuskan pilihan
visual konkret (warna, font) — itu ranah Planning Engine. Kegagalan yang
harus dicegah: lapis dilompati, atau artefak dihasilkan sebagai teks
naratif alih-alih objek terstruktur yang bisa dikonsumsi engine lain.

### 10.2 Planning Engine

Tanggung jawab: menerjemahkan Visual Strategy (L6) menjadi sub-langkah
konkret dan berurutan untuk L7–L10 (grid, tipografi, warna, imagery),
dengan tiap sub-langkah membawa referensi ke lapis mana di atasnya yang ia
penuhi. Berinteraksi dengan: Reference Engine (mencari pola preseden yang
relevan dengan domain & strategi terpilih), Knowledge Graph (mengambil
Pattern node yang cocok). Output: rencana eksekusi terstruktur → dikonsumsi
saat sintesis draf (L11).

### 10.3 Critic Engine

Tanggung jawab: mengevaluasi draf (L11) dari sudut pandang lapis-lapis
awal, bukan dari selera estetika bebas. Artinya Critic Engine bertanya:

- Apakah hierarki visual benar-benar cocok dengan Message Hierarchy (L4)?
  (dicek silang dengan Visual Cognition Engine)
- Apakah ada elemen yang melanggar batas Brand & Voice (L3)?
- Apakah Audience Model (L2) benar-benar terlayani (mis. kontras cukup
  untuk konteks pembacaan yang disebutkan)?

Output: daftar temuan terstruktur, masing-masing menunjuk balik ke lapis
spesifik yang gagal — inilah yang membuat Revision Loop (L13) bisa presisi
(kembali ke lapis yang gagal, bukan mengulang semua dari nol).

### 10.4 Visual Cognition Engine

Tanggung jawab: simulasi jalur perhatian visual (§6.1) atas draf/komposisi,
menghasilkan attention path yang dibandingkan terhadap Message Hierarchy
target. Engine ini adalah satu-satunya yang "melihat" komposisi secara
spasial (bekerja di atas deskripsi layout terstruktur — posisi, ukuran
relatif, kontras — bukan piksel mentah, di v0.1). Keterbatasan v0.1 yang
diakui secara eksplisit: simulasi ini berbasis heuristik perseptual yang
mapan (Gestalt, Gutenberg, F/Z-pattern), bukan model penglihatan komputer
yang memproses piksel sungguhan. Ini didokumentasikan sebagai batasan
terbuka di §16 (Future Expansion).

## 11. Prompt Compiler & Reference Engine

### 11.1 Prompt Compiler

Prompt Compiler bukan kumpulan prompt siap pakai. Ia adalah lapisan
penerjemah yang mengambil:

- Definisi generik dari core/cognition-stack (apa yang harus dicapai di
  suatu lapis)
- Skema I/O dari engine terkait
- Konteks runtime (model target, panjang konteks tersedia, gaya instruksi
  yang optimal untuk model tersebut)

...dan menyusun instruksi konkret yang dikirim ke model. Dengan desain ini,
menambah dukungan untuk model baru (mis. model ke-7) berarti menulis satu
adapter baru, bukan menulis ulang seluruh logika 14 lapis kognisi.

Target skala: hingga 200 varian prompt compiler (per kombinasi engine ×
model × domain) tanpa duplikasi logika — dicapai dengan memisahkan template
inti (satu per engine, model-agnostic) dari transformasi adapter (tipis,
spesifik model).

### 11.2 Reference Engine

Reference Engine bertugas menjawab: "preseden mana dari Knowledge Graph
yang relevan dengan situasi saat ini, dan pola berpikir apa yang bisa
diambil darinya (bukan asetnya)?"

Alur kerja:

1. Menerima konteks dari Reasoning/Planning Engine (domain, strategi
   visual, kendala brand)
2. Query ke Knowledge Graph untuk node Pattern/CaseStudy yang cocok (via
   relasi applies_to, observed_in)
3. Mengembalikan pattern of reasoning terstruktur — bukan gambar atau teks
   yang disalin dari studi kasus, melainkan ringkasan prinsip: "Sistem X
   menyelesaikan masalah Y dengan pendekatan Z, karena alasan W"
4. Menandai jika ada contradicts relevan (trade-off yang perlu disadari)

Batasan etis-struktural: Reference Engine dilarang secara arsitektural
mengeluarkan aset visual asli (gambar, logo, tipografi berlisensi) sebagai
output langsung — hanya deskripsi pola dan struktur keputusan. Ini dijaga
di level skema output, bukan sekadar instruksi lunak.

## 12. Quality Assurance

QA di ODI beroperasi di dua level:

### 12.1 QA Struktural (per kontribusi konten)

Setiap Principle, Pattern, CaseStudy baru yang masuk lewat kontribusi
terbuka wajib melalui gate berikut sebelum masuk Knowledge Graph:

- Traceability check — apakah node baru terhubung ke minimal satu
  Principle yang sudah ada (tidak boleh node yatim)?
- Non-duplication check — apakah pola serupa sudah ada (query kemiripan di
  graph)? Jika ya, harus jadi revisi/relasi supersedes, bukan duplikat
  baru.
- Copyright/asset check — jika CaseStudy menyertakan gambar, verifikasi
  bukan reproduksi karya berlisensi yang direproduksi utuh; gambar hanya
  untuk analisis pola, dengan atribusi.

### 12.2 QA Fungsional (per rilis engine)

Setiap perubahan pada engine (§10) diuji lewat suite benchmarks/:

- Regression benchmark: kasus uji lama yang dulu lolos Critic Engine harus
  tetap lolos.
- Adversarial benchmark: brief yang secara sengaja ambigu/kontradiktif,
  untuk memastikan Reasoning Engine tidak diam-diam menebak alih-alih
  meminta klarifikasi struktural.
- Cross-model benchmark: benchmark yang sama dijalankan lewat adapter
  berbeda (Claude, GPT, dst.) untuk memastikan logika inti — bukan hanya
  kualitas satu model — yang diuji.

Target skala: 100 benchmark di v0.1 sudah harus terkategori (per lapis
kognisi L0–L14, per domain), bukan daftar datar, agar penambahan benchmark
ke-101 dst. tidak menciptakan kekacauan navigasi.

## 13. Versioning

ODI mengadopsi skema versi tiga lapis, karena "versi" di sini bukan cuma
versi kode:

- Spec version (dokumen ini): MAJOR.MINOR — perubahan MAJOR berarti
  perubahan struktur Cognition Stack atau kontrak antar-engine; MINOR
  berarti penambahan/perluasan tanpa mengubah kontrak.
- Knowledge Graph version: snapshot ter-tag dari graph (node + edge),
  independen dari spec version, karena graph bertumbuh jauh lebih cepat
  dari spec.
- Engine version: tiap engine (§10) punya versinya sendiri; kompatibilitas
  antar-versi engine dan spec dijaga lewat schema version yang
  dideklarasikan di core/schemas.

Pola penamaan rilis: `odi-spec@0.1`, `odi-graph@2026.07`,
`odi-engine.critic@0.3` — dipisah agar update ke satu engine tidak memaksa
re-release seluruh spec.

## 14. Roadmap

- Volume 1 (dokumen ini — v0.1): Blueprint & Kontrak Dasar
  - Definisi Cognition Stack (§5), skema data inti (§8.2), kontrak
    antar-engine (§9.3)
  - Belum berisi: modul konten aktual (belum ada Principle/Pattern yang
    ditulis), belum ada implementasi kode
- Volume 2 (usulan): Reference Engine + Knowledge Graph Seed
  - Reverse-engineering 5–10 sistem desain awal (Swiss Design, Apple HIG,
    editorial design) menjadi node Pattern/CaseStudy pertama
  - Validasi skema graph dengan data nyata dalam jumlah kecil sebelum
    discale
- Volume 3 (usulan): Reasoning + Planning Engine — Prototipe
  - Implementasi L0–L10 untuk satu domain sempit dulu (mis.
    poster/single-page saja) sebagai bukti konsep, sebelum digeneralisasi
    ke domain lain
- Volume 4 (usulan): Critic Engine + Visual Cognition Engine
  - Implementasi loop self-critique end-to-end untuk domain yang sama
- Volume 5 (usulan): Prompt Compiler Multi-Model
  - Adapter Claude dulu (native environment eksekusi), lalu GPT, Gemini,
    dst.
- Volume 6+: Scale-out
  - Ekspansi domain (company profile, UI dashboard, dst.), ekspansi
    kontributor, QA pipeline otomatis penuh

## 15. Future Expansion (diakui secara terbuka sebagai batas v0.1)

- Visual Cognition Engine berbasis piksel sungguhan (bukan hanya deskripsi
  layout terstruktur) — memerlukan integrasi model vision terpisah.
- Multi-modal Reference Engine yang bisa menganalisis pola dari
  video/motion design, bukan hanya gambar statis.
- Personalization layer: audience model yang belajar dari feedback
  historis suatu brand/organisasi tertentu (dengan batasan privasi &
  scope yang jelas).
- Cross-domain trade-off resolver: mekanisme lebih formal untuk relasi
  contradicts di Knowledge Graph, agar sistem bisa merekomendasikan
  resolusi trade-off, bukan sekadar menandainya.
- Governance model untuk kontribusi at scale (50+ contributor): perlu
  proses maintainer/reviewer yang eksplisit, di luar cakupan teknis
  blueprint ini.

## 16. Kontrak Terbuka untuk Volume Berikutnya

Sebelum menulis satu modul konten pun, tiga hal berikut harus disepakati
dan dikunci (karena mengubahnya setelah Volume 2 dimulai akan mahal):

1. Skema objek data per lapis kognisi (L0–L14) — bentuk JSON Schema
   konkret untuk setiap artefak yang disebut di §5, belum didefinisikan
   field-per-field di v0.1 ini.
2. Format penyimpanan Knowledge Graph final (Markdown+JSONL seperti
   diusulkan di §8.4, atau alternatif lain) — perlu diuji dengan data seed
   nyata di Volume 2 sebelum dikunci.
3. Domain pertama untuk prototipe (§14, Volume 3) — direkomendasikan domain
   paling sempit dan paling terukur (single-page/poster) agar
   Reasoning–Planning–Critic loop bisa divalidasi cepat sebelum
   digeneralisasi.

Dokumen ini adalah v0.1 — fondasi arsitektural. Tidak ada modul konten,
tidak ada prompt eksekusi, tidak ada kode di dalamnya secara sengaja.
Volume 2 dimulai hanya setelah §16 disepakati.

---

> **Status kontrak §16 di repositori ini:** butir 1 (skema JSON per lapis
> kognisi) sudah didraft di `core/schemas/`. Butir 2 (format penyimpanan
> graph) sudah **divalidasi dengan data seed nyata** — lihat
> `knowledge-graph/README.md` dan `knowledge-graph/build_graph.py` — hasil
> Volume 2 (reverse-engineering 6 sistem desain menjadi 55 node/90 edge).
> Butir 3 (domain pertama) direkomendasikan **poster/single-page** sesuai
> saran spec, tercatat di README repo root, tapi tetap terbuka untuk
> dikunci final oleh maintainer sebelum Volume 3 (implementasi engine)
> resmi dimulai.
