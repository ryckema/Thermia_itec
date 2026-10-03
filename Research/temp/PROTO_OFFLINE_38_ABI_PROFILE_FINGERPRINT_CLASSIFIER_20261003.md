# PROTO-OFFLINE-38 — ABI/profile fingerprint classifier

**Date:** 2026-10-03  
**Status:** **COMPLETE / POSITIVE**  
**Hypothesis:** stable transport/page fingerprints can classify the Online/DCM ABI/topology family of an unknown capture and prevent cross-profile semantic assumptions.  
**Controlled change:** offline classifier/regression only. No bus TX, YAML change, reboot or setting write.

## Classifier features

The classifier uses independent structural fingerprints:

### Legacy DCM/A5 evidence
- active slave `0xA5`;
- `03E8/count13` where visible;
- `0867=0x0016`;
- W5 values restricted to legacy `0006/0007`.

### Modern 0x1E Online evidence
- active slave `0x1E`;
- `03E8/count14`;
- `0867=0x00E8`;
- genuine Eco5 W5=`0000`.

The score is deliberately simple and interpretable. It is not machine learning.

## Regression result

All six genuine reference captures were classified correctly by their known topology provenance:

- **4/4 older genuine Online/DCM captures -> LEGACY_DCM_A5**
- **2/2 genuine Eco5 + Online captures -> MODERN_1E_ONLINE**
- **0 ambiguous**

Legacy scores were 9..12 with modern score 0.
Eco5 captures both scored modern 12 with legacy score 0.

## Important limit

This classifier detects an **ABI/topology family**, not a specific heat-pump product.

A modern `0x1E` result does **not** mean “this is an Eco5” and must not be used to identify XTR versus Eco5.

Likewise, local XTR emulation can deliberately use W5=0006 for the locally proven DCM-icon behavior while still using the modern `0x1E` physical topology. Such a mixed feature set is meaningful and should not be forced into the legacy product class.

## Safety use

Before importing semantics from a donor capture/tooling:

1. classify the capture ABI/topology;
2. apply only semantic rows whose profile provenance is compatible;
3. keep model-specific payload replay prohibited even when page address/count matches.

## Strong conclusion

ABI fingerprinting can now be automated well enough to prevent the most common project error: treating the same `0x0F` page envelope as one universal byte-level schema across generations.

## Tooling

Added:

- `Research/temp/tools/thermia_profile_classifier.py`
- `Research/temp/PROTO_OFFLINE_38_CLASSIFIER_OUTPUT_20261003.txt`

## Live status

Unchanged:
- EXP387 COMPLETE / POSITIVE
- EXP388 RUNNING / PARTIAL
