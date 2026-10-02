# Genuine iTec Eco 5 + Thermia Online gateway evidence

Date reduced: 2026-10-02

Sources:

- `itec_eco5_gateway_20260926.log`
- `itec_eco5_gateway_20260928.log`

This note is **offline capture analysis**. It does not claim a locally run iTec Eco 8 experiment and does not change the status of ECO-WRITE-01, which remains **PREPARED / NOT RUN**.

## Observed facts

Across the two genuine Eco5 gateway captures there are **six successful 0x0F FC17 approval responses**. Each response immediately follows an exact native challenge with:

- read start `0x0730`, count 8;
- write start `0x071C`, count 8;
- byte count 16.

Every successful gateway response is followed by a controller-originated `0x0F FC16 03E8/count14`.

| Source | Challenge ordinal in burst | Challenge body | Gateway response body | Response delay | First 03E8/14 after response |
|---|---:|---|---|---:|---:|
| 20260926 | #29 | `63CEFB32C6F41382087992370CACEEBA` | `1691A5F3F8E8D58738924416E8E6A3D5` | 61 ms | 92 ms |
| 20260926 | #29 | `31FB59FC8FB1175CD89F904D06D92EA4` | `FD636CCD0F921D83FF232A1A2413B372` | 63 ms | 92 ms |
| 20260928 | #29 | `F721E82CD172299F31F375E9BD3A0105` | `792F96654EB1BB29D0E0C37B59BAE167` | 46 ms | 93 ms |
| 20260928 | #3 | `01BD6EBA71BFF920128AB44BAE2537EB` | `826ED2ACBC1B3DB93ADEC93C53087A53` | 30 ms | 482 ms |
| 20260928 | #3 | `1346194DA3AD49C6E90E0F8F825C5F25` | `623C2B46C284B2C985B806AC46EF6F7A` | 32 ms | 465 ms |
| 20260928 | #29 | `755D73CF72A95E5A7600AFA2C4DC8163` | `9A7E802926C0C24D1994C4E5A832462F` | 47 ms | 124 ms |

The six response bodies are different. The capture therefore does **not** support a constant static approval response.

## FC16 ACK behavior

Where the gateway immediately ACKs the first `03E8/count14`, the controller proceeds into the established initial synchronization chain:

`03E8/14 -> ACK -> 03FC/11 -> ACK -> 0410/22 -> ACK -> 042E/15 -> ...`

In the two 20260928 challenge-#3 sessions, no immediate `03E8/count14` ACK is present. In each of those windows the controller emits **nine 03E8/count14 frames during the next 10 seconds** and does not progress to `03FC` during that window.

This is direct genuine-Eco5 evidence that the page ACK is part of synchronization progression; EXP01 does not need to rediscover that fact.

## Strong conclusions

1. **Genuine Eco5 capture evidence:** native Online approval is directly followed by the configuration synchronization path beginning at `03E8/count14`.
2. **Genuine Eco5 capture evidence:** the downstream FC16 address/count ACK chain is real and controls page progression.
3. **Genuine Eco5 capture evidence:** a successful gateway response can occur at challenge ordinal #3 as well as #29. There is no basis for requiring challenge #1.
4. **Genuine Eco5 capture evidence:** response bodies vary; the logs do not establish a static challenge-independent response.
5. **Cross-model XTR M evidence:** the specific captured response `1691...A3D5` was accepted on the locally tested XTR M against a different live challenge.
6. **OPEN / UNKNOWN on the target Eco controller:** whether an old known-good Eco5 response is accepted against a non-matching current challenge.

## Consequence for ECO-WRITE-01

ECO-WRITE-01 is narrowed to the remaining unknown:

> Does an iTec Eco controller accept a known-good Eco5 R1 replay against a non-matching live challenge?

The prepared experiment therefore:

- observes challenges #1 and #2 only;
- replays the captured `1691...A3D5` response once on exact challenge #3;
- sends no FC16 ACK and no semantic setting write;
- calls the run positive if controller `FC16 03E8/count14` follows.

Challenge #3 is used because it is an actually observed successful response ordinal in two genuine Eco5 sessions. The replay body chosen for EXP01 came from a different challenge/session, so the test directly probes replay tolerance rather than reproducing a matching captured pair.

## Unknowns retained

- the native challenge-response derivation;
- whether response generation also depends on session state, timing or secrets in addition to the challenge;
- whether Eco8 and Eco5 apply identical approval acceptance rules;
- replay tolerance on the target Eco unit.

No semantic-write result is inferred from this offline analysis.
