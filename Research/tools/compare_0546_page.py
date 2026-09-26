#!/usr/bin/env python3
"""Compare EXP219 local 0x0F FC16 0546/count20 pages with the genuine reference.

Offline-only: reads text logs, performs no serial/network/GPIO operations.

Expected EXP219 log line:
  [EXP219] 0546/count20 frame=N words=[....] 0553=X 0559=Y

Reference image is the genuine DCM/reference 0546/count20 page observed in the
2026-09-26 reconnect capture:
  [2,0,2,0,0,0,0,0,0,0,0,0,0,4,0,0,0,0,0,0]

Addresses span 0x0546..0x0559.
Known semantics:
  0x0553 / index1363 = Operation Mode
  0x0559 / index1369 = Link Integration
"""

from __future__ import annotations

import argparse
import re
from collections import Counter
from pathlib import Path

START = 0x0546
COUNT = 20
REFERENCE = [2,0,2,0,0,0,0,0,0,0,0,0,0,4,0,0,0,0,0,0]
KNOWN = {
    0x0553: "Operation Mode",
    0x0559: "Link Integration",
}

LINE_RE = re.compile(
    r"\[EXP219\]\s+0546/count20\s+frame=(\d+)\s+"
    r"words=\[([^\]]+)\].*?0553=(-?\d+)\s+0559=(-?\d+)"
)


def parse(path: Path) -> list[tuple[int, list[int]]]:
    out: list[tuple[int, list[int]]] = []
    for line in path.read_text(errors="replace").splitlines():
        m = LINE_RE.search(line)
        if not m:
            continue
        frame_no = int(m.group(1))
        words = [int(x, 16) for x in m.group(2).split()]
        if len(words) != COUNT:
            raise ValueError(f"frame {frame_no}: expected {COUNT} words, got {len(words)}")
        # Sanity check against separately printed known fields.
        if words[0x0553 - START] != int(m.group(3)):
            raise ValueError(f"frame {frame_no}: 0553 sanity check failed")
        if words[0x0559 - START] != int(m.group(4)):
            raise ValueError(f"frame {frame_no}: 0559 sanity check failed")
        out.append((frame_no, words))
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("log", type=Path)
    args = ap.parse_args()

    pages = parse(args.log)
    if not pages:
        print("No EXP219 full 0546/count20 pages found.")
        return 2

    print(f"pages: {len(pages)}")

    # Per-address stability within the local capture.
    print("\nLocal stability:")
    local_modes: list[int] = []
    for i in range(COUNT):
        addr = START + i
        vals = [w[i] for _, w in pages]
        counts = Counter(vals)
        label = KNOWN.get(addr, "")
        suffix = f"  {label}" if label else ""
        if len(counts) == 1:
            print(f"  0x{addr:04X}: {vals[0]} (0x{vals[0]:04X}) stable{suffix}")
        else:
            print(f"  0x{addr:04X}: VARIES {dict(counts)}{suffix}")
        if addr == 0x0553:
            local_modes = vals

    # Compare the first local page to the reference, while also flagging any
    # address whose local values differ across frames.
    first_no, first = pages[0]
    print(f"\nReference diff (using local frame {first_no}):")
    diffs = 0
    non_mode_diffs = 0
    for i, (lv, rv) in enumerate(zip(first, REFERENCE)):
        if lv == rv:
            continue
        addr = START + i
        diffs += 1
        if addr != 0x0553:
            non_mode_diffs += 1
        label = KNOWN.get(addr, "unmapped")
        print(
            f"  0x{addr:04X}: local={lv} (0x{lv:04X}) "
            f"reference={rv} (0x{rv:04X})  {label}"
        )

    if diffs == 0:
        print("  none: local page is byte-for-byte identical to the reference.")
    elif non_mode_diffs == 0:
        print(
            "  Only 0x0553 Operation Mode differs. "
            "All other 19 words match the genuine reference page."
        )

    stable_pages = len({tuple(words) for _, words in pages})
    print(f"\nunique full-page images: {stable_pages}")
    print(f"operation-mode values seen: {sorted(set(local_modes))}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
