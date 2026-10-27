#!/usr/bin/env python3
"""Offline Thermia bus-capture analyzer.

SAFETY: this tool only reads text log files. It has no serial-port or network TX code.

Expected log format: one frame per line, e.g.:
    27.051 0f1008640004835b

The analyzer extracts the events most useful for EXP208/EXP214:
- first A5/A4/05 activity;
- first 0x04 activity;
- first 0x0F FC03 0708/count6 mailbox poll;
- first runtime FC16 page in 07D0..0884;
- first slave-0x0F FC16 ACK / FC03 response;
- the 0x02 FC17 write fingerprint at A811/A812 when present;
- candidate first extended-topology event.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Iterable, Optional

RUNTIME_STARTS = {
    0x07D0, 0x07E4, 0x07F8, 0x080C, 0x0820,
    0x0834, 0x0848, 0x0864, 0x0870, 0x0884,
}


@dataclass(frozen=True)
class Frame:
    t: float
    raw: bytes
    line_no: int

    @property
    def slave(self) -> Optional[int]:
        return self.raw[0] if self.raw else None

    @property
    def function(self) -> Optional[int]:
        return self.raw[1] if len(self.raw) >= 2 else None


@dataclass
class Analysis:
    file: str
    frames: int = 0
    crc_valid_frames: int = 0
    crc_invalid_frames: int = 0
    first_a5: Optional[float] = None
    first_a4: Optional[float] = None
    first_05: Optional[float] = None
    first_04: Optional[float] = None
    first_0708_poll: Optional[float] = None
    first_runtime_fc16: Optional[float] = None
    first_0f_fc16_ack: Optional[float] = None
    first_0f_fc03_response: Optional[float] = None
    first_extended_event: Optional[float] = None
    first_extended_event_kind: Optional[str] = None
    a811: Optional[int] = None
    a812: Optional[int] = None
    a811_a812_first_seen: Optional[float] = None
    extended_topology_seen: bool = False
    evidence_count: int = 0


def modbus_crc(data: bytes) -> int:
    crc = 0xFFFF
    for b in data:
        crc ^= b
        for _ in range(8):
            if crc & 1:
                crc = (crc >> 1) ^ 0xA001
            else:
                crc >>= 1
    return crc & 0xFFFF


def crc_ok(frame: bytes) -> bool:
    if len(frame) < 4:
        return False
    expected = frame[-2] | (frame[-1] << 8)
    return modbus_crc(frame[:-2]) == expected


def parse_log(path: Path) -> Iterable[Frame]:
    for line_no, line in enumerate(path.read_text(errors="replace").splitlines(), 1):
        parts = line.strip().split()
        if len(parts) < 2:
            continue
        try:
            t = float(parts[0])
            raw = bytes.fromhex(parts[1])
        except (ValueError, TypeError):
            continue
        yield Frame(t=t, raw=raw, line_no=line_no)


def u16be(b: bytes, offset: int) -> int:
    return (b[offset] << 8) | b[offset + 1]


def fc03_request(frame: bytes, slave: int, start: int, count: int) -> bool:
    return (
        len(frame) == 8
        and frame[0] == slave
        and frame[1] == 0x03
        and u16be(frame, 2) == start
        and u16be(frame, 4) == count
    )


def fc16_request(frame: bytes, slave: int) -> Optional[tuple[int, int]]:
    if len(frame) < 9 or frame[0] != slave or frame[1] != 0x10:
        return None
    start = u16be(frame, 2)
    count = u16be(frame, 4)
    byte_count = frame[6]
    if len(frame) != 9 + byte_count:
        return None
    return start, count


def fc16_ack(frame: bytes, slave: int) -> bool:
    return len(frame) == 8 and frame[0] == slave and frame[1] == 0x10


def fc03_response(frame: bytes, slave: int) -> bool:
    if len(frame) < 5 or frame[0] != slave or frame[1] != 0x03:
        return False
    byte_count = frame[2]
    return len(frame) == 5 + byte_count


def parse_02_fc17_fingerprint(frame: bytes) -> Optional[tuple[int, int]]:
    """Return A811/A812 from a controller FC17 request writing A80C..A812."""
    if len(frame) < 13 or frame[0] != 0x02 or frame[1] != 0x17:
        return None
    write_start = u16be(frame, 6)
    write_count = u16be(frame, 8)
    byte_count = frame[10]
    if write_start != 0xA80C or write_count < 7 or byte_count < 14:
        return None
    data_start = 11
    data_end = data_start + byte_count
    if data_end + 2 != len(frame):
        return None
    words = [u16be(frame, data_start + 2 * i) for i in range(write_count)]
    return words[5], words[6]


def analyze(path: Path) -> Analysis:
    a = Analysis(file=str(path))
    extended_candidates: list[tuple[float, str]] = []

    for f in parse_log(path):
        a.frames += 1
        if crc_ok(f.raw):
            a.crc_valid_frames += 1
        else:
            a.crc_invalid_frames += 1

        if f.slave == 0xA5 and a.first_a5 is None:
            a.first_a5 = f.t
            extended_candidates.append((f.t, "A5"))
        if f.slave == 0xA4 and a.first_a4 is None:
            a.first_a4 = f.t
            extended_candidates.append((f.t, "A4"))
        if f.slave == 0x05 and a.first_05 is None:
            a.first_05 = f.t
            extended_candidates.append((f.t, "05"))
        if f.slave == 0x04 and a.first_04 is None:
            a.first_04 = f.t

        if fc03_request(f.raw, 0x0F, 0x0708, 6) and a.first_0708_poll is None:
            a.first_0708_poll = f.t
            extended_candidates.append((f.t, "0F.FC03.0708/6"))

        req = fc16_request(f.raw, 0x0F)
        if req and req[0] in RUNTIME_STARTS and a.first_runtime_fc16 is None:
            a.first_runtime_fc16 = f.t
            extended_candidates.append((f.t, f"0F.FC16.{req[0]:04X}/{req[1]}"))

        if fc16_ack(f.raw, 0x0F) and a.first_0f_fc16_ack is None:
            a.first_0f_fc16_ack = f.t
        if fc03_response(f.raw, 0x0F) and a.first_0f_fc03_response is None:
            a.first_0f_fc03_response = f.t

        fp = parse_02_fc17_fingerprint(f.raw)
        if fp is not None and a.a811 is None:
            a.a811, a.a812 = fp
            a.a811_a812_first_seen = f.t

    if extended_candidates:
        extended_candidates.sort()
        a.first_extended_event, a.first_extended_event_kind = extended_candidates[0]

    families = sum(
        x is not None
        for x in (a.first_a5, a.first_0708_poll, a.first_runtime_fc16)
    )
    a.evidence_count = families
    a.extended_topology_seen = families >= 2
    return a


def human(a: Analysis) -> str:
    def fmt(v: Optional[float]) -> str:
        return "-" if v is None else f"{v:.3f} s"

    fp = "-" if a.a811 is None else (
        f"A811=0x{a.a811:04X}, A812=0x{a.a812:04X} @ "
        f"{fmt(a.a811_a812_first_seen)}"
    )
    lines = [
        f"file: {a.file}",
        f"frames: {a.frames} (CRC ok {a.crc_valid_frames}, bad {a.crc_invalid_frames})",
        f"first A5: {fmt(a.first_a5)}",
        f"first A4: {fmt(a.first_a4)}",
        f"first 05: {fmt(a.first_05)}",
        f"first 04: {fmt(a.first_04)}",
        f"first 0708/count6 poll: {fmt(a.first_0708_poll)}",
        f"first runtime FC16: {fmt(a.first_runtime_fc16)}",
        f"first 0F FC16 ACK: {fmt(a.first_0f_fc16_ack)}",
        f"first 0F FC03 response: {fmt(a.first_0f_fc03_response)}",
        f"0x02 fingerprint: {fp}",
        f"first extended event: {fmt(a.first_extended_event)} ({a.first_extended_event_kind or '-'})",
        f"extended topology seen: {'YES' if a.extended_topology_seen else 'NO'} (families={a.evidence_count}/3)",
    ]
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("logs", nargs="+", type=Path)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    results = [analyze(p) for p in args.logs]
    if args.json:
        print(json.dumps([asdict(x) for x in results], indent=2))
    else:
        for i, result in enumerate(results):
            if i:
                print()
            print(human(result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
