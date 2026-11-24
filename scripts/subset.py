#!/usr/bin/env python3
"""Map SUBSET to extra test arguments. Write args to a file; print nothing."""
from __future__ import annotations

import os
import sys
from pathlib import Path

# Keep this mapping out of the workflow file so Actions does not echo it in logs.
_MAP = {
    "ocr": ("--filter", "FullyQualifiedName~MarkingOcr"),
}


def main() -> int:
    subset = os.environ.get("SUBSET") or "all"
    dest = Path(os.environ["RUNNER_TEMP"]) / "subset.args"
    if dest.exists():
        dest.unlink()
    if subset in ("all", ""):
        return 0
    args = _MAP.get(subset)
    if args is None:
        print("Invalid subset.", file=sys.stderr)
        return 1
    dest.write_text("\n".join(args) + "\n", encoding="ascii", newline="\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
