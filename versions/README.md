# Versioning

Realisasi §13. ODI memakai skema versi **tiga lapis independen**:

| Lapis | Contoh | Berubah kapan |
|---|---|---|
| Spec version | `odi-spec@0.1` | MAJOR = perubahan struktur Cognition Stack atau kontrak antar-engine; MINOR = penambahan/perluasan tanpa mengubah kontrak |
| Knowledge Graph version | `odi-graph@2026.07` | Snapshot ter-tag dari graph (node+edge), independen dari spec — graph bertumbuh jauh lebih cepat |
| Engine version | `odi-engine.critic@0.3` | Tiap engine punya versinya sendiri; kompatibilitas dijaga lewat schema version di `core/schemas/` |

Update ke satu engine tidak memaksa re-release seluruh spec.

## Snapshot di Repo Ini

```
versions/
└── odi-spec@0.1/     # snapshot spec v0.1 (dokumen ini sendiri)
```

Snapshot Knowledge Graph (`odi-graph@YYYY.MM`) dan snapshot per-engine akan
ditambahkan mulai Volume 2/3 (§14 Roadmap), saat entitas tersebut mulai
punya rilis nyata untuk di-snapshot.
