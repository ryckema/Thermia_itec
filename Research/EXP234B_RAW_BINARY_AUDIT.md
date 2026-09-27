# EXP234B — Offline raw-binary audit of the Danfoss Link / DHP integration stack

Date: 2026-09-27

Status: **COMPLETE / OFFLINE / NEGATIVE FOR XTR 0730 SERIALIZER IN THE AUDITED LINK CC FIRMWARE**

Current bus experiment remains **EXP238 PREPARED / NOT RUN**. EXP234B is a historical offline completion of EXP234 and changes no heat-pump state.

## Hypothesis

The raw Danfoss Link CC 2.7.42 firmware may contain the missing low-level DCM03 -> Thermia serializer or named constants for the consecutive service pages 0708 / 071C / 0730 (decimal 1800 / 1820 / 1840). If present, it could constrain or reconstruct a genuine XTR 0730..0737 response without guessing.

## Method

Read-only/offline only.

- Materialized an original dlcc_2.7.42 firmware archive.
- Extracted and parsed its Windows CE ccimage.bin B000FF image.
- Reconstructed the CE ROM directory and carved managed DHP/regulation assemblies including ParameterCache.dll and RegulationEngine.dll.
- Parsed CLR metadata sufficiently to map integer constants back to exact managed methods/types.
- Reconstructed the native HECTArch.dll XIP image and inspected its strings/constants.
- Searched the complete 2.7.42 ROM for exact 32-bit values 0x0708, 0x071C and 0x0730 and mapped hits to owning modules/files.
- Re-ran public repository searches for the XTR FC17 page pair and genuine response data.

## Observed facts

### Managed DHP stack reaches an abstract HE boundary

ParameterCache.dll contains DHPParameterCache, SyncParameters, CreateSyncRequest, OnHEServiceSetGet, OnHEServiceBind and HESetGetReqRsp.

It also contains genuine heat-pump parameter IDs including:

- 0x030A OperationMode
- 0x4402 HeatCurve
- 0x4414 IntegrationMode

This proves the extraction is operating on the correct DHP application stack.

### No managed XTR 071C/0730 service-page implementation

No IL constant corresponding to 0x071C or 0x0730 was found in the carved heat-pump/regulation assemblies.

RegulationEngine.dll contains three apparent 0x0708 integer immediates, but method mapping places them in ordinary node constructors where decimal 1800 is used alongside other timing/configuration values. They are not service-register references.

### Full-ROM ownership mapping

Exact 0x071C and 0x0730 constants elsewhere in the complete ROM belong to unrelated Windows/UI/framework code. None maps to ParameterCache, RegulationEngine, HECTArch or another identifiable DHP/Thermia serializer.

### HECTArch is the HE/Z-Wave transport boundary

The reconstructed native HECTArch.dll exposes strings/functions for HESetGetReqRsp, ServiceBind, ServiceSetGet, HE_DEVICE_DESCRIPTION and multiple Z-Wave operations.

No identifiable local Thermia 0708/071C/0730 serializer is present there.

## Strong conclusions

1. The raw Danfoss Link CC 2.7.42 host firmware does not contain an identifiable XTR 0730..0737 serializer or response builder.
2. The visible host architecture is:

~~~text
Link CC / host
  DHP ParameterID + value
        -> HE Set/Get / ServiceBind
        -> HECTArch / Z-Wave
        -> [missing DCM03 / Thermia Connect translator]
        -> Thermia local service protocol
        -> heat-pump controller
~~~

3. The missing XTR response must be sought in another component: most plausibly Thermia Connect/DCM-side firmware, heat-pump Gateway/controller firmware, or genuine XTR traffic.
4. No active 0730 response is justified by this audit.

## Hypotheses

- A genuine XTR-compatible Thermia Connect/DCM firmware image is now the highest-value software artifact.
- The heat-pump controller/Gateway firmware may reveal the 0730..0737 schema from the opposite side.
- 0730..0737 may primarily encode session/approval/status/dirty-selector state rather than a static desired-setting payload.

## Unknowns

- Exact idle values of 0730..0737.
- Whether any 0730 word is analogous in function, but not necessarily position, to reference DCM command-pending state.
- Whether the controller validates identity/version/RTC/session relationships across 071C..0723 and 0730..0737.
- Whether a successful response causes the boot/recovery FC17 family to persist or triggers another transaction.

## Negative result recorded

Do not derive guessed 0730 values from Link CC, do not brute-force the eight words, and do not assume the reference 0708 word layout applies to XTR.

## Next direction

Keep EXP238 PREPARED / NOT RUN while pursuing the DCM-replacement line. Highest-value next work is to obtain a Thermia Connect/DCM03 firmware/update image or corresponding XTR Gateway/controller implementation. Only after an evidence-backed 0730 candidate exists should the XTR be used as a bounded protocol oracle.
