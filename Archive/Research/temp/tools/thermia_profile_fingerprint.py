#!/usr/bin/env python3
"""Offline Thermia ABI/profile-family fingerprint classifier.

Classifies capture evidence into broad protocol families only.
It does NOT identify an exact heat-pump model.

No serial/network/GPIO access.
"""
from collections import Counter
from pathlib import Path
import sys

def u16(b,i): return (b[i]<<8)|b[i+1]

def parse(path):
    out=[]
    for line in Path(path).read_text(errors="replace").splitlines():
        sp=line.split()
        if len(sp)<2: continue
        try: out.append(bytes.fromhex(sp[1]))
        except ValueError: pass
    return out

def features(frames):
    fc16=Counter(); w5=Counter(); v0867=Counter()
    has1e=hasa5=False
    for b in frames:
        if not b: continue
        has1e |= b[0]==0x1E
        hasa5 |= b[0]==0xA5
        if len(b)>=9 and b[:2]==bytes((0x0F,0x10)):
            st,ct=u16(b,2),u16(b,4)
            fc16[(st,ct)]+=1
            if st==0x0864 and ct==4 and len(b)>=17:
                v0867[u16(b,13)] += 1
        if len(b)==17 and b[:3]==bytes((0x0F,0x03,0x0C)):
            w5[u16(b,13)] += 1
    return has1e,hasa5,fc16,w5,v0867

def classify(frames):
    has1e,hasa5,fc16,w5,v0867=features(frames)
    legacy=modern=0; reasons=[]
    if hasa5 and not has1e: legacy+=5; reasons.append("A5 backend")
    if has1e and not hasa5: modern+=5; reasons.append("0x1E backend")
    for (st,ct),n in fc16.items():
        if st==0x03E8:
            if ct==13: legacy+=3; reasons.append("03E8/13")
            if ct==14: modern+=3; reasons.append("03E8/14")
        if st==0x0410:
            if ct==21: legacy+=2; reasons.append("0410/21")
            if ct==22: modern+=2; reasons.append("0410/22")
        if st==0x0492:
            if ct==9: legacy+=2; reasons.append("0492/9")
            if ct==11: modern+=2; reasons.append("0492/11")
        if st==0x051E:
            if ct==9: legacy+=2; reasons.append("051E/9")
            if ct==10: modern+=2; reasons.append("051E/10")
    if v0867:
        v=v0867.most_common(1)[0][0]
        if v==0x0016: legacy+=3; reasons.append("0867=0016")
        if v==0x00E8: modern+=3; reasons.append("0867=00E8")
    if w5:
        v=w5.most_common(1)[0][0]
        if v in (6,7): legacy+=1; reasons.append(f"W5~{v} secondary")
        if v==0: modern+=1; reasons.append("W5=0 secondary")
    if legacy>=6 and modern<=2: label="LEGACY_A5_DCM03_FAMILY"
    elif modern>=6 and legacy<=2: label="MODERN_1E_FAMILY"
    else: label="AMBIGUOUS_OR_MIXED"
    return label,legacy,modern,reasons

def main():
    for p in map(Path,sys.argv[1:]):
        label,l,m,reasons=classify(parse(p))
        print(f"{p.name}: {label} legacy={l} modern={m} :: {'; '.join(reasons)}")

if __name__=="__main__":
    main()
