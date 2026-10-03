# PROTO-OFFLINE-33 — Thermia Connect hardware / OEM fingerprinting

**Date:** 2026-10-03  
**Status:** **COMPLETE / POSITIVE** for hardware-fingerprint narrowing; **OEM / SoC identity remains OPEN**.  
**Hypothesis:** exact Thermia part numbers, regulatory standards, power/interface details and commissioning documentation can identify, or materially narrow, the underlying Thermia Connect gateway platform without possessing the hardware.  
**Controlled change:** external/document research only. No heat-pump access, no ESP TX, no YAML change, no reboot and no setting write.

## Exact product identity

Official Thermia documentation establishes:

- Thermia Connect kit: **206495**
- Gateway: **355202**
- internal PSU: **357577**
- declaration/document ID: **086L6646**, revision 01
- product description: **12 VDC Gateway + 230 VAC/12 VDC PSU**

The EU declaration lists radio/EMC standards including EN 300 328, EN 301 908-1, EN 301 908-13, EN 301 511 and EN 301 489-52.

## Physical/interface fingerprint

The 2025 installation guide identifies:

- USB — explicitly not used in the documented installation;
- 12 V power;
- heat-pump communication port;
- a second connected-but-unused communication port;
- Ethernet;
- LED;
- reset button.

For iTec/Atec, the supplied communication cable connects the heat-pump I/O/EXP side to the gateway HP communication port.

Current Thermia product specifications add:

- IEEE 802.11 b/g/n;
- 2.4 GHz Wi-Fi;
- WPA-PSK access point security;
- gateway max power 20 W;
- max assembly power 25 W with USB;
- internal PSU 230 VAC -> 12 VDC / 20 W.

## Cellular-certification caution

The declaration contains GSM/LTE-family radio standards. However Thermia's public connectivity documentation presents Connect as Wi-Fi/Ethernet connected and separately describes an **external 3G/4G modem from the local provider** when no Internet connection is available.

Therefore the regulatory standards are a useful fingerprint but do **not** prove an active built-in cellular modem in the deployed Connect gateway.

The available documents do not distinguish whether the standards reflect optional/shared hardware, broader certification scope, or an internal capability unused by the normal installation path.

## OEM / chipset search

Targeted searches combined `355202`, `206495`, `086L6646`, the listed radio-standard set and gateway/OEM/module/firmware terminology.

No independent OEM model, processor/SoC, radio-module identifier, FCC-style ID, MAC OUI, IMEI/TAC or duplicated third-party declaration was recovered.

### Strong negative sub-result

The Thermia article numbers and public regulatory material are not sufficient to identify the gateway OEM/chipset from currently indexed sources.

## Architecture relevance

The documentation reinforces the existing southbound target:

```
heat-pump I/O / EXP communication
            |
            v
   Thermia Connect gateway
            |
      Wi-Fi / Ethernet
            |
            v
      Thermia Online
```

The installation guide requires removal of an existing DCM before Connect installation, supporting an architectural replacement relationship without proving firmware equivalence.

The commissioning phrase **"pairing and protocol packages"** remains the strongest clue that model-specific southbound support may be package/data driven.

## Strong conclusions

1. The gateway hardware fingerprint is now specific enough to guide a future teardown or artifact search.
2. USB is a documented physical interface, but there is no evidence yet that it exposes debug, recovery or firmware update functionality.
3. Built-in cellular must remain OPEN.
4. Generic OEM searching has reached diminishing returns without a physical label/PCB, APK, firmware, module ID or protocol package.
5. Highest-value next artifacts remain an OnSite/Online APK/XAPK, Connect firmware/protocol package, or physical Connect gateway.

## Live status

Unchanged:
- EXP387 COMPLETE / POSITIVE
- EXP388 RUNNING / PARTIAL
