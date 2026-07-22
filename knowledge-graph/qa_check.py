#!/usr/bin/env python3
"""Automated QA gate for Knowledge Graph contributions (§12.1).

Realisasi Volume 6+ (§14): "QA pipeline otomatis penuh". Menjalankan tiga
gate struktural yang wajib dilalui setiap Principle/Pattern/CaseStudy baru
sebelum diterima ke Knowledge Graph:

1. Schema validation — setiap node valid terhadap
   core/schemas/knowledge-graph/<type>.schema.json.
2. Referential integrity — setiap edge menunjuk node id yang benar-benar
   ada (didelegasikan ke build_graph.py).
3. Traceability — setiap Pattern/CaseStudy terhubung ke minimal satu
   Principle (langsung atau transitif), DAN setiap referensi silang yang
   dideklarasikan di frontmatter (justified_by, pattern_ids, dst.) benar-benar
   punya edge yang bersesuaian di edges.jsonl (mendeteksi drift antara
   frontmatter dan edges yang di-generate).

Dijalankan dari root repo: `python3 knowledge-graph/qa_check.py`.
Exit 0 jika semua gate lolos, exit 1 jika ada pelanggaran.
"""
import glob
import json
import sys
from pathlib import Path

import jsonschema
import yaml

ROOT = Path(__file__).parent
REPO_ROOT = ROOT.parent
NODES_DIR = ROOT / "nodes"
EDGES_FILE = ROOT / "edges" / "edges.jsonl"
SCHEMA_DIR = REPO_ROOT / "core" / "schemas" / "knowledge-graph"

SCHEMA_FOR_TYPE = {
    "principles": "principle.schema.json",
    "patterns": "pattern.schema.json",
    "case-studies": "case-study.schema.json",
    "systems": "system.schema.json",
    "domains": "domain.schema.json",
    "benchmarks": "benchmark.schema.json",
}

# frontmatter_field -> expected edge relation, direction "out" = node is `from`, "in" = node is `to`
CROSS_REF_EDGES = {
    "patterns": [("justified_by", "justifies", "in")],  # principle --justifies--> pattern
    "case-studies": [("pattern_ids", "observed_in", "in")],  # pattern --observed_in--> case-study
}


def read_frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    return yaml.safe_load(text.split("---", 2)[1])


def main() -> int:
    errors: list[str] = []

    nodes_by_type: dict[str, list[dict]] = {}
    for node_type, schema_file in SCHEMA_FOR_TYPE.items():
        schema = json.loads((SCHEMA_DIR / schema_file).read_text(encoding="utf-8"))
        nodes = []
        for path in sorted((NODES_DIR / node_type).glob("*.md")):
            fm = read_frontmatter(path)
            try:
                jsonschema.validate(fm, schema)
            except jsonschema.ValidationError as e:
                errors.append(f"[schema] {path.relative_to(REPO_ROOT)}: {e.message}")
                continue
            nodes.append(fm)
        nodes_by_type[node_type] = nodes

    edges = []
    if EDGES_FILE.exists():
        for i, line in enumerate(EDGES_FILE.read_text(encoding="utf-8").splitlines(), 1):
            if not line.strip():
                continue
            try:
                edges.append(json.loads(line))
            except json.JSONDecodeError as e:
                errors.append(f"[edges] line {i}: invalid JSON — {e}")

    all_ids = {n["id"] for nodes in nodes_by_type.values() for n in nodes}
    for e in edges:
        for side in ("from", "to"):
            if e[side] not in all_ids:
                errors.append(f"[referential] edge references unknown node id: {e[side]} ({e})")

    edge_set = {(e["from"], e["to"], e["relation"]) for e in edges}
    for node_type, field_relation_list in CROSS_REF_EDGES.items():
        for n in nodes_by_type.get(node_type, []):
            for field, relation, direction in field_relation_list:
                refs = n.get(field, [])
                if not refs:
                    errors.append(
                        f"[traceability] {n['id']}: '{field}' kosong — node yatim, tidak terhubung ke Principle manapun"
                    )
                    continue
                for ref in refs:
                    pair = (ref, n["id"]) if direction == "in" else (n["id"], ref)
                    edge_tuple = (pair[0], pair[1], relation)
                    if edge_tuple not in edge_set:
                        errors.append(
                            f"[traceability] {n['id']}: frontmatter '{field}' menyebut {ref}, "
                            f"tapi tidak ada edge {relation} yang bersesuaian di edges.jsonl "
                            f"(jalankan ulang build_graph.py generator / cek drift manual)"
                        )

    if errors:
        print(f"QA FAILED — {len(errors)} error(s):", file=sys.stderr)
        for err in errors:
            print(f"  - {err}", file=sys.stderr)
        return 1

    total_nodes = sum(len(v) for v in nodes_by_type.values())
    print(f"QA OK — {total_nodes} nodes, {len(edges)} edges, semua gate §12.1 lolos.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
