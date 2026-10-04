#!/usr/bin/env python3
from pathlib import Path
import json, subprocess, sys, csv

BASE=Path(__file__).resolve().parent
MODEL=BASE/"THERMIA_PROTOCOL_MODEL_V1_20261004.json"

def crc16(data):
    c=0xFFFF
    for b in data:
        c ^= b
        for _ in range(8):
            c=(c>>1)^0xA001 if c&1 else c>>1
    return c & 0xFFFF

m=json.loads(MODEL.read_text())
checks=[]

def chk(name,cond,detail=""):
    checks.append((name,bool(cond),detail))
    if not cond:
        raise AssertionError(f"{name}: {detail}")

chk("32 bootstrap pages",len(m["bootstrap"])==32,len(m["bootstrap"]))
chk("bootstrap indices 0..31",[x["index"] for x in m["bootstrap"]]==list(range(32)))
chk("bootstrap page uniqueness",len({x["page"] for x in m["bootstrap"]})==32)

for p in m["bootstrap"]:
    raw=bytes.fromhex(p["ack_frame"])
    got=raw[-2] | (raw[-1]<<8)
    chk(f"CRC {p['page']}/{p['count']}",got==crc16(raw[:-2]))

seen=set()
for s in m["selectors"]:
    key=(s["desired"]["word"],s["desired"]["bit"])
    chk(f"unique desired selector {key}",key not in seen)
    seen.add(key)
    idx=s["index"]
    if idx<16:
        chk(f"{s['page']} low-half selector word",s["desired"]["word"]=="W1")
        chk(f"{s['page']} low-half selector bit",s["desired"]["bit"]==idx)
    else:
        chk(f"{s['page']} high-half selector word",s["desired"]["word"]=="W0")
        chk(f"{s['page']} high-half selector bit",s["desired"]["bit"]==idx-16)

cal=next(s for s in m["selectors"] if s["page"]=="0x055A")
chk("calendar selector not production-authorized",cal["production_authorized"] is False)
p834=next(p for p in m["runtime_pages"] if p["page"]=="0x0834")
chk("0834 capture-only","capture-only" in p834["local_ack_policy"])
p870=next(p for p in m["runtime_pages"] if p["page"]=="0x0870")
chk("0870 recovery qualifier remains open","OPEN" in p870["recovery_rejoin_qualifier"])
chk("EXP388 remains partial",m["live_state"]["current"]["status"]=="RUNNING / PARTIAL")

# Re-run golden evidence regression if fixtures are present.
gold=BASE/"thermia_golden_trace_regression.py"
if gold.exists():
    r=subprocess.run([sys.executable,str(gold)],capture_output=True,text=True)
    chk("PROTO54 golden regression",r.returncode==0 and "PASS" in r.stdout,r.stdout.strip())

# Re-check PROTO57 reachable-state artifact.
r57=BASE/"PROTO_OFFLINE_57_REACHABLE_STATE_GRAPH_20261004.csv"
if r57.exists():
    rows=list(csv.DictReader(r57.open()))
    multi=[r for r in rows if "+" in r["semantic_owners"]]
    chk("PROTO57 no reachable multi-owner state",len(multi)==0,len(multi))

# Re-check PROTO58 0870 shadow matrix.
r58=BASE/"PROTO_OFFLINE_58_0870_SHADOW_POLICY_MATRIX_20261004.csv"
if r58.exists():
    rows=list(csv.DictReader(r58.open()))
    tp=sum(r["actual_ack"]=="True" and r["shadow_ack"]=="True" for r in rows)
    fp=sum(r["actual_ack"]=="False" and r["shadow_ack"]=="True" for r in rows)
    tn=sum(r["actual_ack"]=="False" and r["shadow_ack"]=="False" for r in rows)
    fn=sum(r["actual_ack"]=="True" and r["shadow_ack"]=="False" for r in rows)
    chk("PROTO58 0870 TP/FP/TN/FN",(tp,fp,tn,fn)==(64,0,31,0),(tp,fp,tn,fn))

print(f"THERMIA PROTOCOL MODEL V1: PASS ({len(checks)} checks)")
for name,ok,detail in checks:
    print("PASS",name,detail)