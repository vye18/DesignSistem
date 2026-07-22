# ODI Manifesto & Core Philosophy

> Canonical, versioned. Bersumber dari §2–§4 `docs/spec/odi-spec-v0.1.md`.
> Perubahan pada dokumen ini adalah perubahan MAJOR terhadap spec (§13) dan
> harus dicatat di `versions/`.

## Vision

Dalam lima tahun, ketika sebuah AI menghasilkan desain, seharusnya kita bisa
bertanya "kenapa," dan AI itu bisa menjawab dengan alasan yang sama seperti
yang akan diberikan seorang Art Director senior — bukan dengan deskripsi
permukaan seperti "karena ini terlihat modern."

ODI adalah lapisan kognisi standar yang duduk di atas model AI apa pun —
portable reasoning layer, mirip HTTP di atas jaringan fisik yang berbeda-beda.

## Mission

1. Mendekomposisi proses berpikir desainer profesional menjadi tahapan
   kognitif eksplisit (§5, Cognition Stack).
2. Membangun reasoning engine yang menegakkan urutan tahapan tersebut,
   dengan kemampuan berhenti, mengevaluasi, dan mengulang.
3. Mendokumentasikan decision logic di balik sistem desain kelas dunia —
   bukan meniru outputnya (§11.2, Reference Engine).
4. Menyediakan skema data dan graph pengetahuan yang general untuk ribuan
   studi kasus tanpa perombakan struktural.
5. Menjaga seluruh keluaran framework tetap auditable — dapat ditelusuri
   kembali ke prinsip kognitif atau referensi yang mendasarinya.

## Manifesto

- **Desain adalah keputusan, bukan dekorasi.** AI yang tidak bertanya, tidak
  sedang mendesain — ia sedang menebak.
- **Generic bukan netral, generic adalah default kegagalan.** Tanpa kerangka
  berpikir, AI jatuh ke pola statistik paling umum.
- **Rasa (taste) bisa distrukturkan**, walau tidak bisa dijadikan formula
  tunggal. ODI menyingkirkan keputusan buruk lebih cepat daripada menebak.
- **Kritik adalah bagian dari proses**, bukan tahap darurat.
- **Referensi tanpa pemahaman adalah plagiat; pemahaman tanpa referensi
  adalah spekulasi.** Keduanya wajib berjalan bersama.
- **Skala adalah desain, bukan konsekuensi.** Arsitektur yang tidak
  dipikirkan untuk 10.000 aset sejak awal akan mati di aset ke-500.

## Core Philosophy — Lima Pilar

| Pilar | Apa yang diambil | Bagaimana ODI memakainya |
|---|---|---|
| Cognitive Psychology | Load kognitif, chunking, pengenalan pola, memori kerja | Membatasi jumlah "keputusan" per langkah reasoning agar tidak degenerasi menjadi tebakan |
| Visual Perception | Gestalt, kontras, hierarki fokus mata, Gutenberg diagram, Z/F-pattern | Dasar Visual Cognition Engine — model bagaimana mata bergerak, bukan checklist |
| Communication Design | Pesan vs medium, semiotika, audiens vs niat | Menjustifikasi tahap Message & Audience sebelum tahap visual apa pun |
| Information Architecture | Hierarki informasi, taksonomi, findability | Dasar Knowledge Graph dan tahap IA di cognition stack |
| Systems Thinking & Software Architecture | Dependency graph, modularitas, separation of concerns, versioning | Dasar Architecture, Module Structure, QA, Versioning |

**Uji filosofis wajib** untuk setiap modul baru yang diusulkan: *"Pilar mana
yang menjustifikasi keberadaanmu?"* Tidak ada jawaban → modul itu dekorasi,
ditolak.
