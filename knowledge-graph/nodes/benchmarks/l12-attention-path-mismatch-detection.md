---
id: "benchmark:l12-attention-path-mismatch-detection"
category_layer: "L12"
domain: "domain:dashboard-ui"
type: "regression"
tests: ["principle:contrast-creates-hierarchy", "principle:working-memory-limits-decision-density"]
input_brief: >
  Draf dashboard di mana metrik sekunder diberi warna paling kontras
  (merah terang), sementara metrik utama memakai warna netral.
expected_outcome: >
  Visual Cognition Engine harus mendeteksi attention_path menuju metrik
  sekunder lebih dulu, mismatches dengan Message Hierarchy (L4). Critic
  Engine wajib melaporkan finding severity 'blocking', bukan 'minor'.
---
