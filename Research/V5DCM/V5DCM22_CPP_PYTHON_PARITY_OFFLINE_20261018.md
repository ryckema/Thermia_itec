# UPDATE 2026-10-18 — GitHub Actions actual portable build VERIFIED SUCCESS

GitHub Actions [run 39130592175](https://github.com/ryckema/Thermia_Connect_Firmware/actions/runs/39130592175), commit `9c14bb3976985051d6a053664c828f0e59cb1525`, completed **SUCCESS**. The exact-HEAD job steps individually succeeded for:
- `Compile V5DCM22 passive package join with exact Core`
- `Run V5DCM22 source and epoch safety checks`
- `Compile exact-HEAD byte-preserving passive capture replay`
- `Replay safe synthetic fixtures through Python verifier and C++ actual ledger`
- All pre-existing portable/Core/ESPHome RX-adapter regressions, source audits, embedded Core parity and hard-denied TX checks.

This **resolves the previous uncertainty about actual portable C++ compilation and safe synthetic CI execution**. It does **NOT** mean the exact-HEAD C++ harness has replayed the private original `thermia_capture_20261003_165355.log` on GitHub. The original capture was replayed locally with two independent host implementations (Python and standalone C++), with exact 16/16 counter agreement plus both geometry lists, as detailed below. No physical TX/flash was performed.

**V5DCM22 offline source + CI integration subchecks: COMPLETE / POSITIVE; overall project V5DCM22 RUNNING / PARTIAL until native on-device evidence.**

---

# V5DCM22-REPLAY-02 — independent C++17 vs Python byte-exact parity

Date: 2026-10-18
**Status: COMPLETE / POSITIVE — scoped offline host replay only.**
**V5DCM22 overall: RUNNING / PARTIAL.**
No physical TX, flash, ESPHome compile or current XTR run.

## Controlled question and known-good baseline
Question: Does an **independently compiled C++17** byte-level replay of the genuine historical `thermia_capture_20261003_165355.log` reproduce the previously executed Python verifier's Modbus CRC, FC16 geometry and fail-closed FC23-session continuity outcomes?

Baseline: verified original 2.1.105 profile's 33 W2/W3/W4 package group descriptors, local XTR physical start/count geometry and previous V5DCM22-REPLAY-01 raw source evidence. Previous REPLAY-01 was Python executed and GitHub *actual* portable C++ replay **not** executed.

**Controlled change:** an offline standalone C++ comparator was generated from the already verified 33 public page descriptors, compiled locally at `/mnt/data/V5DCM22_BYTE_REPLAY_STANDALONE.cpp` with `g++ -std=c++17 -O0 -Wall -Wextra -Werror -pedantic` and run over the original intact capture bytes. Python `/mnt/data/v5dcm22_replay_capture.py` was freshly rerun over the same file. C++ deliberately does NOT contain OEM security, native response, TX, UART or mailbox command functions. It models profile revocation on the two FC23 frames and accepts no automatic requalification. Host binary file and results remain conversation artifacts; raw capture bytes have NOT been uploaded to GitHub.

## Observed result (independent host execution)
Input original capture SHA256: `14918065297264473e2357822a8694d184e7821b8c2a3b1cb316039678a708a1`.

Strict C++17 compiler initially flagged formatting-only `-Wmisleading-indentation`; source was corrected **before** successful compilation. No source-behavior change. Final strict compile **PASS**.

| Observation | C++ | Python |
|---|---:|---:|
| Input frames | 2687 | 2687 |
| CRC valid | 2687 | 2687 |
| Invalid CRC | 0 | 0 |
| `0x0F FC16` exact length | 162 | 162 |
| `0x0F FC23` | 2 | 2 |
| All significant starts | 33 | 33 |
| Distinct strict XTR shapes | 31 | 31 |
| Strict shape frame occurrences | 126 | 126 |
| Wrong-count selected frames | 2 | 2 |
| Session invalidations | 2 | 2 |
| Unselected FC16 starts | 10 | 10 |
| Maximum unqualified distinct shapes | 31 | 31 |
| Profile qualified at end | false | false |
| Qualified receipts at end | 0 | 0 |
| Highest qualified receipts | 0 | 0 |
| Physical transmissions | 0 | 0 |

**16/16 scalar comparisons PASS** and both missing/wrong-count lists also match:
- Missing exact local XTR `0x03E8/count14`, `0x0410/count22`.
- Reference traffic has `0x03E8/count13`, `0x0410/count21` (one each).

**Negative fixture:** two-line local file with one original genuine `0x03FC` frame and one deliberately CRC-mutated copy. Both C++ and Python produce frames=2, crc_valid=1, invalid_crc=1, one session invalidation, profile qualified=false. **PASS**. Fixture is synthetic mutation, not a historical capture frame.

## Crucial verification boundary
This C++ checker is a **standalone independent host comparator**, *not* compiled against the exact GitHub `portable/xtr_core.cpp`, `PassivePackageIntegration`, or original `portable/test_xtr_v5dcm22_byte_replay.cpp`. It reproduces the expected byte-level and fail-closed observational logic; it does NOT constitute executed native class integration regression.

Why: exact GitHub repository sources were inspected via connected GitHub tools but cannot be cloned into the execution container (container DNS/network restriction); associated GitHub Actions C++ execution status could not be confirmed by the available Actions/status connector results. Existing GitHub C++ replay harness and workflow remain committed and need independently verified strict CI or compilation against a local exact-HEAD source archive.

C2/Online/controller acceptance and physical slave ownership remain **OPEN / UNKNOWN**. Reference ATEC-style capture geometry differs from locally proven XTR; a matching page start is not equivalent to local XTR package delivery. Physical TX remained zero.

## Abort/recovery
Abort on accidental physical bus TX, writing native security/handshake implementation, a false ready claim, or changing production YAML. None occurred. No recovery necessary: user-flashed v31 FIX4 read-only baseline unchanged.

## Next
Verify the exact-head GitHub C++ replay against this same original log when the full portable sources are available or CI logs become accessible; compare C++ counts with the independently observed `2687/162/33/31/2` baseline. Then determine whether a scoped **RX-only** XTR log offers new evidence, without presupposing all 33 groups appear naturally or asking for compiler output.
