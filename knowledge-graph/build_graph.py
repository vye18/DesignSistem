#!/usr/bin/env python3
"""Compile knowledge-graph/nodes/**/*.md + edges/edges.jsonl into index/graph.db.

Realisasi §8.4: markdown adalah source of truth, graph.db adalah artefak
turunan yang di-generate saat build time, tidak diedit manual. Dijalankan
dari root repo: `python3 knowledge-graph/build_graph.py`.
"""
import glob
import json
import sqlite3
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).parent
NODES_DIR = ROOT / "nodes"
EDGES_FILE = ROOT / "edges" / "edges.jsonl"
DB_FILE = ROOT / "index" / "graph.db"

NODE_TYPES = ["principles", "patterns", "case-studies", "systems", "benchmarks", "domains"]


def read_frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    _, fm_text, _ = text.split("---", 2)
    return yaml.safe_load(fm_text)


def load_nodes() -> list[dict]:
    nodes = []
    for node_type in NODE_TYPES:
        for path in sorted((NODES_DIR / node_type).glob("*.md")):
            fm = read_frontmatter(path)
            if "id" not in fm:
                raise ValueError(f"{path}: missing 'id' in frontmatter")
            nodes.append({"node_type": node_type, "path": str(path.relative_to(ROOT)), **fm})
    return nodes


def load_edges() -> list[dict]:
    if not EDGES_FILE.exists():
        return []
    edges = []
    for i, line in enumerate(EDGES_FILE.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            edges.append(json.loads(line))
        except json.JSONDecodeError as e:
            raise ValueError(f"{EDGES_FILE}:{i}: invalid JSON — {e}") from e
    return edges


def validate(nodes: list[dict], edges: list[dict]) -> list[str]:
    errors = []
    ids = {n["id"] for n in nodes}
    seen = set()
    for n in nodes:
        if n["id"] in seen:
            errors.append(f"duplicate node id: {n['id']}")
        seen.add(n["id"])
    for e in edges:
        for side in ("from", "to"):
            if e[side] not in ids:
                errors.append(f"edge references unknown node id: {e[side]} ({e})")
    return errors


def build_db(nodes: list[dict], edges: list[dict]) -> None:
    DB_FILE.parent.mkdir(parents=True, exist_ok=True)
    if DB_FILE.exists():
        DB_FILE.unlink()
    conn = sqlite3.connect(DB_FILE)
    conn.execute(
        "CREATE TABLE nodes (id TEXT PRIMARY KEY, node_type TEXT, path TEXT, data TEXT)"
    )
    conn.execute(
        "CREATE TABLE edges (from_id TEXT, to_id TEXT, relation TEXT, weight REAL, note TEXT)"
    )
    conn.executemany(
        "INSERT INTO nodes VALUES (?, ?, ?, ?)",
        [(n["id"], n["node_type"], n["path"], json.dumps(n, ensure_ascii=False)) for n in nodes],
    )
    conn.executemany(
        "INSERT INTO edges VALUES (?, ?, ?, ?, ?)",
        [(e["from"], e["to"], e["relation"], e.get("weight", 1), e.get("note", "")) for e in edges],
    )
    conn.commit()
    conn.close()


def main() -> int:
    nodes = load_nodes()
    edges = load_edges()
    errors = validate(nodes, edges)
    if errors:
        print(f"Validation FAILED — {len(errors)} error(s):", file=sys.stderr)
        for err in errors:
            print(f"  - {err}", file=sys.stderr)
        return 1
    build_db(nodes, edges)
    print(f"OK — {len(nodes)} nodes, {len(edges)} edges compiled into {DB_FILE.relative_to(ROOT.parent)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
