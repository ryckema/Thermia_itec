# Thermia iTec XTR M — 071C/0730 Session-Opening Exchange Analysis

**Date:** 2026-10-02  
**Track:** PROTO-OFFLINE-02  
**Status:** COMPLETE / POSITIVE — offline evidence analysis only  
**Device TX performed for this analysis:** none  
**Live XTR experiment status:** unchanged (`EXP388` remains RUNNING / PARTIAL)

## Hypothesis

The native `0x0F FC17` exchange

```text
read  0730/count8
write 071C/count8
```

is a strict per-request cryptographic challenge-response that must be solved in order to open the Thermia Online/DCM session.

The offline test compares:

1. all exact `071C/0730` exchanges in the two genuine iTec Eco5 + Thermia Online captures;
2. the six genuine 16-byte request/response pairs;
3. simple deterministic transform families;
4. locally proven XTR replays where one fixed genuine response was sent against different XTR request payloads.

No new bus experiment was run.

---

## 1. Genuine Eco5 + Online corpus

Exact request frame shape:

```text
0F 17
read_start  = 0730
read_count  = 0008
write_start = 071C
write_count = 0008
byte_count  = 10
<16-byte request payload>
CRC
```

Response shape:

```text
0F 17 10
<16-byte response payload>
CRC
```

### Corpus result

| Capture | exact requests | unique request payloads | 16-byte responses |
|---|---:|---:|---:|
| Eco5 + Online 2026-09-26 | 99 | 98 | 2 |
| Eco5 + Online 2026-09-28 | 64 | 64 | 4 |
| **Total** | **163** | **162** | **6** |

Only **6 / 163** exact requests received a 16-byte FC17 response within 200 ms.

Critically:

- all six responded requests were followed by native `03E8/count14` initial-sync traffic within 1 second;
- no request without the 16-byte response was followed by `03E8/count14` within that window;
- no `03E8` session opening was found without the response.

This makes the response a very strong **session-opening gate** in the genuine Online captures.

Response latency after request:

```text
61 ms
63 ms
46 ms
30 ms
32 ms
47 ms
```

First `03E8/count14` after the response:

```text
92 ms
92 ms
93 ms
482 ms
465 ms
124 ms
```

---

## 2. Six genuine request/response pairs

```text
request:
63CEFB32C6F41382087992370CACEEBA
response:
1691A5F3F8E8D58738924416E8E6A3D5

request:
31FB59FC8FB1175CD89F904D06D92EA4
response:
FD636CCD0F921D83FF232A1A2413B372

request:
F721E82CD172299F31F375E9BD3A0105
response:
792F96654EB1BB29D0E0C37B59BAE167

request:
01BD6EBA71BFF920128AB44BAE2537EB
response:
826ED2ACBC1B3DB93ADEC93C53087A53

request:
1346194DA3AD49C6E90E0F8F825C5F25
response:
623C2B46C284B2C985B806AC46EF6F7A

request:
755D73CF72A95E5A7600AFA2C4DC8163
response:
9A7E802926C0C24D1994C4E5A832462F
```

All six responses are unique.

One genuine request payload is duplicated elsewhere in the 2026-09-26 capture without receiving any response. Therefore the controller may repeat a request, and seeing the same request does not itself force the DCM to answer.

---

## 3. Simple transform tests

The six genuine pairs were checked against deliberately simple candidate families.

### Rejected on the available pairs

- fixed XOR mask;
- fixed add/subtract mask;
- byte permutation + fixed XOR;
- byte permutation + fixed add/subtract;
- per-byte bit rotation + fixed constant;
- 16-bit word permutation + fixed XOR/add;
- direct `MD5(request)`;
- first 16 bytes of `SHA-1(request)`;
- first or last 16 bytes of `SHA-256(request)`;
- first 16 bytes of `BLAKE2s(request)`.

Input/output Hamming distance per pair:

```text
65, 62, 60, 67, 62, 72 bits
```

That is compatible with a nonlinear/keyed transform, but six samples are far too few to identify AES or any other algorithm. The result must **not** be stated as “AES proven”.

The Link CC 2.7.42 image contains generic cryptographic support including AES/Rijndael and hash APIs, but earlier firmware analysis already showed that this host firmware does not contain the final DCM03-to-Thermia RS485 serializer. Crypto-library presence is therefore only background evidence, not a mapping of this bus exchange to AES.

---

## 4. Genuine response is not uniquely selected by A80E/A80F/AFDC state

Successful genuine responses occur in more than one surrounding controller state.

Examples include:

```text
A80E=0008 A80F=003C AFDC=0000
A80E=0028 A80F=000A AFDC=0010
```

But many unanswered `071C/0730` requests occur under those same state combinations.

Therefore:

**A80E/A80F/AFDC is not a sufficient discriminator for whether the genuine DCM sends the 16-byte response.**

Those fields remain useful lifecycle/session context, but they do not explain the six response events by themselves.

---

## 5. Decisive local XTR replay evidence

The current XTR write work does **not** calculate a fresh response from each request.

Instead it reuses one fixed genuine response:

```text
R1 payload:
1691A5F3F8E8D58738924416E8E6A3D5

full frame:
0F17101691A5F3F8E8D58738924416E8E6A3D5E227
```

This is the response from genuine pair #1 above.

The same fixed response has been accepted by the local XTR after multiple **different** `071C/0730` request payloads.

Examples:

```text
local request:
1A0C450CF90603ACDC1EC538001E8F18
same fixed R1
-> 03E8/count14 after about 122 ms
```

```text
local request:
1A0F4528F9060AACDC1EC550001E8F50
same fixed R1
-> 03E8/count14 after about 120 ms
```

```text
local request:
1A12454EF90613ACDC1EC580001E8F9C
same fixed R1
-> 03E8/count14 after about 110 ms
```

```text
local request:
1A094526F90609ACDC02C59C001E8F4C
same fixed R1
-> 03E8/count14 after about 125 ms
-> ordered initial sync
-> 06F4/count19 completion
-> qualified stage-40 runtime
```

The requests differ materially. The response is byte-for-byte identical.

This is stronger evidence than any attempt to infer a cryptographic transform from the six genuine pairs.

### Strong conclusion

For the locally tested iTec XTR M firmware/session path, **strict request-specific response validation is not required for session progression under the already-proven cold-start guard**.

A single known-good genuine response token can open the `03E8` initial-sync path against multiple different local request payloads.

This does not prove that every Thermia/Danfoss controller generation behaves the same way.

---

## 6. Local XTR request payload is structurally different from genuine Eco5 requests

Eight locally logged XTR request payloads were compared:

```text
1A0C450CF90603ACDC1EC538001E8F18
1A0F4526F90609ACDC1EC50C001E8F4C
1A0F4528F9060AACDC1EC550001E8F50
1A114510F90604ACDC1EC568001E8F20
1A114540F90610ACDC1EC5BC001E8F80
1A12454EF90613ACDC1EC580001E8F9C
1A094526F90609ACDC02C59C001E8F4C
1A094538F9060EACDC02C5AC001E8F70
```

Ten of the sixteen byte positions are constant across these samples.

Variable positions are only:

```text
1, 3, 6, 9, 11, 15
```

Two correlations are particularly strong:

- byte 0 is always `0x1A` = decimal 26, matching year 2026;
- byte 1 follows the controller hour;
- byte 9 is `0x1E` on 30 September and `0x02` on 2 October, matching day-of-month.

The controller clock page `06EA/count7` independently supports the clock/date interpretation around these sessions.

### Classification

The local request is **strongly structured and timestamp-related**.

It should not be described as a 128-bit random nonce.

The remaining variable fields and transform that create them remain OPEN.

---

## 7. Revised protocol model

The wording “challenge-response” is still convenient, but the evidence supports a more precise model:

```text
controller
   |
   | FC17 071C/0730 + 16-byte session-opening request
   v
Online/DCM
   |
   | optional/conditional 16-byte FC17 response
   v
controller
   |
   | if accepted
   v
03E8/count14
ordered native configuration export
runtime 0708/page-owned session
```

### Genuine Eco5 / Online

**PROVEN from captures**
- only a subset of exact requests receives the 16-byte response;
- in the examined corpus the response is the gate into `03E8` initial sync;
- genuine responses vary.

**OPEN**
- why only some requests are answered;
- whether the 16-byte response is cryptographically derived from the request, generated from separate shared state, or carries another form of identity/capability token;
- exact algorithm/key material.

### Local XTR M

**PROVEN by local active replay**
- one known-good genuine 16-byte response is accepted against multiple different local request payloads;
- accepted replay opens `03E8/count14` and the full native initial-sync path.

**Strong conclusion**
- cracking a per-request cryptographic algorithm is **not required to emulate the currently proven local XTR M session-opening path**.

---

## 8. Hypotheses that remain possible

The observed behavior is compatible with several explanations, none proven:

1. the response is an identity/capability token rather than a MAC over the request;
2. the XTR validates only part of the response;
3. the XTR accepts a compatibility response used by a controller/DCM generation;
4. request-specific verification exists on some Thermia/Danfoss models but not this XTR firmware;
5. the genuine DCM computes a request-specific value even though the XTR does not strictly verify that dependency.

Do not select one of these without new evidence.

---

## 9. Practical impact on the project

This substantially reduces the importance of “breaking the crypto”.

For the main goal — local emulation of the native Online/DCM path on this XTR M — the useful work is now:

- preserve the proven fixed-R1 cold-start path;
- understand **when** the controller expects/accepts the response;
- understand identity/binding state around the exchange;
- continue decoding the ordered config export and runtime state;
- retain strict fail-closed guards around replay.

A future cross-model/generic implementation may still need the real response-generation algorithm.

---

## Evidence classification

### Observed facts
- 163 exact genuine requests, 162 unique request payloads.
- 6 genuine 16-byte responses.
- exactly those six response events open the `03E8` path in the examined one-second window.
- all six genuine response payloads differ.
- simple fixed/permutation/hash candidate transforms tested here fail.
- local XTR requests have substantial fixed structure and date/time correlations.
- the same fixed R1 is accepted after multiple different local XTR requests.

### Strong conclusions
- the genuine 16-byte response is a session-opening gate in the examined Online captures.
- strict request-specific response validation is not required by the locally tested XTR M path.
- “solve AES before native DCM emulation is possible” is not supported by the evidence.

### Hypotheses
- token/capability/partial-validation/generation-specific mechanisms listed above.
- some local request bytes encode more of the controller RTC/date state.

### Unknowns
- genuine response-generation algorithm;
- DCM-side condition deciding which requests to answer;
- remaining local request-field encoding;
- whether other Thermia controller generations require strict request-specific verification.

## Result

**PROTO-OFFLINE-02 — COMPLETE / POSITIVE**

No new heat-pump traffic was generated for this analysis, and no live experiment status changes.
