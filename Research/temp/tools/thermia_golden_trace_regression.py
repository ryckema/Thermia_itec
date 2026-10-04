#!/usr/bin/env python3
"""PROTO-OFFLINE-54 golden-trace regression suite.

Requires thermia_trace_state_verifier.py and the eight named capture fixtures
in the same directory. Returns non-zero on the first regression.
"""
from pathlib import Path
import importlib.util, sys

BASE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location("tv",BASE/"thermia_trace_state_verifier.py")
tv=importlib.util.module_from_spec(spec); spec.loader.exec_module(tv)

files={
"legacy_20260924":BASE/"thermia_capture_20260924_210001(1).log",
"legacy_20260925_071517":BASE/"thermia_capture_20260925_071517.log",
"legacy_20260925_090209":BASE/"thermia_capture_20260925_090209.log",
"legacy_20260925_090550":BASE/"thermia_capture_20260925_090550.log",
"eco5_20260926":BASE/"itec_eco5_gateway_20260926.log",
"eco5_20260928":BASE/"itec_eco5_gateway_20260928.log",
"atec_20261003":BASE/"thermia_capture_20261003_165355.log",
"local_xtr_passive":BASE/"thermia-logs.txt",
}
r={k:tv.analyze(str(v)) for k,v in files.items()}
def c(k,n): return r[k]["counts"].get(n,0)
assert c("eco5_20260926","bootstrap_complete")==2
assert c("eco5_20260928","bootstrap_complete")==4
assert c("atec_20261003","bootstrap_complete")==1
assert c("legacy_20260925_090209","bootstrap_partial")==1
assert c("eco5_20260926","approval_accepted")==2 and c("eco5_20260926","approval_challenges")==99
assert c("eco5_20260928","approval_accepted")==4 and c("eco5_20260928","approval_challenges")==64
assert c("atec_20261003","approval_accepted")==1 and c("atec_20261003","approval_challenges")==1
assert c("eco5_20260926","desired_pulls")==4 and c("eco5_20260926","desired_confirmed")==4
assert c("atec_20261003","desired_pulls")==1
assert c("legacy_20260925_090550","recovery_0870_windows")==1
assert c("eco5_20260926","085f_acked")==4 and c("eco5_20260926","085f_unacked")==193
assert c("eco5_20260928","085f_acked")==4 and c("eco5_20260928","085f_unacked")==118
assert c("atec_20261003","085f_acked")==2 and c("atec_20261003","085f_unacked")==0
assert c("eco5_20260926","0834_acked")==31 and c("eco5_20260926","0834_unacked")==1
assert c("atec_20261003","0834_acked")==13 and c("atec_20261003","0834_unacked")==0
assert len(r["eco5_20260926"]["approval_overlap_config"])==1
assert len(r["eco5_20260928"]["approval_overlap_config"])==2
assert len(r["atec_20261003"]["atec_steady_085f"])==1
assert len([x for x in r["legacy_20260925_071517"]["standalone_config"] if x["page"]=="03E8"])==2
assert c("local_xtr_passive","mailbox_answered")==0
assert c("local_xtr_passive","local_03e8_unacked")==70
assert c("local_xtr_passive","local_085f_unacked")==35
for k in [x for x in files if x!="local_xtr_passive"]:
    assert c(k,"0f_crc_bad")==0
print("PROTO54 GOLDEN TRACE REGRESSION: PASS")