---
id: "benchmark:l04-message-hierarchy-conflict-detection"
category_layer: "L04"
domain: "domain:poster"
type: "adversarial"
tests: ["principle:contrast-creates-hierarchy"]
input_brief: >
  Brief secara sengaja meminta dua elemen "sama-sama harus paling menonjol"
  (nama acara dan nama sponsor utama keduanya diklaim sebagai prioritas #1).
expected_outcome: >
  Reasoning Engine tidak boleh diam-diam memilih salah satu. L4 wajib
  menandai konflik ini di ambiguities (dari L0) dan meminta klarifikasi
  prioritas sebelum lanjut ke L5.
---
