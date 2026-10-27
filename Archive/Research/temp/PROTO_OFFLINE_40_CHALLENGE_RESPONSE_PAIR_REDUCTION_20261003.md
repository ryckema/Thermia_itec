# PROTO-OFFLINE-40 — Challenge/response pair reduction

**Date:** 2026-10-03  
**Status:** **COMPLETE / NEGATIVE for tested simple-transform families**  
**Scope:** offline evidence analysis only. No bus TX, no YAML change, no live experiment advancement.

## Hypothesis

Adding genuine 16-byte DCM response bodies to the earlier request-only challenge analysis may reveal a simple stateless transform between the `071C` challenge body and the `0730` response body.

## Controlled change

Baseline: PROTO-OFFLINE-32 request-only challenge reduction.  
New variable: pair every CRC-valid approval request with an immediate CRC-valid `0F 17 10 <16-byte body>` response.

## Corpus

- `itec_eco5_gateway_20260926.log`: 99 approval challenges; 2 accepted response pairs.
- `itec_eco5_gateway_20260928.log`: 64 approval challenges; 4 accepted response pairs.
- `thermia_capture_20261003_165355.log`: 1 ATEC/DCM03 approval challenge; 1 response pair.
- Total: 164 challenges, 7 valid request/response pairs.

All seven paired request and response frames pass Modbus CRC validation.

## Observed pairs

| Source | Challenge ordinal | Req→rsp | Challenge | Response |
|---|---:|---:|---|---|
| Eco5 20260926 | 29 | 61 ms | `63cefb32c6f41382087992370caceeba` | `1691a5f3f8e8d58738924416e8e6a3d5` |
| Eco5 20260926 | 99 | 63 ms | `31fb59fc8fb1175cd89f904d06d92ea4` | `fd636ccd0f921d83ff232a1a2413b372` |
| Eco5 20260928 | 29 | 46 ms | `f721e82cd172299f31f375e9bd3a0105` | `792f96654eb1bb29d0e0c37b59bae167` |
| Eco5 20260928 | 32 | 30 ms | `01bd6eba71bff920128ab44bae2537eb` | `826ed2acbc1b3db93adec93c53087a53` |
| Eco5 20260928 | 35 | 32 ms | `1346194da3ad49c6e90e0f8f825c5f25` | `623c2b46c284b2c985b806ac46ef6f7a` |
| Eco5 20260928 | 64 | 47 ms | `755d73cf72a95e5a7600afa2c4dc8163` | `9a7e802926c0c24d1994c4e5a832462f` |
| ATEC/DCM03 20261003 | 1 | 29 ms | `2ee156572b8b84a0bc7a65c72d56185d` | `20b8f28a236f28fa0339669e2c6f600d` |

Latency range 29..63 ms; median 46 ms. All seven challenge bodies and all seven response bodies are unique.

## Tested transform families

No consistent mapping was found across the six Eco5 pairs or across all seven pairs for:

- fixed XOR mask;
- fixed byte-wise addition/subtraction mask;
- fixed byte permutation plus XOR/add mask;
- byte rotation plus XOR mask;
- 16-bit word permutation plus XOR/add mask;
- direct/reversed MD5;
- SHA-1 or SHA-256 truncated to 16 bytes.

There is no single byte position whose `response_byte XOR challenge_byte` is constant across all pairs.

Pairwise mean Hamming distance is 65.81/128 bits for challenges and 66.29/128 for responses; correlation between input and output pairwise Hamming distances is ~0.022 in this small sample.

## Conclusion

The current paired corpus rejects the tested simple stateless transforms. The response behaves like a high-diffusion keyed/stateful transform, but this does **not** distinguish a block cipher, MAC/PRF, credential-derived function, lookup/state machine, or other proprietary algorithm.

The new ATEC pair is valuable cross-profile evidence, but one ATEC pair is insufficient to infer key sharing or algorithm identity between ATEC and Eco5.

## Unknowns

- key/credential material;
- session-state dependence;
- whether controller identity/pairing participates;
- exact DCM03/Connect algorithm.
