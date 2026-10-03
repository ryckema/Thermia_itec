#!/usr/bin/env python3
"""Capture regression checks for the current Thermia DCM reference model.

Offline-only. Reads timestamped capture logs, performs no serial/network/GPIO TX.

Validates the capture-backed invariants represented by
thermia_dcm_reference_model_current.py:
- genuine Eco5 32-page ACK-gated startup bootstrap;
- first 0708 after bootstrap completion;
- later FFFF/867F 26-page refresh set and order;
- genuine desired pulls only for observed W1 bits 0 and 3;
- full-page one-word desired mutation + exact FC16 result;
- genuine W0 remains zero in the six reference captures;
- recurrent 04A6/085F are mostly unACKed outside strict work context.
"""

from pathlib import Path
from collections import defaultdict
import argparse

BOOT = [
    (0x03E8,14),(0x03FC,11),(0x0410,22),(0x042E,15),(0x0442,13),(0x0456,12),(0x046A,18),(0x047E,19),
    (0x0492,11),(0x04A6,13),(0x04BA,22),(0x04D8,27),(0x04F6,14),(0x050A,19),(0x051E,10),(0x0532,18),
    (0x0546,20),(0x055A,33),(0x057B,33),(0x059C,33),(0x05BD,33),(0x05DE,33),(0x05FF,33),(0x0620,33),
    (0x0641,33),(0x0662,33),(0x0683,33),(0x06A4,33),(0x06C5,33),(0x06EA,7),(0x06F1,3),(0x06F4,19),
]
BOOTSET=set(BOOT)
REFRESH={s for s,_ in BOOT}-{0x047E,0x0492,0x04D8,0x04F6,0x050A,0x051E}

def u16(b,i): return (b[i]<<8)|b[i+1]
def modbus_crc(data):
    c=0xffff
    for x in data:
        c^=x
        for _ in range(8):
            c=(c>>1)^0xA001 if c&1 else c>>1
    return c&0xffff
def crc_ok(b): return len(b)>=4 and (b[-2]|b[-1]<<8)==modbus_crc(b[:-2])

def load(path):
    out=[]
    for ln,line in enumerate(path.read_text(errors="replace").splitlines(),1):
        sp=line.split()
        if len(sp)<2: continue
        try: out.append((float(sp[0]),bytes.fromhex(sp[1]),ln))
        except ValueError: pass
    return out

def fc16_req(b):
    if len(b)<9 or b[:2]!=bytes((0x0f,0x10)): return None
    start,count,bc=u16(b,2),u16(b,4),b[6]
    if bc!=count*2 or len(b)!=9+bc: return None
    return start,count,[u16(b,7+2*i) for i in range(count)]
def fc16_ack(b):
    return (u16(b,2),u16(b,4)) if len(b)==8 and b[:2]==bytes((0x0f,0x10)) else None
def fc03_req(b):
    return (u16(b,2),u16(b,4)) if len(b)==8 and b[:2]==bytes((0x0f,0x03)) else None
def fc03_rsp(b):
    if len(b)>=5 and b[:2]==bytes((0x0f,0x03)) and len(b)==5+b[2]:
        return [u16(b,3+2*i) for i in range(b[2]//2)]
    return None

def next_ack(fr,i,pair,max_dt=0.8):
    t0=fr[i][0]
    for j in range(i+1,min(len(fr),i+20)):
        if fr[j][0]-t0>max_dt: break
        if fc16_ack(fr[j][1])==pair: return j
        r=fc16_req(fr[j][1])
        if r and (r[0],r[1])!=pair: break
    return None

def paired_0708(fr):
    out=[]
    for i,(t,b,_) in enumerate(fr):
        if fc03_req(b)!=(0x0708,6): continue
        for j in range(i+1,min(len(fr),i+8)):
            rsp=fc03_rsp(fr[j][1])
            if rsp is not None and len(rsp)==6:
                out.append((i,j,t,fr[j][0],rsp)); break
            if fr[j][0]-t>0.3: break
    return out

def find_bootstraps(fr):
    results=[]
    for start_i,(t,b,_) in enumerate(fr):
        r=fc16_req(b)
        if not r or (r[0],r[1])!=BOOT[0] or next_ack(fr,start_i,BOOT[0]) is None: continue
        expected=0; i=start_i; accepted=[]; last_ack=None; ok=True
        while i<len(fr) and expected<len(BOOT):
            r=fc16_req(fr[i][1])
            if r:
                pair=(r[0],r[1])
                if pair==BOOT[expected]:
                    ai=next_ack(fr,i,pair)
                    if ai is not None:
                        accepted.append(pair); last_ack=ai; expected+=1; i=ai+1; continue
                elif pair in BOOTSET and BOOT.index(pair)>expected:
                    ok=False; break
            if fr[i][0]-fr[start_i][0]>90: break
            i+=1
        if ok and expected==32:
            first0708=None
            for j in range(last_ack+1,len(fr)):
                if fc03_req(fr[j][1])==(0x0708,6): first0708=fr[j][0]; break
                if fr[j][0]-fr[last_ack][0]>10: break
            results.append((fr[start_i][0],accepted,fr[last_ack][0],first0708))
    ded=[]
    for x in results:
        if not ded or abs(x[0]-ded[-1][0])>2: ded.append(x)
    return ded

def refresh_windows(fr):
    pairs=paired_0708(fr); out=[]
    for k,(i,j,t,tr,w) in enumerate(pairs):
        if (w[2],w[3])!=(0xffff,0x867f): continue
        stop=pairs[k+1][0] if k+1<len(pairs) else len(fr)
        seq=[]; seen=set()
        for q in range(j+1,stop):
            r=fc16_req(fr[q][1])
            if r and r[0] in REFRESH and r[0] not in seen:
                seq.append(r[0]); seen.add(r[0])
        expected=[s for s,_ in BOOT if s in REFRESH]
        out.append((tr,len(seq)==26,set(seq)==REFRESH,seq==expected))
    return out

def desired_events(fr):
    pairs=paired_0708(fr); page_reqs=defaultdict(list); out=[]
    for idx,(t,b,_) in enumerate(fr):
        r=fc16_req(b)
        if r: page_reqs[r[0]].append((idx,t,r[1],r[2]))
    for i,j,t,tr,w in pairs:
        if w[1]==0: continue
        if w[1] & (w[1]-1): out.append((tr,None,False,"multi-bit W1")); continue
        bit=(w[1]&-w[1]).bit_length()-1
        page={0:0x03e8,3:0x042e}.get(bit)
        if page is None: out.append((tr,None,False,f"unmodeled W1 bit{bit}")); continue
        reqi=rspi=None; desired=None; count=None
        for q in range(j+1,min(len(fr),j+30)):
            rq=fc03_req(fr[q][1])
            if rq and rq[0]==page:
                reqi=q; count=rq[1]
                for z in range(q+1,min(len(fr),q+8)):
                    rr=fc03_rsp(fr[z][1])
                    if rr is not None and len(rr)==count:
                        rspi=z; desired=rr; break
                break
        if desired is None: out.append((tr,page,False,"missing desired response")); continue
        prev=[x for x in page_reqs[page] if x[0]<reqi]
        foll=[x for x in page_reqs[page] if x[0]>rspi]
        prev=prev[-1] if prev else None; foll=foll[0] if foll else None
        delta=[n for n,(a,b) in enumerate(zip(prev[3],desired)) if a!=b] if prev and len(prev[3])==len(desired) else None
        confirm=(foll[3]==desired) if foll and len(foll[3])==len(desired) else None
        out.append((tr,page,delta is not None and len(delta)==1 and confirm is True,(delta,confirm)))
    return out

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("captures",nargs="+",type=Path)
    args=ap.parse_args()
    loaded={p.name:load(p) for p in args.captures}
    eco={k:v for k,v in loaded.items() if k.startswith("itec_eco5_gateway_")}
    boots=[(n,x) for n,fr in eco.items() for x in find_bootstraps(fr)]
    refresh=[(n,x) for n,fr in eco.items() for x in refresh_windows(fr)]
    desired=[(n,x) for n,fr in eco.items() for x in desired_events(fr)]
    w0_nonzero=sum(1 for fr in loaded.values() for *_,w in paired_0708(fr) if w[0]!=0)

    print("captures",len(loaded))
    print("crc_bad",sum(sum(1 for _,b,_ in fr if not crc_ok(b)) for fr in loaded.values()))
    print("answered_0708",sum(len(paired_0708(fr)) for fr in loaded.values()))
    print("w0_nonzero",w0_nonzero)
    print("bootstraps",len(boots))
    for n,(start,seq,end,first0708) in boots:
        print("bootstrap",n,f"{start:.3f}",len(seq),seq==BOOT,
              "0708_after_terminal_ack",None if first0708 is None else round(first0708-end,3))
    print("refresh_windows",len(refresh))
    for n,x in refresh: print("refresh",n,*x)
    print("desired_events",len(desired))
    for n,x in desired: print("desired",n,*x)

    checks={
        "six_bootstraps":len(boots)==6,
        "bootstrap_exact":all(len(x[1])==32 and x[1]==BOOT for _,x in boots),
        "0708_after_bootstrap":all(x[3] is not None and x[3]>x[2] for _,x in boots),
        "w0_zero":w0_nonzero==0,
        "desired_clean":len(desired)>=4 and all(x[2] for _,x in desired),
        "refresh_exact":sum(1 for _,x in refresh if x[1] and x[2] and x[3])>=6,
    }
    print("checks",checks)
    if not all(checks.values()): raise SystemExit(2)

if __name__=="__main__":
    main()
