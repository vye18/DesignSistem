---
id: "benchmark:l07-grid-vs-message-hierarchy-regression"
category_layer: "L07"
domain: "domain:company-profile"
type: "regression"
tests: ["principle:grid-imposes-order-on-density", "principle:contrast-creates-hierarchy"]
input_brief: >
  Company profile 40 halaman dengan data finansial padat; L4 sudah
  menetapkan 3 tingkat pesan (headline metrik, konteks, catatan kaki).
expected_outcome: >
  Grid modular yang dipilih di L7 harus tetap memetakan tiap zone ke rank
  L4 yang sesuai (maps_to_message_rank). Kasus ini pernah gagal sebelumnya
  ketika grid dipilih murni demi kerapian visual tanpa cek silang ke L4 —
  regresi ini harus tetap lolos di setiap rilis Planning Engine berikutnya.
---
