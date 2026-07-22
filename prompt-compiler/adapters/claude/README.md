# Claude Adapter

Realisasi §7.3, §9, §11.1. Diprioritaskan lebih dulu (§11.1) karena Claude
adalah *native execution environment* untuk pengembangan ODI.

## Yang Diterjemahkan Adapter Ini (bukan logika kognisi)

1. **Format pemanggilan tool** — setiap skema di
   `core/schemas/cognition-stack/` dibind sebagai *tool definition*
   (`input_schema` Claude tool-use), sehingga output lapis dipaksa valid
   secara struktural oleh mekanisme tool-calling, bukan hanya lewat
   instruksi teks.
2. **Gaya instruksi** — Claude merespons konsisten pada instruksi yang
   dipisah lewat XML-tag (`<context>`, `<constraints>`, `<output_schema>`)
   dibanding satu paragraf instruksi panjang.
3. **Batas konteks** — setiap panggilan engine hanya menyertakan artefak
   lapis-lapis yang relevan (lihat kolom "Input" di tiap file
   `core-templates/*.md`), bukan seluruh riwayat sesi, untuk menghemat
   konteks pada domain berskala besar (§7.1).

Logika kognisi (urutan lapis, aturan skip, definisi *blocking* vs
*minor*, dst.) **tidak diulang di sini** — itu tetap didefinisikan sekali
di `prompt-compiler/core-templates/*.md`. File di folder ini hanya
membungkusnya untuk Claude.

## Pola Umum per Engine

Setiap file `reasoning-engine.md`, `planning-engine.md`, `critic-engine.md`,
`visual-cognition-engine.md` di folder ini mengikuti struktur:

```xml
<context>
  <!-- ringkasan tugas dari core-templates/*.md, dipersempit ke lapis yang relevan -->
</context>
<inputs>
  <!-- artefak lapis sebelumnya, di-embed sebagai JSON -->
</inputs>
<constraints>
  <!-- instruksi inti dari core-templates/*.md, tanpa modifikasi substansi -->
</constraints>
<output_schema>
  <!-- $id skema yang harus dipatuhi, dibind sebagai tool input_schema -->
</output_schema>
```

## Status

Kerangka pembungkus (`README.md` ini) sudah ada. File konkret per-engine
(`reasoning-engine.md` dst.) berisi rendering satu contoh nyata untuk
domain `domain:poster`, memakai artefak dari
`examples/poster-prototype/` sebagai referensi input/output — bukan
seluruh kombinasi engine × domain (§11.1 target skala 200 varian dicapai
lewat pemisahan template inti/adapter tipis, bukan menulis manual tiap
kombinasi).
