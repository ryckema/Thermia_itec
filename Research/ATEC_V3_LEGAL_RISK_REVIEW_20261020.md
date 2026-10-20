# ATEC V3 gateway — legal-risk review (Belgium/EU, 2026-10-20)

**Nature:** preliminary legal and source-file risk triage, **not** formal legal advice, not a decision that any person acted unlawfully. Evidence: user-supplied ATEC V3 tar, 23 files, inspected offline; legislation/official sources URLs below. No XTR/ATEC hardware activity, firmware flash or code publication. **NO original vendor handshake key, firmware-authentication implementation, sensitive bus challenge/response or protected mailbox implementation reproduced here.**

## Source observations (VERIFIED FROM SUPPLIED TAR)

1. No file named LICENSE, COPYING, NOTICE, no SPDX license declarations identified in the 23-item archive. There may be another separately granted license; the archive alone does NOT evidence one. The author's own right to publish original work is not negated by this absence; it restricts presumptions of recipients' permission to reproduce, modify or republish it.
2. The external `components/thermia_sniffer/cm930_handshake.h` stores the firmware-derived fixed 128-bit authentication key as C++ constants. The original tar also restates the key/derivation in explanatory documentation. This material would be embedded in released ESP32 firmware. It is not an ESPHome `!secret`; unrelated Home Assistant/Wi-Fi/API/OTA credentials are referenced through `!secret` in YAML.
3. Header provenance explicitly attributes the protocol and handshake interpretation to reverse-engineering Thermia Connect 2.1.105 firmware. Alarm group identifiers/semantics are attributed to vendor firmware tables; the source declares an independently implemented gateway responder. No exact substantial copying of original Thermia protected source was demonstrated by this triage; establishing code derivation would require side-by-side forensic comparison and acquisition provenance.
4. The ESPHome YAML explicitly intends a local native heat pump gateway replacement, with auto-takeover/active RS485 communication, Home Assistant API and OTA. The files do not establish public-cloud account access or a data-collection service. Whether any deployment accesses non-owned installations remains unknown; no such access is assumed.
5. No supplied primary documents substantiate how the firmware was lawfully obtained, whether EULA/NDA restrictions apply, whether publication of the recovered fixed key was authorized, who holds rights to each potentially third-party element, whether copyright-protected firmware code was reused, or whether a separate external license was granted.

## Distinctions under EU/Belgian law

- Directive 2009/24/EC arts 5(3) and 6 permit lawful software observation/study/testing and narrowly scoped decompilation indispensable for interoperability, under conditions (lawful access, necessity, information otherwise unavailable, and limits on use/disclosure). Interoperability does **not** provide a blanket right to copy vendor source or distribute all firmware-derived material.
- CJEU C-406/10 (SAS v WPL) holds software functionalities, language and interface/data format are not themselves the protected code expression. Reproducing protected original implementation text/structure may still infringe.
- Directive 2016/943 art 3 treats reverse engineering of lawfully acquired products as potentially lawful absent legally valid duty restricting acquisition. Article 4 addresses unlawful acquisition/use/disclosure; status as trade secret requires secrecy, commercial value from secrecy and reasonable secrecy steps. A firmware key is **not automatically** a protected trade secret; how it was obtained and disclosed is essential. Public exposure does not conclusively determine legality of earlier disclosure.
- Software-specific anti-circumvention restrictions in Directive 2009/24 art 7(1)(c), with arts 5/6 exceptions, and InfoSoc Directive 2001/29 recital 50 caution against assuming any authentication system necessarily constitutes copyright DRM. The legal purpose of the actual protection and any rights bypassed needs individual assessment. Interoperability-authentication is **not automatically unlawful**.
- No license in the supplied archive means redistribution or creating a public derivative should **not** be presumed authorized; separate consent, a valid external license or a concrete statutory exception would be needed. This does not alone prove the author lacked permission to offer his own code for private use.
- Independent private experimentation on own equipment is generally lower legal risk than distributing an archive with recovered credentials, building commercial products, using a vendor mark as endorsement, or accessing any other party's system/cloud.
- A source review cannot establish compliance with every warranty, product-safety, contractual, data protection, or product-market rule. ESPHome logs may reveal challenge/response diagnostics; sharing them is a separate sensitivity concern.

## Practical recommendations for user's Thermia XTR work

1. Keep the original supplied V3 tar and vendor firmware out of public repositories; preserve private provenance, do not post/authentication keys or raw protected challenge-response sequences.
2. Reuse **independently tested protocol ideas and factual register/geometry observations**, documenting evidence/provenance, not vendor source expression. Get explicit permission/license from ATEC author before copying substantial files.
3. If preparing any PUBLIC sanitized fork, remove the fixed key from source, docs, examples and Git history **before initial publication**, omit protected handshake backend and 0x0708 mailbox implementations; avoiding plaintext source disclosure alone does not solve potential rights in firmware binaries or derived data.
4. Ask the author about rights to use/redistribute original ATEC source, exact firmware acquisition and any Thermia permissions/EULA before community redistribution or commercial release. For publication of recovered authentication material, obtain qualified Belgian IP counsel's advice.
5. Maintain current XTR FAS1 RX_ONLY/HARD_DENY safety and existing research/test statuses, unchanged. This review performs **no** new live experiment.

## Primary legal references

- Directive 2009/24/EC: https://eur-lex.europa.eu/legal-content/NL/TXT/?uri=CELEX:32009L0024
- Directive 2016/943: https://eur-lex.europa.eu/legal-content/NL/ALL/?uri=CELEX:32016L0943
- CJEU SAS v WPL C-406/10: https://eur-lex.europa.eu/legal-content/NL/TXT/?uri=CELEX:62010CJ0406
- Directive 2001/29/EC recital 50 / art 6: https://eur-lex.europa.eu/eli/dir/2001/29/oj?locale=en
- Belgian FOD Economie on computer software copyright: https://economie.fgov.be/nl/themas/intellectuele-eigendom/intellectuele-eigendomsrechten/auteursrecht-en-naburige/auteursrechten/intellectuele-eigendom-op/creatie-van-een/door-welke-rechten-kan
- Belgian FOD Economie on trade secret qualifications: https://economie.fgov.be/nl/themas/intellectuele-eigendom/intellectuele-eigendomsrechten/specifieke-beschermingsregimes/bedrijfsgeheimen-bescherming
- GitHub licensing discussion (supplementary): https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository
