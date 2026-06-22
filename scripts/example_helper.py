#!/usr/bin/env python3
"""Deterministic helper for checking process design drafts.

This script performs a lightweight text check for recommended sections in a
workflow, SOP, decision tree, bottleneck analysis, or agent flow draft. It does
not call external services, modify files, or make decisions.
"""

from __future__ import annotations

import argparse
from pathlib import Path

RECOMMENDED_TERMS = {
    "objective": ["objective", "goal", "purpose"],
    "scope": ["scope", "start trigger", "end state", "end condition"],
    "decision_logic": ["decision", "criteria", "if", "then"],
    "human_review": ["human review", "approval", "escalation", "review gate"],
    "metrics": ["metric", "kpi", "cycle time", "conversion", "quality"],
    "risks": ["risk", "failure mode", "bottleneck", "exception"],
}


def check_text(text: str) -> dict[str, bool]:
    """Return whether each recommended concept appears in the text."""
    lowered = text.lower()
    return {
        category: any(term in lowered for term in terms)
        for category, terms in RECOMMENDED_TERMS.items()
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Check a process design draft for recommended concepts.")
    parser.add_argument("path", type=Path, help="Path to a Markdown or text draft.")
    args = parser.parse_args()

    if not args.path.exists() or not args.path.is_file():
        print(f"error: file not found: {args.path}")
        return 1

    text = args.path.read_text(encoding="utf-8")
    results = check_text(text)
    missing = [name for name, present in results.items() if not present]

    print("Process design draft check")
    for name, present in results.items():
        status = "ok" if present else "missing"
        print(f"- {name}: {status}")

    if missing:
        print("Missing recommended concepts: " + ", ".join(missing))
        return 2

    print("All recommended concepts were found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
