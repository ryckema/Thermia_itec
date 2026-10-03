#!/usr/bin/env python3
"""Offline Thermia Online/DCM ABI/topology classifier.

This is a deterministic evidence classifier, not a product/model detector.
It performs no network, serial, GPIO or device TX.

Classes:
- LEGACY_DCM_A5: older genuine Online/DCM ABI with A5 backend traits.
- MODERN_1E_ONLINE: modern 0x1E-backed Online ABI traits.
- AMBIGUOUS: insufficient or mixed evidence.

Do not interpret MODERN_1E_ONLINE as proof of a specific Thermia model.
"""

from collections import Counter
from pathlib import Path
import argparse

def u16(b, i):
    return (b[i] << 8) | b[i + 1]

def load(path):
    frames = []
    for line in path.read_text(errors="replace").splitlines():
        parts = line.split()
        if len(parts) < 2:
            continue
        try:
            frames.append((float(parts[0]), bytes.fromhex(parts[1])))
        except ValueError:
            pass
    return frames

def fc16_request(b):
    if len(b) < 9 or b[:2] != bytes((0x0F, 0x10)):
        return None
    start, count, bc = u16(b,2), u16(b,4), b[6]
    if bc != count * 2 or len(b) != 9 + bc:
        return None
    return start, count, [u16(b, 7 + 2*i) for i in range(count)]

def fc03_request(b):
    if len(b) == 8 and b[:2] == bytes((0x0F,0x03)):
        return u16(b,2), u16(b,4)
    return None

def fc03_response(b):
    if len(b) >= 5 and b[:2] == bytes((0x0F,0x03)) and len(b) == 5 + b[2] and b[2] % 2 == 0:
        return [u16(b, 3 + 2*i) for i in range(b[2] // 2)]
    return None

def paired_0708(frames):
    out = []
    for i,(t,b) in enumerate(frames):
        if fc03_request(b) != (0x0708,6):
            continue
        for j in range(i+1, min(i+8, len(frames))):
            if frames[j][0] - t > 0.3:
                break
            words = fc03_response(frames[j][1])
            if words is not None and len(words) == 6:
                out.append(words)
                break
    return out

def classify(path):
    frames = load(path)
    a5 = sum(1 for _,b in frames if b and b[0] == 0xA5)
    onee = sum(1 for _,b in frames if b and b[0] == 0x1E)
    c13 = c14 = history = 0
    v0867 = []
    for _,b in frames:
        r = fc16_request(b)
        if not r:
            continue
        start,count,words = r
        if (start,count) == (0x03E8,13):
            c13 += 1
        if (start,count) == (0x03E8,14):
            c14 += 1
        if (start,count) == (0x0864,4):
            v0867.append(words[3])
        if (start,count) == (0x0884,60):
            history += 1

    w5 = [w[5] for w in paired_0708(frames)]
    legacy = modern = 0
    if a5: legacy += 4
    if onee: modern += 4
    if c13: legacy += 3
    if c14: modern += 3
    if v0867 and set(v0867) == {0x0016}: legacy += 3
    if v0867 and set(v0867) == {0x00E8}: modern += 3
    if w5 and set(w5) <= {6,7}: legacy += 2
    if w5 and set(w5) == {0}: modern += 2

    if legacy > modern:
        cls = "LEGACY_DCM_A5"
    elif modern > legacy:
        cls = "MODERN_1E_ONLINE"
    else:
        cls = "AMBIGUOUS"

    return {
        "file": path.name,
        "frames": len(frames),
        "a5": a5, "onee": onee,
        "03e8_13": c13, "03e8_14": c14,
        "w5": dict(Counter(w5)),
        "0867": sorted(set(v0867)),
        "0884": history,
        "legacy_score": legacy, "modern_score": modern,
        "class": cls,
    }

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("captures", nargs="+", type=Path)
    args = ap.parse_args()
    for p in args.captures:
        x = classify(p)
        print(x)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
