# G02 exclusive native work owner: research plan, 2026-10-13

Status G02-01 to G02-06: PREPARED / NOT RUN. G02-07: PROPOSED / NOT RUN decision only. No bus TX, ESP flashing, register write, genuine DCM attachment, room sensor disconnection or controller restart required. Physical controller epoch G01 is OPEN. Native TX HARD DENY.

## Three distinct claims

PHYSICAL_SENDER = electrically transmitting device. CRC-valid slave-addressed short ACK lacks unique sender ID. An observed response shape when the ESP provably did not send anything may show another active responder but not who or permanent exclusivity.

CONTROLLER_WORK_OWNER = a bounded controller-owned request/work item in a documented native state. W4 selectors and page geometry are request metadata, NOT a demonstrated exclusive bus lease.

TX_AUTHORITY = a separate and stricter decision. G01 independent current epoch, G02 actual ownership, G03 physical frame end, G04 exclusive reply slot, G05 FIFO/DE release and G06 reset fail-low are all separate conditions. No G02 observer grants authority.

## Experimental sequence

### G02-01 evidence ledger, PREPARED/NOT RUN
Hypothesis: historical local XTR and genuine cross-model captures allow response-shape, sender, work item, epoch and slot to remain independent typed fields. Baseline: user-live CO/DI-B6 RX-only, EXP355/386/S11F, EXP419/420/423/425, firmware CM930. Change: only an offline provenance/evidence matrix for 0x0F FC23 0730/071C, FC16 03E8/14, 0662/33, 085F/5, 0884/60, FC03 0708/6. Positive: every field supported or explicitly UNKNOWN. Negative/abort: ACK, W4 or shape promoted to owner, or Eco5 called local XTR. Recovery: revise offline matrix.

### G02-02 firmware claim/lease audit, PREPARED/NOT RUN
Hypothesis: original Connect device_client 2.0.18/2.1.105 either exposes an actual on-wire owner/lease mechanism or only internal session/work bookkeeping in inspected functions. Change: read FC23/FC16/FC03 handlers, state transitions, timeout and work selectors. Positive: exact claim geometry FOUND, or carefully scoped NO_CLAIM_IDENTIFIED_IN_INSPECTED_PATHS. Abort: absolute nonexistence claimed with code gaps or publishing private approval transform. Recovery: source review; mark PARTIAL when unavailable.

### G02-03 genuine gateway present/absent, PREPARED/NOT RUN
Hypothesis: request/response-shape replay can describe observed responder availability within bounded windows, without identifying the physical sender. Baseline: seven genuine Eco5/ATEC originals, including reported gateway-absent interval with 41 FC23 requests and no matching reply. Change: offline replay with original CRC/provenance. Positive: RESPONSE_PRESENT or NO_RESPONSE_OBSERVED only. Abort: no response interpreted as empty address or host timestamps as physical EOF. Recovery: raw replay.

### G02-04 historical local XTR owner contexts, PREPARED/NOT RUN
Hypothesis: distinguish fresh bootstrap, retained service, runtime work and orphan without inventing lease. Baseline EXP419 INCONCLUSIVE (target not seen), EXP420 scoped positive, EXP423 orphan 0662/33 INCONCLUSIVE, EXP425 COMPLETE/NEGATIVE (one ACK stopped retry but 0683 ordered tail absent), EXP426 INCONCLUSIVE. Change: raw XTR replay where original exists, otherwise DOCUMENTARY_ONLY. Positive: correct candidate/UNKNOWN classes and preserved old negatives. Abort: ACK, payload signature or OTA gap reinterpreted as owner. Recovery: reclassify offline.

### G02-05 passive owner reducer + adversarial tests, PREPARED/NOT RUN
Hypothesis: a metadata-only state projection can track owner candidates and observed peer responses but always deny native TX. Baseline: G01-04 guarded host-only epoch model and G02-01..04. Change: standalone offline owner_candidate, peer_response_seen, epoch_unknown, integrity, tx_authorized=false. Negative fixtures: duplicate/missing ACK, other responder while ESP TX zero, repeated FC23, corrupted CRC, stale W4, switched profile, orphan 0662, ESP OTA and malformed order. Positive: all cases DENY, ambiguous contexts UNKNOWN/HOLD. Abort: any automatic TX, false sender identification or made-up local proof. Recovery: offline rollback.

### G02-06 optional RX-only on-device observation, PREPARED/NOT RUN
Hypothesis: existing CO/B6 P74L diagnostics already show the required response shapes and software TX counters. Change: offline source/log preflight first; only if genuinely missing, prepare minimal no-TX HA Configuration diagnostic with all production blocks preserved and red/brown logs. Positive: a response seen while ESP TX is independently known zero means other responder activity in that window, not identity; no response means PEER_UNKNOWN. Abort: any native TX/DE, new resync/drop, loss of production HA functionality. Recovery: previous confirmed RX-only CO/CN firmware, no controller restart.

### G02-07 later decision, PROPOSED/NOT RUN
Only after independent G01, bounded work and peer analysis plus separate G03-G06 hardware gates, evaluate OWNER_CANDIDATE_FOR_REVIEW or G02_OPEN_NO_GO. No automatic TX and no approval to start a new active test. Each later active action would require explicit authorization, exact register/target/current value and effect, unintended effects, rollback and abort.

## Existing evidence boundaries and next action

Firmware CM930 internal NOT_ACCEPTED to RESPONSE_SENT to ACCEPTED does not identify an exclusive physical responder. The conservative H003/H004/H005/H009 host runtime ownership policy is an architecture, not an on-wire lease. Current XTR CO sample had 214 FC16 request shapes, no observed FC23/short ACK and TX=DENY; it cannot prove that no other responder exists. Begin G02-01 and G02-02 OFFLINE. Source: canonical Research files and Thermia_Connect_Firmware CM930_NATIVE_DCM_STATE_MACHINE, CM930_MODBUS_FLAGS_MAP, XTR_RUNTIME_OWNERSHIP_HARDENING_20261005, XTR_S11Y_C_TO_L_NATIVE_RUNTIME_085F_20261008.
