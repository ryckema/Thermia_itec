#!/usr/bin/env python3
"""
Thermia native 0x0F trace replay / state-machine verifier.

PROTO-OFFLINE-45
- Parses two capture formats:
  1) "<seconds> <hexframe>"
  2) ESPHome "[HH:MM:SS.mmm] ... RX N bytes: AA BB ..."
- Validates Modbus CRC.
- Pairs FC16 ACKs, FC03 responses and FC17 responses.
- Detects approval attempts, ordered 32-page bootstraps, 0708 mailbox replies,
  desired-page pulls, runtime/service pages, and recovery-style 0870 retry runs.
- Produces a conservative trace summary; it does NOT authorize new bus TX.

Usage:
  python thermia_trace_state_verifier.py capture1.log capture2.log ...
"""

from pathlib import Path
import re, sys, collections, statistics

CONFIG_PAGES = [
    0x03E8,0x03FC,0x0410,0x042E,0x0442,0x0456,0x046A,0x047E,
    0x0492,0x04A6,0x04BA,0x04D8,0x04F6,0x050A,0x051E,0x0532,
    0x0546,0x055A,0x057B,0x059C,0x05BD,0x05DE,0x05FF,0x0620,
    0x0641,0x0662,0x0683,0x06A4,0x06C5,0x06EA,0x06F1,0x06F4,
]
PAGE_INDEX = {p:i for i,p in enumerate(CONFIG_PAGES)}
RUNTIME_PAGES = [0x07D0,0x07E4,0x07F8,0x080C,0x0820,0x0834,0x0848,0x085F,0x0864,0x0870,0x0884]

CANONICAL_BUCKETS = {
    (0x07D0,0x07E4): "A",
    (0x07F8,0x080C): "B",
    (0x0820,0x0834): "C",
    (0x0848,0x0864): "D",
    (0x0870,): "E",
}

def modbus_crc(data):
    crc = 0xFFFF
    for b in data:
        crc ^= b
        for _ in range(8):
            crc = ((crc >> 1) ^ 0xA001) if (crc & 1) else (crc >> 1)
    return crc & 0xFFFF

def crc_ok(bs):
    if len(bs) < 3:
        return False
    c = modbus_crc(bs[:-2])
    return bs[-2] == (c & 0xFF) and bs[-1] == ((c >> 8) & 0xFF)

def parse_capture(path):
    rows = []
    t0 = None
    for line_no, line in enumerate(Path(path).read_text(errors="ignore").splitlines(), 1):
        m = re.match(r"\s*([0-9]+\.[0-9]+)\s+([0-9A-Fa-f]+)\s*$", line)
        if m:
            t = float(m.group(1))
            hx = m.group(2)
        else:
            m = re.search(
                r"\[(\d\d):(\d\d):(\d\d)\.(\d\d\d)\].*?\bRX\s+\d+\s+bytes:\s+((?:[0-9A-Fa-f]{2}\s*)+)",
                line
            )
            if not m:
                continue
            h, mi, s, ms = map(int, m.groups()[:4])
            t = h*3600 + mi*60 + s + ms/1000
            hx = "".join(m.group(5).split())
        try:
            bs = bytes.fromhex(hx)
        except ValueError:
            continue
        if t0 is None:
            t0 = t
        rows.append({"t": t-t0, "line": line_no, "bs": bs, "crc": crc_ok(bs)})
    return rows

def decode(bs):
    if len(bs) < 2:
        return {"kind":"short"}
    addr, fc = bs[0], bs[1]
    d = {"addr":addr, "fc":fc}
    if addr == 0x0F and fc == 0x10:
        if len(bs) == 8:
            d.update(kind="fc16_ack", start=(bs[2]<<8)|bs[3], count=(bs[4]<<8)|bs[5])
        elif len(bs) >= 9:
            st=(bs[2]<<8)|bs[3]; ct=(bs[4]<<8)|bs[5]; bc=bs[6]
            if len(bs) == 9 + bc:
                words=[]
                if bc == 2*ct:
                    words=[(bs[7+2*i]<<8)|bs[8+2*i] for i in range(ct)]
                d.update(kind="fc16_pub", start=st, count=ct, bc=bc, words=words)
            else:
                d.update(kind="fc16_other")
    elif addr == 0x0F and fc == 0x03:
        if len(bs) == 8:
            d.update(kind="fc03_req", start=(bs[2]<<8)|bs[3], count=(bs[4]<<8)|bs[5])
        elif len(bs) >= 5 and len(bs) == 5 + bs[2]:
            bc=bs[2]
            words=[(bs[3+2*i]<<8)|bs[4+2*i] for i in range(bc//2)]
            d.update(kind="fc03_rsp", bc=bc, words=words)
        else:
            d.update(kind="fc03_other")
    elif addr == 0x0F and fc == 0x17:
        if len(bs) >= 13:
            rs=(bs[2]<<8)|bs[3]; rc=(bs[4]<<8)|bs[5]
            ws=(bs[6]<<8)|bs[7]; wc=(bs[8]<<8)|bs[9]; bc=bs[10]
            if len(bs) == 13 + bc:
                d.update(kind="fc17_req", read_start=rs, read_count=rc,
                         write_start=ws, write_count=wc, bc=bc, data=bs[11:11+bc])
            elif len(bs) == 5 + bs[2]:
                d.update(kind="fc17_rsp", bc=bs[2], data=bs[3:3+bs[2]])
            else:
                d.update(kind="fc17_other")
        elif len(bs) >= 5 and len(bs) == 5 + bs[2]:
            d.update(kind="fc17_rsp", bc=bs[2], data=bs[3:3+bs[2]])
        else:
            d.update(kind="fc17_other")
    else:
        d.update(kind="other")
    return d

def enrich(rows):
    a=[]
    for r in rows:
        a.append({**r, **decode(r["bs"])})
    for i,e in enumerate(a):
        if e["kind"] == "fc16_pub":
            e["acked"]=False
            for j in range(i+1, min(len(a),i+20)):
                x=a[j]
                if x["t"]-e["t"] > 0.30:
                    break
                if x["kind"]=="fc16_ack" and x["start"]==e["start"] and x["count"]==e["count"]:
                    e["acked"]=True; e["ack_dt"]=x["t"]-e["t"]; e["ack_index"]=j
                    break
        elif e["kind"] == "fc03_req":
            e["responded"]=False
            for j in range(i+1, min(len(a),i+30)):
                x=a[j]
                if x["t"]-e["t"] > 0.50:
                    break
                if x["kind"]=="fc03_rsp":
                    e["responded"]=True; e["rsp_index"]=j; e["rsp_dt"]=x["t"]-e["t"]; e["rsp_words"]=x.get("words",[])
                    break
                if x["kind"]=="fc03_req":
                    break
        elif e["kind"] == "fc17_req":
            e["responded"]=False
            for j in range(i+1, min(len(a),i+30)):
                x=a[j]
                if x["t"]-e["t"] > 0.50:
                    break
                if x["kind"]=="fc17_rsp":
                    e["responded"]=True; e["rsp_index"]=j; e["rsp_dt"]=x["t"]-e["t"]; e["rsp_data"]=x.get("data",b"")
                    break
                if x["kind"]=="fc17_req":
                    break
    return a

def mailbox(a,i):
    e=a[i]
    if e["kind"]=="fc03_req" and e.get("start")==0x0708 and e.get("count")==6 and e.get("responded"):
        w=e.get("rsp_words",[])
        if len(w)==6:
            return tuple(w)
    return None

def profile_for(name):
    n=Path(name).name
    if n.startswith("itec_eco5_gateway"):
        return "eco5"
    if n == "thermia_capture_20261003_165355.log":
        return "atec_dcm03"
    if n == "thermia-logs.txt":
        return "local_xtr_passive"
    return "legacy_a5"

def steady_mailbox(profile, mb):
    if not mb:
        return False
    W0,W1,W2,W3,W4,W5=mb
    if W0 or W1 or W2 or W3:
        return False
    if profile=="eco5":
        return W4 in (0x0000,0x0100)
    if profile in ("legacy_a5","atec_dcm03"):
        return W4==0x077F
    return False

def bootstrap_sequences(a):
    """Find accepted-challenge 32-page ACKed bootstrap sequences, plus a pre-mailbox ordered partial sequence."""
    seqs=[]
    phase="UNKNOWN"; exp=0; seq=[]
    for i,e in enumerate(a):
        if e["kind"]=="fc17_req" and e.get("read_start")==0x0730 and e.get("read_count")==8 and e.get("write_start")==0x071C and e.get("write_count")==8:
            phase="WAIT" if e.get("responded") else "APPROVAL_RETRY"
            exp=0; seq=[]
            continue
        if e["kind"]=="fc16_pub" and e.get("acked") and e.get("start") in PAGE_INDEX:
            if phase=="WAIT" and e["start"]==CONFIG_PAGES[0]:
                phase="BOOT"; exp=1; seq=[i]
            elif phase=="BOOT":
                if exp < len(CONFIG_PAGES) and e["start"]==CONFIG_PAGES[exp]:
                    seq.append(i); exp+=1
                    if exp==len(CONFIG_PAGES):
                        seqs.append({"kind":"complete","indices":seq[:]})
                        phase="POST_BOOT"; seq=[]; exp=0
    # capture may start mid-bootstrap before first 0708
    first_mb=next((i for i in range(len(a)) if mailbox(a,i)),len(a))
    s=[]; last=None
    for i,e in enumerate(a[:first_mb]):
        if e["kind"]=="fc16_pub" and e.get("acked") and e.get("start") in PAGE_INDEX:
            pi=PAGE_INDEX[e["start"]]
            if last is None or pi==last+1:
                s.append(i); last=pi
            else:
                if len(s)>=3 and not any(set(s)<=set(q["indices"]) for q in seqs):
                    seqs.append({"kind":"partial_pre_mailbox","indices":s[:]})
                s=[i]; last=pi
    if len(s)>=3 and not any(set(s)<=set(q["indices"]) for q in seqs):
        seqs.append({"kind":"partial_pre_mailbox","indices":s[:]})
    return seqs

def desired_pages(mb):
    if not mb: return []
    W0,W1,*_=mb
    out=[]
    if W0 & 0x0001: out.append(0x0546)
    if W0 & 0x0002: out.append(0x055A)
    if W1 & 0x0001: out.append(0x03E8)
    if W1 & 0x0008: out.append(0x042E)
    if W1 & 0x0010: out.append(0x0442)
    return out

def analyze(path):
    rows=parse_capture(path); a=enrich(rows); prof=profile_for(path)
    c=collections.Counter()
    c["frames"]=len(a)
    c["0f_frames"]=sum(1 for e in a if e.get("addr")==0x0F)
    c["0f_crc_bad"]=sum(1 for e in a if e.get("addr")==0x0F and not e["crc"])
    c["approval_challenges"]=sum(1 for e in a if e["kind"]=="fc17_req" and e.get("read_start")==0x0730 and e.get("write_start")==0x071C)
    c["approval_accepted"]=sum(1 for e in a if e["kind"]=="fc17_req" and e.get("read_start")==0x0730 and e.get("write_start")==0x071C and e.get("responded"))
    boots=bootstrap_sequences(a)
    c["bootstrap_complete"]=sum(1 for s in boots if s["kind"]=="complete")
    c["bootstrap_partial"]=sum(1 for s in boots if s["kind"]!="complete")

    last_mb=None; last_mb_t=None
    cache={}
    desired=[]
    pending=None
    recovery_streak=0
    recovery_windows=0
    approval_retry=False
    approval_overlap_config=[]
    standalone_config=[]
    atec_steady_085f=[]
    last_config_ack_t=None

    # Runtime mailbox buckets
    mbidx=[i for i in range(len(a)) if mailbox(a,i)]
    steady_buckets=[]
    for k,i in enumerate(mbidx):
        mb=mailbox(a,i)
        if not steady_mailbox(prof,mb):
            continue
        j=mbidx[k+1] if k+1<len(mbidx) else len(a)
        seq=tuple(
            a[x]["start"] for x in range(i+1,j)
            if a[x]["kind"]=="fc16_pub" and a[x]["start"] in RUNTIME_PAGES and a[x]["start"] not in (0x085F,0x0884)
        )
        if seq:
            steady_buckets.append((a[i]["t"],seq))
    c["steady_runtime_buckets"]=len(steady_buckets)
    c["exact_canonical_buckets"]=sum(1 for _,s in steady_buckets if s in CANONICAL_BUCKETS)
    c["noncanonical_buckets"]=c["steady_runtime_buckets"]-c["exact_canonical_buckets"]

    for i,e in enumerate(a):
        if e["kind"]=="fc17_req" and e.get("read_start")==0x0730 and e.get("write_start")==0x071C:
            approval_retry=not e.get("responded")
            if e.get("responded"):
                approval_retry=False
            last_mb=None; last_mb_t=None
            continue

        mb=mailbox(a,i)
        if mb:
            last_mb=mb; last_mb_t=e["t"]
            c["mailbox_answered"]+=1
            if mb[0] or mb[1]: c["mailbox_desired"]+=1
            if mb[2] or mb[3]: c["mailbox_config"]+=1
            continue

        if e["kind"]=="fc16_pub":
            st=e["start"]
            if st in CONFIG_PAGES:
                if e.get("acked"): c["config_acked"]+=1
                else: c["config_unacked"]+=1
                if approval_retry and e.get("acked"):
                    approval_overlap_config.append((e["t"],st,e["count"]))
                # Cross-profile standalone config push: ACKed page while last mailbox is steady and W2/W3=0
                if e.get("acked") and last_mb and steady_mailbox(prof,last_mb):
                    # only count if no desired selector is active
                    if last_mb[0]==0 and last_mb[1]==0 and last_mb[2]==0 and last_mb[3]==0:
                        standalone_config.append((e["t"],st,e["count"],tuple(e.get("words",[]))))
                cache[st]=e
                if e.get("acked"): last_config_ack_t=e["t"]

                if pending and st==pending["page"] and pending["delta"]>0 and e["t"]-pending["t"]<=3:
                    if e.get("acked") and tuple(e.get("words",[]))==pending["desired"]:
                        c["desired_confirmed"]+=1
                    else:
                        c["desired_confirm_mismatch"]+=1
                    pending=None
                continue

            if st in RUNTIME_PAGES:
                c["runtime_pub"]+=1
                if e.get("acked"): c["runtime_acked"]+=1
                else: c["runtime_unacked"]+=1
                if st==0x085F:
                    if e.get("acked"): c["085f_acked"]+=1
                    else: c["085f_unacked"]+=1
                    if prof=="atec_dcm03" and e.get("acked") and last_mb and steady_mailbox(prof,last_mb):
                        atec_steady_085f.append((e["t"],last_mb))
                if st==0x0834:
                    if e.get("acked"): c["0834_acked"]+=1
                    else: c["0834_unacked"]+=1
                if st==0x0870:
                    if e.get("acked"):
                        c["0870_acked"]+=1
                        if recovery_streak>=2:
                            recovery_windows+=1
                        recovery_streak=0
                    else:
                        c["0870_unacked"]+=1
                        recovery_streak+=1
                elif st not in (0x085F,):
                    # any other runtime publication breaks a raw repeated-0870 streak
                    if recovery_streak and st!=0x0870:
                        recovery_streak=0
                continue

        if e["kind"]=="fc03_req" and e.get("start") in PAGE_INDEX and e.get("responded"):
            pages=desired_pages(last_mb) if last_mb_t is not None and e["t"]-last_mb_t<=3 else []
            if e["start"] in pages:
                current=cache.get(e["start"])
                desired_words=tuple(e.get("rsp_words",[]))
                delta=None
                if current and len(current.get("words",[]))==len(desired_words):
                    delta=sum(1 for x,y in zip(current["words"],desired_words) if x!=y)
                desired.append((e["t"],e["start"],delta))
                c["desired_pulls"]+=1
                if delta==0: c["desired_noop"]+=1
                elif delta is None: c["desired_unbracketed"]+=1
                elif delta>0:
                    c["desired_delta"]+=1
                    pending={"page":e["start"],"desired":desired_words,"delta":delta,"t":e["t"]}

    c["recovery_0870_windows"]=recovery_windows

    # Local passive retry-loop characterization
    if prof=="local_xtr_passive":
        p03=[e for e in a if e["kind"]=="fc16_pub" and e.get("start")==0x03E8]
        p85=[e for e in a if e["kind"]=="fc16_pub" and e.get("start")==0x085F]
        c["local_03e8_unacked"]=sum(1 for e in p03 if not e.get("acked"))
        c["local_085f_unacked"]=sum(1 for e in p85 if not e.get("acked"))
        c["duration_s"]=round(a[-1]["t"]-a[0]["t"],3) if a else 0

    return {
        "file":Path(path).name,
        "profile":prof,
        "counts":dict(c),
        "bootstraps":[
            {
                "kind":s["kind"],
                "count":len(s["indices"]),
                "first":f"{a[s['indices'][0]]['start']:04X}",
                "last":f"{a[s['indices'][-1]]['start']:04X}",
                "t_start":round(a[s["indices"][0]]["t"],3),
                "t_end":round(a[s["indices"][-1]]["t"],3),
            } for s in boots
        ],
        "desired":[{"t":round(t,3),"page":f"{p:04X}","delta_words":d} for t,p,d in desired],
        "approval_overlap_config":[{"t":round(t,3),"page":f"{p:04X}","count":ct} for t,p,ct in approval_overlap_config],
        "standalone_config":[{"t":round(t,3),"page":f"{p:04X}","count":ct,"words":list(w)} for t,p,ct,w in standalone_config],
        "atec_steady_085f":[{"t":round(t,3),"mailbox":[f"{x:04X}" for x in mb]} for t,mb in atec_steady_085f],
        "steady_bucket_exceptions":[
            {"t":round(t,3),"seq":[f"{x:04X}" for x in seq]}
            for t,seq in steady_buckets if seq not in CANONICAL_BUCKETS
        ],
    }

def main(argv):
    if not argv:
        print("Provide one or more capture files.", file=sys.stderr)
        return 2
    results=[analyze(p) for p in argv]
    for r in results:
        c=r["counts"]
        exact=c.get("exact_canonical_buckets",0); total=c.get("steady_runtime_buckets",0)
        pct=(100*exact/total) if total else 0
        print(f"{r['file']} [{r['profile']}]")
        print(f"  0F frames={c.get('0f_frames',0)} crc_bad={c.get('0f_crc_bad',0)} "
              f"approval={c.get('approval_accepted',0)}/{c.get('approval_challenges',0)} "
              f"bootstrap_complete={c.get('bootstrap_complete',0)} partial={c.get('bootstrap_partial',0)}")
        print(f"  mailbox={c.get('mailbox_answered',0)} desired_pulls={c.get('desired_pulls',0)} "
              f"confirmed={c.get('desired_confirmed',0)} recovery0870={c.get('recovery_0870_windows',0)}")
        print(f"  runtime={c.get('runtime_pub',0)} acked={c.get('runtime_acked',0)} "
              f"085F={c.get('085f_acked',0)}/{c.get('085f_acked',0)+c.get('085f_unacked',0)} ACKed "
              f"0834={c.get('0834_acked',0)}/{c.get('0834_acked',0)+c.get('0834_unacked',0)} ACKed")
        if total:
            print(f"  steady mailbox buckets exact canonical={exact}/{total} ({pct:.1f}%)")
        if r["approval_overlap_config"]:
            print(f"  approval/config overlap={r['approval_overlap_config']}")
        if r["standalone_config"]:
            print(f"  standalone ACKed config pushes={[(x['t'],x['page']) for x in r['standalone_config']]}")
        if r["atec_steady_085f"]:
            print(f"  ATEC steady 085F ACK={r['atec_steady_085f']}")
        if r["profile"]=="local_xtr_passive":
            print(f"  local passive loop: 03E8 unACKed={c.get('local_03e8_unacked',0)}, "
                  f"085F unACKed={c.get('local_085f_unacked',0)}, duration={c.get('duration_s',0)}s")
        print()
    return 0

if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))