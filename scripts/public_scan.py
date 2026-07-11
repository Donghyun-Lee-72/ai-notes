#!/usr/bin/env python3
"""Fail when public site sources contain private or operational artifacts."""

from __future__ import annotations

import re
import sys
from pathlib import Path


PATTERNS = {
    "internal project": re.compile(r"\b(IMMS|CP3)\b", re.I),
    "local path": re.compile(r"(/data/|/home/|/mnt/|~/|C:\\\\)", re.I),
    "private platform": re.compile(
        r"ChatGPT|Slack|Discord|Notion|source snapshot|email snapshot", re.I
    ),
    "secret material": re.compile(
        r"\b(access token|auth token|bearer token|secret|credential|password|api[_ -]?key|private repo|ssh key)\b",
        re.I,
    ),
    "private identity": re.compile(r"청신|동현|Ewha|이화|학생|인턴"),
    "email address": re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.I),
    "network detail": re.compile(
        r"\b(?:tailscale|localhost|127\.0\.0\.1|10\.(?:\d{1,3}\.){2}\d{1,3}|192\.168\.(?:\d{1,3}\.)\d{1,3})\b",
        re.I,
    ),
}

EXTENSIONS = {".md", ".yml", ".yaml", ".json", ".js", ".css", ".html", ".txt"}
SKIP = {"site", ".git", ".venv", "__pycache__"}


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
    findings: list[str] = []
    for path in sorted(root.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in EXTENSIONS:
            continue
        relative = path.relative_to(root)
        if relative.as_posix() == "scripts/public_scan.py":
            continue
        if any(part in SKIP for part in relative.parts[:-1]):
            continue
        for line_number, line in enumerate(path.read_text(errors="replace").splitlines(), 1):
            for label, pattern in PATTERNS.items():
                if pattern.search(line):
                    findings.append(f"{relative}:{line_number}: {label}: {line.strip()[:160]}")
    if findings:
        print("\n".join(findings))
        print(f"Blocked findings: {len(findings)}", file=sys.stderr)
        return 1
    print(f"Public-source scan passed: {root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
