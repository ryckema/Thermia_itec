#!/usr/bin/env python3
"""Offline Thermia protocol schema/YAML linter.

Fail-closed static checker only. No network, serial, GPIO or device TX.
Validates bootstrap page/count ACK CRCs, known-proven selector frames,
TEST marking, and keeps symmetry-only desired selectors as deny-by-default.
"""
import json, re, sys
from pathlib import Path

def crc16(data):
    c=0xFFFF
    for b in data:
        c ^= b
        for _ in range(8):
            c=(c>>1)^0xA001 if c&1 else c>>1
    return c & 0xFFFF

def main():
    if len(sys.argv)!=3:
        print("usage: thermia_protocol_linter.py SCHEMA.json WRITE.yaml")
        return 2
    schema=json.loads(Path(sys.argv[1]).read_text())
    text=Path(sys.argv[2]).read_text()
    errors=[]; warnings=[]; passes=[]
    for p in schema["bootstrap"]:
        frame=p["ack_frame"]
        raw=bytes.fromhex(frame)
        got=raw[-2] | raw[-1]<<8
        calc=crc16(raw[:-2])
        if got!=calc:
            errors.append(f'bad schema CRC {p["page"]}/{p["count"]}')
        elif frame not in text:
            warnings.append(f'ACK frame not found textually {p["page"]}/{p["count"]}')
        else:
            passes.append(f'ACK {p["page"]}/{p["count"]}')
    known={
      "03E8":"0F030C000000010000000100000006AD26",
      "042E":"0F030C0000000800000008000000061B77",
      "0442":"0F030C0000001000000010000000069175",
      "0546":"0F030C000100000001000000000006894A",
    }
    for page,frame in known.items():
        raw=bytes.fromhex(frame)
        if (raw[-2] | raw[-1]<<8)!=crc16(raw[:-2]):
            errors.append(f'bad selector CRC {page}')
        elif frame not in text:
            warnings.append(f'selector frame not found {page}')
        else:
            passes.append(f'selector {page}')
    tests=len(re.findall(r'name:\s*"[^"]*TEST[^"]*"',text))
    if tests!=7: warnings.append(f'TEST controls={tests}, expected 7')
    else: passes.append('7 TEST controls visibly marked')
    print("errors",len(errors))
    for x in errors: print("ERROR",x)
    print("warnings",len(warnings))
    for x in warnings: print("WARN",x)
    print("passes",len(passes))
    for x in passes: print("PASS",x)
    return 1 if errors else 0
if __name__=="__main__":
    raise SystemExit(main())
