# V5DCM22-REPLAY-01 — byte-for-byte offline capture replay, 2026-10-18

**Experiment status: COMPLETE / POSITIVE (offline raw-frame verifier, no live execution).**
**Overall V5DCM22: RUNNING / PARTIAL** (new actual-C++ harness committed; exact GitHub CI build not yet independently verified).
No physical TX, no ESPHome compile or flash, no change to existing v31 FIX4 RX-only deployment.

## Hypothesis and previous evidence
Hypothesis: the historical `thermia_capture_20261003_165355.log` contains 33 source-significant FC16 *starts* but cannot complete the **local XTR 2.4.2 strict 33-group ledger** because `03E8` and `0410` have reference capture counts distinct from the locally established XTR geometry. Any native `0x0F FC23` must also revoke passive profile evidence until independently reselected. Prior V5DCM22 33-group mapping, previous local XTR count captures and V5DCM21 RX-only ledger are retained as baseline.

## Controlled change
**Offline replay only** of existing line-by-line timestamped hex frames; no reconstructed or rewritten payload bytes, no recomputed CRC attached to source frames. A raw Python verifier reads each original byte stream, checks Modbus CRC16 over original bytes, strictly parses FC16 request bytecount and entire length, and matches against exactly the committed 33 start/count descriptors. All ordinary frames are retained for chronological integrity; `0x0F FC23` causes provenance revocation. After a revocation there is **no automatic external profile requalification**. Separately maintain shape-only maximum, which is *not* a C2 claim.

**Source**: original user historical `thermia_capture_20261003_165355.log` 14918065297264473e2357822a8694d184e7821b8c2a3b1cb316039678a708a1 (SHA-256). This is historical/ref-style material, NOT independently certified current local XTR data. Exact raw capture bytes are not published to GitHub.

## Executed offline verifier — OBSERVED FACTS
- **2,687** timestamped frames, 2,687 CRC-valid, **0 invalid CRC**, 0 malformed lines.
- **162** CRC- and exact-length-valid slave `0x0F FC16` requests.
- **33/33** significant start addresses present; **31/33** exact local XTR start+count shapes present.
- **126** matched-shape frame occurrences. **2** mismatched selected-start frames: `0x03E8/count13` (XTR 14) and `0x0410/count21` (XTR 22); each occurred once.
- **2** CRC-valid slave `0x0F FC23` frames at capture timestamps **27.400** and **27.429**, both **before the first `0x0F FC16` at 29.262**. In the current RX-only join, these revoke provenance.
- **31** distinct matching shapes is the *shape-only* potential after hypothetical independent reselection. Current fail-closed ledger, when initially qualified and then passively fed the entire timeline **without a new independent profile select**, stays **unqualified** and yields **0 qualified receipts** after the FC23 boundaries.
- No original frame proves controller-origin / physical owner / native semantic application C2 / Connect OPERATION / Online.
- Offline verifier made **0 physical transmissions**.
- Separate negative checks executed: modifying the recorded CRC makes the frame invalid; the count13/count21 shapes remain rejected despite their valid CRC.

## Added reproducibility to Thermia_Connect_Firmware
- `tools/v5dcm22_replay_capture.py`: pure byte-preserving offline verifier reading local input, never publishing payloads or response logic.
- `portable/test_xtr_v5dcm22_byte_replay.cpp`: source-level C++ executable that passes each intact received frame into the **actual** `PassivePackageIntegration::observe_adapter_event`, with full life-cycle revocation.
- `.github/workflows/v5dcm21-readiness.yml`: mandatory strict C++17 compile and Python/C++ synthetic safe replay checks; **no original capture committed**, so CI tests safe synthetic fixtures. This is distinct from local Python execution against original bytes.
- **Current status of newly added C++ harness:** committed but **not yet observed compiling/running against original capture**. GitHub CI result is not independently verified here. Do not claim end-to-end C++ replay PASS.

Offline reproduction:
```bash
python tools/v5dcm22_replay_capture.py /path/to/thermia_capture_20261003_165355.log
# After separately compiling against exact repository HEAD:
# /tmp/v5dcm22_capture_replay /path/to/thermia_capture_20261003_165355.log
```

## Conclusion
**COMPLETE / POSITIVE** for the controlled raw-frame replay and its intended **fail-closed/incomplete** discriminator. Exact local-XTR geometry cannot be relaxed to reference traffic. **C2/Online and physical XTR reception remain OPEN / UNKNOWN**.

## Abort/recovery/evidence
Abort if unknown ACK, TX, physical bus interaction, private `0x0F` response/security publication, destructive file replacement, or unauthorized automatic requalification. None occurred. No deployment changed; no recovery necessary. Next: verify exact-HEAD C++ CI; when possible run C++ harness on original private capture, cross-check counters with Python, and only then consider RX-only on-device provenance observation.
