# THERMIA PROJECT STATE

Last updated: 2026-09-27

## Authoritative experiment state


## Authoritative current state — 2026-09-27 after EXP229

- Last completed experiment: **EXP229 — COMPLETE / OFFLINE POSITIVE STRUCTURE: `055A..06E5` is a stable 396-word structured family with strong 12-word periodicity; the XTR-only differences sit in transition records rather than the repeated templates**.
- Current experiment: **none running**. Heat-pump restarts remain paused. EXP229 used only existing captures; no ESP TX, no Thermia setting change and no controller restart.
- Hypothesis: the `055A..06C5` count-33 sequence is a coherent table/descriptor family, and the EXP228 XTR-only values near `061C/061E` and `067E/067F` may explain the model-dependent page-selection pattern.
- Genuine ATEC/DCM full-sync (`090209`, `090550`) contains exactly 12 consecutive `count33` pages:
  `055A, 057B, 059C, 05BD, 05DE, 05FF, 0620, 0641, 0662, 0683, 06A4, 06C5`.
  Every start is exactly `+0x21` words from the previous one; together they cover the contiguous range `055A..06E5` with no gaps or overlap.
- All 396 words in that family are identical between the two independent ATEC full-sync captures. This is strong evidence that the family is static/configuration/descriptor-like on that reference system rather than ordinary fast-changing telemetry; immutability across other configurations is not proven.
- The 396-word image has a strong 12-word periodicity:
  - `315/384` word comparisons (`82.0%`) match at lag 12;
  - when aligned from `055A`, the image can be represented as 33 candidate logical records of 12 words;
  - exact repeated 12-word templates occur in runs of 7 records (`records 9..15`), 7 records (`17..23`), 3 records (`29..31`) and 2 records (`6..7`).
- The local XTR `05FF/count33` page was observed 31 times with one identical payload (EXP141+EXP222). It matches ATEC in 31/33 words; the only differences are:
  - `061C`: XTR `0003`, ATEC `0000`;
  - `061E`: XTR `0001`, ATEC `0000`.
  In the 12-word model these lie in **record 16**, immediately after the seven-record repeated template at records `9..15`.
- The local XTR `0662/count33` page was observed 268 times with one identical payload. It also matches ATEC in 31/33 words; the only differences are:
  - `067E`: XTR `0003`, ATEC `0000`;
  - `067F`: XTR `0001`, ATEC `0000`.
  These lie in **record 24**, immediately after the seven-record repeated template at records `17..23`.
- Therefore the four strongest EXP228 discriminators in this family are not random page-tail values: they occur specifically in **transition records between highly repetitive table regions**. This materially strengthens a table-metadata/model-configuration interpretation.
- Numeric page-jump correlation:
  - local sync jumps `05FF -> 0662`, which is exactly `3 * 0x21` words, while XTR `061C=3`;
  - `0662 + 3 * 0x21 = 06C5`, and XTR also has `067E=3`.
  This is **hypothesis-generating only**. The second correlation does not behave as a simple next-page pointer because the local XTR became quiescent after ACKing `0662` and did not emit `06C5`.
- Additional negative discriminator: the ATEC 396-word family contains **no `0003` values at all**. Thus the two XTR `0003` fields are especially platform-specific in the compared corpus. `0001` is common in ATEC and is less distinctive by itself.
- An alternative semantic interpretation remains open: repeated constants such as `001F=31`, `000C=12`, `003B=59`, and `0017=23` are compatible with calendar/range/constraint metadata. Therefore EXP229 does **not** label the table as an Online capability table or scheduler jump table.
- Strong conclusion: this family is best treated as **structured static/descriptor data with model-specific transition-record fields**, not as a set of ordinary runtime registers.
- No write target is justified. Do not copy ATEC zeros or other reference values into `061C`, `061E`, `067E`, or `067F`.
- Preferred next experiment: **EXP230 — OFFLINE 12-word descriptor semantics**, testing competing explanations (calendar/range descriptors vs model/capability/page-selection metadata) using the public Online register map, recovered firmware semantics and all available cross-model captures.



## Authoritative current state — 2026-09-27 after EXP228

- Last completed experiment: **EXP228 — COMPLETE / OFFLINE POSITIVE FIELD-LEVEL DISCRIMINATOR MAP**.
- Current experiment: **none running**. Heat-pump restarts remain paused. No bus TX or setting change was performed for EXP228.
- Hypothesis: persistent word-level differences inside the homologous `0x0F` pages shared by XTR and genuine ATEC/DCM systems may expose model/platform/capability fields, while transient operating-state words can be filtered out offline.
- Sources: local XTR raw EXP221, EXP222 and EXP141 page payloads; the already-proven local Operation-Mode correlation on `0546/count20`; genuine ATEC/DCM boot/rejoin captures `090209` and `090550`; EXP227 page-homology result.
- High-confidence persistent cross-system discriminator candidates now include:
  - `0x0546`: XTR `0001` vs ATEC `0002`;
  - `0x0547`: XTR `0001` vs ATEC `0000`;
  - `0x054A`: XTR `0002` vs ATEC `0000`;
  - `0x054F`: XTR `0003` vs ATEC `0000`;
  - `0x04BA`: XTR `0014` vs ATEC `0013`;
  - `0x04C0`: XTR `0028` vs ATEC `001E`;
  - `0x061C`: XTR `0003` vs ATEC `0000`;
  - `0x061E`: XTR `0001` vs ATEC `0000`;
  - `0x067E`: XTR `0003` vs ATEC `0000`;
  - `0x067F`: XTR `0001` vs ATEC `0000`.
- Replication strength:
  - local `0546/count20`: 55 identical EXP221 page images, plus prior A/B/A evidence that only known Operation Mode register `0553` changes across `AUTO -> COMPRESSOR -> AUTO`; genuine `090209` and `090550` carry the same ATEC values;
  - local `04BA/count22`: 5 identical images across EXP221/222; genuine `090209` and `090550` are identical and differ only at `04BA` and `04C0`;
  - local `05FF/count33`: 30 identical EXP141 images plus the identical EXP222 image; genuine `090209` and `090550` are identical; only `061C` and `061E` differ;
  - local `0662/count33`: 267 identical EXP141 images plus the identical EXP222 image; genuine `090209` and `090550` are identical; only `067E` and `067F` differ;
  - `085F/count5` is an explicit negative discriminator: all five words are zero on both platforms in all compared frames.
- Important exclusions:
  - `0x0553` is **not** promoted as a platform/capability discriminator because local experiments already prove it is Operation Mode (`1=AUTO`, `2=COMPRESSOR`); the ATEC value `4` can therefore reflect runtime mode rather than architecture;
  - `04A6/count13` is **not** a fixed capability candidate: the local XTR payload itself changes between EXP221 and EXP222 (`04A6/04A7` and `04B0` vary), despite a stable but very different ATEC image.
- Structural discriminator candidates from EXP227 remain: XTR uses `03E8/count14` versus ATEC `/13`, and XTR `0410/count22` versus ATEC `/21`. These +1 extensions are model/schema candidates, not scheduler-enable bits.
- Strong conclusion: EXP228 identifies a **small persistent discriminator set**, but does **not** identify a proven Online scheduler-enable flag. The fields above may encode model, installed hardware, capability, configuration or table metadata; causality must not be inferred from the cross-system difference alone.
- New high-value pattern for offline follow-up: XTR sends `05FF/33` and then `0662/33`, while genuine ATEC full-sync also includes the intermediate `0620/33` and `0641/33` pages. The XTR-specific tail values at `061C/061E` and `067E/067F` sit at boundaries of this 33-word family. This is a **hypothesis-generating structural correlation only**, not proof that these fields control page selection.
- Preferred next experiment: **EXP229 — OFFLINE 33-word family/table-structure analysis (`055A..06C5`)**, testing whether the XTR discriminator words and skipped pages form a coherent model/capability table. No active responder/write is justified.

## Authoritative current state — 2026-09-27 after EXP227

- Last completed experiment: **EXP227 — COMPLETE / OFFLINE POSITIVE ARCHITECTURE HOMOLOGY: XTR and genuine ATEC/DCM share a homologous native `0x0F` page/register family, while the extended runtime service scheduler/topology is different and remains absent locally**.
- Current experiment: **none running**. Heat-pump restarts remain paused. Next preferred work is another offline experiment, focused on cross-system page/value discriminators rather than active scheduler probing.
- EXP227 was fully offline: no heat-pump restart, no ESP TX, no setting change.
- Sources compared: four genuine ATEC/DCM captures (`210001`, `071517`, `090209`, `090550`), local XTR raw EXP221/222 evidence, and the locally proven ACK-walk sequence from EXP137–142.
- The local XTR proven sync path is:
  `03E8/14 -> 0410/22 -> 042E/15 -> 04A6/13 -> 04BA/22 -> 05FF/33 -> 0662/33`.
- Every one of those seven XTR stage start addresses has a counterpart in the genuine ATEC/DCM full-sync sequence and appears in the same relative order:
  - `03E8`: XTR count14 vs ATEC count13;
  - `0410`: XTR count22 vs ATEC count21;
  - `042E/15`, `04A6/13`, `04BA/22`, `05FF/33`, `0662/33`: exact start/count matches.
- Two additional recurrent local XTR pages also align exactly with genuine ATEC/DCM pages: `0546/20` and `085F/5`.
- Selected exact shared-page payload comparisons strongly support homologous layouts rather than coincidental addresses:
  - `04BA/22`: 20/22 words equal in compared XTR vs ATEC frames;
  - `05FF/33`: 31/33 equal;
  - `0662/33`: 31/33 equal;
  - `085F/5`: 5/5 equal;
  - `0546/20`: 15/20 equal in the compared states.
  `04A6/13` is structurally shared but its values differ strongly between the compared states/models.
- Therefore EXP175's topology result is refined, not reversed: **the outer bus/service topology differs, but the inner/native `0x0F` application/register serializer is substantially shared across XTR and ATEC/DHP-AQ-family systems**.
- Genuine ATEC/DCM full synchronization contains many intermediate pages that the local XTR ACK-walk skips. Current hypothesis: the common serializer emits a model/firmware/capability-dependent subset on XTR. This is not yet proven as the cause.
- The genuine extended Online/DCM runtime service task remains absent locally. Reference systems combine:
  - A5 service traffic;
  - controller `0x0F FC03 0708/count6` mailbox polling;
  - cyclic `0x0F FC16` runtime uploads in the `07D0..0884` family.
  Local indexed/raw evidence continues to show none of that subsystem.
- Genuine DCM rejoin capture `090550` strengthens the separation of scheduler activation from endpoint readiness: A5 and `0708` scheduling are active from the start, while the `0x0F` endpoint remains silent until ~66.86 s; 16 `0708` polls are unanswered before the first DCM mailbox response.
- `0x06` is further demoted as an Online/DCM endpoint hypothesis for these reference systems: across the four genuine captures there are 69 exact `0x06 FC17 AFC8/12 -> AFDC/5` controller polls and **zero** slave-0x06 responses, despite working Online/DCM traffic on `0x0F`/A5.
- The ATEC slave-0x04 path and local XTR slave-0x1E path are not wire-level address substitutes:
  - reference 0x04 uses recurrent FC17 `ABE0/12 -> ABF4/4`;
  - local 0x1E uses FC16 `0000/9`, `0014/3` plus FC04 `0000/22`, `001E/6`.
  Functional relationship may exist at a higher platform level, but wire protocol is different.
- EXP226 also prevents a false equivalence: local `071C/0730` FC17 is RTC/calendar-bearing traffic, whereas reference `0708/count6` is a mailbox/session header. They must not be treated as the same transaction family solely because both sit near `0x07xx`.
- Strongest current architectural model:
  1. a largely shared native `0x0F` register/page serializer exists across platforms;
  2. page lengths/selection and outer device topology vary by model/controller generation;
  3. the Online/DCM command path depends on an additional controller-side extended service scheduler/binding state;
  4. the missing local problem is therefore no longer “find the `0x0F` register map”, but “identify what enables the extended scheduler/topology on XTR, if XTR supports it at all”.
- No active responder/write experiment is justified by EXP227 alone. Production functionality remains unchanged.

## Authoritative current state — 2026-09-27 after EXP226

- Last completed experiment: **EXP226 — COMPLETE / OFFLINE POSITIVE: `0x0F FC17 071C..0723` is predominantly a transformed controller calendar/clock image**.
- Current experiment: **none running**. Next preferred work is **EXP227 — OFFLINE XTR vs genuine ATEC/DCM architecture comparison**.
- EXP226 performed **no interaction with the heat pump**: no restart, no bus TX, no configuration change. It re-analysed 129 already-recorded exact `0x0F FC17 read 0730/count8 + write 071C/count8` requests: EXP221=47, EXP222=25, EXP225=32, plus 25 older 2026-09-22 frames from EXP71/EXP71B for out-of-sample date/time validation.
- The write words are now mapped structurally as:
  - `071C`: high byte = year-2000; low byte = hour (`1A0E` on 2026-09-22 14h, `1A16`/`1A17` on 2026-09-26 22h/23h).
  - `071D`: high byte `45`; low byte = `2 * second`.
  - `071E`: constant `F906` in all 129 analysed frames; exact meaning unknown.
  - `071F`: low byte `AC`; high byte = `floor(second/2)`.
  - `0720`: high byte `DC`; low byte = day-of-month (`16` hex = 22 on Sep 22; `1A` hex = 26 on Sep 26).
  - `0721`: high byte `C5`; low byte = `4 * minute`.
  - `0722`: constant `001E` in all 129 analysed frames; exact meaning unknown.
  - `0723`: high byte `8F`; low byte = `4 * second`.
- The previously discovered algebraic relations are therefore explained by redundant second encoding:
  - `0723 = (2 * 071D + 0x0500) mod 65536`;
  - `low(071F)=0xAC`;
  - `high(071F)=floor(low(071D)/4)`.
- Reconstructing `hour:minute:second` from `071C/0721/071D` tracks logger time with a stable controller-clock lead: about +200.98 s on 2026-09-22 and +206.3 s on 2026-09-26 (within-run scatter roughly sub-second). This independently validates the clock interpretation.
- Strong conclusion: the changing portion of `071C..0723` is **not a generic free-running session counter and not a direct heating-settings image**; its observed variation is explained by controller RTC/calendar data. The previous apparent `071C 1A16 -> 1A17` change is simply hour 22 -> 23, and the slow `0721` progression is minute encoding.
- The exact role of the fixed/magic bytes (`45`, `F906`, `AC`, `DC`, `C5`, `001E`, `8F`) is not fully proven. `0722=001E` numerically equals 30, the number of days in September, but this is only a hypothesis because all available raw validation captures are from September.
- `0730..0737` remains completely unknown. EXP226 provides **no basis to synthesize or guess a response**.
- Active project constraint: **do not restart/power-cycle the heat pump for now**. Prefer offline analysis and ordinary-runtime passive observation unless the user explicitly lifts this constraint.
- Production functionality remains unchanged.



## Authoritative current state — 2026-09-26 after EXP225

- Last completed experiment: **EXP225 — COMPLETE / PROCEDURAL-INCONCLUSIVE FOR HEAT-CURVE CORRELATION; POSITIVE cold-boot reproduction of the 071C/0730 FC17 stream**.
- Current experiment: **none running**. The next experiment should be a passive rerun with automatic/guarded phase handling before any new responder work.
- EXP225 reproduced the exact local XTR `0x0F FC17 read 0730/count8 + write 071C/count8` stream after a real controller power cycle. The stream resumed immediately after bus recovery and then continued at roughly 4.2 s cadence.
- The user-side Power ON marker was pressed late, after the FC17 stream had already restarted and after Heat Curve had already been changed from 36 to 37. That marker reset the experiment phase to 1. The `+1` phase marker was never accepted/recorded and the later restore marker was refused because the firmware still considered the experiment in phase 1.
- Therefore the final summary `baseline=32 plus=0 restored=0` is a **procedural invalidation**, not evidence that Heat Curve has no effect on `071C..0723`.
- The actual bus ground truth still shows Heat Curve `36 -> 37 -> 36` while FC17 traffic was active. Across those changes there is no obvious discrete reversible jump in the 071C image; instead the dynamic words continue the same deterministic counter/time progression already identified in EXP223. This is supportive evidence for a timer/session/challenge structure, but not a valid negative semantic correlation because phase control was invalid.
- All 32 captured FC17 frames satisfy the previously identified `0723` and `071F` deterministic relations. The observed image keeps `071C=1A17`, `071E=F906`, `0720=DC1A`, `0722=001E` constant while `071D/071F/0721/0723` progress structurally.
- Parser integrity remained clean (`resync=0`, `drops=0`).
- No response values for `0730..0737` are inferred. No responder experiment is justified yet.
- Production functionality remains unchanged; EXP225 was RX-only.



## Authoritative current state — 2026-09-26 after EXP224

- Last completed experiment: **EXP224 — COMPLETE / INCONCLUSIVE FOR HEAT-CURVE CORRELATION BECAUSE TARGET FC17 WAS NOT EXERCISED; POSITIVE evidence that 071C/0730 FC17 is not continuously present in ordinary runtime**.
- Current experiment: **EXP225 — PREPARED / PASSIVE COLD-BOOT-GATED 071C/0730 CORRELATION; not yet run**.
- EXP224 was RX-only and parser-clean. The Heat Curve A/B/A was successfully exercised (`37 -> 36` visible in native `03E8/count14` ground truth), with 96 `03E8` frames, but the exact target `0x0F FC17 read 0730/count8 + write 071C/count8` appeared **zero** times in baseline, +1, and restored phases.
- EXP224 therefore does not answer whether Heat Curve changes the 071C write image. It does establish that this FC17 family is not an always-on steady-runtime exchange.
- EXP221 cold-boot evidence is now reinterpreted more narrowly: after Thermia/controller power-on, exact 071C/0730 FC17 requests began at ~2.9 s post-on and continued at ~4.2 s cadence through the end of the ~200 s observation. The stream is therefore strongly associated with controller cold-boot/recovery/service-session state.
- This makes the XTR FC17 family more interesting as a possible startup/session handshake with an absent slave-0x0F endpoint, and less likely to be an ordinary background heartbeat. Exact semantics remain unknown.
- EXP225 keeps the ESP independently powered, performs one controlled Thermia/controller cold boot to re-establish the proven FC17 stream, requires >=3 exact FC17 frames before permitting the Heat Curve phase marker, then performs the same single semantic variable `baseline -> +1 -> baseline`.
- EXP225 remains fully RX-only: no FC17 response, no ACK, no scan, no semantic write, no room-sensor emulation.
- Do not infer or guess `0730..0737` response values. A responder experiment remains blocked pending genuine-response evidence or a proven transformation.
- Production functionality remains unchanged. Experiment YAMLs/logs stay out of GitHub; canonical Research files may be maintained under the user's standing permission.



## Authoritative current state — 2026-09-26 after EXP223

- Last completed experiment: **EXP223 — COMPLETE / OFFLINE POSITIVE DISCRIMINATION: local XTR exposes a recurring slave-0x0F FC17 `read 0730/count8 + write 071C/count8` exchange that is absent from the three available ATEC/DCM captures**.
- Current experiment: **EXP224 — PREPARED / PASSIVE 071C/0730 HEAT-CURVE A/B/A CORRELATION; not yet run**.
- EXP222 remains **COMPLETE / IMPORTANT NEGATIVE**: six exact FC16 ACKs during local cold boot did not create A5/A4/0x04/0x05, `0x0F FC03`, `0708` or `07D0`.
- EXP223 reorients the local path away from assuming the ATEC scheduler is one-for-one transferable to XTR. In all three available genuine ATEC/DCM captures, slave `0x04` and A5 are active and slave `0x1E` is absent; the local XTR topology instead uses slave `0x1E` and lacks `0x04`/A5.
- The local XTR recurring frame has exact request shape:
  `0F 17 0730 0008 071C 0008 10 <16-byte write image> CRC`.
  It asks slave `0x0F` to return 8 registers at `0730..0737` while the controller writes 8 registers at `071C..0723`.
- EXP221 supplied 47 such requests over the observed post-boot interval; EXP222 supplied 25 more. No reply exists locally because no DCM/Online endpoint is attached.
- Across all 72 analysed local requests, several write-side relations are deterministic:
  - `071C=0x1A16`, `071E=0xF906`, `0720=0xDC1A`, `0722=0x001E` were constant in both runs;
  - `0723 == (2 * 071D + 0x0500) mod 65536` held for all 72 frames;
  - low byte of `071F` stayed `0xAC`, while its high byte matched `floor(low_byte(071D)/4)` for all 72 frames;
  - `0721` advanced only occasionally, approximately on a minute-scale cadence.
- These relations make `071C..0723` look more like a timed heartbeat/challenge/session structure than ordinary scalar heating settings, but exact semantics are unknown.
- EXP224 changes only Heat Curve manually `baseline -> +1 -> baseline` and remains fully RX-only. It logs every exact `071C/0730` request plus the proven `03E8` Heat Curve state page as semantic ground truth.
- EXP224 must not answer `0730` yet: the eight return registers are unknown and may carry command/session semantics.
- Production functionality remains unchanged. Do not publish experiment YAMLs/logs to GitHub without explicit same-query permission.



## Authoritative current state — 2026-09-26 (supersedes all older current-experiment bullets below)

- Last completed experiment: **EXP221 — COMPLETE / STRONG NEGATIVE for spontaneous Online/DCM scheduler activation on local no-DCM cold boot; POSITIVE for native post-boot 0x0F serializer/runtime activity**.
- Current experiment: **EXP222 — PREPARED / BOUNDED COLD-BOOT 0x0F FC16 ACK COMPLETION TEST; not yet run**.
- EXP220 is **COMPLETE / POSITIVE**: local `0x0546/count20` page was stable across `AUTO -> COMPRESSOR -> AUTO`; only `0x0553` followed `1 -> 2 -> 1`, while `0x0546`, `0x0547`, `0x054A`, `0x054F` and `0x0559` remained stable.
- EXP221 cold boot observed ~200 s after power-on with **A5=0, A4=0, slave04=0, slave05=0, 0x0F FC03=0, 0708=0**. Local native `0x0F` traffic (`04BA`, `04A6`, `085F`, FC17 `0730`) resumed without the genuine scheduler.
- Correction from EXP221: a lone `0x0F FC16 085F/count5` is **not** a scheduler/topology proof. Genuine runtime-exporter detection must not count `085F` alone.
- Re-analysis of the genuine DCM startup capture `thermia_capture_20260925_090209.log` shows a long ACKed controller->DCM FC16 initialization sequence ending with `06F4/count19` and `085F/count5`; the first observed `0x0F FC03 0708/count6` follows a few seconds later and the cyclic runtime exporter begins at `07D0/count19`.
- A temporary `A4/0x05` burst in `thermia_capture_20260925_090550.log` occurs **after** `0708` is already active, so that A4/0x05 burst is not the primary scheduler-start trigger.
- EXP222 tests the narrow causal hypothesis that **completion of the genuine FC16 initialization/full-sync via exact standard FC16 ACKs is sufficient to start the native FC03/0708 scheduler**.
- EXP222 only enables TX for CRC-valid slave `0x0F` FC16 request frames whose exact start/count pair is on a fixed allow-list derived from previously observed local/genuine pages. It sends only the standard FC16 echo ACK; no semantic desired values, no FC03 response, no room-sensor emulation.
- First `0x0F FC03` or `07D0/count19` is a positive discriminator and disables TX immediately. Unknown FC16 shapes, parser resync, or RX-buffer faults fail closed and disable TX.
- Production functionality remains unchanged outside the dedicated experimental YAML. Do not publish experiment YAMLs/logs to GitHub without explicit same-query permission.


## Authoritative current state — 2026-09-25 (supersedes older current-experiment bullets below)

- Last completed experiment: **EXP167 — COMPLETE / INCONCLUSIVE for the intended combined 0x06 + exercised 0x0F-ACK hypothesis; STRONG NEGATIVE for 0x06-driven service activation**.
- Current experiment: **none armed**. Do not repeat EXP167 or reboot the heat-pump/controller merely to obtain another copy of this result.
- Next research step: **offline transmitter/ownership and earliest-service analysis of the genuine DCM power-up capture `thermia_capture_20260925_090209.log` before defining EXP168**.
- Runtime/no-reboot remains the default experimental strategy. Genuine DCM service can become operational while the controller is already running, so a controller reboot is not intrinsically required.
- Production functionality remains unchanged.

### EXP164–167 consolidated finding

- EXP164 reproduced the no-DCM cold-boot baseline: C8 discovery, `0x06` polling, A80E `0 -> 8 -> 0x28`, AFDC `0x10`, and sustained unACKed `0x0F FC16` can all occur without A5, A4/0x05 or `0x0F FC03`.
- Genuine DCM runtime power-up (`090209`) differs sharply: the `0x0F` service is already ACK-capable within ~0.4 s and A5 becomes operational roughly 0.8 s later, while C8 continues in parallel.
- EXP165 proved that runtime `0x0F FC16` ACK service alone does not activate A5 or `0x0F FC03`. Its intended simultaneous 0x06 role was invalid because of a 27-byte/23-byte FC17 matcher bug.
- EXP166 corrected that matcher and transmitted 169 valid `0x06` responses in 180 s. `EXP 0.0` appeared immediately, proving runtime `0x06 -> EXP/version metadata`, but no A5, A4/0x05 or `0x0F FC03` appeared and no `0x0F FC16` occurred in that window.
- EXP167 extended the corrected runtime `0x06` responder to 600.009 s. It transmitted **559** valid 0x06 responses while the controller emitted **zero 0x0F frames of any kind**: `s0F=0`, `0F16req=0`, `0FtxACK=0`, `0F03req=0`, `A5=0`, `A4=0`, `s05=0`. Bus integrity remained clean: `resyncDelta=0`, `dropDelta=0`.
- Therefore sustained, valid `0x06` accessory/version presence does **not** induce native `0x0F` service or A5 scheduling during runtime.
- The exact intended EXP167 condition `active 0x06 + actually exercised controller-originated 0x0F FC16 ACK` still never occurred, so that narrow combination remains technically untested. However, waiting longer on `0x06` as the trigger is now low-value.
- The missing prerequisite is increasingly likely to be an earlier/parallel discovery, binding, electrical ownership or service-availability property of the genuine DCM topology rather than a simple `0x06` metadata response.

### Current protocol model

1. **0x06 accessory/version metadata path** — independently activatable; valid responses can expose `EXP / UITBR.KAART`, and `AFD1` maps to displayed version/10. This does not establish the Online/DCM session.
2. **0x0F bidirectional mailbox/service** — controller can emit FC16 writes without a DCM, but genuine DCM topology provides an operational/ACK-capable service and later FC03 reads. Physical ownership remains unresolved.
3. **A5 service** — appears only in genuine DCM topology so far; exact physical owner and activation mechanism remain unresolved.
4. **A4 <-> 0x05 sibling path** — genuine-topology alternate/discovery-like service; not a simple mandatory A5 precursor.
5. **C8 FC03 0x2328/count2** — generic native startup discovery, not DCM-specific.

### Do not repeat without new evidence

- isolated A5 responder;
- direct A5 read triplet after known 0x0F ACKs;
- 0x0F ACK-only activation;
- `0x06` presence-only activation, including longer dwell times;
- C8 response guessing;
- A80E/AFDC or `EXP 0.0` as DCM-recognition criteria.

## Permanent YAML generation invariants

These rules apply to every future experiment YAML and are not experiment variables:

- Preserve the known-good top-level production configuration unless an experiment explicitly requires changing it.
- Always preserve the `substitutions:` block used by the production YAML, including at minimum `device_name` and `friendly_name` when the file references `${device_name}` / `${friendly_name}`.
- Before delivering a new YAML, verify that every `${...}` substitution referenced in the file is defined.
- Treat a missing top-level production block (for example `substitutions:`, `esphome:`, Wi-Fi/API/OTA, UART, or known-good production entities) as a generation error, not as an experimental change.
- Validate YAML syntax and run a substitution-reference sanity check before delivery. When possible, compile with ESPHome; if no local ESPHome compile is run, state that explicitly.
- Preserve bus-health bookkeeping: after every CRC-valid frame, refresh `thermia_last_valid_frame_ms`, increment `thermia_valid_frame_count`, and publish `thermia_bus_healthy=true`; the watchdog may only publish `false` after the configured stale timeout.


- Last completed experiment: **EXP105**
- EXP93 status: **PASSIVE A80F=50 discriminator armed in two captures but never triggered; not a negative result and now superseded as next priority**
- Current experiment: **EXP106 — passive integration-sync window correlator — PREPARED, not yet run**
- Current control architecture target: **emulate Thermia/Danfoss Online/Connect/DCM03 on slave 0x06**
- Room-sensor emulation on slave 0x0A is **not pursued as the control architecture**

## System

- Heat pump: Thermia iTec XTR M / Total Compact, older non-Genesis controller
- Integration target: ESP32 / ESPHome / Home Assistant
- Bus: Modbus RTU-like, 9600 baud, 8E1, valid Modbus CRC
- Safety policy: read-only/passive by default; active responses only in exact known response slots with fail-closed guards

## Confirmed protocol findings

### 0x06 accessory/DCM slot

- Controller polls slave 0x06 with FC17.
- Normal unserved cadence is about 4.3 s.
- A syntactically valid response starts a fast alternating cadence of roughly 0.7 s SHORT and 1.4 s FAST-LONG.
- Accessory response contains 12 words corresponding to AFC8..AFD3.
- Controller writes five words AFDC..AFE0 in the FC17 request.

### Four-phase handshake

- AFCA / accessory response word2 is the REQ/data-valid level.
- REQ low: AFCA=0000.
- REQ asserted: AFCA=03E8.
- In correct phase, 03E8 causes controller 0x0F:0861 to rise 0 -> 16.
- Keeping 03E8 asserted keeps ACK high.
- Returning AFCA to 0000 while keeping the other payload stable causes 0861 to return 16 -> 0.
- This is a proven transport-level four-phase handshake.

### Historical A80E/AFDC cycle

Older passive captures repeatedly showed:

- A80E 0 -> 32
- AFDC 0 -> 32 shortly afterwards
- about 17 s later A80E 32 -> 0 and AFDC 32 -> 0
- recurrence around ~65 s in those captures

This is distinct from the 0861 transaction ACK.

## EXP90-92 conclusions

### EXP90

Persistent response w0=00FF for 90 s. 84 responses. No A80E/AFDC cycle. Negative.

### EXP91

Persistent historical envelope with REQ low:

00FF,0001,0000,0001,0...

for 90 s. 84 responses. No A80E/AFDC cycle, no settings change, no parser/RX error. Negative.

### EXP92

Hypothesis: a completed transport handshake might initialize hidden controller/accessory state required before the historical REQ-low envelope can cause the old A80E/AFDC cycle.

Sequence executed successfully:

1. stable LONG baseline
2. historical envelope preloaded with REQ low
3. AFCA 0000 -> 03E8 on SHORT
4. 0861 0 -> 16 after 401 ms
5. AFCA returned to 0000 with payload stable
6. 0861 16 -> 0 after 1031 ms
7. same historical REQ-low envelope maintained for 90 s

Result:

- handshake_complete=1
- total responses=90
- observation responses=84
- A80E peak/current=0000, changes=0
- AFDC peak/last=0000, changes=0, nonzero=0
- status peak=16
- settings_changed=0
- resync_delta=0
- drop_delta=0

**Strong conclusion:** one correctly completed four-phase 03E8 transaction is not sufficient to initialize the historical A80E/AFDC online-state cycle.

## Current architectural direction

The project target is now explicitly to emulate the official Thermia/Danfoss Online/Connect/DCM03 accessory through slave `0x06`. Room-sensor emulation on `0x0A` remains useful protocol evidence but is not the desired control path.

Firmware analysis of Danfoss Link CC recovered the host-side HE/DHP parameter protocol:

- request format: endpoint byte, GET/SET count nibbles, 16-bit parameter IDs, then SET values;
- heat-pump parameters include `0x030A OperationMode`, `0x4402 HeatCurve`, `0x440A HotWaterStart`, `0x4414 IntegrationMode`, and others;
- `0x4414 IntegrationMode` is GET-on-sync and SET-on-sync, then its one-shot SET flag is cleared;
- parameters are assigned to partial sync groups 0/1/2.

The Link CC firmware does not contain the final DCM03 -> Thermia RS485 serializer. The unresolved layer remains:

```text
HE ParameterID/value
    -> DCM03 translation/state machine
    -> AFC8..AFD3 / AFDC..AFE0
    -> Thermia controller
```

Official Danfoss documentation adds two relevant constraints:

- DHP-AQ Link integration requires heat-pump software 2.2 or newer, indicating controller-side firmware support for the integration path;
- Link firmware 4.2.1724 can keep re-offering Heat Curve for 30 minutes after initial HP communication if the HP rejects/forgets it, indicating an initial synchronization/desired-state model rather than a one-shot raw register write.

## EXP93 status

**Hypothesis:** historical `A80E/AFDC 0x0000 <-> 0x0020` cycling is gated by controller state and appears while `A80F=50`.

Result to date:

- EXP93 was correctly armed in two supplied captures;
- `A80F` remained at 10 in the observed periods;
- no `EXP93 TRIGGER` or `EXP93 SUMMARY` occurred;
- therefore EXP93 did not execute its 180 s observation window and is **not** a negative test of the hypothesis.

EXP93 is superseded as the immediate priority because the DCM03 startup/synchronization model now offers a more direct route toward the chosen `0x06` control architecture.

## EXP94 — Passive cold-boot + initial-sync timeline — COMPLETED

**Hypothesis:** after a true Thermia controller cold boot, the controller executes a reproducible accessory/integration startup or synchronization sequence that exposes preconditions/state required before semantic DCM03 commands are accepted.

**Observed facts:**

- >=5 s bus silence was correctly detected; first resumed CRC-valid frame started the 600 s capture.
- At +717 ms: `A80C..A812 = 0040,0000,0000,0005,0005,FFFF,0000`.
- At +1758 ms: `A80E 0000 -> 0008`.
- At +2846 ms: `A80E 0008 -> 0028`.
- First 0x06 poll at +1038 ms: `AFDC..AFE0 = 0000,0000,0000,0000,0019`.
- Second 0x06 poll at +5575 ms: `AFDC..AFE0 = 0010,0000,0000,0000,0014`; therefore `AFDC 0000 -> 0010`.
- `A80F/A810` start at `0005` after cold boot and return to `000A` at about +11.3 s.
- `0861` initialized to `0000` and had zero transitions during the 600 s capture.
- No settings changes occurred.
- 140 exact 0x06 polls were observed; cadence remained unserved/long at 4086..4537 ms.
- Final controller state remained `A80C..A812 = 0040,0000,0028,000A,000A,FFFF,0000`.
- Final 0x06 controller-write image remained `AFDC..AFE0 = 0010,0000,0000,0000,0014`.
- Summary: `frames=5185`, `ctrl_changes=3`, `rsp02_changes=1`, `0861_changes=0`, `settings_changes=0`, `resync_delta=1`, `drop_delta=0`.

**Strong conclusions:**

- The cold-boot controller/accessory sequence is short: the relevant state settles within roughly 11 s and then remains stable for at least 10 minutes when slave 0x06 is unanswered.
- Historical `A80E/AFDC 0x20 <-> 0` cycling is not ordinary cold-boot initialization.
- `0861` is separate from the longer-lived `A80E/AFDC` controller/accessory state machine.
- The stable unanswered post-boot state is `A80E=0x28`, `AFDC=0x10`, `A80F/A810=10`; exact semantics remain unknown.

**Hypothesis:** `AFDC=0x10` may represent an accessory-not-established / waiting state. This is not proven.

## EXP95 — Cold-boot zero-presence from first 0x06 poll — COMPLETED

**Hypothesis:** syntactic DCM presence from the first cold-boot `0x06` poll is sufficient to move the controller away from EXP94's stable application/waiting state.

**Observed facts:**

- full capture duration `120000 ms`;
- `1133` valid frames; `112` exact 0x06 polls; `112` transmitted responses; `0` TX refusals;
- 0x06 cadence accelerated to `638..1503 ms`;
- controller boot sequence remained `A80E 0->8->0x28`, `A80F/A810 5->10`;
- `AFDC` still became `0x10`;
- final application state remained `A80E=0x28`, `A80F=A810=10`, `AFDC=0x10`, `0861=0`;
- `0861_changes=0`; `settings_pushes=0`; `settings_changes=0`; `outdoor_state_changes=0`;
- `resync_delta=1`; `drop_delta=0`.

**Strong conclusions:**

- a syntactically valid `0x06` responder from the first cold-boot poll is enough to enter the fast accessory polling cadence;
- syntactic presence alone does **not** advance the higher DCM/application session state;
- `AFDC=0x10` cannot simply mean “no 0x06 slave/accessory present”;
- transport presence and DCM application/session establishment are distinct layers.

**Negative result:** zero-presence from poll #1 does not change the EXP94 cold-boot application state.

## EXP96 — Cold-boot historical envelope + canonical REQ/ACK handshake — COMPLETED

**Hypothesis:** the historical DCM envelope may only have semantic/session effect when delivered after a true cold boot in the stable EXP95 controller context.

**Observed facts:**

- true cold boot reproduced the EXP94/95 startup state;
- zero-presence established fast `0x06` polling;
- exactly one historical-envelope transaction completed;
- `0861 0->16` occurred 367 ms after REQ assertion;
- `0861 16->0` occurred 1196 ms after REQ deassertion;
- summary: `06polls=112`, `tx=112`, `refused=0`, `handshake=1`;
- `ctrl_changes=3`, `rsp02_changes=0`, `settings_pushes=0`, `settings_changes=0`, `outdoor_state_changes=0`;
- final higher-layer state remained the same as EXP95.

**Strong conclusion:** cold-boot context does not make the historical `00FF,0001,REQ,0001` envelope semantically sufficient. It remains a valid transport envelope only; the semantic DCM03 serializer/init payload is still missing.

**Important natural observation before EXP96 ARM:** while the ESP was passive, `A80E` changed `0x28 -> 0x20 -> 0x00`, followed shortly by `AFDC 0x10 -> 0x00`. This was not caused by EXP96. It weakens any simple interpretation of A80E/AFDC as a dedicated DCM session indicator and suggests broader controller-state propagation.

## EXP97 — Passive natural A80E/AFDC edge correlator — COMPLETED

**Hypothesis:** the spontaneous `A80E 0x28->0x20->0x00` / `AFDC 0x10->0x00` sequence correlates with ordinary controller/outdoor-unit state and is not DCM03 session establishment.

**Design:**

- 100% passive/read-only for 600 s;
- no cold boot required;
- no response to slave `0x06`;
- no UART TX / DE enable;
- trigger/event log on every natural `A80E` or `AFDC` transition;
- each event logs the latest `A80C..A812`, `A7F8..A806`, `AFDC..AFE0`, `0861`, `0x1E 0000..0008`, and outdoor-state context;
- controls remain under Home Assistant Configuration.

**Observed:** during the passive run the exact natural sequence recurred:
- `A80E 0x28 -> 0x20` at +71.278 s;
- `A80E 0x20 -> 0x00` 1.062 s later;
- `AFDC 0x10 -> 0x00` 2.655 s after the second A80E edge.

At all three events, `0861=0`, outdoor state remained `0x10`, and the captured `CMD1E` and paired `RSP02` blocks were unchanged.

**Strong conclusion:** A80E/AFDC transitions can occur naturally with no ESP TX and no observed DCM transaction. They must not be used as a primary DCM-session-success criterion. The monitored outdoor/controller blocks did not explain the transition, so exact semantics remain unknown.

**Negative result:** no direct correlation was found with the monitored `0x1E`/outdoor state, `0861`, `CMD1E`, or paired `RSP02`.

## EXP98 — AFC8 single-word A/B/A influence test — COMPLETED NEGATIVE

**Hypothesis:** `AFC8` participates in the accessory application layer and the historical value `0x00FF`, isolated from all other payload fields, may produce a measurable controller effect even with `AFCA=0`.

**Design:** 90 s active but non-setting test: 0–20 s zero-presence baseline, 20–50 s `AFC8=00FF` only, 50–90 s zero-presence recovery. No `03E8`, HE/DHP payload, setting target, or 0x0A emulation. Observe full controller/settings/outdoor changes and cadence.


## EXP99 — historical-field matrix, REQ low — PREPARED

Hypothesis: the non-REQ words from the historical DCM envelope may have standalone or combinatorial application-layer meaning.

Design: 80 s, ten 8 s phases. Only AFC8/AFC9/AFCB are varied using historically observed values (AFC8=00FF, AFC9=0001, AFCB=0001). AFCA remains 0000 throughout, so no REQ/ACK transaction is intentionally started. Exact known 0x06 FC23 response slot only; no setting target and no 0x0A emulation.

EXP98 result carried forward: AFC8=00FF alone produced no detectable semantic effect; controller state, AFDC..AFE0, 0861, settings, CMD1E, outdoor state and cadence remained unchanged across A/B/A phases.


## EXP99 completed result

**Hypothesis:** historically observed non-REQ fields (`AFC8=00FF`, `AFC9=0001`, `AFCB=0001`) may have standalone or combinatorial application-layer meaning while `AFCA=0000`.

**Observed:** all ten 8 s phases completed cleanly. The run delivered 75/75 guarded responses with no refusals. All single, pairwise, and full historical non-REQ combinations produced no change in controller state, paired RSP02, AFDC..AFE0, `0861`, settings, CMD1E, or outdoor state. Poll cadence remained the normal fast-presence pattern (`707..1450 ms`). Parser resync and RX-drop deltas were zero.

**Strong conclusion:** `AFC8=00FF`, `AFC9=0001`, and `AFCB=0001` are not standalone semantic triggers, individually or in the tested combinations, when `AFCA` remains low. The only historical field with proven behavioural effect remains `AFCA=03E8` as transaction REQ.

## EXP100 — prepared

**Hypothesis:** the historical non-REQ fields may acquire meaning only when carried inside a valid four-phase `AFCA=03E8` transaction.

Six payload combinations are tested sequentially in one run. Each is preloaded with REQ low, asserted with `AFCA=03E8`, held until `0861=0010`, deasserted with payload stable, held until `0861=0000`, then followed by 3 s zero-presence observation. No HE/DHP parameter ID or setting target is used.

## EXP100 — Multi-transaction historical-field matrix — COMPLETED NEGATIVE

**Hypothesis:** the historical non-REQ fields (`AFC8=00FF`, `AFC9=0001`, `AFCB=0001`) may acquire meaning only when transported inside a valid canonical `AFCA=03E8` REQ/ACK transaction.

**Observed:** all six planned transactions completed. Each produced the canonical `0861` ACK-high and ACK-low cycle; summary: `complete=1`, `hard_stop=0`, `ack_hi=6`, `ack_lo=6`, `t1..t6=1`, `0861_changes=12`. No controller, RSP02, AFDC..AFE0, settings, CMD1E or outdoor-state changes were observed; no parser resyncs or RX drops occurred.

**Strong conclusion:** none of the tested historical non-REQ field combinations becomes semantically effective merely by being carried inside a valid REQ/ACK transaction. The four-field historical pattern is therefore insufficient as a DCM application command. `AFCA=03E8` remains a transport transaction strobe; the missing semantic layer lies elsewhere in `AFC8..AFD3` and/or requires a larger/multi-message session structure.

**Current direction:** stop iterating AFC8/AFC9/AFCB combinations. Next work should target the remaining response-bank structure / multi-message initialization rather than further permutations of the historical four-word envelope.


## EXP100 — Multi-transaction historical-field matrix with canonical REQ/ACK — COMPLETED

**Hypothesis:** AFC8/AFC9/AFCB may gain application-layer meaning only when carried inside a valid AFCA=03E8 four-phase transaction.

**Observed facts:**

- all six planned transactions completed;
- `ack_hi=6`, `ack_lo=6`, `0861_changes=12`;
- every transaction produced the normal controller ACK-high and ACK-low sequence;
- `ctrl_changes=0`, `rsp02_changes=0`, `06_changes=0`;
- `settings_pushes=0`, `settings_changes=0`;
- `cmd1e_changes=0`, `outdoor_changes=0`;
- `resync_delta=0`, `drop_delta=0`;
- no hard stop and no TX refusal.

**Strong conclusion:** the historical values in AFC8/AFC9/AFCB are not semantically sufficient even when presented inside a fully valid transport transaction. The first-four-word historical-envelope branch is exhausted as a standalone application command hypothesis.

**Negative result:** six valid transport transactions produced zero application-layer effect.

## EXP101 — AFCC..AFD3 one-word influence matrix — PREPARED

**Hypothesis:** one or more of the still-unmapped response words AFCC..AFD3 participates in the DCM03 application layer.

**Only experimental variable:** eight canonical transactions; exactly one tail word per transaction is set to `0x0001`: AFCC, AFCD, AFCE, AFCF, AFD0, AFD1, AFD2, AFD3. All other application words are zero except AFCA during the already-proven REQ phase.

**Safety:** semantics of AFCC..AFD3 are unknown. `0x0001` is therefore treated as a minimal unknown probe, not as a known-good value. No HE/DHP ParameterID or known Thermia setting target is encoded; one unknown word changes at a time; 3 s all-zero recovery follows each completed transaction; TX remains restricted to the exact known `0x06 FC23` response slot.

## EXP101 — AFCC..AFD3 one-word influence matrix — COMPLETED NEGATIVE

**Hypothesis:** one or more of the still-unmapped response words `AFCC..AFD3` participates in the DCM03 application layer and may produce a measurable controller effect when a minimal `0x0001` value is carried inside a valid canonical REQ/ACK transaction.

**Observed facts:** all eight planned transactions completed successfully. Each tail word (`AFCC` through `AFD3`) was tested alone as `0x0001` with all other application words zero except `AFCA=03E8` during the proven REQ phase. Summary: `complete=1`, `hard_stop=0`, `ack_hi=8`, `ack_lo=8`, `t1..t8=1`, `0861_changes=16`. No controller, paired RSP02, AFDC..AFE0, settings, CMD1E or outdoor-state changes were observed. No parser resyncs or RX drops occurred.

**Strong conclusion:** none of `AFCC..AFD3=0001`, when tested individually, has a detectable standalone semantic effect inside an otherwise valid transport transaction. The simple one-word-selector hypothesis is negative across the entire remaining tail of the 12-word response bank.

**Unknowns:** this does not exclude multi-word payload structure, values other than `0x0001`, checksums/lengths/sequence fields inside the payload, or a multi-message DCM initialization state machine. The application-layer format remains unresolved.

**Current direction:** stop one-word probing across `AFC8..AFD3`; the full bank has now been covered either by historical-field tests or minimal tail-word tests. The next experiment should target message structure or multi-message sequencing rather than more isolated word values.

## Archive re-analysis before EXP102 — MATERIAL FINDING

A bulk archive containing 98 historical Thermia logs was re-analysed before defining EXP102.

Important recovered coverage that was underrepresented in the condensed experiment summary:
- EXP18 varied AFC8/word0 across 0000,0001,00FE,00FF,0100,FFFF while keeping AFC9=1, AFCA=03E8, AFCB=1; transport ACK occurred but no semantic write was established.
- EXP16 varied AFC9/word1 across 0000,0001,0002,0004,0008,FFFF with AFCA=03E8 and AFCB=1; again transport ACK was largely independent of that value.
- EXP14/15 varied AFCB/word3 over small and boundary values with AFCA=03E8; ACK behavior did not establish application semantics.
- EXP24 and EXP25 already probed words 4..11 with 0001 inside the 0861-active window; no settings change occurred.
- EXP26 and EXP28 tested structured word4/word5 combinations with current/target setpoint-like values and observed no write.

**Strong conclusion:** repeating isolated-word tests is low value. The remaining useful hypothesis is interaction/structure: a field such as AFC9 or AFCB may declare payload length/count, causing tail data in earlier experiments to be ignored when the declared count remained 1.

## EXP102 — count / structure interaction matrix — PREPARED

**Hypothesis:** `AFC9` and/or `AFCB` is a payload length/count field. Earlier tail-word probes may have been structurally invalid because extra non-zero words were supplied while the historical header still declared `0001`.

**Transactions:**
- T1 control: `AFC8=00FF, AFC9=1, AFCA=REQ, AFCB=1`
- T2 AFC9-length2: `AFC9=2`, `AFCC=1`
- T3 AFC9-length3: `AFC9=3`, `AFCC=1`, `AFCD=1`
- T4 AFCB-length2: `AFCB=2`, `AFCC=1`
- T5 AFCB-length3: `AFCB=3`, `AFCC=1`, `AFCD=1`
- T6 both-length2: `AFC9=2`, `AFCB=2`, `AFCC=1`

All six use the proven canonical AFCA=03E8 REQ/ACK handshake with payload stability through ACK-high -> REQ-low -> ACK-low, followed by 3 s all-zero recovery. No known setting register or HE/DHP ParameterID is transmitted. Small values 1..3 only. Hard stop 80 s.

## EXP102 — count / structure interaction matrix — COMPLETED NEGATIVE

**Hypothesis:** `AFC9` and/or `AFCB` is a payload length/count field, so tail data may only be interpreted when the declared count grows coherently with the payload.

**Observed facts:** all six planned coherent structures completed the canonical transaction handshake. Summary: `complete=1`, `hard_stop=0`, `ack_hi=6`, `ack_lo=6`, `t1..t6=1`, `0861_changes=12`. No controller, paired RSP02, AFDC..AFE0, settings, CMD1E or outdoor-state changes occurred; no parser resyncs or RX drops occurred.

**Strong conclusion:** the simple length/count interpretation of AFC9 and AFCB is not supported. Increasing either field to 2/3 while adding matching tail words did not produce any detectable application-layer effect. T6 with both fields at 2 was likewise negative.

**Hypotheses still open:** the DCM application layer may use a different structured encoding, a checksum/sequence/type field, a multi-message initialization/session state machine, or values observed only from a real DCM03.

**Current direction:** stop simple count/length experiments. Prefer evidence-driven reconstruction from real/historical multi-frame patterns or a real DCM03 capture rather than further arbitrary field permutations.


## Historical log archive audit after EXP102

A systematic audit of 98 archived logs recovered substantially broader historical coverage than the condensed experiment history implied. The archive contains extensive first-word/header, selector, tail-word, same-packet, phase, session/presence, HE-envelope and cold-boot tests. At least 45 unique logged experimental `0x06` response payload forms were extracted; early logs sometimes record only the first four words, so this is a lower bound.

**Strong conclusion:** no archived frame was identified as a genuine DCM03/Thermia Online accessory response. Recognisable `AFC8..AFD3` TX payloads are synthetic ESP experiment responses; raw `06 17 AFC8...AFDC...` frames are controller->accessory requests. Therefore the archive is valuable primarily as a negative-test/deduplication corpus, not as a hidden source of the genuine DCM serializer.

**Experiment policy:** do not start EXP103 as another guessed payload probe. EXP103 remains intentionally undefined until new structural evidence is obtained. Preferred evidence is a real DCM03/Online/Connect cold-boot capture plus one known setting change/rollback; next-best evidence is DCM firmware/PCB/debug information or an external owner's capture.


## EXP103 — repeated identical canonical transaction chain — COMPLETED NEGATIVE

**Hypothesis:** the missing DCM03 application/session layer may require multiple consecutive successful transactions with the same application envelope before higher-layer state is established.

**Observed facts:** three identical canonical transactions using `00FF,0001,REQ,0001,0...` completed successfully with no 3 s zero-recovery gap between T1/T2/T3. Each transaction produced the normal `0861 0->16->0` ACK cycle. T1 ACK-low occurred 1077 ms after REQ deassert, T2 after 1076 ms, T3 after 1076 ms. The final summary was `complete=1`, `hard_stop=0`, `ack_hi=3`, `ack_lo=3`, `t1=t2=t3=1`, `settings_changes=0`, `ctrl_changes=0`, `06_changes=0`, `cmd1e_changes=0`, `outdoor_changes=0`, `resync_delta=0`, `drop_delta=0`.

**Strong conclusion:** repeating the exact same historical envelope across three back-to-back valid transport transactions is not sufficient to establish the DCM application/session layer or produce a semantic write. A simple cumulative/repetition requirement is therefore not supported.

**Post-experiment observation:** after EXP103 had already completed and its summary had been emitted, the controller naturally changed `A80E 0->32` and shortly afterwards `AFDC 0->32`. The same natural sequence occurred again later in the same log. Because these transitions occurred after the experiment had ended, they are not attributed to EXP103 and further reinforce that A80E/AFDC transitions are not a reliable DCM-session success criterion.

**Diagnostic note:** this run was captured with the pre-fix EXP103 health bookkeeping bug. `Bus Last Valid Frame Age` remained `nan` and `Valid Frames Since Boot` remained `0` despite continuous valid raw frames. This affects Home Assistant health diagnostics only; it does not invalidate the EXP103 0x06 transaction result. The corrected EXP103 YAML restores last-valid-frame timestamping, valid-frame counting, and Bus Healthy recovery on every CRC-valid frame.

**Next direction:** do not extend this branch to longer arbitrary repetition counts without new evidence. The highest-value next evidence remains a genuine DCM03/Online/Connect capture or hardware/firmware evidence revealing the missing serializer/session protocol.


## EXP104 — AFC8 sequence-toggle canonical transaction chain — PREPARED

**Hypothesis:** `AFC8` may participate in a transaction identity / sequence mechanism whose meaning only appears when its value changes between consecutive canonical transactions. Earlier experiments tested AFC8 values individually; EXP104 tests only the ordering interaction.

**Only experimental variable:** AFC8 alternates across three back-to-back canonical transactions: T1=`00FF`, T2=`00FE`, T3=`00FF`. AFC9 remains `0001`, AFCB remains `0001`, all tail words remain zero, and AFCA uses only the proven `0000 -> 03E8 -> 0000` transport handshake. No 3 s zero-recovery is inserted between transactions; after T3, replies return to all zeros for a 10 s observation window.

**Safety:** `00FF` and `00FE` were already exercised as AFC8 values in earlier tests without a semantic write. No known setting register or HE/DHP ParameterID is transmitted. TX remains restricted to the exact known `0x06 FC23` response slot with the 5 ms UART-empty guard and driver-enable off outside TX. Hard stop 60 s.

**Production invariants retained:** corrected bus-health bookkeeping from the fixed EXP103 is present: every CRC-valid frame refreshes `thermia_last_valid_frame_ms`, increments `thermia_valid_frame_count`, and restores `Bus Healthy=true`.


## EXP104 — AFC8 sequence-toggle canonical transaction chain — COMPLETED NEGATIVE

**Hypothesis:** `AFC8` may participate in a transaction identity / sequence mechanism whose meaning appears only when its value changes between consecutive canonical transactions.

**Observed facts:** T1=`AFC8=00FF`, T2=`AFC8=00FE`, T3=`AFC8=00FF` all completed the canonical `AFCA 0000 -> 03E8 -> 0000` transaction with `0861 0000 -> 0010 -> 0000`. ACK-high delays were 447 ms, 441 ms and 447 ms; ACK-low followed REQ deassert by 1076 ms for all three. Final summary: `complete=1`, `hard_stop=0`, `ack_hi=3`, `ack_lo=3`, `t1=t2=t3=1`, `settings_pushes=0`, `settings_changes=0`, `cmd1e_changes=0`, `outdoor_changes=0`, `resync_delta=0`, `drop_delta=0`.

**Observed controller state during final observation:** after the three experiment transactions had completed and while replies were already all-zero, natural `A80E 0->32` and then `AFDC 0->32` changes occurred. The same A80E/AFDC cycle later returned to zero and repeated multiple times in the same log, so it is not attributed to the AFC8 sequence toggle.

**Strong conclusion:** alternating AFC8 `00FF -> 00FE -> 00FF` across consecutive valid transactions does not produce a semantic setting write or establish the missing DCM application/session state. The simple transaction-sequence interpretation of AFC8 is therefore not supported by this test.

**Production diagnostic validation:** the bus-health repair carried into EXP104 worked. `Valid Frames Since Boot` increased normally and `Bus Last Valid Frame Age` remained finite/near zero during active traffic.

**Next direction:** avoid further arbitrary single-field toggles. Prefer a genuinely new structural hypothesis or new external evidence (real DCM03/Online/Connect capture, firmware/PCB/debug evidence, or cross-model reproduction of the AFCA/0861 handshake).


## EXP105 — State-gated canonical transaction — PREPARED

**Hypothesis:** the unresolved DCM03 application/session layer may only accept the already-known canonical transaction during a controller-advertised lifecycle/service window. The natural `A80E=0x0020` followed by `AFDC=0x0020` cycle is the only evidence-backed candidate window currently available.

**Only experimental variable changed:** transaction timing relative to controller state. Payload remains the previously tested historical envelope `00FF,0001,REQ,0001,0...`; no new values or setting IDs are introduced.

**Sequence:**

1. Arm and remain strictly passive.
2. Wait until current `A80E=0x0020` and an exact `0x06` FC23 poll carries `AFDC=0x0020`.
3. On that poll preload `00FF,0001,0000,0001,0...`.
4. On the next safe SHORT poll while the gate remains high, assert `AFCA=0x03E8`.
5. Complete the proven `0861 0->16->0` four-phase handshake.
6. Reply zeros for 20 s observation.
7. Hard stop at 180 s if no usable window/completed transaction occurs.

If the gate closes before REQ assertion, the attempt is abandoned and the experiment returns to passive waiting.


## EXP105 — State-gated canonical transaction — COMPLETED NEGATIVE

**Hypothesis:** a semantic/application transaction may only be accepted during the natural lifecycle window where `A80E=0x0020` and `AFDC=0x0020`.

**Observed:**
- gate occurred naturally and was detected with `A80E=0020` and `AFDC=0020`;
- one historical canonical transaction was executed inside that window;
- `0861` ACK-high occurred 373 ms after REQ assert;
- ACK-low occurred 1151 ms after REQ deassert;
- `gate_seen=1`, `gate_aborts=0`, `txn_complete=1`;
- no settings, CMD1E, outdoor, or semantic state changes;
- no parser resyncs or RX drops.

**Conclusion:** controller-state gating at the natural `0x20/0x20` window does not make the known historical envelope semantically valid. This materially weakens the hypothesis that our missing layer is merely a timing/window condition. The unresolved layer remains the DCM03 application/session serializer or startup dialogue.

**Decision:** do not continue nearby timing/state-gating variants without new evidence. Prefer genuine DCM traffic, second-unit cross-check of the handshake, or hardware/firmware evidence.


## EXP106 — Passive integration-sync window correlator — PREPARED

**Hypothesis:** historical `A80F=0x0032` (decimal 50) intervals may mark a broader controller integration/synchronisation phase. EXP93 never actually reached this state. EXP105 showed that `A80E=0x20` + `AFDC=0x20` alone is not a sufficient semantic gate, so EXP106 characterises the wider passive state around A80F=50 without transmitting.

**Experimental variable:** observation only. No Thermia-bus value is changed.

**Design:** remain fully RX-only for up to 30 minutes; trigger on the first observed `A80F=0x0032`; then continue passive observation for 180 s. Log change-only context for `A80C..A812`, paired `A7F8..A806`, exact `0x06` `AFDC..AFE0` polls/cadence, `0x0F:0861`, settings pushes, `0x1E` command image, and outdoor-unit operating state. If A80F=50 never appears, hard-stop at 1800 s and record that explicitly.

**Safety:** no RS485 TX anywhere in EXP106. Driver-enable is continuously forced off. No response to `0x06`, no `0x0A` emulation, no register write. Corrected bus-health bookkeeping remains intact.

**Success / information criterion:** a repeatable constellation of controller/accessory changes specifically associated with entering/leaving A80F=50 that narrows the candidate DCM initial-sync window. A no-trigger run is inconclusive about the hypothesis but records occurrence frequency; a triggered run with no distinctive DCM-related behaviour is evidence against A80F=50 as the missing sync discriminator.


## Cross-model update from Piotr Romanowski / thermia-bus-sniffer (2026-09-23)

Independent iTec Eco 8 / DHP-AQ observations materially refine several interpretations:

- `0x1E FC04 0x001E..0x0033` is **not frozen** and not a boot snapshot. It changes rarely and out of step with the live `0x0000..0x0015` block. Treat it only as a delayed/latched-looking region with exact semantics unknown.
- `0x0A:B3B1` is a **proven semantic request channel** when returned by the accessory in the controller's FC23 poll response. Encoding is whole °C (x1). A non-zero value requests a stored room-setpoint change; `0` means no request and does not revert the stored setpoint.
- `0x0A:B3C5` is the controller's push-back/confirmed room setpoint and independently confirms acceptance of a B3B1 request.
- On the Eco 8, `AFDD`, `AFDE`, `AFDF` remained constant `0`; `AFE0` equals displayed outdoor temperature x1.
- On the Eco 8, `AFDC` pulses `0 <-> 0x20` continuously with ~64 s period (~17 s high / ~47 s low), and `A80E` moves with it to the second. This is strong cross-model evidence that the A80E/AFDC 0x20 cycle is ordinary controller lifecycle/heartbeat behaviour, not DCM login/approval/session acceptance.
- `0x0F:0861` has remained passively at `0` on the Eco 8 over multi-day observation. Therefore any `0861` transition during an active 0x06 test is highly meaningful and continues to support its role as a transaction-level response to `AFCA=0x03E8`.
- A80E can carry additional bits independently of the 0x20 heartbeat (Piotr observed bit 3 for ~10 minutes). Exact bit semantics remain open.
- One isolated `AFDC=0x10` observation coincided with the outdoor-unit active status rising. This is one coincidence only and is not sufficient evidence for an approval window.

**Protocol correction:** do not use `AFDC=0x10`, `AFDC=0x20`, or matching `A80E` values as a DCM approval/session gate without new evidence.

**Next-experiment implication:** if/when EXP107 is prepared, prefer testing a continuously present/stable accessory image followed by one isolated known `AFCA 0 -> 03E8 -> 0` pulse, rather than gating on AFDC/A80E state. EXP107 is only a candidate until EXP106 is formally closed.


## Experiment transition — 2026-09-23

### EXP106 — CLOSED (partial capture, hypothesis sufficiently rejected)

Hypothesis:
`A80F=0x0032` might identify a special integration/synchronisation phase relevant to 0x06/DCM activity.

Observed:
- one run reached `A80F=0x0032` after `0x0050 -> 0x0032`;
- the same A80E/AFDC `0 <-> 0x20` lifecycle was already observed at A80F values 75 and 80 and continued at 50;
- A80F=50 coincided with ordinary outdoor-unit sequencing toward idle;
- a later run remained at A80F=10 for at least the captured interval without any trigger;
- no `0861` activity or settings mutation occurred passively;
- the first triggered run did not include the planned final 180 s summary, so the capture is formally incomplete.

Strong conclusion:
A80F=50 is neither required nor unique for the A80E/AFDC lifecycle and is not a justified DCM approval/session gate. Piotr's Eco 8 evidence independently shows AFDC/A80E `0<->0x20` can be a steady controller heartbeat.

Negative result recorded:
Do not use A80F=50, AFDC=0x20, AFDC=0x10, or matching A80E values as 0x06 semantic-session gates without new evidence.

### EXP107 — PREPARED

Hypothesis:
The controller may require the 0x06 accessory image to be continuously present and stable before the already-known AFCA request pulse is asserted.

Only experiment-level variable changed versus the prior short-preload handshake test:
- REQ-low historical accessory image stabilization time is increased to >=60 s.

Accessory image:
`00FF,0001,0000,0001,0000,0000,0000,0000,0000,0000,0000,0000`

Then ONLY:
`AFCA: 0000 -> 03E8 -> 0000`

All other words remain unchanged.

No new semantic register target or value is introduced.

Current experiment: **EXP107 — PREPARED, not yet run**.


## EXP107 — COMPLETED — Persistent accessory image then isolated AFCA pulse

Hypothesis:
The controller may require the 0x06 accessory image to be continuously present and stable before the already-known AFCA request pulse is asserted.

Observed:
- Baseline qualified with AFDC..AFE0 = `0000,0000,0000,0000,0016`, `0861=0`, `A80E=0`.
- Settings baseline source was the validated persisted cache.
- Historical REQ-low image `00FF,0001,0000,0001,0,0,0,0,0,0,0,0` was then answered continuously.
- Presence immediately switched the controller to the familiar fast alternating cadence (~0.71 s / ~1.43-1.46 s).
- The same REQ-low image was held for 61.023 s before AFCA was changed.
- At 61.023 s, only AFCA changed `0000 -> 03E8`.
- `0861` rose `0 -> 16` after 328 ms.
- On the next exact 0x06 poll, only AFCA changed `03E8 -> 0000`.
- `0861` fell `16 -> 0` after 1122 ms.
- The identical REQ-low image remained present for another 90 s.
- Final summary:
  - handshake_complete=1
  - total_responses=144
  - observe_responses=84
  - A80E_peak=0, A80E_changes=0
  - AFDC_peak=0, AFDC_changes=0, AFDC_nonzero=0
  - status_peak=16
  - settings_changed=0
  - resync_delta=0, drop_delta=0

Strong conclusion:
Long-lived stable accessory presence before the canonical AFCA request pulse is NOT sufficient to unlock semantic DCM/Online behaviour. It changes transport cadence/presence exactly as before and completes the normal 0861 transport handshake, but produces no settings mutation or new DCM/session state.

Negative result recorded:
Reject the simple hypothesis that a 30–60 s persistent historical accessory image, followed by the known AFCA strobe, is the missing initialization step.

Current project direction:
Stop varying dwell time / simple envelope timing. The highest-value next work is firmware-led reconstruction of identity/binding/integration/initial-sync state, especially around:
`ProductID`, `BrandID`, `DivisionID`, `ServiceBind`, `IntegrationMode`, `SystemIntegrationInitRequest`, `InitialSyncDone`.

Current experiment: **EXP107 COMPLETE**.


## Firmware reverse engineering — 2026-09-23 — 2.1.35 vs 2.7.42

Deep extraction of the Windows CE `ccimage.bin` files recovered embedded .NET assemblies.

### Historical split
- `2.1.35` already contains a generic `DHPParameterCache` / HE service infrastructure, but its `RegulationEngine.dll` contains no `HPNode`, `IntegrationMode`, `SystemIntegrationInit`, or `HeatPumpRegulation` application layer.
- `2.7.42` contains a dedicated `HPNode` in `RegulationEngine.dll` plus the full DHP parameter model and integration lifecycle.

This means the generic HE/DHP transport/cache substrate predates the later heat-pump application/regulation layer.

### Exact DHP parameter IDs recovered from `ParameterCache.dll`
The 2.7.42 `ParameterID` static constructor confirms:
- 0x4400 HeatPumpType
- 0x4401 RoomValue
- 0x4402 HeatCurve
- 0x4403 HeatCurveMin
- 0x4404 HeatCurveMax
- 0x4405 HeatCurvePlus5
- 0x4406 HeatCurveZero
- 0x4407 HeatCurveMinus5
- 0x4408 HeatStop
- 0x4409 RoomFactor
- 0x440A HotWaterStart
- 0x440B ControllerDemand
- 0x440C SupplyLineTemperature
- 0x440D ReturnLineTemperature
- 0x440E ExternalControl1
- 0x440F ExternalControl2
- 0x4410 AuxiliaryHeaterPowerStage
- 0x4411 HotWaterTemperature
- 0x4412 OperationStatus
- 0x4413 ExternalControl3
- 0x4414 IntegrationMode
- 0x4415 DefrostDemand
- 0x4416 EVU_SW
- 0x4417 EVU_HW

### Critical correction: init flags are INTERNAL, not wire ParameterIDs
`m_SystemIntegrationInitRequest` and `m_InitSyncDone` are ordinary internal boolean fields in `HPNode`; they are not HE ParameterIDs.

The wire-visible trigger is `IntegrationMode` (`0x4414`). When that parameter updates:
- `OnIntegrationModeParameterUpdated()` sets `m_SystemIntegrationInitRequest = true`;
- sets `RegulationRequired = true`;
- signals model/node changed.

During the next regulation pass:
- `SystemIntegrationInit()` runs;
- `m_InitSyncDone` is cleared;
- `Sync(fullUpdate=true)` runs;
- only after successful full sync is `m_InitSyncDone` set true.

Therefore do NOT search AFC8..AFD3 for literal "SystemIntegrationInitRequest" or "InitialSyncDone" fields unless independent local-bus evidence appears.

### IntegrationMode semantics
`get_IsSystemIntegration()` returns true whenever the IntegrationMode parameter value is non-zero.

The IntegrationMode Parameter object is configured:
- default value 0;
- GetOnSync = true;
- SetOnSync = true;
- ClearSetOnSync = true;
- UseLateCommit = true;
- PartialUpdateIndex = 0.

### System integration changes sync ownership
`UpdateParameterFlow(isSystemIntegration)` switches these parameters:
- RoomValue
- HeatCurve
- HeatCurvePlus5
- HeatCurveZero
- HeatCurveMinus5

When system integration is active, those parameters become SET-on-sync; when not active, they become GET-on-sync.

### Full initial sync is explicitly split into three partial-update groups
`Sync(fullUpdate=true)` executes partial update indices 0, 1, and 2, and only commits GET values after all groups succeed.

This strongly supports a stateful, grouped synchronization model rather than independent scalar writes.

### Binding/identity architecture
2.7.42 `DHPParameterCache::OnHEServiceBind()` explicitly accepts/rejects devices by:
- physical address;
- DivisionID;
- BrandID;
- ProductID.

Only an accepted descriptor gets an endpoint.

Important scope limitation:
This proves HE/Z-Wave-side identity and binding. It does NOT prove that the local DCM03↔heat-pump RS485 mailbox contains the same identity fields.

### Practical consequence
After EXP107's negative result, the next useful 0x06 experiment should not guess an internal init flag.
Research priority is now:
1. reconstruct exact partial sync group composition and ordering;
2. determine whether the local 12-word DCM mailbox represents a grouped sync transaction;
3. only then design EXP108 around one evidence-backed group-0 / IntegrationMode-related structure.


---

## 2026-09-24 — EXP134–136 and genuine Online/DCM capture correction

### EXP134 — passive DHW START correlation — PROCEDURAL / INCIDENTAL
- Strictly passive.
- Only observed settings-word change was `0x03E8: 34 -> 35`, matching Heating Curve.
- No valid DHW START A/B/A conclusion.
- `0x041D` was not observed.

### EXP135 — passive DHW START A/B/A — COMPLETE / NEGATIVE FOR 0x03F1
Hypothesis: manual `SERVICE -> WARMWATER -> START` ±1 °C causes a reversible native `0x0F` word change.
Observed:
- valid baseline / changed / restored markers;
- recurrent `0x03E8..0x03F5` remained unchanged;
- `0x03F1` remained `40`;
- no observed block covered `0x041D`.
Conclusion:
- previous `0x03F1 = Hot Water Start` interpretation is downgraded to OPEN / locally unsupported;
- `0x041D` remains OPEN.

### EXP136 — passive DHW COMFORT/ECO A/B/A — COMPLETE / NEGATIVE
Hypothesis: DHW mode `COMFORT <-> ECO` maps to one of `0x03F2`, `0x03F3`, `0x03F5`.
Observed:
- physical Thermia mode was genuinely changed and restored;
- `wordChanges=0`;
- no change anywhere in recurrent `0x03E8..0x03F5`;
- parser resync/drop deltas remained zero.
Conclusion:
- DHW COMFORT/ECO mode is not represented in the recurrent `0x03E8..0x03F5` block on the tested XTR M.

### Genuine Thermia Online external capture — architecture correction
External capture from a working Thermia Online installation contains:
- a real slave `0x0F` that ACKs controller-originated FC16 writes;
- controller FC03 reads from slave `0x0F`, including `0x03E8`;
- during a deliberate Heat Curve `20 -> 21 -> 20` change, two observed `0x03E8` read snapshots differ only in the first word (`23 -> 22`), independently strengthening `0x03E8` as Heat Curve-related;
- recurrent controller writes to `0x0F` across large block families (`07D0`, `07E4`, `07F8`, `080C`, `0820`, `0834`, `0848`, `0864`, `0870`, `0884`);
- `0x06` is polled but no `0x06` response is present in the supplied working-Online capture;
- an active slave `0xA5` is present; exact identity remains unknown.

Strong architectural correction:
- `0x06` remains proven as an expansion/accessory presence interface, but is no longer treated as the required Online/DCM path.
- `0x0F` is now strongly indicated as the shared controller <-> Online/DCM register interface.
- Direction/ownership matters: controller FC16 writes likely populate controller->Online state, while controller FC03 reads likely consume Online->controller desired/config values.
- Exact physical ownership of slave `0x0F` and role of `0xA5` remain unknown.

### EXP137 — PREPARED
Hypothesis:
If simple slave-`0x0F` presence is the first missing step, ACKing only already-observed XTR `0x0F` FC16 write shapes may cause the XTR controller to begin FC03 reads from slave `0x0F`.

Controlled active behavior:
- 30 s passive baseline;
- abort if a pre-existing `0x0F` responder or FC03 activity is detected;
- active phase ACKs only exact known XTR FC16 shapes:
  - `03E8 / count 14`
  - `0442 / count 13`
  - `04A6 / count 13`
  - `085F / count 5`
- standard FC16 ACK only; no register values transmitted;
- never answer FC03;
- first post-ACK `0x0F` FC03 request is the positive discriminator and immediately disables TX;
- 90 s active timeout;
- fail closed on parser/RX-buffer error.

Current experiment: **EXP137 — slave 0x0F FC16 ACK-only presence probe — PREPARED, not yet run**.


---

## 2026-09-24 — EXP138 PREPARED — sequential 0x0F FC16 ACK probe

Hypothesis:
EXP137 proved that a standard ACK to controller-originated `0x0F FC16 03E8/count14` advances the controller to a new `0410/count22` stage. EXP138 tests the smallest next discriminator: does ACKing `0410/count22` advance the controller again to a new FC16 stage or to an FC03 read phase?

Only experimental variable changed versus EXP137:
- add `0x0410/count22` to the exact FC16 ACK whitelist.

Everything else remains unchanged:
- 30 s passive baseline;
- abort on any pre-existing 0x0F responder/read activity;
- no register-value injection;
- no FC03 response;
- no slave-0x06 responder;
- no room-sensor emulation;
- exact start/count whitelist only;
- parser/RX-drop fail-closed guards;
- DE LOW outside the brief ACK transmission.

Active ACK whitelist:
- `03E8/count14`
- `0410/count22`  **NEW**
- `0442/count13`
- `04A6/count13`
- `085F/count5`

Positive criterion:
After at least one successful ACK of `0410/count22`, either:
1. a previously unseen 0x0F FC16 block appears; or
2. the controller issues an 0x0F FC03 request.

For a new FC16 shape, EXP138 logs it, does NOT ACK it, forces DE LOW, and stops. For FC03, EXP138 likewise does NOT answer and stops.

Safety rationale for new target:
`0410/count22` is not guessed. EXP137 locally observed it immediately after the successful `03E8/count14` ACK and then saw it retransmitted 83 times while unacknowledged. ACKing that exact request is therefore the smallest bounded continuation of the proven controller sequence.

Current experiment: **EXP138 PREPARED, not yet run**.


---

## 2026-09-24 — Correction after fclauson follow-up analysis of genuine Online capture

The follow-up GitHub comments contain an automated interpretation of the same capture. The raw frames were re-parsed independently before accepting those claims.

Raw-frame correction:
- `0x0F FC16 start 0x0848 count 23` occurs at ~12.116 s and ~33.107 s.
- At 12.116 s, register `0x0858` is `0x0000`.
- At 33.107 s, register `0x0858` is `0x0015` (=21).
- Register `0x085A` is `0x0014` (=20) in BOTH 0x0848 frames.
- Therefore the statement that the same 0x0848 field changed `20 -> 21` is incorrect. The actual observed delta is:
  `0x0858: 0 -> 21`, while `0x085A` remains 20.
- The `0x07E4` frame at ~43.705 s matches the earlier recurring `0x07E4` block and does not by itself prove a `21 -> 20` revert of the same field.

What remains useful:
- A value 21 appears exactly once in the second `0x0848` block, at `0x0858`, temporally during the user's Heat Curve 20->21->20 test.
- This makes `0x0858` a strong event/command/synchronization candidate related to the Heat Curve change, but NOT yet a proven persistent Heat Curve register.
- The earlier `0x03E8` FC03 responses still differ by exactly one in their first word (`23 -> 22`) and remain independently consistent with Heat Curve correlation, but exact click timestamps are still needed to assign the two snapshots unambiguously to 20/21/20 phases.

Protocol implication:
Do not adopt the follow-up comment's claim that `0x0848` directly carries a persistent 20->21->20 setpoint in one field. Keep the raw-frame facts separate from that interpretation.

EXP138 remains the next controlled local test because it only probes the locally proven ACK sequence and does not depend on the disputed semantic interpretation of `0x0858`.


---

## 2026-09-24 — EXP138 COMPLETE — sequential 0x0F FC16 ACK probe

Hypothesis:
After EXP137 proved `03E8/count14 -> ACK -> 0410/count22`, ACKing the exact locally observed `0410/count22` stage should advance the XTR controller to the next 0x0F transfer stage.

Observed:
- At EXP138 start, the controller was already repeatedly transmitting `0410/count22` during the 30 s passive baseline.
- This means the controller-side 0x0F transfer state persisted across the ESP reboot / firmware change after EXP137.
- Baseline summary before active phase:
  - `fc16Seen=28`
  - `whitelisted=28`
  - `unknown=0`
  - no pre-existing 0x0F ACK responder
  - no FC03 activity
  - parser/drop counters clean.
- Active phase:
  - first `0410/count22` request was ACKed once.
  - `ack0410=1`.
  - ~1.54 s later the controller advanced to a NEW block:
    `042E/count15` (decimal 1070..1084).
  - EXP138 correctly did NOT ACK the new block and stopped immediately.
- Final summary:
  - reason=`POSITIVE_NEW_FC16_STAGE_AFTER_0410`
  - duration_ms=31949
  - fc16Seen=30
  - whitelisted=29
  - unknown=1
  - ackTx=1
  - txRefused=0
  - fc16AckSeen=0
  - fc03Req=0
  - fc03Resp=0
  - existingResponder=NO
  - resyncDelta=0
  - dropDelta=0
  - DE_LOW.

Strong conclusions:
1. The local XTR 0x0F transfer is a controller-side persistent acknowledged sequence.
2. Sequence state survives the ESP reboot / responder disappearance: after EXP137 stopped at `0410`, EXP138 booted and the controller resumed/retried `0410`.
3. One valid ACK to `0410/count22` deterministically advances the controller to `042E/count15`.
4. The sequence established locally is now at least:
   `03E8/count14 -> ACK -> 0410/count22 -> ACK -> 042E/count15`.
5. `042E/count15` is now a locally proven XTR 0x0F transfer block, not merely an external-map candidate.

External-map alignment:
`0x042E` = decimal 1070 and count 15 covers decimal 1070..1084, exactly matching a block family seen in the external DHP/ATEC register map. Semantics of individual words remain unproven on XTR.

Negative result:
No FC03 read phase is reached before `042E/count15` is acknowledged.

Current experiment: **EXP138 COMPLETE / POSITIVE TRANSPORT PROGRESSION**.

Smallest next experiment:
EXP139 should add only `042E/count15` to the exact ACK whitelist. All other behavior remains unchanged. The first new FC16 shape or first FC03 request after that ACK is the positive discriminator and must not be answered.


---

## 2026-09-24 — EXP139 PREPARED — sequential 0x0F FC16 ACK probe, stage 0x042E

Hypothesis:
EXP138 proved the local acknowledged sequence:
`03E8/count14 -> ACK -> 0410/count22 -> ACK -> 042E/count15`.
EXP139 tests the smallest next discriminator: does ACKing the exact locally observed `042E/count15` stage advance the controller again to another FC16 transfer block or to the FC03 read phase seen in the genuine Online capture?

Only experimental variable changed versus EXP138:
- add `0x042E/count15` to the exact FC16 ACK whitelist.

Known facts about the new target before testing:
- address `0x042E` = decimal 1070;
- count 15 covers `0x042E..0x043C` / decimal 1070..1084;
- EXP138 locally observed this block only after a valid ACK to `0410/count22`;
- EXP138 stopped before acknowledging it;
- external DHP/ATEC material contains a structurally matching 1070..1084 block family, but individual semantics are NOT imported as XTR truth.

Possible effect:
ACKing this request may advance the controller's 0x0F synchronization state to the next stage. No semantic register value is generated or modified by the ESP; the ACK only confirms receipt of the controller's own write request.

Everything else remains unchanged:
- 30 s passive baseline;
- abort on pre-existing 0x0F responder/read activity;
- no value injection;
- no FC03 response;
- no slave-0x06 responder;
- no room-sensor emulation;
- exact start/count whitelist only;
- fail closed on parser/RX-drop errors;
- DE LOW outside brief ACK transmission.

Active ACK whitelist:
- `03E8/count14`
- `0410/count22`
- `042E/count15` **NEW**
- `0442/count13`
- `04A6/count13`
- `085F/count5`

Positive criterion:
After at least one successful ACK of `042E/count15`, either:
1. a previously unseen 0x0F FC16 block appears; or
2. the controller issues an 0x0F FC03 request.

For either positive discriminator, EXP139 does not answer the new stage and stops with DE LOW.

Current experiment: **EXP139 PREPARED, not yet run**.


---

## 2026-09-24 — EXP139 COMPLETE — sequential 0x0F FC16 ACK probe, stage 0x042E

Hypothesis:
After EXP138 proved `03E8/14 -> ACK -> 0410/22 -> ACK -> 042E/15`, ACKing the exact locally observed `042E/count15` stage should advance the controller to the next 0x0F transfer stage.

Observed:
- At experiment start, the controller was already repeatedly transmitting `042E/count15` during the 30 s passive baseline.
- This again confirms that the Thermia/controller-side 0x0F transfer state persists across ESP reboot / firmware replacement.
- Baseline before active phase:
  - `fc16Seen=28`
  - `whitelisted=28`
  - `unknown=0`
  - no pre-existing 0x0F responder
  - no FC03 activity
- Active phase:
  1. `042E/count15` was ACKed once (`ack042E=1`);
  2. ~0.52 s later the controller sent `04A6/count13`;
  3. `04A6/count13` was already in the unchanged whitelist and was ACKed;
  4. ~1.55 s later the controller advanced to a previously unseen block:
     `04BA/count22` (decimal 1210..1231);
  5. EXP139 did not ACK `04BA/count22` and stopped immediately.
- Final summary:
  - reason=`POSITIVE_NEW_FC16_STAGE_AFTER_042E`
  - duration_ms=32936
  - fc16Seen=31
  - whitelisted=30
  - unknown=1
  - ackTx=2
  - txRefused=0
  - fc16AckSeen=0
  - fc03Req=0
  - fc03Resp=0
  - existingResponder=NO
  - resyncDelta=0
  - dropDelta=0
  - DE_LOW.

Strong conclusions:
1. ACKing `042E/count15` advances the controller out of the 042E retry state.
2. The next observed stage is `04A6/count13`; because that exact shape was already whitelisted from earlier XTR observations, it was ACKed without changing the experiment design.
3. After the `04A6/count13` ACK, the controller advances to new block `04BA/count22`.
4. The locally proven acknowledged sequence is now at least:
   `03E8/14 -> ACK -> 0410/22 -> ACK -> 042E/15 -> ACK -> 04A6/13 -> ACK -> 04BA/22`.
5. `04BA/count22` is now a locally proven XTR 0x0F transfer block.
6. Controller-side sequence state again persists across ESP reboot / responder disappearance.

Important nuance:
EXP139 does not isolate whether `04A6/count13` is exclusively caused by the 042E ACK or is an independently recurring block; however, in this run it appears 0.52 s after the 042E ACK and its ACK is immediately followed by the new 04BA stage. Treat `04A6` as a proven observed intermediate stage in this sequence, but not yet as uniquely sequence-owned.

Negative result:
No FC03 read phase was reached before `04BA/count22` was acknowledged.

Current experiment: **EXP139 COMPLETE / POSITIVE TRANSPORT PROGRESSION**.

Smallest next experiment:
EXP140 should add only `04BA/count22` to the exact ACK whitelist. Everything else remains unchanged. The first new FC16 shape or first FC03 request after that ACK is the positive discriminator and must not be answered.


---

## 2026-09-24 — EXP140 PREPARED — sequential 0x0F FC16 ACK probe, stage 0x04BA

Hypothesis:
EXP139 locally extended the acknowledged sequence to:
`03E8/14 -> ACK -> 0410/22 -> ACK -> 042E/15 -> ACK -> 04A6/13 -> ACK -> 04BA/22`.
EXP140 tests the smallest next discriminator: does ACKing the exact locally observed `04BA/count22` stage advance the controller to another FC16 transfer block or to the FC03 read phase?

Only experimental variable changed versus EXP139:
- add `0x04BA/count22` to the exact FC16 ACK whitelist.

Known facts before testing the new target:
- `0x04BA` = decimal 1210;
- count 22 covers `0x04BA..0x04CF` / decimal 1210..1231;
- EXP139 observed it only after successful ACKs to `042E/count15` and then `04A6/count13`;
- EXP139 stopped before ACKing it;
- exact word semantics are unknown.

Possible effect:
ACKing `04BA/count22` may advance the controller's 0x0F synchronization state. The ESP still does not create, alter or inject semantic register values; it only returns the standard FC16 acknowledgement for the controller's own request.

Everything else remains unchanged:
- 30 s passive baseline;
- abort on pre-existing 0x0F responder/read activity;
- no FC03 response;
- no slave-0x06 responder;
- no room-sensor emulation;
- exact start/count whitelist only;
- fail closed on parser/RX-drop errors;
- DE LOW outside brief ACK transmission.

Active ACK whitelist:
- `03E8/count14`
- `0410/count22`
- `042E/count15`
- `0442/count13`
- `04A6/count13`
- `04BA/count22` **NEW**
- `085F/count5`

Positive criterion:
After at least one successful ACK of `04BA/count22`, either:
1. a previously unseen 0x0F FC16 block appears; or
2. the controller issues an 0x0F FC03 request.

For either positive discriminator, EXP140 does not answer the new stage and stops with DE LOW.

Current experiment: **EXP140 PREPARED, not yet run**.


---

## 2026-09-24 — EXP140 COMPLETE — sequential 0x0F FC16 ACK probe, stage 0x04BA

Hypothesis:
After EXP139 extended the locally observed sequence to `... -> 04BA/count22`, ACKing that exact block should advance the controller to the next 0x0F transfer stage.

Observed:
- At EXP140 start, the controller was already repeatedly transmitting `04BA/count22` during the 30 s passive baseline.
- This is a third independent confirmation that the controller-side 0x0F transfer state persists across ESP reboot / firmware replacement.
- Baseline before active phase:
  - `fc16Seen=28`
  - `whitelisted=28`
  - `unknown=0`
  - no pre-existing 0x0F responder
  - no FC03 activity
  - parser/drop counters clean.
- Active phase:
  1. `04BA/count22` was ACKed once (`ack04BA=1`);
  2. ~0.65 s later the controller advanced to a previously unseen block:
     `05FF/count33` (decimal 1535..1567);
  3. EXP140 did not ACK the new block and stopped immediately.
- Final summary:
  - reason=`POSITIVE_NEW_FC16_STAGE_AFTER_04BA`
  - duration_ms=31011
  - fc16Seen=30
  - whitelisted=29
  - unknown=1
  - ackTx=1
  - txRefused=0
  - fc16AckSeen=0
  - fc03Req=0
  - fc03Resp=0
  - existingResponder=NO
  - resyncDelta=0
  - dropDelta=0
  - DE_LOW.

Strong conclusions:
1. ACKing `04BA/count22` deterministically advances the controller to `05FF/count33`.
2. `05FF/count33` is now a locally proven XTR 0x0F transfer block.
3. The acknowledged controller->0x0F sequence is longer than previously known and remains stateful across ESP reboot.
4. No FC03 read-side phase has been reached yet.

Locally proven sequence so far:
`03E8/14 -> ACK -> 0410/22 -> ACK -> 042E/15 -> ACK -> 04A6/13 -> ACK -> 04BA/22 -> ACK -> 05FF/33`.

New block range:
`0x05FF..0x061F` (count 33; decimal 1535..1567).

Unknowns:
- exact semantics of the `05FF` block;
- whether this is still initialization/snapshot sync or already part of command/state exchange;
- how many stages remain before FC03;
- whether additional non-FC16 handshake elements occur later.

Current experiment: **EXP140 COMPLETE / POSITIVE TRANSPORT PROGRESSION**.

Smallest next experiment:
EXP141 should add only `05FF/count33` to the exact ACK whitelist. All other behavior remains unchanged. The first new FC16 shape or first FC03 request after that ACK is the positive discriminator and must not be answered.


---

## 2026-09-24 — EXP141 PREPARED — gated 0x0F sequence walker

Hypothesis:
EXP137–EXP140 established a repeatable controller-side acknowledged FC16 sequence, with state persisting across ESP reboots:
`03E8/14 -> 0410/22 -> 042E/15 -> 04A6/13 -> 04BA/22 -> 05FF/33`.
Instead of reflashing once per newly discovered block, EXP141 tests whether the same sequence can be traversed safely within one firmware session using human-gated ACK approval for each new unknown stage.

Change in experimental method:
- `05FF/count33`, locally discovered by EXP140, is added as the one newly known automatic ACK target.
- Any later unknown FC16 shape is NOT automatically ACKed.
- An unknown candidate must repeat at least 3 times with identical start/count before it becomes lockable.
- The HA control `EXP141 ARM ACK Current Candidate Once` does not transmit asynchronously. It only arms the candidate; the standard FC16 ACK is sent on the next exact matching request.
- After manual approval, exact retransmissions of that one approved runtime shape may be ACKed during the same run.
- Maximum 8 manually approved new stages per run.
- The first FC03 request is logged and terminates the experiment without a response.
- A real/pre-existing 0x0F FC16 ACK or FC03 response aborts the experiment.
- Parser resync or RX-drop deltas abort TX.
- Full FC16 payloads are logged for audit.

Safety rationale:
The walker never fabricates or modifies register payload values. It only acknowledges the controller's own exact FC16 write request. New write targets still require explicit human approval after repeated observation. This is faster than one-firmware-per-stage while preserving a controlled gate before each newly discovered target.

Known automatic ACK shapes:
`03E8/14`, `0410/22`, `042E/15`, `0442/13`, `04A6/13`, `04BA/22`, `05FF/33`, `085F/5`.

Controls remain under Home Assistant Configuration:
- START walker
- ARM ACK current candidate once
- STOP walker

Active window: 600 s after a 30 s passive baseline.

Current experiment: **EXP141 PREPARED, not yet run**.


---

## 2026-09-24 — EXP141 RUNNING / PARTIAL POSITIVE — gated sequence walker reached 0x0662/count33

Hypothesis:
A human-gated sequence walker can traverse multiple unknown controller-side 0x0F FC16 stages in one firmware session without reflashing, while requiring repeated observation plus explicit operator approval for each new target.

Observed in first EXP141 run:
- 30 s passive baseline contained only repeated `05FF/count33`, already known from EXP140.
- Active walker ACKed `05FF/count33` once.
- ~1.56 s later a new unknown block appeared:
  `0662/count33` (decimal 1634..1666; hex range `0x0662..0x0682`).
- The full payload remained identical across repeated requests.
- After the third identical start/count observation, EXP141 correctly emitted:
  `CANDIDATE_LOCKED start=0662 count=33 repeats=3 action=WAIT_FOR_HA_ARM`.
- The controller then continued retrying `0662/count33` without progression because no HA ARM action was present in the supplied log.
- Parser resync and RX-drop counters remained unchanged at zero throughout the shown run.
- No FC03 request/response and no real 0x0F responder was observed in the supplied log fragment.

Strong conclusions:
1. `05FF/count33 -> ACK -> 0662/count33` is now locally proven.
2. `0662/count33` is a new locally proven XTR 0x0F transfer stage.
3. The gated-walker qualification mechanism works as designed: the unknown stage was observed repeatedly, locked after 3 identical requests, and was not ACKed automatically.
4. The controller remains blocked/retrying the outstanding stage until explicit approval, preserving the safety gate.

Status:
**EXP141 RUNNING / PARTIAL POSITIVE — candidate 0662/count33 locked, awaiting manual ARM.**

Next action:
While EXP141 is still active, press `EXP141 ARM ACK Current Candidate Once`. The button only arms the candidate; the actual FC16 ACK is sent on the next exact matching `0662/count33` request. Then observe the next candidate or FC03 discriminator. No reflash is required.


### EXP141 continuation — 0x0662/count33 manually ACKed; sequence becomes quiet

Observed continuation of the same EXP141 run:
- Operator pressed the HA ARM control for locked candidate `0662/count33`.
- Log confirms:
  - `ARM_OK candidate=0662 count=33`
  - next exact `0662/count33` request received `ACK_TX kind=MANUAL_GATED`
  - `MANUAL_STAGE_ACKED stage=1 start=0662 count=33`.
- After that ACK, the supplied log shows no further EXP141/0x0F FC16 stage and no FC03 request for at least ~11 s before the log fragment ends.
- Other Thermia traffic continues and bus-health telemetry remains normal.

Interpretation:
- `0662/count33` ACK was accepted at transport level in the sense that the repeated retry stream ceased immediately.
- Unlike prior stages, no next FC16 block appeared within the usual ~0.5–1.6 s transition window.
- This may indicate that `0662/count33` is a terminal or phase-boundary stage, OR that the next phase requires a longer delay/event/other handshake.
- No FC03 read-side transition is proven yet.

Status remains:
**EXP141 RUNNING / PARTIAL POSITIVE — 0662/33 manually ACKed; waiting for post-sequence behavior.**

Next action:
Do not reflash and do not press ARM again unless a new `CANDIDATE_LOCKED` appears. Let EXP141 continue through its active window and capture any FC03 request, new FC16 candidate, or timeout summary.


---

## 2026-09-24 — EXP142 PREPARED — post-0x0662 gated sequence walker

Hypothesis:
EXP141 proved `05FF/count33 -> ACK -> 0662/count33`, and a manually gated ACK to `0662/count33` stopped its retransmissions without an immediate next FC16 block or FC03 request in the supplied ~11 s continuation. EXP142 tests whether treating the now locally proven `0662/count33` stage as an automatic known ACK target reveals a delayed post-sync phase, subsequent FC16 stage, or FC03 read-side transition.

Only protocol-target variable changed versus EXP141:
- add `0x0662/count33` to the exact static ACK whitelist.

Known facts before testing:
- `0662/count33` was repeatedly observed with a stable payload;
- EXP141 locked it only after >=3 exact repetitions;
- operator explicitly armed it;
- the next exact `0662/count33` request received one standard FC16 ACK;
- retransmissions ceased immediately afterward;
- no immediate next FC16/FC03 event was visible in the supplied continuation.

Experimental behavior:
- 30 s passive baseline;
- exact known stages auto-ACKed during active phase, now including `0662/count33`;
- any later unknown FC16 shape still requires >=3 exact repetitions plus explicit HA ARM;
- FC03 is detection-only and never answered;
- real 0x0F responder activity, parser resync, or RX drops abort TX;
- full FC16 payloads remain logged;
- max 8 manually approved later stages.

Observation window:
- active window extended from 600 s to 900 s to give delayed post-0662 behavior more time to appear. This is an observation-window change only; no additional write target is introduced.

Current experiment: **EXP142 PREPARED, not yet run**.


---

## 2026-09-24 — EXP142 RUNNING / IMPORTANT NEGATIVE — post-0x0662 state is quiet across reboot

Hypothesis:
If `0662/count33` is merely another ACK-gated stage, promoting it to a known automatic ACK target should cause the controller to retransmit it after reboot and reveal a subsequent FC16 or FC03 phase.

Observed:
- EXP142 started normally and completed its 30 s passive baseline.
- During the entire baseline, `fc16Seen=0`: no slave-0x0F FC16 write request was observed at all.
- EXP142 entered active mode with:
  `baseline_clean=YES fc16Seen=0 known=0 unknown=0`.
- In the supplied log, active observation continues for ~61 s after the phase transition with:
  - no 0x0F FC16 request;
  - no 0x0F FC03 request;
  - no 0x0F response/ACK from another responder;
  - normal traffic from 0x02, 0x06, 0x0A and 0x1E;
  - parser resyncs = 0;
  - RX buffer drops = 0.
- Therefore EXP142 never had an opportunity to auto-ACK `0662/count33`; that request did not recur.

Strong conclusions:
1. The controller-side state reached after the successful EXP141 ACK of `0662/count33` persists across ESP reboot/firmware replacement.
2. The repeated controller->0x0F FC16 initialization/synchronization stream has stopped in this state.
3. EXP142's absence of 0x0F traffic is not a failure of the walker; it is the observed controller behavior after completing the known ACK chain.

Hypotheses:
- `0662/count33` is the terminal block of this controller->0x0F startup/snapshot synchronization sequence; or
- it is a phase boundary after which further 0x0F communication is event-driven, delayed, or initiated from the other side.

Unknowns:
- whether FC03 begins only after a specific external/Online-side action;
- whether the official Online module periodically initiates reads that our passive emulator is not currently producing;
- whether another handshake/address family is required after the FC16 snapshot completes.

Current status:
**EXP142 RUNNING / IMPORTANT NEGATIVE — post-0662 state remains quiet; no 0x0F FC16/FC03 activity observed in the supplied window.**

Smallest useful next experiment:
Do not keep extending passive wait time indefinitely. The next experiment should test one narrowly-scoped, evidence-based trigger for the post-sync read phase while remaining non-semantic and fail-closed.


---

## 2026-09-24 — EXP143 PREPARED — passive post-sync Heat Curve trigger probe

Hypothesis:
EXP142 showed that the post-`0662/count33` state is quiescent across reboot: no 0x0F FC16 or FC03 traffic appeared in the baseline or supplied active window. In the genuine Online capture, 0x0F FC03 reads of the settings block were present while the Online module was connected, and a Heat Curve 20->21->20 user action was part of that capture context. EXP143 therefore tests the smallest safe trigger hypothesis: a manual change of the already-proven Heat Curve setting may provoke post-sync 0x0F activity.

Experiment variable:
- manually change Heat Curve by exactly +1 on the Thermia user interface, observe, then restore the original value.
- No ESP-originated Modbus write or ACK is permitted.

Procedure:
1. START EXP143.
2. Wait for `READY_FOR_MANUAL_CHANGE` after the 30 s baseline.
3. Note the current Heat Curve value on the Thermia UI.
4. Change only Heat Curve to current+1.
5. Press `EXP143 MARK Heat Curve +1 Applied`.
6. Observe approximately 30 s.
7. Restore the exact original Heat Curve value.
8. Press `EXP143 MARK Heat Curve Restored`.
9. EXP143 observes a final 60 s and ends automatically.

Safety:
- ESP TX disabled for the experiment; DE forced LOW.
- no FC16 ACK;
- no FC03 response;
- no register-value injection;
- no slave-0x06 or room-sensor emulation;
- only the user's normal Thermia UI changes one known setting and restores it;
- parser resync/RX drop abort remains active.

Positive discriminator:
Any post-sync 0x0F FC16 or FC03 traffic appearing in temporal relation to the manual Heat Curve change/restore.

Negative:
No 0x0F activity through the +1 and restore observation windows.

Current experiment: **EXP143 PREPARED, not yet run**.


---

## 2026-09-24 — EXP143 COMPLETE / STRONG POSITIVE — manual Heat Curve change re-triggers 0x0F FC16 sync at 0x03E8

Hypothesis:
After the post-`0662/count33` quiet state, a normal manual Heat Curve change on the Thermia UI may re-activate 0x0F communication.

Observed:
- EXP143 was strictly passive from the ESP side:
  - no ACKs;
  - no FC03 responses;
  - no Modbus writes;
  - DE remained LOW.
- 30 s baseline completed with no 0x0F traffic:
  - `fc16=0`
  - `fc03Req=0`.
- After the user changed Heat Curve by +1 on the Thermia UI, the controller began transmitting:
  - `0x0F FC16 @ 0x03E8 count14`.
- First observed triggered frame:
  `03E8/count14 payload=0024 0014 0028 0001 0000 0000 0014 0014 0002 0028 001E 0001 0016 0002`
- Home Assistant simultaneously reported `Heating Curve = 36`.
- Because EXP143 intentionally did not ACK, the controller repeatedly retransmitted the exact `03E8/count14` request.
- After the user restored Heat Curve to the original value, the first payload word changed from:
  - `0x0024` = 36
  - to `0x0023` = 35,
  while the other 13 words remained unchanged in the shown frames.
- Home Assistant simultaneously reported `Heating Curve = 35`.
- The controller then continued retransmitting `03E8/count14` with first word `0x0023`, again because no ACK was sent.
- Final summary:
  `reason=COMPLETE_POST_RESTORE_WINDOW duration_ms=152709 fc16=103 fc03Req=0 fc03Resp=0 fc16Ack=0 plusMarkMs=45997 restoreMarkMs=92482 resyncDelta=0 dropDelta=0 DE_LOW`.

Strong conclusions:
1. A normal manual Heat Curve change on the Thermia UI re-activates the otherwise quiescent controller->0x0F FC16 synchronization path.
2. The reactivated path starts at the already-proven `03E8/count14` block.
3. In the controller->0x0F FC16 `03E8/count14` payload, the first 16-bit word tracks the actual Heat Curve setting directly in this experiment:
   - Heat Curve 36 -> first word `0x0024`
   - Heat Curve 35 -> first word `0x0023`.
4. The controller retransmits `03E8/count14` until ACKed, confirming again that the event-triggered sync path is ACK-gated.
5. The post-0662 quiet state is therefore not permanent. A settings change can restart the synchronization sequence.
6. No FC03 request was observed because EXP143 intentionally never ACKed the first restarted FC16 stage.

Important correction/refinement:
The genuine Online capture's 0x0F FC03 read-side values must not be assumed to be numerically identical to the controller->0x0F FC16 write-side payload representation. EXP143 locally proves the FC16 write-side first word of block 03E8 directly mirrors the Heat Curve value in this run.

Current experiment:
**EXP143 COMPLETE / STRONG POSITIVE.**

Smallest useful next experiment:
EXP144 should repeat the same manual Heat Curve +1 trigger, but automatically ACK only the already locally proven FC16 sequence shapes, starting with `03E8/count14`, and stop on the first new FC16 shape or first FC03 request after the triggered sync completes. Restore the Heat Curve after observation. This tests whether a user-setting-triggered sync reaches a post-sync phase different from the earlier startup/recovery sequence.


---

## 2026-09-24 — EXP144 PREPARED — Heat Curve-triggered known-sequence progression

Hypothesis:
EXP143 proved that a manual Heat Curve change restarts the otherwise quiescent controller->0x0F sync path at `03E8/count14`. EXP144 tests whether ACKing only already locally proven FC16 shapes during that event-triggered sync reaches either:
1. a previously unseen FC16 stage; or
2. the 0x0F FC03 read-side phase.

Only experimental change versus EXP143:
- after the manual Heat Curve +1 trigger, ACK exact already-proven FC16 shapes instead of remaining fully passive.

Known ACK shapes:
- `03E8/14`
- `0410/22`
- `042E/15`
- `0442/13`
- `04A6/13`
- `04BA/22`
- `05FF/33`
- `0662/33`
- `085F/5`

Procedure:
1. START EXP144.
2. Wait for `READY_FOR_MANUAL_CHANGE`.
3. Note the current Heat Curve.
4. Change only Heat Curve to current+1 on the Thermia UI.
5. Press `MARK Heat Curve +1 Applied`.
6. EXP144 waits for the triggered `03E8/count14` and then ACKs only exact known shapes.
7. EXP144 stops immediately on the first unknown FC16 shape or first FC03 request; neither is answered.
8. Restore the original Heat Curve manually and press `MARK Heat Curve Restored` if the experiment is still active / for cleanup logging.

Safety:
- no semantic register values are generated or injected;
- only standard FC16 ACKs to exact locally proven shapes;
- no FC03 response;
- no unknown FC16 ACK;
- baseline must be free of pre-existing 0x0F activity;
- abort on real 0x0F responder, parser resync, or RX drops;
- SG production functionality unchanged.

Current experiment: **EXP144 PREPARED, not yet run**.


---

## 2026-09-24 — EXP144 ABORTED / PROCEDURAL — baseline already contained pending 0x03E8/count14

Hypothesis:
After a manual Heat Curve +1 trigger, ACKing only already-proven FC16 shapes should walk the event-triggered 0x0F sequence toward either a new FC16 stage or FC03 read-side activity.

Observed:
- EXP144 started after an ESP reboot.
- Immediately during the passive baseline, slave 0x0F was already repeatedly receiving:
  `FC16 @ 0x03E8 count14`
  with payload first word `0x0023` (35), matching the restored Heat Curve state from EXP143.
- 29 such FC16 requests were observed during the 30 s baseline.
- No FC03 request/response and no real 0x0F FC16 ACK was observed.
- Parser resync and RX-drop counters remained zero.
- EXP144 correctly aborted at baseline completion with:
  `reason=ABORT_BASELINE_0F_ACTIVITY fc16=29 fc03Req=0 fc03Resp=0 fc16Ack=0 DE_LOW`.

Strong conclusions:
1. EXP144 did NOT test its intended hypothesis because the required quiet baseline condition was not met.
2. The pending event-triggered `03E8/count14` retry state created during EXP143 persisted across ESP reboot/firmware replacement.
3. The controller remains blocked waiting for an ACK to the event-triggered `03E8/count14` stage.
4. This persistence mirrors the controller-side ACK-gated behavior already seen in the startup/snapshot sequence.

Important interpretation:
This is a procedural abort, not a negative result for the event-triggered sequence hypothesis.

Smallest useful next experiment:
EXP145 should resume the existing pending event-triggered sequence rather than require a quiet baseline or make another Heat Curve change.
- Baseline may contain only exact `03E8/count14`.
- Any other 0x0F FC16 shape, FC03 activity, or real responder during baseline aborts.
- After baseline, ACK the pending `03E8/count14` and then ACK only already-proven sequence shapes.
- Stop without answering on the first unknown FC16 shape or first FC03 request.
- No additional Heat Curve change is required.

Current experiment:
**EXP144 ABORTED / PROCEDURAL — hypothesis not tested.**


### EXP144 repeat attempts 2 and 3 — same procedural abort reproduced

Additional observation:
Two further EXP144 start attempts reproduced the same baseline condition:
- repeated `0x0F FC16 @ 0x03E8 count14`;
- payload first word remained `0x0023` (Heat Curve 35);
- each run again reached 29 FC16 requests during the 30 s baseline;
- no FC03 request/response;
- no real 0x0F FC16 ACK;
- no parser resync or RX-drop issue;
- each run aborted with `ABORT_BASELINE_0F_ACTIVITY`.

Conclusion:
The pending event-triggered `03E8/count14` state is stable and persistent, not transient. Repeating EXP144 without ACKing that outstanding stage cannot advance the experiment.

Next experiment remains EXP145: accept exact `03E8/count14` as the expected baseline-pending state and ACK it after a short confirmation window, then ACK only already-proven shapes and stop on the first unknown FC16 or first FC03 request.


---

## 2026-09-24 — EXP145 PREPARED — pending 0x03E8 sync to FC03 transition probe

Hypothesis:
EXP143 created an event-triggered `0x0F FC16 @ 03E8/count14` transaction and EXP144 attempts proved that this unacknowledged transaction persists across repeated experiment starts. EXP145 tests whether completing this already-pending controller->0x0F synchronization with only locally proven ACKs is sufficient to cause the higher-value post-sync transition: an `0x0F FC03` request or other new post-sync traffic.

Important scope correction:
EXP145 is not another semantic Heat Curve test and does not change any Thermia setting. It resumes the exact outstanding transport state created by EXP143.

Baseline:
- 10 s passive confirmation;
- at least 3 `03E8/count14` requests required;
- `03E8/count14` is the only allowed 0x0F FC16 baseline shape;
- any different 0x0F FC16, any 0x0F FC03, or any real 0x0F responder aborts.

Active sequence:
ACK only exact locally proven shapes:
`03E8/14`, `0410/22`, `042E/15`, `0442/13`, `04A6/13`, `04BA/22`, `05FF/33`, `0662/33`, `085F/5`.

Stop conditions:
- first unknown 0x0F FC16 -> log, no ACK, stop;
- first 0x0F FC03 request -> log, no response, stop;
- parser resync/RX drop -> abort.

Post-0662:
After a successful ACK of `0662/count33`, EXP145 disables further experimental TX and observes passively for 120 s. It logs:
- any 0x0F FC03 request;
- any 0x0F FC16 reappearance/new post-sync block;
- A5/A4 FC03 requests as passive discriminators because those were present in the genuine Online capture.

Interpretation targets:
- FC03 appears -> strong evidence that completing the controller snapshot is sufficient for the read-side transition.
- new FC16 appears -> identify the true next transport stage.
- 120 s complete silence after 0662 -> strong evidence that snapshot completion alone is insufficient and an Online-side action/handshake is missing.

Current experiment: **EXP145 PREPARED, not yet run**.


---

## 2026-09-24 — EXP145 COMPLETE / IMPORTANT NEGATIVE — event-triggered 03E8 update ends after one ACK

Hypothesis:
Completing the persistent event-triggered `0x0F FC16 @ 03E8/count14` transaction with only proven ACKs might continue through the known snapshot chain and reveal either a new FC16 stage or an `0x0F FC03` read-side transition.

Observed:
- 10 s baseline contained exactly the expected pending `03E8/count14` request.
- 10 repeats were observed; payload first word remained `0x0023` (Heat Curve 35).
- Baseline passed:
  `EXP145 PHASE ACK_KNOWN_SEQUENCE baseline_ok=YES baseline03E8=10`.
- The next exact `03E8/count14` request was ACKed once:
  `EXP145 ACK_TX n=1 start=03E8 count=14`.
- After that ACK, the repeated `03E8/count14` traffic stopped immediately.
- In the remainder of the supplied log (at least ~69 s after the ACK):
  - no `0410/count22`;
  - no other `0x0F FC16`;
  - no `0x0F FC03`;
  - no A5/A4 FC03;
  - no real `0x0F` responder;
  - normal bus traffic continued;
  - parser resyncs and RX drops remained zero.

Strong conclusions:
1. The event-triggered Heat Curve synchronization is NOT the same multi-block startup/snapshot sequence observed in EXP137–140.
2. For this event-triggered update, ACKing `03E8/count14` is sufficient to clear the outstanding retry state.
3. The controller does not automatically proceed from this event-triggered `03E8/count14` ACK to `0410/count22` or the rest of the known startup chain.
4. No `0x0F FC03` transition is caused merely by ACKing the event-triggered `03E8/count14`.
5. The earlier assumption that a user-setting-triggered sync might replay the entire known FC16 snapshot chain is disproven.

Hypotheses:
- Runtime setting changes are sent as sparse/event-specific FC16 block updates, while the longer 03E8→...→0662 chain is a different initialization/snapshot mode.
- FC03 read-side traffic likely requires a separate Online-side master/session action rather than following automatically from controller-originated FC16 update acknowledgement.

Unknowns:
- exact trigger for the genuine Online `0x0F FC03` reads;
- whether A5 activity is prerequisite, consequence, or parallel traffic;
- whether a specific Online-side poll/session frame must be generated before the controller/master begins FC03 reads.

Current experiment:
**EXP145 COMPLETE / IMPORTANT NEGATIVE.**

Smallest useful next experiment:
Stop extending controller-originated FC16 ACK chains. Next experiment should target the missing Online-side read trigger using evidence from the genuine Online capture, preferably reproducing only the minimal preceding A5/0x0F interaction pattern necessary to test whether FC03 begins, without writing semantic register values.


---

## 2026-09-24 — EXP146 PREPARED — direct Online-style 0x0F FC03 read probe

Hypothesis:
The genuine Online capture may contain traffic from the Online-side master itself, rather than FC03 requests generated automatically by the heat-pump controller. If logical slave `0x0F` is a shared mailbox/slave, sending one exact FC03 request copied from the genuine Online capture should elicit the same 0x0F response locally.

Why this experiment now:
EXP145 proved that ACKing a runtime controller->0x0F FC16 update does not cause FC03 traffic. This weakens the assumption that FC03 is a controller-side continuation and strengthens the alternative that the Online module actively issues those reads.

Exact test request from genuine Online capture:
`0F 03 07 08 00 06 44 50`
= slave `0x0F`, FC03, start `0x0708`, count 6.

In the genuine Online capture this request received a 12-byte data response from 0x0F and appeared immediately before the settings read `0F 03 03E8 000D`.

Experimental variable:
One exact FC03 read request to `0x0F:0708`, count 6.

Safety:
- read-only semantic operation;
- no register write;
- no FC16;
- no ACK emulation;
- no room-sensor or 0x06 emulation;
- 10 s passive baseline must contain no 0x0F activity;
- exactly one request is transmitted;
- 2 s response window;
- abort on parser resync/RX drops;
- DE LOW outside the single request.

Positive:
A valid 0x0F FC03 response with byte-count 12.

Negative:
No response within 2 s.

Interpretation:
A positive result would strongly support that ESP can occupy the Online-side master role and directly read the shared 0x0F mailbox. It would materially redirect subsequent work toward reproducing the genuine Online FC03/FC16 master operations rather than waiting for the controller to generate FC03 itself.

Current experiment: **EXP146 PREPARED, not yet run**.


---

## 2026-09-24 — EXP146 INVALID / PROCEDURAL — response window bug, hypothesis not tested

Hypothesis:
One exact genuine-Online read request (`0F 03 0708 0006`) sent by the ESP may elicit the same slave-0x0F FC03 response seen in the genuine Online capture.

Observed:
- Two runs reached the intended clean 10 s baseline and transmitted exactly one request:
  `0F 03 07 08 00 06 44 50`.
- In both runs the log emitted `NO_RESPONSE_2S` only ~8–10 ms after `FC03_TX`, not after 2 seconds.
- Cause: the interval lambda computes `phase_ms` before changing phase 1 -> phase 2. After TX, the same lambda continues with the stale ~10 s `phase_ms`, so the phase-2 timeout condition (`>=2000 ms`) fires immediately.
- Therefore the experiment disabled itself essentially immediately after transmitting and did not provide the intended 2 s response-observation window.
- First run stayed parser-clean in the shown post-TX period.
- Second run showed two parser CRC resync warnings ~60 ms after TX (`0x1E 0x04`, `0x02 0x8C`). These occurred after the experiment had already incorrectly ended and cannot by themselves establish whether the FC03 request caused bus corruption.

Strong conclusions:
1. EXP146 does not establish "no response".
2. The Online-side-master hypothesis remains untested.
3. The YAML contains a timing/state-transition bug and must not be reused unchanged.

Hypotheses:
- A valid 0x0F response may still have arrived later than the ~10 ms window but would not have been classified by EXP146 because the experiment had already stopped.
- The second-run CRC resyncs may be unrelated normal parser behavior, self-echo/collision side effect, or timing interference; evidence is insufficient.

Unknowns:
- Whether `0x0F` answers the exact `0708/count6` request locally.
- Whether a larger idle-gap/collision guard is required before sending.
- Whether TX self-echo needs explicit handling.

Next:
EXP147 should be the corrected repeat of the exact same protocol test. Change only timing mechanics:
- after TX set phase 2 and return from that interval invocation;
- start a fresh response timer from the actual TX timestamp;
- observe for a true 2 s window;
- optionally capture raw bytes around TX/response;
- keep the exact same read request and all other safety constraints.

Current experiment:
**EXP146 INVALID / PROCEDURAL — hypothesis not tested.**


---

## 2026-09-24 — EXP147 PREPARED — corrected direct Online-style 0x0F FC03 0708 read probe

Hypothesis:
Same as EXP146: if logical slave `0x0F` is directly readable by the Online-side master, one exact genuine-Online FC03 request to `0x0708/count6` may elicit the same 12-byte-data response locally.

Only experimental change versus EXP146:
- fix the response-window timing bug.
- The request, address, count, baseline, collision guard, safety rules, and response criterion are unchanged.

Exact request remains:
`0F 03 07 08 00 06 44 50`

Timing correction:
- EXP147 stores a dedicated `tx_ms` timestamp immediately after TX;
- phase 2 begins from that exact timestamp;
- the interval handler returns immediately after TX;
- timeout is evaluated as `now - tx_ms >= 2000 ms`.

This prevents the stale phase-1 elapsed time from prematurely ending the experiment.

Safety:
- read-only semantic operation;
- one request only;
- no FC16;
- no ACK emulation;
- no register write;
- no 0x06 or room-sensor emulation;
- baseline must be free of 0x0F traffic;
- abort on parser resync/RX drops;
- DE LOW outside the single request.

Positive:
valid `0x0F FC03` response with byte-count 12.

Negative:
no matching response during a real 2 s post-TX window.

Current experiment: **EXP147 PREPARED, not yet run**.


---

## 2026-09-24 — EXP147 COMPLETE / NEGATIVE — direct Online-style FC03 read receives no local 0x0F response

Hypothesis:
One exact genuine-Online FC03 request to logical slave `0x0F`, start `0x0708`, count 6, may elicit the same response locally if the ESP can simply assume the Online-side master role.

Observed facts:
- EXP147 baseline completed without logged 0x0F activity.
- At 23:38:38.137 the ESP transmitted exactly:
  `0F 03 07 08 00 06 44 50`.
- The next experiment summary occurred at 23:38:40.375, ~2.238 s after TX.
- No matching `0x0F FC03` response was logged in that interval.
- No `OTHER_0F_ACTIVITY` was logged in the response window.
- Normal bus traffic continued during the response window.
- A parser resync count of 1 appeared later, around 23:38:46.921, several seconds after EXP147 had already ended.
- RX buffer drops shown later remained 0.

Logging defect:
The `NO_RESPONSE_TRUE_2S` summary format string contains one more `%u` placeholder than supplied arguments. Therefore printed fields from `responseWindowMs` onward are shifted/corrupted:
- printed `responseWindowMs=1`, `tx=0`, and huge `dropDelta` are invalid summary formatting artefacts;
- the actual TX is independently proven by the preceding `EXP147 FC03_TX` line;
- the real response-window duration is independently established from log timestamps (~2238 ms).

Strong conclusions:
1. EXP147 successfully provided a real >2 s observation window after the exact FC03 request.
2. No decodable local `0x0F` response was observed to `0708/count6`.
3. Therefore a bare Online-style FC03 request is insufficient in the current local controller state.
4. The simplest model "ESP can directly become the Online master and read 0x0F with no prior session/presence state" is weakened.

Hypotheses:
- 0x0F may only be instantiated/responding when the genuine Online/Connect session is present.
- A5/A4 activity, another logical endpoint, or an initialization/session step may create or expose the 0x0F mailbox.
- The genuine Online capture may contain multiple logical devices/master roles, so copying one FC03 request outside that topology is not sufficient.

Unknowns:
- whether A5 is a prerequisite, side effect, or independent device;
- what exact event makes 0x0F answer FC03 in the genuine Online environment;
- whether the 0x0F responder lives physically in the Online/DCM hardware rather than in the heat-pump controller.

Next direction:
Do not change FC03 address yet. First reconstruct the genuine Online topology more precisely. The highest-value next experiment should target the repeatedly observed A5 polling/response pattern or establish which side physically generates the 0x0F FC03 response before any further semantic write attempt.

Current experiment:
**EXP147 COMPLETE / NEGATIVE (with summary-format logging defect).**


### EXP147 second run — negative reproduced

A second EXP147 run reproduced the same protocol result:
- START at 23:39:03.305;
- exact FC03 request TX at 23:39:13.389:
  `0F 03 07 08 00 06 44 50`;
- terminal summary at 23:39:15.632, giving ~2.243 s actual post-TX observation;
- no matching `0x0F FC03` response;
- no logged other 0x0F activity during the response window.

The same summary-format argument mismatch remains, so printed `responseWindowMs`, `tx`, and later numeric fields are not trustworthy. Timing and TX are instead established from the timestamped log lines.

Strengthened conclusion:
The negative EXP147 result is reproducible across two independent runs. A bare direct FC03 read to `0x0F:0708/count6` is therefore unlikely to be sufficient in the local no-Online-module topology.


---

## 2026-09-24 — EXP148 PREPARED — passive Online topology and timing profiler

Hypothesis:
The genuine Online environment contains additional logical topology/session activity — especially A5/A4 — that is absent locally and may explain why direct 0x0F FC03 reads receive no response.

Experimental variable:
Observation only. No bus value is changed and no experimental frame is transmitted.

Duration:
300 s.

Captured event families:
- A5 FC03 request/response;
- A4 FC03 request/response;
- 0x0F FC03 request/response;
- 0x0F FC16 write/ACK;
- 0x06 FC17 request/response.

Timing profiler:
For each relevant event, EXP148 logs:
- elapsed experiment time;
- slave;
- function code;
- event kind;
- gap to the previous relevant event;
- previous relevant slave/function.

Gap counters:
- <=20 ms;
- 21–100 ms;
- 101–500 ms;
- >500 ms.

Safety:
- strictly passive;
- DE continuously forced LOW;
- no FC03 request;
- no FC16;
- no ACK;
- no 0x06 response;
- no room-sensor emulation;
- abort on parser resync or RX drops.

Purpose:
This is a topology discriminator, not another register probe. If A5/A4 remain entirely absent locally while normal 0x06/0x02/0x1E traffic continues, that materially supports the model that A5/A4 belong to genuine Online/DCM topology/session state. If they do appear naturally, their timing relationship to 0x0F traffic becomes the next controlled target.

Current experiment: **EXP148 PREPARED, not yet run**.


---

## 2026-09-24 — EXP148 COMPLETE / STRONG TOPOLOGY NEGATIVE

Hypothesis:
The genuine Online environment contains additional logical topology/session activity — especially A5/A4 — that is absent locally and may explain why direct 0x0F FC03 reads receive no response.

Final summary:
- duration_ms=300092
- A5req=0
- A5resp=0
- A4req=0
- A4resp=0
- 0F03req=0
- 0F03resp=0
- 0F16write=280
- 0F16ack=0
- 06req=69
- 06resp=0
- gaps_le20=0
- gaps_21_100=0
- gaps_101_500=69
- gaps_gt500=279
- resyncDelta=0
- dropDelta=0
- DE_LOW

Observed:
1. Full 300 s passive run completed cleanly.
2. No A5 or A4 FC03 activity appeared at all.
3. No 0x0F FC03 request/response appeared.
4. No 0x0F FC16 ACK appeared.
5. 280 controller-originated 0x0F FC16 writes were observed; all inspected writes were the recurring `04A6/count13` pending transaction.
6. 69 0x06 FC17 requests were observed.
7. All 69 short cross-endpoint timing events fell in the 101–500 ms bucket, matching the repeatedly observed ~253–255 ms delay from each 0x06 FC17 request to the following 0x0F FC16 `04A6/count13`.
8. Parser resync and RX drop deltas remained zero; experiment stayed passive with DE LOW.

Strong conclusions:
1. A5/A4 activity is not part of the normal local no-Online-module bus topology over this 300 s window.
2. The simplest model in which A5/A4 should naturally appear locally is rejected.
3. Local 0x0F FC16 activity can remain substantial without any local 0x0F FC03 activity.
4. The fixed ~254 ms relationship between 0x06 FC17 polling and the following 0x0F `04A6/count13` write is now highly repeatable and likely reflects a common controller scheduler/cycle; semantic causation is still not proven.
5. The genuine Online environment therefore contains additional active topology/session behavior not reproduced by the local controller alone.

Hypotheses:
- A5/A4 may be logical endpoints implemented by the genuine Online/DCM hardware.
- 0x0F FC03 responsiveness may depend on the presence/state of that external Online/DCM component rather than just on a master request.
- The persistent 04A6 transaction is an independent controller->0x0F synchronization/mailbox item and is not equivalent to Online read-side availability.

Unknowns:
- Which physical side owns the 0x0F FC03 responder in the genuine capture.
- Whether A5 is the Online/DCM module itself, a companion endpoint, or another logical service.
- What minimal non-semantic presence/session exchange makes 0x0F readable.

Decision:
Do not probe more arbitrary FC03 addresses. The next experiment should target ownership/presence: reproduce only the smallest evidenced A5/Online-side interaction from the genuine capture, or otherwise discriminate whether the genuine 0x0F FC03 response is physically generated by the Online module.

Current experiment: **EXP148 COMPLETE / STRONG TOPOLOGY NEGATIVE.**


---

## 2026-09-24 — EXP149 PREPARED — A5 0x0000 ownership probe

Hypothesis:
Address `0xA5` may be a logical endpoint implemented by the genuine Online/DCM hardware rather than by the heat-pump controller. If A5 exists locally without Online hardware, one exact read copied from the genuine Online capture should receive the same response. If it does not, that strongly supports external ownership/presence.

Evidence for the exact request:
The genuine Online capture repeatedly shows:
`A5 03 00 00 00 12 DC E3`
followed by an A5 FC03 response with byte count `0x24` (36 data bytes).

Experimental variable:
Exactly one read-only FC03 request to A5, start `0x0000`, count 18.

Sequence:
1. 5 s passive local baseline;
2. require no spontaneous A5 traffic;
3. wait for >=20 ms idle bus gap;
4. transmit exactly once:
   `A5 03 00 00 00 12 DC E3`;
5. observe for a true 2 s post-TX window;
6. stop immediately on a valid A5 36-byte-data response.

Safety:
- FC03 read only;
- exactly one TX;
- no FC16;
- no ACK emulation;
- no semantic register write;
- no 0x06 or room-sensor emulation;
- abort on parser resync/RX drop;
- DE LOW outside the single request.

Positive:
A5 FC03 response, byte count `0x24`, 41-byte total frame.

Negative:
No A5 response within the real 2 s window.

Interpretation:
- positive: A5 is reachable locally and is not dependent on the physical genuine Online module being present;
- negative: together with EXP148's 300 s absence of A5, strongly supports A5 being owned/created by the missing Online/DCM topology.

Current experiment: **EXP149 PREPARED, not yet run**.


---

## 2026-09-24 — EXP149 COMPLETE / NEGATIVE — A5 does not answer locally

Hypothesis:
Address `0xA5` may be a logical endpoint implemented by the genuine Online/DCM hardware rather than by the heat-pump controller. If A5 exists locally without Online hardware, one exact read copied from the genuine Online capture should receive the same response.

Observed facts:
- EXP149 started at 23:55:29.113.
- After the 5 s passive baseline, the ESP transmitted exactly once at 23:55:34.138:
  `A5 03 00 00 00 12 DC E3`
  (FC03, start 0x0000, count 18).
- A true 2.016 s post-TX response window completed at 23:55:36.158.
- Summary:
  `NO_A5_RESPONSE_2S duration_ms=7035 responseWindowMs=2016 tx=1 txRefused=0 A5reqSeen=0 A5respSeen=0 otherA5=0 0F03=0 resyncDelta=0 dropDelta=0 DE_LOW`
- No A5 response appeared.
- No other A5 activity appeared.
- No 0x0F FC03 appeared.
- Parser and RX remained clean.
- Normal controller/outdoor/room/0x06 traffic continued.

Strong conclusions:
1. The local no-Online topology does not answer the exact genuine-Online A5 FC03 read.
2. Combined with EXP148's 300 s complete absence of spontaneous A5/A4 traffic, this strongly supports the model that A5 is created/owned by the genuine Online/DCM-side topology rather than the heat-pump controller alone.
3. A5 is therefore not a useful direct local read target unless its missing owner/presence layer is emulated.
4. The negative is transport-clean and not explained by parser drops or collision evidence in this run.

Hypotheses:
- A5 may be the Online/DCM module itself or a logical endpoint hosted by it.
- A4 may be a related/fallback logical endpoint of the same external hardware.
- The genuine 0x0F FC03 responder may likewise be hosted or enabled by the Online/DCM module, not inherently by the controller.

Unknowns:
- Exact physical ownership of 0x0F.
- Whether A4 differs functionally from A5 or is another address/state of the same device.
- Which smallest non-semantic presence/session exchange causes the controller to expose/accept Online semantics.

Comparison:
- EXP147: exact genuine 0x0F FC03 read received no response locally.
- EXP148: no A5/A4 or 0x0F FC03 appeared spontaneously over 300 s.
- EXP149: exact genuine A5 FC03 read also received no response.
Together these three experiments strongly reject the simple model that genuine Online logical endpoints are directly addressable on the local no-Online bus without additional external/session state.

Decision:
Do not probe arbitrary additional A5/0x0F addresses. Next work should discriminate physical ownership/presence using the genuine capture sequence around A5/A4 and 0x0F, or test the smallest evidenced non-semantic A5/A4 presence transition only if its exact frame shape is known.

Current experiment:
**EXP149 COMPLETE / NEGATIVE.**


---

## 2026-09-24 — EXP150 PREPARED — staged Online/DCM bootstrap role-emulation harness

Hypothesis:
A sustained, syntactically correct slave-side presence on `0x0F` may be the missing prerequisite that enables the genuine Online/DCM read-side/discovery behaviour.

Efficiency objective:
EXP150 combines several dependent discriminators in one gated run instead of requiring a firmware flash for each step. Each later phase is entered only after the earlier phase remains coherent.

Controlled staged sequence:
1. 10 s passive baseline.
2. 30 s: ACK only a strict whitelist of already observed/proven `0x0F FC16` write shapes.
3. 30 s: continue the same ACK behaviour and additionally arm exact responses for the three genuine A5 discovery reads:
   - `A5 03 0000 0012`
   - `A5 03 0023 0001`
   - `A5 03 002E 000A`
   using byte-identical captured A5 responses.
4. If no spontaneous read-side progress occurs, send one exact read-only genuine request:
   `0F 03 0708 0006 4450`.
5. Only if phase 4 receives the expected 12-byte response, send the second exact genuine read-only request:
   `0F 03 03E8 000D 0551`.
6. Stop with an explicit summary.

Important known effect:
ACKing `0x0F FC16` is not semantically inert: EXP137-141 proved that ACKs advance the controller's ACK-gated synchronization/transfer state machine. This is the intentional variable in EXP150. No register payload is changed by ESP.

0x0F FC16 ACK whitelist:
- 03E8/14
- 0410/22
- 042E/15
- 04A6/13
- 04BA/22
- 05FF/33
- 0662/33
- 07D0/19
- 07E4/17
- 07F8/17
- 080C/18
- 0820/18
- 0834/18
- 0848/23
- 0864/4
- 0870/17
- 0884/60

Safety:
- no semantic register value is invented or transmitted;
- no FC16 request is generated by ESP;
- A5 responses are byte-identical to the genuine capture and only for exact known request shapes;
- 0x0F active probes are FC03 read-only and copied exactly from genuine traffic;
- second FC03 probe is conditional on a valid first response;
- unknown A5 request or unknown 0x0F FC16 shape causes immediate abort/no response;
- parser resync/RX drop abort;
- DE LOW outside exact response/probe windows;
- no room-sensor emulation.

Current experiment:
**EXP150 PREPARED, not yet run.**


---

## 2026-09-25 — EXP150 COMPLETE / NEGATIVE — ACK-side presence does not bootstrap read-side service

Hypothesis:
A sustained, syntactically correct slave-side presence on `0x0F` may be the missing prerequisite that enables genuine Online/DCM read-side/discovery behaviour.

Observed facts:
- EXP150 entered phase 1 normally and passively observed repeated pending `0x0F FC16 04A6/count13`.
- Phase 2 began after the planned 10 s baseline.
- The ESP ACKed `04A6/count13` once, then ACKed `0662/count33` once.
- No further known `0x0F FC16` blocks appeared during the remainder of the 30 s ACK-only phase.
- Phase 3 armed the exact captured A5 responder for 30 s, but no A5 request appeared; therefore no A5 response was transmitted.
- No A4 traffic appeared.
- No spontaneous `0x0F FC03` request or response appeared.
- Phase 4 transmitted exactly one genuine read-only request:
  `0F 03 0708 0006 4450`.
- A true 2.015 s response window elapsed without a `0x0F` FC03 response.
- Final summary:
  `NO_0F0708_RESPONSE_AFTER_BOOTSTRAP duration_ms=72068 ack=2 ackRefused=0 A5req=0 A5resp=0 A4=0 0F03req=0 0F03resp=0 responseWindowMs=2015 resyncDelta=0 dropDelta=0 DE_LOW`.
- Bus traffic remained otherwise healthy; parser resync and RX drops stayed at zero.

Strong conclusions:
1. ACKing the pending known `0x0F FC16` transfers is not sufficient to bootstrap the genuine Online/DCM read-side service.
2. ACK-side presence also does not trigger spontaneous A5/A4 discovery in the observed window.
3. Even after clearing the currently pending controller-to-0x0F transfers (`04A6`, then `0662`), the exact genuine `0x0F 0708/count6` read remains unanswered.
4. The simplest model "controller only needs an ACK-capable 0x0F slave before it exposes FC03 read service" is rejected.
5. EXP150 strengthens the architectural model that the FC03 responder and A5/A4 discovery side are likely owned or enabled by the missing external Online/DCM component, or require an additional presence/session channel not exercised here.

Hypotheses:
- The genuine `0x0F` FC03 responder may be implemented by the Online/DCM hardware rather than the heat-pump controller.
- The missing bootstrap may require the `0x06` accessory side to be present simultaneously with the `0x0F` mailbox side.
- A5/A4 may be a separate discovery/service endpoint of the same external module rather than something controller-triggered.

Unknowns:
- Exact physical owner of `0x0F`.
- Whether a simultaneous `0x06` + `0x0F` role is necessary.
- Whether A5/A4 is polled by another physical master not represented in the local no-Online topology.
- Why the controller progressed from `04A6/count13` directly to `0662/count33` in this persisted state rather than replaying the full earlier initialization chain.

Comparison:
- EXP147: direct `0x0F 0708/count6` read unanswered.
- EXP148: A5/A4 and `0x0F FC03` absent for 300 s while `0x0F FC16` remained active.
- EXP149: direct exact A5 read unanswered.
- EXP150: even after controlled ACK-side `0x0F` presence and clearing two pending known FC16 transfers, A5/A4 remain absent and the exact `0x0F 0708/count6` read is still unanswered.

Decision:
Do not spend more experiments on ACK-only 0x0F presence or arbitrary FC03 reads. The highest-value next direction is combined role emulation: reproduce the known-good `0x06` accessory presence together with the `0x0F` ACK/mailbox side in one harness, while still withholding semantic writes. This tests whether the missing prerequisite is simultaneous multi-endpoint device presence.

Current experiment:
**EXP150 COMPLETE / NEGATIVE.**


---

## 2026-09-25 — EXP151 PREPARED — combined 0x06 + 0x0F role-emulation harness

Hypothesis:
The missing genuine Online/DCM bootstrap may require simultaneous presence of both known roles:
1. the `0x06` accessory responder; and
2. the `0x0F` ACK/mailbox side.

EXP150 showed that the 0x0F ACK role alone is insufficient.

Experimental variable:
Simultaneous role presence. No new semantic setting target is introduced.

Phase 1:
10 s passive baseline.

Phase 2:
60 s simultaneous:
- exact known `0x06 FC17` responder for read `AFC8..AFD3` / write `AFDC..AFE0`;
- response image:
  `00FF,0001,0000,0001,0000,0000,0000,0000,0000,0000,0000,0000`;
- known `0x0F FC16` ACK service;
- exact genuine A5 discovery responder if A5 requests appear;
- A4 and 0x0F FC03 observed passively.

The 0x06 image is historical REQ-low transport presence already exercised repeatedly without semantic settings mutation. It intentionally changes only the accessory-presence role and polling cadence.

Phase 3:
After 60 s combined presence, if no spontaneous read-side result has answered the question, send exactly one read-only genuine request:
`0F 03 0708 0006 4450`.

Phase 4:
Only if the 0708 response succeeds, send:
`0F 03 03E8 000D 0551`.

Safety:
- no AFCA=03E8 REQ strobe;
- no semantic setting payload invented;
- no FC16 request generated by ESP;
- 0x06 response only for exact known poll shape;
- 0x0F ACK only for strict known whitelist, now including locally observed `085F/count5`;
- A5 responses only for exact genuine captured reads;
- unknown 0x06/A5/0x0F shape aborts;
- parser/drop error aborts;
- no room-sensor emulation;
- DE LOW outside exact response/probe windows.

Current experiment:
**EXP151 PREPARED, not yet run.**


---

## 2026-09-25 — EXP151 COMPLETE / NEGATIVE — combined 0x06 + 0x0F presence still does not enable read-side service

Hypothesis:
The missing genuine Online/DCM bootstrap may require simultaneous presence of both known roles:
1. the `0x06` accessory responder; and
2. the `0x0F` ACK/mailbox side.

Observed facts:
- EXP151 started cleanly.
- Passive baseline observed 2 normal `0x06` polls with no response.
- Phase 2 began after 10 s.
- The ESP then answered the exact known `0x06 FC17` poll continuously with the REQ-low image:
  `00FF,0001,0000,0001,0,0,0,0,0,0,0,0`.
- 60 `0x06` requests were observed in total; 58 were answered after phase 2 began; `06refused=0`.
- The expected fast `0x06` cadence reappeared (~0.7 / ~1.4 s pattern), confirming transport presence.
- No `0x0F FC16` write occurred during the active combined-role window, so no 0x0F ACK was actually transmitted (`ack=0`, `ackRefused=0`).
- No A5 request appeared; no A5 response was sent.
- No A4 activity appeared.
- No spontaneous `0x0F FC03` request or response appeared.
- After 60 s combined-role presence, phase 3 sent exactly one genuine read-only request:
  `0F 03 0708 0006 4450`.
- The ESP continued answering 0x06 polls during the 2.010 s response window.
- No `0x0F FC03` response arrived.
- Final summary:
  `NO_0F0708_RESPONSE_AFTER_COMBINED_ROLES duration_ms=72042 06req=60 06resp=58 06refused=0 ack=0 ackRefused=0 A5req=0 A5resp=0 A4=0 0F03req=0 0F03resp=0 responseWindowMs=2010 resyncDelta=0 dropDelta=0 DE_LOW`.
- Parser resync and RX drop deltas remained zero.
- Normal production telemetry continued.

Strong conclusions:
1. A sustained valid `0x06` accessory presence by itself does not trigger A5/A4 discovery or `0x0F FC03`.
2. Simultaneous intended multi-role operation was only partially exercised because no `0x0F FC16` write occurred during the window; therefore the `0x0F ACK` side was armed but not actually used.
3. Nevertheless, the exact `0x0F 0708/count6` read remains unanswered even while the `0x06` accessory role is continuously present and transport-active.
4. The simple model "0x06 presence is the missing prerequisite for 0x0F read-side availability" is rejected.
5. The no-response result is transport-clean and not explained by bus/parser errors.

Hypotheses:
- The genuine `0x0F` FC03 responder may be physically implemented inside the Online/DCM module itself.
- A5/A4 may be polled by a separate master/device that is absent from the local bus, rather than being triggered by the heat-pump controller.
- The 0x06 accessory role and the 0x0F mailbox/service role may indeed belong to one physical Online/DCM device, but merely emulating the 0x06 side does not instantiate the 0x0F read responder.
- A real cold-start of the controller while both emulated roles are present may still differ from runtime insertion, but earlier cold-boot work already showed that 0x06 presence alone does not establish semantics.

Unknowns:
- Exact physical owner of the 0x0F FC03 responder.
- Which device is the master issuing A5/A4 reads in the genuine capture.
- Whether the genuine Online/DCM hardware internally bridges its own A5 service and 0x0F mailbox without requiring the heat-pump controller to initiate those reads.

Comparison:
- EXP147: direct 0x0F read unanswered.
- EXP148: A5/A4/0x0F FC03 absent passively for 300 s.
- EXP149: direct A5 read unanswered.
- EXP150: 0x0F ACK-side bootstrap insufficient.
- EXP151: sustained valid 0x06 transport presence also fails to expose 0x0F read-side service or trigger A5/A4.

Decision:
Stop treating A5/A4 and the 0x0F FC03 responder as likely latent controller endpoints waiting for a local bootstrap. The evidence now strongly favors them being functions/endpoints of the genuine external Online/DCM device or another missing bus participant.

Next direction:
Analyze the genuine Online capture as a multi-device ownership problem. The highest-value next experiment should distinguish which physical participant originates each request/response direction, preferably from timing/electrical-source evidence or by emulating the external device as the responder/owner rather than continuing to query absent endpoints as a master.

Current experiment:
**EXP151 COMPLETE / NEGATIVE.**


---

## 2026-09-25 — EXP152 COMPLETE / OFFLINE ANALYSIS — genuine Online traffic ownership reconstruction

Hypothesis:
A5/A4 and 0x0F FC03 may be latent heat-pump-controller endpoints unlocked by Online presence, or may instead be functions/endpoints of the external Online/DCM topology. The genuine capture is analysed as a multi-device ownership/scheduling problem before more active bus experiments.

Observed facts from the genuine Online capture:
- The bus shows a highly regular polling/scheduling pattern containing 0x02 FC17, A5 FC03, 0x04 FC17, occasional 0x06 FC17, 0x0F FC03 and 0x0F FC16.
- A5 appears as three repeated FC03 reads:
  - 0000/count18
  - 0023/count1
  - 002E/count10
  each followed by a valid A5 response.
- 0x0F FC16 writes are followed by standard FC16 ACKs, proving that a responsive 0x0F slave endpoint exists in the genuine topology.
- 0x0F FC03 reads are followed by data responses, proving that the same logical address also provides read-side service in the genuine topology.
- One recurring scheduler sequence is:
  A5 read cycle -> 0x04 FC17 -> 0x06 FC17 -> 0x0F FC03 0708/count6.
- At 11.383 s the 0x0F 0708/count6 read is answered at 11.406 s (~23 ms), followed at 11.447 s by 03E8/count13 and its response at 11.486 s (~39 ms).
- At the end of the capture, after normal A5 cycles stop, the same three discovery-shaped reads are attempted at A4:
  - A4 0000/count18
  - A4 0023/count1
  - A4 002E/count10
  with no responses in the captured tail.
- The A4 fallback occurs in the same broad scheduler context as the earlier A5 activity.
- Local no-Online experiments show:
  - 0x02/0x04/0x06 controller polling remains present;
  - A5/A4 polling is absent;
  - 0x0F FC16 controller writes can remain present;
  - 0x0F FC03 is absent;
  - direct ESP reads to A5 and 0x0F are unanswered.

Strong conclusions:
1. The genuine topology contains at least one additional responsive logical participant absent locally: 0x0F is a real slave/service endpoint there, not merely a register namespace inside the local controller.
2. A5 is also a real responsive slave/service endpoint in the genuine topology; A4 behaves like an address fallback/discovery candidate when A5 stops answering.
3. The repeated ordering A5 -> 0x04 -> 0x06 -> 0x0F FC03 is strongly scheduler-like. It is more consistent with A5/A4 and 0x0F FC03 being part of a coordinated master poll schedule than with spontaneous slave-originated traffic.
4. Because the local controller already generates 0x02/0x04/0x06 traffic and 0x0F FC16 writes, the strongest current ownership hypothesis is that the heat-pump controller is the common master and extends its polling schedule to A5/A4 and 0x0F FC03 only when a genuine external Online/DCM participant has been recognized.
5. This common-master interpretation is still not PROVEN from a two-wire capture alone because electrical source identity is unavailable.
6. EXP147-151 reject simple runtime insertion as sufficient:
   - bare 0x0F read fails;
   - bare A5 read fails;
   - 0x0F ACK-only runtime presence fails;
   - 0x06 runtime presence plus armed 0x0F/A5 roles fails.

Key untested quadrant:
A true heat-pump/controller cold boot while BOTH external roles are already present:
- valid 0x06 accessory responder from the first poll;
- valid 0x0F slave ACK/service presence from the first controller FC16 write.

Earlier cold-boot experiments only supplied the 0x06 role. EXP150 supplied 0x0F ACK presence only at runtime. EXP151 supplied 0x06 presence at runtime while 0x0F ACK was armed but never exercised because no FC16 occurred during the active phase.

Hypotheses:
- Genuine recognition may be latched only during controller boot / initial enumeration.
- A successful early 0x0F ACK sequence together with 0x06 accessory presence may cause the controller to add A5/A4 and 0x0F FC03 to its runtime poll schedule.
- A5/A4 could still be another external sub-endpoint; exact physical hosting remains open.

Unknowns:
- Physical transmitter identity for each request on the genuine two-wire capture.
- Exact device hosting A5/A4.
- Exact device hosting 0x0F.
- Whether a cold-boot combined-role emulation is sufficient without additional identity/application payload.

Decision:
EXP153 should test the untested cold-boot combined-role quadrant, not another runtime read probe.

Current experiment:
**EXP152 COMPLETE / OFFLINE ANALYSIS. Next: EXP153 cold-boot combined 0x06 + 0x0F presence test.**


---

## 2026-09-25 — EXP153 PREPARED — cold-boot combined 0x06 + 0x0F role presence

Hypothesis:
Genuine Online/DCM recognition may be latched during controller boot. If the known external roles are present from the first relevant returned traffic, the controller may add A5/A4 and/or 0x0F FC03 to its scheduler.

Procedure:
1. ESP remains powered.
2. Press `EXP153 ARM Cold Boot Combined Roles`.
3. Restart/power-cycle the heat-pump/controller while leaving the ESP powered.
4. EXP153 remains completely passive until it has observed >=3 s of bus silence.
5. On the first CRC-valid frame after bus return, combined-role emulation begins automatically:
   - exact known 0x06 FC17 response with REQ-low historical image;
   - ACK only strict known 0x0F FC16 shapes;
   - if A5 appears, answer only the three exact genuine captured reads to permit scheduler continuation;
   - A4 is observe-only;
   - spontaneous 0x0F FC03 is observe-only and counts as the strongest success signal.
6. If A5/A4/0x0F FC03 appears, hold for 30 s context then stop.
7. If none appears within 300 s after bus return, stop negative.

Success:
Any spontaneous A5 request, A4 request, or 0x0F FC03 request after the genuine cold-boot transition.

Safety:
- no AFCA=03E8 transaction;
- no semantic setting payload;
- no ESP-generated FC16 request;
- no active FC03 master probe;
- exact known 0x06 response only;
- strict 0x0F FC16 ACK whitelist;
- unknown shapes fail closed;
- no room-sensor emulation.

Current experiment:
**EXP153 PREPARED, not yet run.**


---

## 2026-09-25 — EXP153 COMPLETE / NEGATIVE — cold-boot combined 0x06 + 0x0F presence does not activate Online scheduler

Hypothesis:
Genuine Online/DCM recognition may be latched during controller boot. If both known external roles are present from the first relevant returned traffic (`0x06` accessory responder + `0x0F` ACK/mailbox side), the controller may add A5/A4 and/or `0x0F FC03` traffic to its scheduler.

Observed facts:
- EXP153 armed cleanly and remained passive before the intended controller restart.
- A real bus-down interval was detected after >=3 s silence.
- The bus stayed down for approximately 18.547 s.
- First valid frame after return was `slave=0x1E, fc=0x04`.
- Combined-role emulation started immediately on bus return.
- Within the first ~4.5 s after boot return the ESP ACKed six known `0x0F FC16` writes:
  - `04BA/count22`
  - `05FF/count33`
  - `04A6/count13`
  - `085F/count5`
  - `0662/count33`
  - `04A6/count13`
- The ESP also responded continuously to exact known `0x06 FC17` polls with the historical REQ-low image.
- Final counts after 300 s post-boot observation:
  - `06req=297`
  - `06resp=283`
  - `06refused=0`
  - `ack=6`
  - `ackRefused=0`
  - `unknown0F16=0`
  - `A5req=0`
  - `A5resp=0`
  - `A4=0`
  - `0F03req=0`
  - `0F03resp=0`
  - `resyncDelta=0`
  - `dropDelta=0`
- No A5 traffic appeared.
- No A4 traffic appeared.
- No spontaneous `0x0F FC03` appeared.
- No parser or RX-buffer deterioration occurred during the experimental window.
- Normal production telemetry continued after the experiment stopped.

Strong conclusions:
1. The combined `0x06 + 0x0F` presence was genuinely exercised during a real controller cold boot.
2. Boot-time availability of both known roles is still insufficient to activate the genuine Online scheduler.
3. The simple boot-latched-presence hypothesis is rejected.
4. The controller can successfully exchange/ACK known 0x0F initialization/snapshot blocks and concurrently maintain a valid 0x06 accessory presence without ever adding A5/A4 or 0x0F FC03 read-side traffic.
5. Therefore the missing prerequisite is likely not mere transport presence or timing; additional identity/application semantics are required.
6. EXP147–153 collectively rule out:
   - bare direct 0x0F read,
   - bare direct A5 read,
   - runtime 0x0F ACK presence,
   - runtime combined 0x06+0x0F presence,
   - and cold-boot combined 0x06+0x0F presence
   as sufficient causes of the genuine Online read/discovery layer.

Hypotheses:
- A semantic identity/binding/integration field is required before the controller recognizes the accessory as genuine Online/DCM.
- The relevant discriminator may be among the firmware-derived integration concepts already identified earlier: `ProductID`, `BrandID`, `DivisionID`, `ServiceBind`, `IntegrationMode`, or grouped initial synchronization semantics.
- The genuine 0x0F FC03 endpoint may still physically belong to the external Online/DCM hardware; if so, controller recognition may depend on data content, not just ACK behavior.
- A5/A4 may be activated only after a successful identity/application exchange that is absent from the current REQ-low 0x06 image.

Unknowns:
- Which field or transaction carries Online/DCM identity.
- Whether the required semantic identity is carried in `0x06` response words, in `0x0F` state written/returned during boot, or in another endpoint.
- Exact meaning of the boot-time FC16 blocks `04BA`, `05FF`, `04A6`, `085F`, `0662`.
- Exact physical ownership of A5/A4 and 0x0F FC03 remains not electrically proven.

Comparison:
- EXP150: 0x0F ACK runtime presence insufficient.
- EXP151: valid 0x06 runtime presence plus armed 0x0F role insufficient.
- EXP152: genuine capture suggests coordinated multi-endpoint Online topology.
- EXP153: the missing cold-boot quadrant was tested directly; even with both roles active from boot return, no extra topology appeared.

Decision:
Stop varying presence timing, cold-boot timing, or simple ACK behavior. The next experiment must target one semantic identity/application variable, grounded in firmware or capture evidence, not a guessed register.

Current experiment:
**EXP153 COMPLETE / NEGATIVE.**


---

## 2026-09-25 — EXP154 COMPLETE / OFFLINE — semantic bridge candidate: HE IntegrationMode -> Online registerIndex 0x0559 Link Integration

Hypothesis:
The missing Online/DCM recognition state is semantic rather than transport-only and may be represented by an integration-mode parameter that can be mapped from the recovered Danfoss Link HE model to the Thermia Online/native register namespace.

Observed facts from existing project evidence:
- Recovered Link firmware defines `0x4414 IntegrationMode`.
- Firmware semantics:
  - `0 = LIGHT / non-system integration`
  - non-zero (normally `1`) = SYSTEM integration.
- `IntegrationMode` is configured GET-on-sync and SET-on-sync, with `ClearSetOnSync` and late commit.
- Updating IntegrationMode raises the internal `SystemIntegrationInitRequest`, after which `SystemIntegrationInit()` performs a full three-group sync and eventually sets internal `InitSyncDone`.
- Those init flags are internal host booleans, not wire ParameterIDs.
- In system integration, ownership changes for RoomValue, HeatCurve, HeatCurvePlus5, HeatCurveZero and HeatCurveMinus5 from GET-on-sync to SET-on-sync.
- A public Thermia Online DCM dump independently exposes writable registerIndex `1369 = 0x0559` named `Link Integration`.
- That Online dump uses the same enum:
  - `0 = LIGHT`
  - `1 = SYSTEM`.
- The Online registerIndex namespace is not merely cloud-local: `0x0442 Activate Cooling` from the same dump was experimentally verified on this XTR M as the exact native local `0x0F:0442` register.
- The same dump also maps the heating family `03E8..03EE`, which aligns strongly with the locally proven heating block.
- EXP119 specifically watched for native `0x0553` and `0x0559` during a complete cold boot and saw neither; therefore `0x0559` is not an ordinary unsolicited controller boot broadcast on this XTR M.
- The genuine Online capture currently available does not contain a direct `0x0559` FC16/FC03 transaction in its ~46 s window.

Strong conclusions:
1. `0x4414 IntegrationMode` in the recovered host firmware and Online `0x0559 Link Integration` are a very strong semantic match: same concept and same LIGHT/SYSTEM enum.
2. Because the Online registerIndex namespace has already been locally validated at `0x0442` and strongly aligns at `0x03E8..03EE`, `0x0559` is the best current evidence-backed local-wire candidate for IntegrationMode.
3. This is still not locally PROVEN on the XTR M: no native `0x0559` frame has yet been observed, and the serializer mapping from HE `0x4414` to local `0x0559` is inferred from independent semantic agreement.
4. The candidate is substantially stronger than random 0x06 mailbox guessing and is the first identity/integration discriminator with both firmware semantics and Online register-index evidence.

Hypothesis:
- `0x0F:0559 = 0/1` is likely the local Thermia representation of Link/IntegrationMode.
- A genuine Online/DCM module may cause or maintain `SYSTEM (1)` through a mailbox/service path rather than by a controller-originated broadcast.
- The absence of 0559 in passive/cold-boot local traffic is compatible with it being read from or written by the external 0x0F/DCM side rather than periodically broadcast by the controller.

Unknowns:
- Whether `0x0559` is readable/writable from the XTR controller in the no-Online topology.
- Exact direction of ownership on the local RS485 bus.
- Whether setting `SYSTEM` alone is sufficient to activate A5/A4/0x0F FC03, or only one prerequisite of a larger grouped sync.
- Exact block shape containing `0x0559` in genuine DCM traffic.

Decision:
Do NOT issue a blind standalone second-master write to `0x0559`; prior direct 0x0F second-master writes were not authoritative and the ownership direction is unresolved.

Best next experiment:
EXP155 should be a passive/role-aware `0x0559` discovery experiment:
- watch specifically for any block/request range covering `0x0559`;
- record direction and surrounding block shape;
- during a controlled cold boot with the 0x0F role present, log every FC03/FC16 range around `0x0540..0x0570`;
- no semantic write until an actual ownership/read path is observed.

Current experiment:
**EXP154 COMPLETE / OFFLINE. Next: EXP155 0x0559 Link Integration ownership discovery.**


---

## 2026-09-25 — EXP154 REFINEMENT — Danfoss HP-kit manual reveals explicit DCM integration mode and DCM↔HP approval state

New external documentary evidence materially refines EXP154.

Danfoss Link HP-kit installation manual (086L2382 / DCM03) states:
- for DHP-AQ, DCM03 connects by cable directly to an available RJ45 connection on the relay board;
- the DCM03 itself has a selectable integration mode: Danfoss Link versus Danfoss Online;
- triple-pressing the DCM button changes/reports that mode;
- transition Online -> Link is indicated by 3 fast LED flashes;
- transition Link -> Online by 2 slower flashes.

For HP-kit variants using a GateWay board, the same manual explicitly documents GateWay lifecycle states:
- startup;
- `DCM-HP approval`;
- approval failed;
- `sending settings to DCM`;
- all OK.

Interpretation:
- There is explicit product-level evidence for a semantic DCM↔heat-pump approval/commissioning state above raw bus presence.
- This independently matches the negative EXP147–153 result: syntactic 0x06/0x0F presence is not enough.
- The public Online `0x0559 Link Integration` 0=LIGHT / 1=SYSTEM remains an important candidate, but the manual shows that Link-vs-Online mode is also a real DCM-side configuration state. Therefore `0x0559` must NOT yet be treated as proven controller-local IntegrationMode.
- A genuine DCM03 mode transition is now a uniquely valuable controlled stimulus because it can reveal which RS485 bytes/registers encode integration mode and/or the approval sequence.

Best next evidence:
Capture a genuine DCM03-connected DHP-AQ/iTec system while deliberately switching DCM03 integration mode:
1. stable Danfoss Online mode baseline;
2. triple-press DCM button -> Danfoss Link integration;
3. capture 30–60 s;
4. triple-press again -> Danfoss Online;
5. capture 30–60 s.
Record exact timestamps of both button actions.

This is superior to another local 0x0559 probe because local EXP119/153 already showed no native 0559 broadcast / no 0x0F FC03 without genuine DCM hardware.

Current next experiment:
**EXP155 = genuine DCM03 Link↔Online mode-transition capture / differential analysis.**
If genuine DCM hardware is not locally available, this should be requested from an external owner/collaborator rather than replaced by another guessed local write.


---

## 2026-09-25 — EXP155 PREPARED — genuine DCM03 Link ↔ Online mode-transition capture

Hypothesis:
A genuine DCM03 Link/Online mode transition will expose the application-level approval/integration transaction missing from local emulation.

Design:
- genuine DCM03 connected;
- passive RX-only ESP;
- Online baseline 30–60 s;
- HA marker immediately before physical DCM triple-press to Link;
- ~60 s observation;
- HA marker immediately before physical triple-press back to Online;
- ~60 s observation;
- manual stop or 300 s auto-stop.

Focus:
raw 0x06/0x0F/A5/A4 traffic, explicit 0x0F FC03/FC16 ranges, 0x0559 and 0x0553 coverage/value detection, marker-relative timestamps, parser/drop deltas.

Safety:
DE forced low; no bus TX, responder, ACK, probe, semantic write, or room-sensor emulation.

Current experiment:
**EXP155 PREPARED, not yet run.**


---

## 2026-09-25 — EXP155 PREPARATION CORRECTION — genuine DCM03 capture not locally executable

Correction:
The prepared EXP155 YAML assumed access to a genuine DCM03 module. The local test installation does not have a DCM03, so that experiment cannot be executed locally and must not be treated as the active next bus experiment.

Status:
- EXP155 genuine DCM03 Link↔Online transition capture = NOT EXECUTABLE LOCALLY.
- No result exists.
- Do not count this as a negative experiment.

Best local path:
Return to offline/evidence-driven reconstruction using:
1. the existing genuine Online capture;
2. the public Thermia Online DCM dump;
3. recovered Danfoss Link firmware semantics;
4. external DCM03 documentation;
5. local XTR native block mappings.

The immediate research goal is to identify the serializer/ownership bridge around `0x0559 Link Integration` and related grouped sync semantics without issuing guessed writes.

Current experiment state:
**EXP155 = OFFLINE serializer/ownership reconstruction around Link Integration / grouped sync, no bus TX.**

---

## 2026-09-25 — EXP155 OFFLINE ANALYSIS — Discussion #143 differential re-read

Hypothesis:
The existing genuine Online capture plus the external 0F mailbox model may already contain enough structure to narrow the write path without another speculative bus test.

Observed facts:
- fclauson explicitly states device 0x0F is the Online gateway-side device and that two areas are read from 0x0F while other identified 0x0F transactions are FC16 writes.
- The discussion provides a directional mailbox model: one side writes data to 0x0F and the other reads those areas; and vice versa.
- The genuine capture includes repeated 0x0F FC03 reads of 0x0708/count6 and 0x03E8/count13, plus cyclic FC16 writes into 0x07D0..0x0884 families.
- The discussion attachment names `0F_register_value_map.xlsx`, `modbus_slave.py`, and `config.yaml` are potentially higher-value artifacts than further guessed local probing; their contents are not currently present in the project files.
- The discussion's later AI interpretation of the Heat Curve change is not reliable as written. Direct parsing of the genuine capture shows:
  - 12.116 FC16 0x0848/count23 has 0x0858=0 and 0x085A=20.
  - 33.107 FC16 0x0848/count23 has 0x0858=21 and 0x085A=20.
  - therefore the changed word is 0x0858: 0->21, while 0x085A remains 20.
  - 43.705 is an FC16 write to 0x07E4/count17 and does not establish a direct 0x0858 21->20 reversal.
- The 0x03E8 FC03 response first word changes from 23 at 11.486 to 22 at 24.067, but exact user-action timestamps are unavailable, so causal mapping to 20->21->20 remains unresolved.

Strong conclusions:
1. Do not adopt the discussion AI's claimed `0x0848 20->21->20` semantic mapping; it conflates different offsets/blocks.
2. The 0x0F bidirectional mailbox architecture remains strongly supported and is the most promising path.
3. The highest-value immediate next step is to obtain/analyse fclauson's actual `0F_register_value_map.xlsx`, `modbus_slave.py`, and `config.yaml`, because these may encode the two read blocks, address ownership, and emulator assumptions directly.
4. If those files cannot be obtained, the next-best local/offline task is a transaction-level differential reconstruction of the existing genuine capture, not another speculative write.

Current experiment:
**EXP155 OFFLINE — acquire/reconstruct 0x0F mailbox implementation artifacts and validate against genuine capture.**


---

## 2026-09-25 — EXP155 OFFLINE ARTIFACT ANALYSIS — fclauson 0F map materially clarifies mailbox direction

New artifacts analysed:
- `0F_register_value_map.xlsx`
- `modbus_slave.py`
- two HA add-on manifests.

Observed facts:
- `modbus_slave.py` is not actually a semantic slave implementation; it is a passive UDP forensic logger. Its stated purpose is to recover absolute Unit-15/0x0F register addresses from raw packets.
- The logger specifically tracks two FC03 read-block shapes on Unit 0x0F:
  - 13-register block, target position 12;
  - 21-register block, target position 13.
- The spreadsheet resolves these as:
  - 1000..1012, with register 1012 at position 12;
  - 1040..1060, with register 1053 at position 13.
- Spreadsheet labels:
  - 1012 = target `20/21 field`;
  - 1053 = target `30/31/32/33 field`.
- These line up with fclauson's room-target and DHW-start experiments.
- The workbook's FC16 write map also contains a block:
  - 1350..1369, count 20;
  - register 1363 = value 4 in the captured snapshot;
  - register 1369 = value 0.
- Public Online semantics independently identify:
  - 1363 / 0x0553 = Operation Mode;
  - 1369 / 0x0559 = Link Integration.
- Therefore, in this captured topology, `0x0559 Link Integration` occurs inside an FC16 write *to slave 0x0F*, not in one of the tracked FC03 command/read blocks.
- The workbook contains the decimal-2000 FC16 family as well, including 2000, 2020, 2040, 2060, 2080, 2100, 2120, 2148, 2160 and 2180; this matches the same broad family seen in our genuine Online capture.
- The `config*.yaml` files are only Home Assistant add-on manifests and add no Thermia protocol semantics.

Strong conclusions:
1. The artifacts strongly support the two-direction mailbox model:
   - controller/master writes large state/snapshot blocks to 0x0F using FC16;
   - controller/master reads smaller command/desired-state areas from 0x0F using FC03.
2. `0x0559 Link Integration` belongs, at least in this evidence set, to the controller->0x0F FC16 state/snapshot direction. It is therefore a poor candidate for a blind DCM->controller activation write.
3. The prior plan to target `0x0559=1` directly should be abandoned unless new direction evidence appears.
4. The most valuable unresolved part is now the exact content/ownership of the FC03 read-side command mailbox and the condition that makes the controller schedule those reads.
5. fclauson's logger/map is structurally useful, but does not itself contain the missing semantic DCM serializer or activation handshake.

Important cross-model/platform caveat:
- fclauson's tracked FC03 blocks are 1000..1012 and 1040..1060.
- Our ~46 s genuine Online capture shows FC03 reads at 0x03E8/count13 and 0x0708/count6.
- The first matches 1000..1012 exactly; the second does not match 1040..1060.
- Therefore do not assume the second read block is invariant across platform/session/firmware.

Best next path:
Use the proven 1000..1012 FC03 mailbox as an anchor and reconstruct command direction from genuine captures. Focus on what changes in the 13-word FC03 response around a known Online action, and separately solve what causes FC03 scheduling. Do not pursue 0x0559 as an activation write.

Current experiment:
**EXP155 COMPLETE / OFFLINE ARTIFACT ANALYSIS.**
Next experiment should be designed from the FC03 command-mailbox model, not from 0x0559.

## 2026-09-25 — EXP156 COMPLETE — genuine Online connected, local display Heating Curve change

Hypothesis:
A setting changed locally on the heat-pump display while Thermia Online/DCM is connected should propagate through the controller->0x0F FC16 state/snapshot direction, but should not require the 0x0F FC03 command-mailbox path used for remote desired-state commands.

Observed facts from `thermia_capture_20260925_071517.log` (~79.4 s, 674 frames):
- Genuine Online topology is active throughout: repeated A5 FC03 polling, 0x04 FC17, 0x06 FC17 requests, 0x0F FC16 cyclic writes, and 0x0F FC03 reads.
- 0x0F FC03 traffic in this capture consists only of `0x0708/count6` (18 requests/responses). There are **zero** `0x03E8/count13` FC03 reads.
- The controller-originated FC16 settings snapshot `0x03E8/count13` appears twice:
  - t=22.185 s: 03E8 = 23; remaining words = 25,40,0,1,1,18,18,2,40,30,60,21.
  - t=61.676 s: 03E8 = 22; all other 12 words are unchanged.
- Therefore the local display change is reflected as a clean `0x03E8 23 -> 22` change in the FC16 state/snapshot direction.
- The recurring 0x0848/count23 block changes independently at dynamic fields:
  - 0x0858: 6 -> 27 -> 48 -> 9;
  - 0x0859: 19 -> 20 only on the final sample;
  - these do not form a clean representation of the local Heating Curve 23 -> 22 change.
- A4 is probed transiently at ~32.7 s, followed shortly by A5 resuming. This weakens the earlier idea that A4 appears only after A5 has permanently failed; A4 is better treated as alternate/discovery/fallback-like probing until further evidence.

Strong conclusions:
1. Local/display-originated Heating Curve changes propagate through controller->0x0F FC16 state/snapshot traffic (`03E8`), as expected for authoritative controller state.
2. A local display change does **not** inherently trigger the `0x0F FC03 03E8/count13` command-mailbox read. This materially strengthens the directional model: FC03 03E8/count13 is likely associated with externally supplied desired state, not merely any change to the same setting.
3. The previous genuine Online capture's FC03 `03E8/count13` event becomes more significant: it is not a generic periodic mirror of the controller's heating block.
4. The 0x0848 family should not be used as a direct Heating Curve carrier based on current evidence.

Hypotheses:
- The DCM exposes `03E8/count13` over FC03 only when command/desired-state data is pending or valid for the controller to consume.
- The controller may then accept that desired state and later publish the resulting authoritative state back to 0x0F via FC16.

Unknowns:
- What exact condition causes the controller to issue FC03 `03E8/count13`.
- Whether FC03 03E8 word 0 directly carries the desired Heating Curve or whether another handshake/state determines interpretation.
- Exact role of A4 versus A5.

Next highest-value experiment:
A genuine Thermia Online remote Heating Curve A/B/A capture with exact action timestamps and a long post-restore tail. Compare FC03 `03E8/count13` command images against subsequent FC16 `03E8` authoritative-state snapshots.

Current experiment:
**EXP156 COMPLETE / POSITIVE DIRECTIONAL DIFFERENTIAL.**

## 2026-09-25 — EXP157 COMPLETE / OFFLINE BOOT-CAPTURE ANALYSIS

Hypothesis:
A genuine DCM power-up and HP power-up capture can expose the ordering that makes the Online topology usable, in particular whether A5 discovery, 0x0F mailbox readiness, and the controller state-sync are separate stages.

Artifacts:
- `thermia_capture_20260925_090209.log` — DCM power-up while HP/controller already running.
- `thermia_capture_20260925_090550.log` — HP power-up; capture start is delayed/limited because the Ether-to-TCP interface is powered from the HP and comes up with it.

Observed facts — DCM power-up capture:
- Valid `0xC8 FC03 start=0x2328 count=2` requests recur during the first ~8.5 s; no response is visible in the capture.
- `0x0F` is already responsive very early: FC16 `0x042E/count15` is ACKed at t=0.389 s.
- A5 FC03 is responsive by t=1.236 s and then enters the familiar three-read pattern (`0000/18`, `0023/1`, `002E/10`).
- The controller performs a long ACKed FC16 state/configuration upload to `0x0F`, continuing through block starts `042E,0442,0456,046A,047E,0492,04A6,04BA,04D8,04F6,050A,051E,0532,0546,055A,057B,059C,05BD,05DE,05FF,0620,0641,0662,0683,06A4,06C5,06EA,06F1,06F4` before normal runtime blocks `07D0...` appear.
- The `0x0546/count20` block carries `0x0553=4` (Operation Mode HOT_WATER in the public map) and `0x0559=0` (Link Integration LIGHT), confirming again that these are pushed controller->0x0F during initial sync.
- A valid single-register frame `A4 FC06 0x0032 <- 0x0046` occurs once at ~51.6 s with no visible response. Ownership/meaning is unknown.

Observed facts — HP power-up capture:
- A5 is already responsive at the beginning of the available capture.
- For ~66 s, `0x0F FC03 0x0708/count6` requests receive no response.
- During the same interval, the controller repeatedly transmits the same `0x0F FC16 0x0870/count17` block about every ~2.1 s with no ACK.
- The first visible successful 0x0F FC16 ACK occurs at t=66.860 s for `0x0870/count17`.
- The next `0x0F FC03 0x0708/count6` request at t=68.210 s receives a response at t=68.235 s.
- Immediately afterwards the controller starts a broad ACKed state/configuration upload beginning with `03E8/count13`, `03FC/count11`, `0410/count21`, `042E/count15`, then the same block sequence observed during DCM power-up.
- The first synced `03E8/count13` image is `[22,20,40,0,1,1,18,18,2,40,30,60,20]`.
- A4 gets the same three discovery-style FC03 probes at ~43.6 s, followed by one `0x05 FC17` probe, while A5 later resumes normally. This discovery sweep occurs before 0x0F becomes responsive.

Strong conclusions:
1. A5 availability and 0x0F mailbox readiness are separate boot stages. In the HP-power-up capture A5 is already responsive while 0x0F remains unavailable for more than a minute.
2. The first successful 0x0F ACK is a strong gate for the controller's full controller->DCM state/configuration sync. Once 0x0F begins ACKing, FC03 responses appear and the broad FC16 sync starts immediately.
3. The long FC16 `03E8..06F4` family is best interpreted as an initial/settings-state synchronization upload to the DCM/0x0F service, not ordinary periodic telemetry.
4. The A4/A5/0x05 discovery activity can occur before 0x0F readiness and therefore is not by itself proof that the command mailbox is ready.
5. `0x0559=0` during the genuine initial-sync sequence again argues against treating `0559=1` as the missing low-level recognition trigger.

Hypotheses:
- The DCM exposes at least two application services/stages: an A5 discovery/status endpoint that comes online early, and the 0x0F settings/command mailbox that becomes ready later.
- The repeated pre-ready `0x0870` FC16 write may be the controller's pending sync/state item; its first ACK marks mailbox-service availability, after which the controller performs full synchronization.
- The early `0xC8 FC03 0x2328/count2` traffic and the one `A4 FC06 0x0032=0x0046` frame may be DCM boot/discovery/binding traffic, but source ownership is not yet established.

Unknowns:
- What causes the controller to begin A5 polling in the first place; the HP capture misses the earliest power-up interval because the Ether-to-TCP logger powers from the HP.
- Who transmits the C8 and A4-FC06 frames and what they mean.
- Whether first 0x0F ACK is merely service readiness or also part of higher-level approval/binding.
- Exact event immediately preceding the very first A5 scheduler activation.

Current experiment:
**EXP157 COMPLETE / POSITIVE BOOT-SEQUENCE RESULT.**

Best next step:
Stay passive. Reconstruct the DCM boot sequence around C8/A4/A5 and, if possible, obtain one repeated DCM-only power-cycle capture to test whether `C8 FC03 0x2328/count2` and `A4 FC06 0x0032=0x0046` are deterministic boot/binding events. Do not convert these frames into local writes until transmitter ownership and repeatability are established.

## 2026-09-25 — EXP158 COMPLETE / OFFLINE CROSS-CAPTURE STRUCTURAL ANALYSIS

Hypothesis:
The two boot captures can reveal structural pairing between device addresses and distinguish deterministic initial-sync data from dynamic/runtime fields.

Artifacts:
- `thermia_capture_20260925_090209.log` — DCM-only power-up.
- `thermia_capture_20260925_090550.log` — HP power-up with delayed logger availability.

Observed facts:
- The DCM power-up capture contains nine unanswered `0xC8 FC03 0x2328/count2` probes from t=0.130..8.522 s. Their gaps alternate ~1.284 s / ~0.81 s, giving a ~2.09 s pair period that matches the wider Online scheduler cadence.
- `0xA4` and `0xA5` use the same FC03 register shapes (`0000/18`, `0023/1`, `002E/10`) when probed.
- In the HP boot capture an A4 three-read probe is immediately followed by one `0x05 FC17 read AC12/count12 write AC26/count4` request. Normal Online runtime instead uses A5 together with `0x06 FC17 read AFC8/count12 write AFDC/count5`.
- Address arithmetic is exact: `0xA4 - 0x05 = 0x9F` and `0xA5 - 0x06 = 0x9F`. This strongly supports logical pairing `A4 <-> 05` and `A5 <-> 06`.
- The `0x05` and `0x06` FC17 frames are structurally homologous accessory-slot transactions. The observed 0x05 write payload ends in the same `...0005` lifecycle/status value used by 0x06.
- The DCM-power-up one-off `A4 FC06 0x0032=0x0046` targets a register inside the same shared A4/A5 FC03 map. In the contemporaneous A5 `002E/count10` response, register `0x0032` is also `0x0046`. This is direct evidence that A4/A5 share not just query shapes but register semantics/layout.
- Comparing the two genuine boot captures, 28 overlapping initial-sync FC16 blocks in `0x042E..0x06F1` are available in both captures. 27 of 28 payloads are byte-identical. The only differing block is `0x06EA/count7`.
- `0x06EA/count7` decodes as `[seconds, minutes, hour, day, month, two-digit-year, weekday]`. In DCM power-up it is `[22,6,8,25,9,26,4]`; in HP power-up `[14,11,8,25,9,26,4]`.
- The later runtime `0x0848/count23` block contains the same seven RTC fields at `0x0858..0x085E`. In the DCM capture, `0x06EA` at t=27.583 gives `08:06:22 25/09/26 weekday=4`; `0x0848` at t=46.543 gives `08:06:41 25/09/26 weekday=4`, exactly matching the +18.96 s elapsed time.
- Therefore `0x06EA..0x06F0` is a boot/initial-sync RTC block and `0x0858..0x085E` is its runtime mirror.
- The HP-power-up initial sync does not visibly include `0x06F4/count19` before normal `0x07D0` runtime resumes, whereas the DCM-only power-up does include `0x06F4/count19`. This difference is real in the available captures but its meaning is open.
- During HP boot, once 0x0F becomes responsive, `0x085F/count5` is injected about every 4.2 s during the long initial-sync upload. It is therefore an independent periodic/status block that can pre-empt the bulk sync rather than part of the linear configuration sequence.
- The first successful HP-boot `0x0F FC03 0x0708/count6` response after mailbox readiness is `[0,0,0x7FFF,0xFFFF,0x0080,0x0007]`; after initial sync, later responses become `[0,0,0,0,1919,6]`. In DCM-only boot, the first visible post-sync response is `[0,0,0,0,128,6]` and then settles to `[0,0,0,0,0,6]`. The 0708 block therefore carries boot/session state, not a fixed heartbeat.

Strong conclusions:
1. `A4/05` and `A5/06` form two structurally paired logical accessory slots/services. A4 is not merely a fallback address for A5.
2. The A4/A5 register map is shared: the one-off A4 FC06 write targets `0x0032`, and the same register/value is present in the A5 FC03 response map.
3. The large genuine initial-sync upload is highly deterministic across independent DCM and HP boot scenarios: all overlapping configuration blocks are identical except the RTC block.
4. `0x06EA..0x06F0` and `0x0858..0x085E` are the same RTC/date-time data represented in initial-sync and runtime snapshot namespaces respectively.
5. `0x085F/count5` is an independent recurring status/handshake block that can interleave with the initial-sync upload.

Hypotheses:
- `A4/05` may represent an adjacent unused/alternate accessory slot while `A5/06` is the occupied Online/DCM slot, or the two pairs may represent related service endpoints of the same accessory class. Exact ownership remains open.
- `0xC8 FC03 0x2328/count2` may belong to early discovery/binding, but no response or ownership proof exists yet.
- Changes in `0x0708/count6` likely encode mailbox/session/synchronization state transitions.

Unknowns:
- Why the HP boot sync omits `0x06F4/count19` in the visible capture.
- Exact semantics of `0x085F/count5` and `0x0708/count6`.
- Which physical device owns A4/A5/05/06 and whether A5/06 is definitively the DCM rather than a paired service exposed by it.
- Source/meaning of `0xC8` and the A4 FC06 write.

Current experiment:
**EXP158 COMPLETE / POSITIVE STRUCTURAL PAIRING + RTC MIRROR RESULT.**

## EXP159 — Passive wildcard no-DCM cold-boot differential — PREPARED

**Hypothesis:** the newly discovered DCM-era boot addresses/functions (`0xC8`, `0xA4/0xA5`, `0x05/0x06`, FC06 and `0x0F` mailbox traffic) can be classified against a clean local no-DCM cold boot only if the parser is widened beyond the address/function whitelist used in older EXP94-era tooling.

**Why this is not a repeat of EXP94:** EXP94 established the no-DCM controller/accessory state machine (`A80E 0->8->0x28`, `AFDC 0->0x10`) but its parser/logging was designed before `C8`, `A4/A5`, `0x05` and A4 FC06 were known as relevant boot/discovery traffic. EXP159 changes only observability: wildcard legal-slave parsing plus FC06 recognition.

**Only controlled variable:** power-cycle the heat-pump/controller with no DCM present. ESP32/Waveshare remains externally powered and already listening. No setting is changed.

**Instrumentation:**
- accept CRC-valid Modbus frames for legal slave IDs `0x01..0xF7`;
- recognize FC03/FC04/FC06/FC16/FC17 and exception frames;
- focused red/brown logs for `C8`, `A4/A5`, `05/06`, `0x0F`, first 15 s of `0x02`, and first-seen unexpected slave IDs;
- auto-detect >=3 s complete bus silence, set first returning valid frame to t=0, capture 180 s;
- summary counts include `C8`, A4, A5, 05, 06, 0F FC03 req/rsp, 0F FC16 req/ACK, unexpected addresses, parser resyncs and RX drops.

**Safety:** strictly passive RX-only; GPIO17 TX not configured; DE forced LOW; no replies/ACKs, no 05/06 response, no scan, no register write, no room-sensor emulation. Known-good production parsing/entities remain intact.

**Success criteria:** determine with current observability whether `C8`, A4/A5, 05/06 pairing, FC06, 0x0F FC03 or ACKed 0x0F FC16 appear during a no-DCM cold boot and align their timing against EXP157 genuine DCM/Online boot.

**Negative result:** none of the newly discovered discovery/mailbox frames appears despite a valid complete boot capture with zero parser/RX errors. This would materially strengthen the conclusion that the missing layer is DCM-dependent rather than ordinary controller startup.

**Prepared YAML:** `thermia_exp159_passive_wildcard_cold_boot_profiler.yaml`.

**Current experiment:** **EXP159 PREPARED / PASSIVE WILDCARD NO-DCM COLD-BOOT DIFFERENTIAL.**

## 2026-09-25 — EXP159 COMPLETE / POSITIVE GENERIC-DISCOVERY DIFFERENTIAL

Hypothesis:
The newly observed boot/discovery frames (`0xC8`, A4/A5, 05/06, FC06 and 0x0F mailbox traffic) may be DCM-dependent and can be classified by a widened, fully passive no-DCM cold-boot capture.

Controlled variable:
- Heat-pump/controller power-cycled with NO DCM present.
- ESP32/Waveshare remained externally powered and RX-only.
- No responses, ACKs, scans, setting changes or room-sensor emulation.

Observed facts:
- Bus-down was detected after 3005 ms quiet; first returned valid frame became t=0.
- First returned valid frame was slave 0x1E FC04.
- Contrary to the pre-test hypothesis, the exact `0xC8 FC03 0x2328/count2` probe appears naturally with NO DCM present.
- No-DCM boot produced 20 C8 probes from t=0.565 s through t=20.775 s, roughly ~1.0 s apart. No C8 response was observed.
- Controller state followed the known cold-boot path: A80E 0 -> 8 -> 0x28 and A80F/A810 5 -> 10.
- 0x06 FC17 requests appeared from t=0.789 s. AFDC write image changed from 0x0000 on the first poll to 0x0010 on later polls, matching the established no-DCM waiting state.
- 0x0F FC16 requests appeared immediately: `04BA/count22` twice, then repeated `04A6/count13` plus recurring `085F/count5`.
- None of those 0x0F FC16 requests was ACKed in the captured no-DCM interval.
- No `0x0F FC03` request/response, no A4, no A5, no 0x05 and no FC06 frame was observed in the available ~90 s post-boot capture.
- The log ended before the planned 180 s automatic summary, so EXP159 is complete for the early-boot differential but not a full 180 s census.

Strong conclusions:
1. `C8 FC03 0x2328/count2` is NOT DCM-specific. It is a native controller boot/discovery probe that occurs even when no DCM exists.
2. DCM presence is therefore not what causes C8 probing. The genuine DCM boot instead appears to shorten/terminate the C8 retry phase while higher Online services become available.
3. `A4/A5/0x05` and `0x0F FC03` remain absent from the observed no-DCM boot and therefore remain materially stronger candidates for DCM-dependent discovery/session establishment than C8 itself.
4. UnACKed controller->0x0F FC16 retries (`04BA`, then `04A6`/`085F`) are native no-DCM startup behaviour and must not be treated as evidence that a DCM is present.

Hypotheses:
- C8 may be a generic discovery/commissioning target polled for a bounded timeout; when genuine Online/DCM services become available, the controller advances out of that discovery phase sooner.
- The important discriminator is likely not the presence of C8 requests, but the transition that causes C8 probing to stop and A5/0x0F mailbox activity to become established.

Unknowns:
- What device/service should answer slave 0xC8 and what registers 0x2328..0x2329 represent.
- Whether the shorter nine-probe C8 sequence in the genuine DCM capture is causally terminated by A5/0x0F readiness or simply a capture-specific phase difference.
- Exact event that enables A5 and 0x0F FC03 scheduling.

Decision:
Do not emulate C8 based on its mere presence. C8 is now classified as generic native boot discovery. Next active work should focus on the first genuine discriminator absent in no-DCM boot: A5 service availability / A4-A5 slot establishment, while keeping guessed C8 and A4 FC06 responses out of scope until their semantics are known.

Current experiment:
**EXP159 COMPLETE / POSITIVE GENERIC-DISCOVERY DIFFERENTIAL.**

---

## PART 9 HANDOFF — authoritative continuation point

- Last completed experiment: **EXP159 COMPLETE / POSITIVE GENERIC-DISCOVERY DIFFERENTIAL**.
- Next recommended experiment: **EXP160 — isolated genuine A5 responder — PROPOSED / NOT YET RUN**.
- EXP159 proved `C8 FC03 2328/count2` occurs during a clean local no-DCM cold boot and is therefore generic controller discovery, not a DCM-specific signature.
- The strongest remaining DCM/session discriminators are A5 service responses, A4/05 sibling-slot activity, responsive `0x0F` FC03/FC16 mailbox behaviour, and the full ACKed `03E8..06xx` initial sync.
- EXP160 should change only one variable: exact genuine A5 FC03 responses for `0000/18`, `0023/1`, `002E/10`; keep C8, 0x06, 0x0F, A4 and 0x05 passive.
- No room-sensor emulation path. No genuine DCM exists locally.
- Detailed continuation notes are in `THERMIA_PART9_HANDOFF.md`.

---

## PART 9 STATE UPDATE — EXP160–EXP163 (supersedes earlier Part 9 handoff)

### EXP160 — COMPLETE / NEGATIVE
Exact genuine A5 slave responses were armed during a clean 180 s no-DCM cold boot, but the controller never issued an A5 request (`A5=0`, `A5tx=0`). No A4/05 or `0x0F FC03` appeared. Conclusion: A5 responder availability alone cannot advance startup; the captured payloads themselves were not tested because the responder was never invoked.

### EXP161 — COMPLETE / POSITIVE OFFLINE ANALYSIS
Cross-capture ordering shows that genuine DCM operation has working 0x0F service before the first visible A5 request while C8 discovery can continue in parallel. A4 can appear later while A5 is already established. Therefore C8 completion is not a required A5 gate and A4 is not a simple A5 precursor.

### EXP162 — COMPLETE / NEGATIVE
Combined known 0x0F FC16 ACK + waiting genuine A5 responder was tested for 180 s. Six whitelisted 0x0F FC16 requests were ACKed by the ESP (`0FtxACK=6`), but there was still no A5 request/response, no A4/05 and no `0x0F FC03`. Final summary: `frames=1388 s02=344 s05=0 s06=43 s0F=49 A4=0 A5=0 A5tx=0 0FtxACK=6 C8=20 unexpectedSlaves=0 0F03req=0 0F03rsp=0 0F16req=6 0F16ack=0 resyncDelta=1 dropDelta=0`.

**Strong conclusions after EXP162:**
1. The local 0x0F FC16 ACK implementation is exercised and can satisfy the visible ACK-gated writes.
2. Correct ACK of those known 0x0F FC16 startup writes is not sufficient to activate A5 polling or `0x0F FC03`.
3. A5 activation and visible 0x0F ACK readiness are separate stages/components of a broader DCM service state.
4. C8 remains generic parallel discovery; no evidence justifies inventing a C8 response.

**Current hypothesis:** an earlier discovery/binding/ownership/service-state prerequisite makes the controller schedule A5 and the runtime 0x0F FC03 mailbox when a genuine DCM is present.

**Unknowns:** exact event that enables A5; physical/logical ownership of A5; whether the genuine DCM is the A5 master or A5 slave; exact binding mechanism.

### Current experiment — EXP163 PROPOSED / NOT YET RUN
**Hypothesis:** A5 may be an endpoint actively read by the genuine DCM. After the known 0x0F ACK phase, one exact bounded A5 FC03 master probe sequence may reveal the direction/ownership model.

Change only this variable relative to EXP162: remove the A5 slave responder and send one read-only A5 triplet `0000/count18`, `0023/count1`, `002E/count10` after the 0x0F ACK phase. No A5 writes, no broad scan, no room-sensor emulation. C8/0x06/A4/0x05 otherwise remain passive.

**Success:** CRC-valid A5 response or a repeatable new A5/0x0F FC03/A4/05 state transition. **Negative:** bounded triplet produces no response or higher-layer change; stop rather than escalating to guessed writes.

Authoritative continuation point: **EXP162 is the last completed experiment; EXP163 is the current proposed test.**


---

## PART 9 STATE UPDATE — EXP163 COMPLETE / EXP164 PROPOSED

### EXP163 — COMPLETE / NEGATIVE
**Hypothesis:** after six successful known-shape `0x0F FC16` ACKs, transmitting the exact genuine A5 FC03 read triplet (`0000/18`, `0023/1`, `002E/10`) might reveal or activate the missing A5 service endpoint.

**Observed facts:**
- Valid no-DCM cold boot; bus-down confirmed after 3023 ms quiet and the returned bus was captured for 180020 ms.
- Six whitelisted controller `0x0F FC16` requests were ACKed by the ESP.
- The exact three read-only A5 FC03 requests were transmitted once each after ACK #6.
- Final summary: `frames=1363 s02=338 s05=0 s06=42 s0F=48 A4=0 A5=0 A5probeTX=3 A5rsp=0 0FtxACK=6 C8=20 unexpectedSlaves=0 0F03req=0 0F03rsp=0 0F16req=6 0F16ack=0 resyncDelta=5 dropDelta=0`.
- No A5 response, autonomous A5 traffic, A4, 0x05, or `0x0F FC03` appeared.
- `0x06 FC17` continued independently through the run, with the established no-DCM `AFDC=0x0010` state after startup.
- Five parser resyncs occurred immediately around/after the third injected A5 request; no RX drops followed and the resync count then remained stable.

**Strong conclusions:**
1. `0x0F FC16` ACK progression plus correctly timed exact genuine A5 FC03 reads is still insufficient to create the genuine Online/DCM service topology.
2. EXP149's timing objection is substantially reduced: the full genuine A5 triplet was tested only after six successful `0x0F` ACKs and still received no response.
3. A5 increasingly fits an endpoint supplied by the genuine DCM/service topology rather than a latent controller endpoint unlocked by simply polling the right registers. Physical ownership is still not proven.
4. `0x06` activity is independent of A5 availability and cannot by itself be used as evidence that the Online/DCM session is established.

**Negative result retained:** do not repeat isolated or post-ACK A5 master reads unless a new prerequisite is identified.

### Current experiment — EXP164 PROPOSED / NOT YET RUN
**Hypothesis:** the missing prerequisite occurs before A5 and before the runtime `0x0F FC03` scheduler. A bounded passive cold-boot timing census with finer classification of the first 25 s can identify a still-unmodelled discriminator without adding another speculative bus transmission.

**Change relative to EXP163:** remove all active A5 probe code and all active `0x0F` ACK responses. Keep production RX functionality unchanged. Add only passive timestamp/order logging for C8, 0x06, 0x0F FC16 block starts/counts, A4/A5/0x05, controller A80E/A80F/A810 transitions, and first/last occurrence counters.

**Safety:** fully passive / RX-only; DE remains low; no writes, ACKs, responses, scans, or room-sensor emulation.

**Purpose:** establish a clean post-EXP163 no-DCM baseline with enough event ordering to compare mechanically against the genuine DCM power-up capture before selecting another active target.

Authoritative continuation point: **EXP163 is the last completed experiment; EXP164 is the current proposed passive test.**

---

## 2026-09-25 — EXP164 COMPLETE / POSITIVE PASSIVE DISCRIMINATION; EXP165 PREPARED

Authoritative continuation point: **EXP164 is the last completed experiment; EXP165 is prepared / not yet run.**

### EXP164 — COMPLETE / POSITIVE PASSIVE DISCRIMINATION
Hypothesis: a clean passive no-DCM cold boot may expose an early discriminator preceding A5 / 0x0F FC03 activation.

Observed facts:
- Full 180 s passive run completed with `PASSIVE_ONLY_DE_LOW`.
- Summary: `frames=1601 s02=337 s05=0 s06=42 s0F=291 A4=0 A5=0 C8=20 0F03req=0 0F03rsp=0 0F16req=249 0F16ack=0 resyncDelta=0 dropDelta=0`.
- No-DCM startup again reaches C8 discovery, 0x06 FC17 polling, A80E `0 -> 8 -> 0x28`, and sustained unACKed 0x0F FC16 traffic without any A5, A4/0x05 or 0x0F FC03 service.

Strong conclusions:
- C8 activity, 0x06 transport activity, AFDC=0x0010 and A80E=0x28 are not sufficient DCM-presence/binding discriminators.
- EXP164 strongly reproduces EXP159 and establishes a stable no-DCM boot reference.

### Runtime DCM-recognition correction
The genuine `thermia_capture_20260925_090209.log` is a **DCM power-up while the heat-pump/controller is already running**. It shows successful 0x0F FC16 ACK at ~0.389 s and the first working A5 triplet beginning ~1.179 s. Therefore a controller reboot is not required for the genuine DCM topology to become operational.

Important UI correction: the earlier runtime `EXP 0.0` / `UITBR.KAART` observation is already explained by EXP129-132. A valid 0x06 responder makes the expansion-board entry appear and AFD1 is rendered as version/10. This is 0x06 accessory metadata, not proof of DCM recognition.

Project constraint: avoid further controller power cycles unless uniquely required. Prefer runtime tests and offline capture analysis.

### EXP165 — PREPARED / NOT YET RUN
Hypothesis: activating the already-known 0x06 accessory presence and 0x0F ACK service simultaneously while the controller is already running may reproduce the missing DCM hot-plug transition and cause native A5 and/or 0x0F FC03 service to appear.

Why this is a remaining test:
- EXP151 attempted runtime combined presence, but no 0x0F FC16 request occurred during its combined-role phase, so the ACK side was never exercised.
- EXP153 tested combined 0x06 + 0x0F presence at cold boot and was negative.
- Genuine 090209 demonstrates runtime DCM activation.

EXP165 active surface:
- exact known 0x06 FC17 REQ-low response image only;
- strict whitelist 0x0F FC16 ACKs only;
- exact captured A5 FC03 responses only if the controller autonomously requests A5;
- no AFCA strobe, no semantic setting write, no master probe, no scan, no room-sensor emulation;
- A4/0x05/C8 passive;
- 180 s runtime window; **NO controller reboot**.

Prepared YAML: `thermia_exp165_runtime_dcm_surface_hotplug.yaml`.

---

## 2026-09-25 — EXP165 COMPLETE / NEGATIVE FOR 0x0F-ONLY RUNTIME ACTIVATION; 0x06 ROLE NOT EXERCISED

Hypothesis:
Runtime activation of the already-known 0x06 accessory-presence responder together with the known 0x0F FC16 ACK service might reproduce the genuine DCM hot-plug transition and activate native A5 and/or 0x0F FC03 without rebooting the controller.

Observed facts:
- 180.020 s runtime-only run; no controller reboot.
- summary: `frames=1330 s05=0 s06=43 s0F=5 A4=0 A5=0 06tx=0 0FtxACK=5 A5tx=0 0F03req=0 0F03rsp=0 0F16req=5 resyncDelta=0 dropDelta=0`.
- Five known 0x0F FC16 requests were ACKed: 04A6/13, 085F/5, 04BA/22, 05FF/33 and 0662/33.
- The controller stopped presenting further 0x0F FC16 traffic after those ACKs during the observed window.
- 43 valid slave-0x06 frames were observed, but `06tx=0`: the intended 0x06 responder never transmitted.
- No A5, A4/0x05 or 0x0F FC03 traffic appeared.
- Bus remained clean: `resyncDelta=0`, `dropDelta=0`.
- User observed no change on VERSION during the run, consistent with the missing 0x06 responses.

Implementation finding:
The EXP165 0x06 responder used an incorrect exact request-length gate: `bytes.size()==27`. The native FC17 request `06 17 AFC8 000C AFDC 0005 0A + 10 data bytes + CRC` is 23 bytes. Therefore the 43 valid 0x06 polls could never satisfy the responder condition.

Strong conclusions:
- EXP165 validly confirms that runtime 0x0F FC16 ACK service alone does not activate A5, A4/0x05 or 0x0F FC03.
- EXP165 does NOT test the intended simultaneous 0x06 + 0x0F runtime presence hypothesis, because the 0x06 role was not exercised.
- No reboot is required for the next experiment.

Current experiment:
**EXP165 COMPLETE / NEGATIVE FOR 0x0F-ONLY RUNTIME ACTIVATION; INVALID FOR COMBINED 0x06+0x0F HYPOTHESIS.**

## 2026-09-25 — EXP166 PREPARED — corrected runtime 0x06 + 0x0F hot-plug

Hypothesis:
If the proven 0x06 REQ-low accessory-presence responder is actually exercised during normal runtime (`06tx > 0`) while the known 0x0F FC16 ACK service is also available, the controller may transition toward the genuine DCM service state and autonomously activate A5 and/or 0x0F FC03.

Only experimental correction from EXP165:
- exact 0x06 FC17 request length gate corrected from 27 bytes to 23 bytes.

Everything else remains unchanged:
- same known 0x06 response image `00FF,0001,0000,0001,0...`, AFCA/REQ low;
- same strict known 0x0F FC16 ACK whitelist;
- same exact A5 captured responses only if A5 is requested natively;
- no AFCA=03E8 strobe, no semantic settings write, no master probe, no scan, no room-sensor emulation;
- no controller reboot; runtime-only 180 s observation.

Required validity criteria:
- `s06 > 0` and `06tx > 0`; VERSION `EXP 0.0` appearance is a useful UI corroboration but not itself DCM proof.
- If no 0x0F FC16 request occurs during the 180 s window, the combined-role hypothesis is not fully exercised and must be classified accordingly.

Primary positive discriminator:
- spontaneous A5 traffic and/or spontaneous `0x0F FC03` after both known roles have actually been exercised.

Authoritative continuation point:
**EXP165 is the last completed experiment. EXP166 is the current prepared runtime experiment. Avoid further controller power cycles; reboot only if a future hypothesis uniquely requires boot-time observation.**

---

## 2026-09-25 — EXP166 COMPLETE / POSITIVE 0x06→EXP MAPPING, NEGATIVE DCM ACTIVATION

Hypothesis:
If the proven 0x06 REQ-low accessory-presence responder is actually exercised during normal runtime while the known 0x0F FC16 ACK service is available, the controller may transition toward the genuine DCM service state and autonomously activate A5 and/or 0x0F FC03.

Observed facts:
- Runtime-only experiment; no heat-pump/controller reboot.
- EXP166 armed at 13:47:11.517. First valid 0x06 response was transmitted at 13:47:14.823, ~3.3 s after ARM.
- The user observed `EXP 0.0` appear on VERSION almost immediately after the responder became active.
- Final 180 s summary: `frames=1444 s05=0 s06=169 s0F=0 A4=0 A5=0 06tx=169 0FtxACK=0 A5tx=0 0F03req=0 0F03rsp=0 0F16req=0 resyncDelta=0 dropDelta=0`.
- All 169 observed 0x06 transactions were answered by the EXP166 responder (`06tx=169`).
- No 0x0F traffic occurred during the armed window, therefore the prepared 0x0F ACK role was never exercised.
- No A5, A4/0x05, or 0x0F FC03 activity appeared.
- Bus remained clean: no parser resync delta and no RX drops.

Strong conclusions:
- Runtime 0x06 response is sufficient to make the Thermia UI expose the `EXP 0.0` expansion/version metadata; no controller reboot is required.
- 0x06 accessory/version presence alone is insufficient to activate A5 or the 0x0F mailbox/service layer.
- `EXP 0.0` must not be used as evidence that a DCM/Online session is bound or operational.
- EXP166 does not fully test simultaneous 0x06 + exercised 0x0F ACK presence because no 0x0F FC16 request occurred in its 180 s window.

Comparison:
- EXP165 exercised runtime 0x0F ACKs but failed to exercise 0x06 due to an implementation gate error.
- EXP166 exercised 0x06 correctly but encountered no 0x0F traffic.
- Taken together, EXP165 and EXP166 show that each visible surface can be presented independently without causing A5/0x0F-FC03 activation. They still do not constitute one simultaneous run in which both roles are actually exercised.
- Genuine DCM power-up capture 090209 differs qualitatively: the controller already receives a successful 0x0F FC16 ACK at ~0.389 s and A5 is responsive by ~1.236 s while C8 discovery continues. The missing discriminator is therefore upstream of, or part of, service binding/ownership rather than simple 0x06 metadata visibility.

Unknowns:
- Exact event that causes the controller to schedule the first A5 request.
- What causes runtime 0x0F FC16 traffic to be generated when a genuine DCM is powered.
- Whether an accessory-slot lifecycle/status value, A4/A5 service-side action, or another physical/binding signal causes that transition.
- Transmitter ownership and semantics of the one-off genuine `A4 FC06 0032=0046` remain unresolved; do not reproduce it yet.

Recommended next step:
Do not reboot and do not add a guessed write. Perform an offline differential analysis of the earliest genuine DCM-power-up interval against the now-proven local runtime state, focusing specifically on frames/events that precede the first successful 0x0F ACK and first A5 request. Treat C8, 0x06 metadata and A80E as already-demoted discriminators. Only promote a new active EXP167 variable if the capture provides a concrete, bounded candidate with known transmitter ownership/effect.

Current experiment:
**EXP166 COMPLETE. No EXP167 active test is authorized/prepared yet; next step is offline differential analysis before selecting one bounded runtime variable.**


---

## 2026-09-25 — EXP167 COMPLETE / 0x06 runtime dwell does not activate native 0x0F/A5

**Hypothesis:** after at least one proven runtime `0x06` accessory response, a naturally occurring controller-originated known `0x0F FC16` request could be ACKed; that combined state might trigger spontaneous A5 and/or `0x0F FC03`.

**Controlled change from EXP166:** only the experiment timing/state machine changed. The known 0x06 responder remained identical. `0x0F` ACKing was gated behind `06tx > 0`; no ESP-generated FC16, AFCA strobe, semantic write, A5 master probe, scan, room-sensor emulation, A4/05 or C8 response was introduced. No heat-pump/controller reboot was used.

**Observed facts:**
- run duration `600009 ms`;
- `frames=4715`;
- `s06=559`, `06tx=559`;
- `s0F=0`;
- `0F16req=0`, `0FtxACK=0`;
- `0F03req=0`, `0F03rsp=0`;
- `A5=0`, `A5tx=0`, `A4=0`, `s05=0`;
- `resyncDelta=0`, `dropDelta=0`;
- terminal classification from firmware: `INCONCLUSIVE_COMBINED_ROLE_NOT_EXERCISED_DE_LOW_IDLE`.

**Strong conclusions:**
1. Sustained valid `0x06` presence for ten minutes is not sufficient to make the controller start native `0x0F` traffic or A5 scheduling at runtime.
2. EXP166's shorter negative was not merely a 180 s observation-window artefact; EXP167 extends the same absence to 600 s and 559 successful 0x06 replies.
3. The intended `0x06 + exercised 0x0F ACK` interaction remains technically untested because the controller never emitted a native `0x0F FC16` during the armed window.
4. Further experiments that merely wait longer for `0x06` to cause `0x0F` are low-value.
5. The genuine DCM topology contains an additional service-availability / ownership / discovery / binding property that our current 0x06 emulation does not reproduce.

**Unknowns:**
- physical/logical owner of slave `0x0F`;
- physical/logical owner of A5;
- exact event before/around the first genuine 0x0F ACK that makes the DCM-side service available;
- whether the missing prerequisite is an unseen protocol exchange, electrical/topological presence, or both.

**Next step:** offline analysis of the earliest `090209` DCM-power-up interval, with emphasis on transmitter ownership and any event preceding the first successful 0x0F ACK/A5 request. Do not reboot the controller merely to repeat already captured startup behaviour.


## 2026-09-25 — EXP168 PREPARED

**Hypothesis:** with the proven runtime `0x06` responder already active, ACKing one deliberately triggered controller-originated `0x0F FC16 0x03E8/count14` Heat Curve event may reproduce the missing DCM service transition and cause native A5 and/or `0x0F FC03` activity.

**Only experimental change from EXP167:** after at least 10 valid `0x06` replies, the operator changes Heat Curve by +1 on the Thermia display. ESP ACKs only the exact `0x0F FC16 0x03E8/count14` request; that ACK is T0. A5/A4/0x05 remain observation-only. Observe 120 s after T0.

**Safety:** no heat-pump/controller reboot; no AFCA strobe; no ESP-generated semantic write or FC16; no scan; no room-sensor emulation. Restore Heat Curve manually only after the EXP168 summary.

**Status:** PREPARED / NOT YET RUN.


## 2026-09-25 — EXP168 COMPLETE / VALID NEGATIVE

**Hypothesis:** with the proven runtime `0x06` responder already active, ACKing one deliberately triggered controller-originated `0x0F FC16 0x03E8/count14` Heat Curve event may reproduce the missing DCM service transition and cause native A5 and/or `0x0F FC03` activity.

**Observed facts:**
- EXP168 armed without controller/heat-pump reboot.
- After 10 valid `0x06` replies the experiment reached READY.
- The operator changed Heat Curve by +1 on the Thermia display.
- The expected exact controller-originated `0x0F FC16 0x03E8/count14` appeared at +43.148 s.
- First payload word was `36 / 0x0024`, matching the changed Heat Curve.
- ESP ACKed that exact request once; this ACK defined T0.
- `0x06` remained continuously active throughout the post-T0 window.
- The full 120 s post-ACK observation completed.
- Final summary: `duration_ms=163187 frames=1308 s05=0 s06=155 s0F=1 A4=0 A5=0 06tx=155 0FtxACK=1 A5tx=0 0F03req=0 0F03rsp=0 0F16req=1 firstAckRelMs=43163 resyncDelta=0 dropDelta=0`.

**Strong conclusions:**
1. EXP168 is a valid negative test of the combined runtime condition left unresolved by EXP167: active proven `0x06` presence plus an actually exercised known `0x0F FC16` ACK is **not sufficient** to activate native A5, A4/0x05, or `0x0F FC03`.
2. The entire simple transport-role branch is now strongly exhausted: `0x0F` ACK alone (EXP165), `0x06` presence alone (EXP166/167), and their deliberate runtime combination (EXP168) all fail to reproduce the genuine DCM service topology.
3. The missing prerequisite therefore lies outside the currently emulated transport roles, most plausibly in a discovery/binding/service-availability/ownership layer that is already present very early in the genuine DCM topology.
4. The known runtime Heat Curve event remains a clean controller-originated trigger: `03E8/count14`, first word `36`, then one ACK.

**Hypotheses strengthened:**
- genuine DCM startup includes a missing service-ownership or binding state that makes `0x0F` and A5 operational independently of simple `0x06` presence;
- the real DCM may physically/logically own one or more service endpoints rather than merely responding inside the known `0x06` slot.

**Unknowns:**
- exact owner of slave `0x0F`;
- exact owner of A5;
- whether an unseen discovery/binding exchange occurs before the first visible successful genuine `0x0F` ACK;
- whether the missing prerequisite is protocol-only, electrical/topological, or both.

**Current experiment state:** EXP168 COMPLETE / VALID NEGATIVE.

**Next direction:** do not iterate further combinations of known `0x06` presence and known `0x0F` ACK behaviour. Before defining EXP169, perform offline transmitter/ownership analysis of the earliest genuine DCM power-up/reconnect capture, especially the interval before the first successful `0x0F` transaction and first A5 request. No controller reboot is justified at this point.


## 2026-09-25 — EXP169 COMPLETE / INCONCLUSIVE

**Hypothesis:** ACKing an exact native controller-originated `0x0F FC16 0x042E/count15` request may itself be the visible service-activation boundary that causes native A5 scheduling.

**Observed facts:** runtime-only test; no `0x042E/count15` appeared during 600.005 s; no native `0x0F` traffic at all; final `frames=4295 s06=140 s0F=0 A4=0 A5=0 0FtxACK=0 0F03req=0 0F16req=0 resyncDelta=0 dropDelta=0`.

**Conclusion:** target not exercised; ordinary runtime without DCM does not enter the relevant `0x0F` sync state on its own.

## 2026-09-25 — EXP170 COMPLETE / INCONCLUSIVE DUE PRE-EXISTING 0x04A6 RETRY STATE

**Hypothesis:** deliberately trigger the proven `0x0F` sync path with Heat Curve +1, ACK exact `03E8/14 -> 0410/22 -> 042E/15`, then test whether the `042E/15` ACK activates native A5.

**Observed facts:**
- EXP170 armed cleanly at runtime with no controller reboot.
- Before the manual Heat Curve change, the controller was already repeatedly issuing `0x0F FC16 0x04A6/count13`; EXP170 correctly refused those unexpected ACKs.
- Heat Curve +1 produced exact `0x0F FC16 0x03E8/count14` with first word `37 / 0x0025`; ESP ACKed it once.
- After that ACK, the controller did **not** issue `0x0410/count22`; instead it continued repeatedly issuing the already-pending `0x04A6/count13`.
- Final: `SYNC_STAGE_TIMEOUT duration_ms=54541 phase=1 ackTx=1 ack03E8=1 ack0410=0 ack042E=0 0F16req=48 resyncDelta=0 dropDelta=0`.

**Strong conclusions:**
1. EXP170 did not exercise the intended chain and therefore does not test whether `042E` ACK activates A5.
2. The controller entered EXP170 with a pre-existing/pending `0x04A6/count13` retry state which dominated the `0x0F` scheduler.
3. ACKing a new `03E8/count14` event does not necessarily restart or override an already-pending native 0x0F block.
4. Native 0x0F progression is stateful; current pending-block context matters.

**Current experiment:** EXP170 COMPLETE / INCONCLUSIVE.

**Next direction:** do not repeat EXP170 unchanged. First analyze how the pending `0x04A6/count13` state is established/cleared and compare it with EXP137–141 and genuine DCM startup. Prefer offline analysis; no reboot justified yet.

---

## 2026-09-25 — EXP171–EXP173 CORRECTION AND CURRENT STATE

### EXP171 — capture-role correction / controller-side scheduler
Re-analysis of `090209` and `090550` established that the capture roles had been reversed in the earlier interpretation. `090209` is consistent with a heat-pump/controller power-up while the DCM is already powered and responsive; `090550` is consistent with DCM power-up/rejoin while the controller keeps running. In `090550`, A5 and `0x0F FC03 0708/count6` scheduling are already active while the DCM is still silent. Therefore A5 is not the DCM and the extended scheduler is controller-side.

### EXP172 — COMPLETE
Passive 180 s controller fingerprint. Local XTR repeated `A7F8 read-count=15`, `A80C..A812=0040,0000,0000,000A,000A,FFFF,0000`; no A5/A4/0x05/0x0F FC03. Scheduler-enabled reference uses read-count 13 and `A811/A812=000C/0500` while A5 and `0x0F FC03` are active. These are strong correlation markers but not proven controls.

### EXP173 — COMPLETE / VALID NEGATIVE
**Hypothesis:** the local-vs-reference discriminator may be caused by live `0x06` accessory presence.

**Observed facts:**
- 30 s passive baseline: read-count 15, A811=FFFF, A812=0000;
- 60 s exact known `0x06 FC17` REQ-low presence responder, 56 responses;
- no change in read-count, A811, or A812 during active presence;
- 180 s passive recovery remained unchanged;
- no A5, A4, `0x05`, or `0x0F FC03` appeared;
- final summary: `duration_ms=270035 06tx=56 A5=0 A4=0 s05=0 0F03req=0 lastReadCount=15 lastA811=FFFF lastA812=0000 resyncDelta=0 dropDelta=0`.

**Strong conclusions:**
1. Known `0x06` accessory presence is not sufficient to change A811/A812 or the A7F8 read-span.
2. Known `0x06` accessory presence is not sufficient to activate the extended A5/A4/0x05/0x0F FC03 scheduler.
3. The scheduler discriminator is not explained by simple current accessory presence.
4. The highest-value remaining hypothesis is persistent controller-side configuration / commissioning / firmware-platform state.

**Unknowns:** exact semantics of A811/A812; whether those values are configurable or firmware-defined; whether scheduler enablement can be reached on the local XTR without genuine commissioning.

**Current experiment:** EXP173 COMPLETE / VALID NEGATIVE.

---

## 2026-09-25 — EXP174 COMPLETE / EXP175 COMPLETE

### EXP174 — VALID NEGATIVE FOR FINGERPRINT MUTABILITY

Hypothesis: `A811/A812` plus A7F8 read-count might be ordinary mutable runtime/setting state.

Observed: across a real Heat Curve A/B/A cycle `36 -> 37 -> 36`, the controller fingerprint stayed `readCount=15`, `A811=FFFF`, `A812=0000`; no A5/A4/0x05/0x0F FC03 appeared.

Conclusion: these fields are less likely to be ordinary mutable setting/runtime fields. Their scheduler correlation remains non-causal.

### EXP175 — PASSIVE TOPOLOGY FINGERPRINT — COMPLETE / VALID NEGATIVE

Hypothesis: the scheduler-enabled external captures may represent a broader/different controller topology rather than a scheduler state that can be reproduced one-for-one on this XTR M.

Observed 180.009 s passive census:
- frames=1457
- slave 0x02=336
- slave 0x04=0
- slave 0x1E=670
- slave 0x05=0
- slave 0x06=42
- slave 0x0F=168
- A4=0
- A5=0
- C8=0
- 0x0F FC03 req/rsp=0/0
- 0x0F FC16 req=168
- fingerprint stayed readCount=15, A811=FFFF, A812=0000
- resyncDelta=0, dropDelta=0

Local 0x1E traffic is active and structured: repeated FC16 writes to 0x0000/count9 and 0x0014/count3, plus FC04 reads at 0x0000/count22 and 0x001E/count6.

Comparison with scheduler-enabled reference captures:
- reference platform continuously uses slave 0x04 and A5 and schedules 0x0F FC03;
- local XTR M continuously uses slave 0x1E and shows none of 0x04/A5/A4/0x05/0x0F FC03;
- reference fingerprint is A811/A812=000C/0500 with A7F8 read-count 13; local remains FFFF/0000 with read-count 15.

Strong conclusion: the external scheduler-enabled captures and local XTR M are not the same observed bus topology. Treating the external scheduler as a direct one-for-one target for the XTR is no longer justified.

Important limitation: this does not prove that slave 0x04 vs 0x1E alone causes the scheduler difference. It may be model/firmware/controller-board topology, commissioning/configuration, or a combination.

Research direction: stop using direct A811/A812 write as next step. Next work should identify the role/equivalence of reference slave 0x04 versus local slave 0x1E and determine whether the scheduler family is platform-specific or merely differently addressed/configured.

**Current experiment: EXP175 COMPLETE / VALID PASSIVE TOPOLOGY RESULT.**

---

## 2026-09-25 — EXP177 PREPARED / GUARDED 0x03E8 SEMANTIC WRITE PROBE

Hypothesis: a freshly learned native XTR `0x0F FC16 0x03E8/count14` image may be accepted as a semantic Heat Curve write when written back to slave `0x0F`, rather than being only an outbound mirror.

Controlled variable: only word 0 of the freshly captured 14-word 0x03E8 image changes, from restored baseline to baseline+1. The remaining 13 words must be byte-for-byte identical between the native +1 capture and the native restored capture before FIRE is enabled.

Known before test: `0x03E8` is strongly/proven correlated with Heating Curve; local UI Heat Curve changes emit native `0x0F FC16 0x03E8/count14`; exact FC16 ACK of this block is already proven for retry clearing. Unknown: whether ESP-originated FC16 to `0x0F:03E8` is ignored, mailbox-only, or semantically accepted by the controller.

Safety: no controller reboot; no scans/probes; no 0x06 responder; no AFCA; no 0559/A811/A812 write; no room-sensor emulation. Test is +1 only, requires fresh same-run payload capture, idle-system FIRE guard, >=15 ms bus silence, and automatic exact-baseline restore after 5 s plus dedicated FORCE RESTORE control.

Authoritative continuation point: **EXP176 COMPLETE / OFFLINE NEGATIVE for 0x0559 scheduler-gate hypothesis. EXP177 is PREPARED / NOT YET RUN.**

---

## 2026-09-25 — EXP177 COMPLETE / VALID NEGATIVE FOR DIRECT 0x0F:03E8 SEMANTIC WRITE

Hypothesis: a freshly learned native XTR `0x0F FC16 0x03E8/count14` image, written back to slave `0x0F` with only Heat Curve word0 changed by +1, may be accepted as a semantic Heat Curve write.

Observed facts:
- native baseline was 36; UI-driven +1 produced native `03E8/count14` with word0=37;
- UI restore produced native `03E8/count14` with word0=36;
- the 13 remaining words were identical across the +1 and restored native payloads (`pairValidated=YES`);
- ESP transmitted exactly one guarded test frame with word0=37 and exact captured other13 words;
- after 5 s, ESP transmitted exactly one automatic restore frame with word0=36 and exact captured other13 words;
- no native `03E8` frame appeared after FIRE (`native03E8afterFire=0`);
- no HA Heating Curve state change was observed after the ESP-originated test frame during the observation window;
- parser resync delta=0 and RX drop delta=0.

Strong conclusions:
1. The experiment cleanly exercised the intended direct ESP->slave0x0F FC16 03E8/count14 path with a validated native payload image.
2. There is no evidence that a direct master-originated write to slave `0x0F:03E8` is accepted as a semantic Heat Curve command on this local XTR.
3. Native controller->0x0F `03E8` traffic is therefore better treated as outbound synchronization/mirroring unless a different write direction/session/handshake is proven.

Hypotheses remaining:
- the semantic write target may be a different slave/transport direction;
- writes may require an active service/session/mailbox state absent locally;
- a command may be represented by a different frame family than controller-originated FC16 sync blocks.

Unknowns:
- whether slave `0x0F` stored the injected image transiently without exposing a semantic effect;
- whether a response/ACK from 0x0F to the injected test frame occurred but was not separately classified in EXP177;
- the true XTR-local semantic command ingress path.

Decision: do not repeat direct `0x0F FC16 03E8/count14` writeback with nearby values. Next work should identify command ingress direction/ownership before another semantic write.

Authoritative continuation point: **EXP177 COMPLETE / VALID NEGATIVE FOR DIRECT 0x0F:03E8 SEMANTIC WRITE.**

---

## 2026-09-25 — EXP178–EXP181 — AFCA/mailbox trigger line re-evaluated

### EXP178 — INCONCLUSIVE / HANDSHAKE NOT REACHED
Hypothesis: combining stable 0x06 presence + exercised 0x0F FC16 ACK service + AFCA `0000->03E8->0000` might trigger controller-originated 0x0F FC03 mailbox polling.
Observed: native 0x0F FC16 `04A6/count13` and `0662/count33` were ACKed; AFCA=03E8 was then returned repeatedly, but `0861` never rose to 16; no 0x0F FC03 appeared; parser/drop deltas stayed zero.
Conclusion: not a valid negative for mailbox triggering because the prerequisite AFCA/0861 transport handshake never completed.

### EXP179 — INCONCLUSIVE / WRONG PHASE REPRODUCTION
Hypothesis: removing all 0x0F ACK service would restore the canonical AFCA handshake.
Observed: AFCA=03E8 was returned, but without explicitly enforcing the proven SHORT command slot; no 0861 high, no 0x0F FC03, clean parser.
Conclusion: invalid as a handshake reproduction because EXP58-61 had already proven that the 03E8 trigger is phase-sensitive and must be sent on the direct SHORT slot.

### EXP180 — VALID NEGATIVE FOR PHASE-ONLY EXPLANATION
Hypothesis: restoring the proven sequence — passive slow LONG (~4.3 s), all-zero stage1 on LONG, then selector-only AFCA=03E8 on the direct SHORT (550..950 ms) — should reproduce `0861=16`.
Observed: two stable LONG baselines at 4285/4290 ms; stage1 sent on LONG at 4288 ms; direct SHORT arrived 707 ms later; 03E8 trigger sent exactly there; no `0861=16`, no 0x0F FC16/FC03 observed, parser/drop clean.
Conclusion: wrong poll phase alone does not explain the failed EXP178/179 handshakes in the current controller runtime.

### EXP181 — VALID NEGATIVE FOR RESPONSE-DELAY EXPLANATION
Hypothesis: the remaining implementation difference versus successful EXP59 was pre-response timing; changing the delay from ~250 us to the old proven 5 ms might restore ACK.
Observed: slow LONG baselines 4289/4284 ms; stage1 on LONG at 4291 ms; direct SHORT 707 ms later; exact selector-only 03E8 trigger sent after 5 ms pre-response delay; still no `0861=16`; no 0x0F FC16/FC03; parser resync/drop deltas zero.
Strong conclusions:
1. Neither incorrect LONG/SHORT phase nor the shorter EXP180 pre-response delay explains the current failure to reproduce the historical AFCA/0861 handshake.
2. The current runtime differs from the successful EXP59/60/92/96/107 context in some still-unidentified controller/accessory state.
3. Further nearby AFCA timing variants have low expected value and should be stopped unless new evidence identifies a specific missing state variable.

Most important open question now: what controller-side state enabled historical `AFCA=03E8 -> 0861=16` and, separately, the scheduler-enabled `0x0F FC03` mailbox family? Priority returns to offline comparison of successful historical handshakes and genuine DCM captures rather than additional timing tweaks.

Authoritative continuation point: **EXP181 COMPLETE / VALID NEGATIVE FOR 5 ms RESPONSE-DELAY HYPOTHESIS. Pause AFCA timing variants; next work should be offline/state-difference reconstruction before another active experiment.**

---

## 2026-09-25 — EXP178–181 NEGATIVE TIMING BRANCH + DCM MAILBOX BREAKTHROUGH

### EXP178–181 summary

EXP178 tested AFCA/0861 plus 0x0F ACK context, EXP179 removed 0x0F ACK service, EXP180 restored proven LONG->direct-SHORT phase selection, and EXP181 additionally restored the historical 5 ms response delay. None reproduced 0861=16 in the current runtime context. EXP180/181 were parser-clean and hit the intended LONG (~4.29 s) -> direct SHORT (~0.707 s) sequence. Therefore further AFCA timing micro-variants are low priority. The historical AFCA/0861 handshake remains proven from earlier experiments, but its current runtime preconditions are not fully reconstructed.

### Offline genuine-DCM finding — 0708 word1 gates 03E8 desired-state read

Re-analysis of `thermia_capture_20260924_210001(1).log` found the exact previously referenced controller read `0F 03 03E8 000D` twice.

At ~11.383 s:
- controller: `0F 03 0708 0006`
- DCM response words: `0000,0001,0000,0000,077F,0006`
- 41 ms later controller: `0F 03 03E8 000D`
- DCM response 13 words: `0017,0014,0028,0000,0001,0001,0012,0012,0002,0028,001E,003C,0014`

At ~23.962 s the same pattern repeats:
- `0708/count6` response again has word1=`0001`
- ~39 ms later controller reads `03E8/count13`
- returned 13-word image is identical except first word `0016` instead of `0017`.

All other `0708/count6` responses in that capture use word1=`0000` and are not followed by `03E8/count13`. The two `03E8` snapshots coincide with the documented deliberate Heat Curve `20 -> 21 -> 20` event and differ only in the first word (`23 -> 22`).

Strong conclusions:
1. The exact `0F 03 03E8 000D` desired-state read is genuine and source-proven; it was not present in the three newer DCM boot/rejoin captures because no command was pending there.
2. `0x0708/count6` is not merely a heartbeat/status read. Its response contains at least one command/dirty selector: response word1=`1` is strongly correlated with immediate controller scheduling of `0x03E8/count13`.
3. The most plausible current command model is:
   - controller periodically FC03-reads `0708/count6` from slave0F;
   - DCM returns a command/dirty bitmap/header;
   - word1=1 requests the heating-family desired-state fetch;
   - controller immediately FC03-reads `03E8/count13`;
   - DCM returns desired heating values, with word0 Heat Curve-related.
4. EXP177 tested the wrong direction for semantic command ingress: FC16 state push toward 0x0F. The genuine DCM command path is controller-initiated FC03 after a 0708 selector indication.

Unknowns:
- exact meaning of all six 0708 words and whether word1 is a bitmask, command index, or group-dirty flag;
- exact mapping/count semantics for all 13 words in the 03E8 desired image;
- how/if the local XTR controller can be made to schedule the 0708 FC03 poll family, because local passive topology still lacks the scheduler family seen in the external DCM system.

Research direction:
- stop AFCA timing variants;
- offline-map all genuine DCM `0708/count6` responses and immediate downstream FC03/FC16 traffic;
- treat `0708 word1=1 -> immediate 03E8/count13 read` as the highest-value proven command-dispatch relation;
- do not attempt a local 0708 response experiment until the local controller itself emits a genuine `0F 03 0708 0006` request or a separate justified scheduler-enablement mechanism is identified.

**Current experiment state: EXP181 COMPLETE / VALID NEGATIVE for 5 ms timing hypothesis. Next work is offline DCM mailbox reconstruction before EXP182 active testing.**


---
## 2026-09-26 — EXP222 COMPLETE / IMPORTANT NEGATIVE

Hypothesis:
A local minimal-DMC responder that ACKs the controller's known `0x0F FC16` boot/state writes may be sufficient to complete the controller's Online/DCM initialization and cause native `0x0F FC03 0708/count6` polling and the extended runtime exporter.

Observed:
- Controlled power cycle with ESP independently powered and ACK mode armed before Thermia power-on.
- First post-power-on acknowledged controller frames appeared ~9.4 s after power-on.
- Exactly 6 allow-listed FC16 requests were ACKed: `04BA/count22`, `05FF/count33`, `04A6/count13`, `085F/count5`, `0662/count33`, then another `04A6/count13`.
- After those ACKs, controller-originated FC16 activity stopped; no unknown FC16 target appeared.
- No `0x0F FC03`, no `0708/count6`, no `07D0` runtime start, no A5, A4, slave 0x04 or 0x05 traffic appeared during 113 s post-on observation.
- `0x0F FC17 0730/count8` and normal `0x06` polling continued.
- Parser integrity remained clean: resync delta 0, RX-drop delta 0.

Strong conclusions:
- ACK-only presence on slave `0x0F` is insufficient to create the extended Online/DCM scheduler/topology on this XTR.
- Completing the locally offered short/pending FC16 chain is not sufficient to transition into FC03 desired-state polling.
- A real DCM's earlier A5/service-topology context is therefore likely an independent prerequisite rather than a consequence of ordinary FC16 ACK completion.
- The genuine observation that A5 is active before the DCM's `0x0F` endpoint boots is now especially important: it weakens the idea that full-sync ACK completion is the primary scheduler trigger.

Important limitation:
- EXP222 did NOT reproduce the genuine full FC16 initialization dump. The local controller offered only the subset listed above, so this is not a proof that ACKing every possible genuine startup page can never matter. It is a strong negative for the actual local ACK-only boot condition tested.

Current direction:
Prioritize identifying the earliest prerequisite that makes A5/service topology exist before DCM `0x0F` readiness: persistent binding, commissioning/configuration state, model/firmware capability, or an earlier service-discovery event. Do not continue blind FC16 ACK-chain expansion.

Current experiment: **EXP222 COMPLETE / IMPORTANT NEGATIVE**.
