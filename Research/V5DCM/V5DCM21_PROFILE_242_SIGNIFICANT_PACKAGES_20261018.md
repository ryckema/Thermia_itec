# V5DCM21-PACKAGES-02 — XTR 2.4.2 significant data-package census
Date: 2026-10-18

**Experiment overall:** **RUNNING / PARTIAL** — source-derived offline analysis + verified strict CI; **no new user-confirmed V5DCM21 live TX/handshake/session**. This report is not original-firmware execution and not native Connect OPERATION proof.

## Question, hypothesis and evidence
Question: Which W2/W3/W4 request groups are *actually referenced by the sensor/configuration semantic profile* selected for a local XTR M with `0867=242` (2.4.2), instead of indiscriminately requesting all 32+11 page groups?

**Original 2.1.105 code inspected** in user-provided `device_client.zip`:
- `cm/modbus_server15.py::_get_all_data_package_to_request` unions `_sensors_parser.significant_registers()` and `_configs_parser.significant_registers()` (NOT the operations parser, alarms parser or InfoMessageCollector in this specific method), filters non-integer/MQTT token references, maps each integer to request group with `_register_and_bit_for_address(..., request=True)`, then deduplicates the resulting (register,bit) pairs into a set.
- `data/parsers.py::DataParser.significant_registers` unions extractor dependencies; `data/extractor.py::ParamExtractor._tokenize` collects literals in read `formula`, all `conditions`, and expression-valued `min`, `max`, `default`. It does **not** collect `set_register_formulas` as required receive dependencies.
- This is an **initial requirement over all loaded sensor/configuration definitions**; merely having a feature condition that might later be false does not itself exclude its referenced registers during the construction of this request set.
- The three pending masks W2/W3/W4 and C0 -> C1 -> C2 receipt transition remain separate from native H/B/M/R axes and Connect runtime A4.

**Offline normalized original-firmware-derived dataset** used for profile contents, not claimed as a freshly re-extracted RAUC source: `ryckema/Thermia_Connect_Firmware/data/cm930_semantic_objects.csv`, exact rows `firmware=2.1.105; profile=2.3.0-2.4.3; category=sensor/configuration`. Firmware selector map `data/cm930_modbus_flags_map.csv` and **independent local-XTR physical page counts** `data/xtr_portable_profile_xtr_2_4_2.json`. Separate older `appfs_2018.zip` only contains `2.3.0-2.4.1` and cannot itself verify the 2.4.2 profile. The 2.1.105 RAUC was **not newly unpacked to revalidate every normalized JSON row in this step**; original source execution and exact full source-to-derived-index equivalence are therefore OPEN.

## OBSERVED SOURCE-ANALYSIS FACTS
The normalized 2.1.105 `2.3.0-2.4.3` profile contains:
- **99 sensor definitions** + **471 configuration definitions** = **570** checked source objects;
- **541 unique numeric register dependencies** when collecting literal tokens from formula, conditions, min/max/default (after deduplication); MQTT/other string topics excluded;
- all 541 numeric references mapped **unambiguously** to exactly one already-known W2/W3/W4 selector range and a known XTR local physical page start;
- **33 distinct candidate-required receipt groups**: 15 upper-settings (W2), 10 lower-settings (W3), 8 operation/runtime (W4).

**Selected starts (read-only description, NOT an instruction to set mailbox bits or transmit):**
- W2 upper settings 15: `0546 055A 057B 059C 05BD 05DE 05FF 0620 0641 0662 0683 06A4 06C5 06EA 06F4`.
- W3 lower settings 10: `03E8 03FC 0410 042E 0442 0456 046A 04A6 04BA 0532`.
- W4 operation/runtime 8: `07D0 07E4 07F8 080C 0820 0848 0864 0870`.

**Profile-specific absence from this *application-completeness* dependency list** (not a claim these frames are never transmitted):
- W2: `06F1` not selected;
- W3: `047E 0492 04D8 04F6 050A 051E` not selected;
- W4: `0834 085F 0884` not selected.

The firmware `request_read_all_registers()` excludes W4 group at `0864`, whereas this profile's significant-register set **includes** the `0864` group through dependencies such as the version register `0867`. Those methods have different selection objectives and must not be merged.

**Crucial distinction:** `modbus-flags.json` range lengths are *selector ownership spans*, NOT physical FC16 page word counts. The XTR profile JSON supplies independently observed physical geometry; e.g. `03E8/count14`, `0410/count22`, `0864/count4` despite larger selector spans. This is source-to-source offline consistency, not a new local bus read.

## FIX4 diagnostic coverage and current live significance
The user-confirmed **read-only v31 FIX4** has a 13-family `Native Settings Pages Seen` diagnostic, covering **13/33** of these candidate-required groups:
- 1 W2 group: `0546`;
- 6 W3 groups: `03E8 03FC 0410 042E 0442 0532`;
- 6 W4 groups: `07D0 080C 0820 0848 0864 0870`.

The other **20/33** groups are **not monitored** by this specific HA Y/N sensor; an `N` for another tracked group is not a claim about unseen groups. In the user's first FIX4 live snapshot at 151s only `03E8:Y`; the twelve other tracked groups N, with later user qualitative report “nog steeds op N” but no exact later uptime/mask. This is **READ-V31-UNKNOWN-01 RUNNING / PARTIAL**, not a DCM handshake or C2 proof.

Even **13/13 Y** could never establish all **33/33** application package requirements under this source-derived profile. Additionally C2 cannot be assumed from the XTR completed 32-page cold bootstrap, as eight runtime groups and independent application initialization also matter.

## One controlled source-only reproducibility change and actual validation
**No bus communication.** Added `Thermia_Connect_Firmware/tools/audit_v5dcm21_significant_packages.py`: read-only, uses literal source expression tokens (not write formulas), filters to 2.1.105 matching profile sensor/config only, joins to published selector range CSV, checks every mapping against independent XTR physical start/count reference, counts FIX4 covered/uncovered groups, and emits descriptive metadata only. It neither creates mailbox frames nor exposes the private 0x0F responder/security algorithm. Synthetic negative assertions ensure write-only dependency strings cannot create receive obligations and that bit-suffix and unsigned tokens are parsed as originating register numbers.

**Verified strict CI:** firmware commit `cfafd2cdfadb978d488d5999b07f806764e8741e`, GitHub Actions [39126103885](https://github.com/ryckema/Thermia_Connect_Firmware/actions/runs/39126103885) **SUCCESS** including the **10** new source-profile audit assertions and all previous mandatory strict C++17 24 Core + 46 RX + 22 delivery + 26 package ledger + 5 capture + 4 chronology + 30 firmware model + 35 lifecycle guard, embedded/portable parity and TX hard deny. Original earlier V5DCM21-PACKAGES-01 `PassivePackageLedger` remains a **generic nontransmitting ledger**; it has not yet been populated from an independently certified, exact-profile live runtime source.

## Evidence classification and next action
- **PROVEN / exact retrieved public normalized source files + executed host CI:** the computed **570 objects, 541 numeric dependencies, 33 selected groups (15/10/8), 13 FIX4 tracked, 20 not tracked**; 2.1.105 source-level extraction/union semantics verified in `device_client.zip`. This is **not local XTR evidence of those pages actually arriving**.
- **STRONGLY SUPPORTED / firmware-derived:** real 2.1.105 parameter publication requires the pending significant packages to be cleared after the relevant owned FC16 callback, distinct from 32-page bootstrap and Online/cloud.
- **HYPOTHESIS / awaiting direct matching binary re-extraction:** every row of the repository's normalized `2.3.0-2.4.3` index exactly matches the actual original 2.1.105 RAUC semantic JSON without derivation errors.
- **OPEN / UNKNOWN:** actual native XTR C1->C2 package arrival sequence, physical owner/response slot/epoch, protected FC23 native response delivery, correct profile conditions on this installation, app A4 OPERATION and Online, exact current flashed v31 image equality.
- **Status:** V5DCM21 **RUNNING / PARTIAL**, source/CI audit PASS. No newly executed hardware experiment, no CRC-active transmissions, no arbitrary register writes, no confidential responder or command-mailbox tooling.
- **Next:** compare normalized `2.3.0–2.4.3` rows against the actual original 2.1.105 profile JSON from the RAUC when available; then run source/capture-only 33-group receipt chronology and select the **smallest missing active native response class** using locally proven EXP325–329 ownership/ACK evidence for a separately scoped user-initiated live test under standing autonomous TX permission. Do not infer raw page emission from the 13-bit FIX4 mask alone.
