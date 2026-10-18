# Thermia iTec — passive read-only ESPHome

The legacy Thermia iTec research includes a single consolidated **experimental** XTR M RX-only monitor and a separately maintained Eco compatibility profile.

## iTec XTR M

Use the [XTR read-only directory](Thermia%20itec%20XTR/README.md), containing exactly:
- `Thermia itec XTR/thermia_itec_xtr_m_read_only.yaml` — **v31 FIX3, PREPARED / NOT RUN**; 257 named entities, optional pool/circuit/buffer fail-closed gating plus cooling source/RAW diagnostics; uncompiled/unflashed in this project.
- `Thermia itec XTR/README.md` — installation, conditional HA card example, status and safety.

**Important:** v31 is NOT yet the verified on-device production baseline. The previously recommended v29 public/research YAML and v26–v28 history are preserved in [the original XTR folder archive](../Research/Archive/Read-only_XTR_before_FIX2). The separate V5DCM19 FIX1 RX-only experiment is maintained independently, with results under [Research](../Research/THERMIA_PROJECT_STATE.md).

## iTec Eco

`iTec Eco/thermia_itec_eco_waveshare_public_v01.yaml` is a separate, cross-model profile. Do not assume XTR-only native mappings are proven on the Eco.

## Bus and safety

Read-only builds use **9600 baud, 8E1, GPIO18 receive, GPIO21 driver-enable LOW, no UART TX pin** on Waveshare ESP32-S3-RS485-CAN. Transmissions, native DCM responses, service writes and calendar/alarm HA entities are not part of the XTR v31 read-only candidate.

Use local ESPHome secrets; validate and compile yourself before any user-initiated passive flash. Keep the last independently verified installed baseline for rollback. Status and evidence live in `Research/THERMIA_PROJECT_STATE.md`, `EXPERIMENT_LOG.md` and `PROTOCOL_FINDINGS.md`.
