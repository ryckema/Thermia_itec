# S11Y-AE–AH — offline volgorde van werkpagina's, overlays en XTR-rejoin-diagnose

**Onderzoeksperiode:** 8–9 oktober 2026. **Doel:** native Thermia/Danfoss Online/Connect/DCM-pad voor iTec XTR M, met ESP32/ESPHome + Home Assistant. **Status per onderzoek:** COMPLETE / POSITIVE voor de afgebakende *offline* replay en testcriteria; COMPLETE / INCONCLUSIVE voor universele controller-wachtrijprioriteit, actuele XTR-owner, automatische ACK-toelating en werkende native rejoin. **Geen nieuwe live test, TX, controllerreset, wijziging in ESPHome of semantische write.**

Deze openbare synthese bevat enkel onderzoeksresultaten en geen private respondercode, beveiligingsalgoritmen, command-mailbox tooling of raw buslogs. De volledige afzonderlijk opgeleverde Markdown-rapporten zijn beschikbaar in het oorspronkelijke projectwerk; SHA-256 vingerafdrukken staan onderaan.

## Bewijshiërarchie en baseline

- **Genuine externe buscaptures:** Eco5/Online 2026-09-26 en 2026-09-28, ATEC/DCM03 2026-10-03. Bevestigde historische service- en runtimevolgordes, *geen rechtstreeks bewijs van de interne scheduler op de XTR M*.
- **Oudere lokale XTR-fragmenten:** twee oudere captures voor aanvullende vergelijking; niet op één doorlopende controller-epoch plakken.
- **Lokaal XTR / experimentele eerstehandsresultaten:** S11B, S11T, S11U FIX1, S11V FIX1, S11W, S11Y-M FIX1, S11Y-Y FIX2 en S11Y-AA. Sommige oude ruwe logs zijn alleen via eerder gedocumenteerde resultaten beschikbaar; niet opnieuw CRC-geverifieerd door elke AE–AH-stap.
- **Firmware-derived:** Thermia Connect 2.1.105 `0708`-mailbox- en selectorprofielen; semantiek daarvan blijft versiespecifiek, en een firmware-label is geen lokaal XTR-bus-/UI-bewijs.
- **Bestaande audits:** H011/H012/H013: echte `085F/5`-census 321 all-zero requests / 10 historische ACKs; één positief geval zonder voorafgaande ACK binnen de willekeurig gekozen vijf seconden. Vijf seconden is een *analytisch venster*, niet een bewezen controllerdeadline.

## Experiment S11Y-AE — volgorde en antecedenten

**Hypothese:** de laatst werkelijk beantwoorde `0708/count6`-selector en eerdere afgehandelde FC16-pagina's beschrijven context beter dan één numerieke bitprioriteit.

**Baseline:** bovenstaande genuine captures + lokaal reeds geclassificeerde `085F(0800)+0708`-rejoin. **Exacte gecontroleerde verandering:** alleen offline CRC16 RTU replay met request/ACK-koppeling, werkelijke beantwoorde `0708`-beelden, tijdlijn en first-next FC16; geen busacties.

**Geobserveerd:** 20/20 replaychecks geslaagd; originele 321/10 census; 329 werkelijk beantwoorde `0708`-polls over de drie genuine traces. Vier `085F`-ACKs vlak na `06F4` gevolgd door `07D0`; drie andere gingen via een nieuwe `FC23` vóór `03E8`; de overige voorbeelden bevatten `0864` (2) of opnieuw `085F` (1). Dit zijn **eerste *tijdelijk volgende* FC16-events**, geen bewezen ACK-causale keuzes. In drie bootstraps volgde op een daadwerkelijk beantwoord `0708` met W4=`0100` toch `07D0`, niet direct `0864`.

**Resultaat:** POSITIVE voor context/tegenvoorbeelden; NEGATIVE voor universele «laagste W4-bit = eerstvolgende pagina»; INCONCLUSIVE voor exacte controllerprioriteit of TX-permissie. Abortcriterium: CRC-/koppeling-/chronologiefout. Recovery: offline geen fysiek herstel nodig.

## Experiment S11Y-AF — strikt volledige runtimecycli

**Hypothese:** een normale ACK-gekoppelde basiscyclus is te onderscheiden van contextafhankelijke `085F`-/`0884`-overlays.

**Baseline:** AE-parsing op dezelfde genuine captures. **Exacte wijziging:** anker elk kandidaatinterval tussen opeenvolgende *fysiek ACKed* `07D0/19`-pagina's en eis exact de negen core-pagina's in de verwachte volgorde; aparte overlay/service-burst-analyse. Het gebruikte request/ACK-venster (0,5 s), servicegap (8 s), selectorcontext (12 s) en maximale cyclus (60 s) zijn **hostselectiecriteria, geen vendor- of TX-timers**.

**Genuine observaties:** 111 kandidaatintervallen → **47 strikt volledige** cycli, **64 niet-gekwalificeerde**, onder meer door FC23-grens of afwijkende/onvolledige kernvolgorde. Core: `07D0 → 07E4 → 07F8 → 080C → 0820 → 0834 → 0848 → 0864 → 0870`. Van de 47 complete cycli hadden 13 een `0884`-overlay en 1 een `085F`-overlay. In drie genuine captures: 321 `085F` requests, 10 ACK; context van eerste request na andere pagina: **314 na `04BA`** (zeven gegroepeerde bursts), **4 na `06F4`**, **3 na `0848`** (twee bursts). Alle **13 `0884`-requests** hadden in die samples `0870` als voorafgaande andere pagina.

**Tegenvoorbeelden:** overlay `0884` ondanks beantwoorde W4=`0000`; `085F` ondanks W4.bit7=0; meerdere `0708` met W4=`0100` gevolgd door `07D0`; Eco5 W4-afbouw `038C → 0380 → 0300 → 0200 → 0000` tijdens progressie is correlatie, geen bewezen prioriteitsalgoritme.

**Resultaat:** **44/44** offline checks POSITIVE; NEGATIVE voor «W4 is een exclusieve FIFO»; INCONCLUSIVE voor wat de 64 uitgesloten vensters intern betekenen. Een ontbrekende stap bewijst geen skip. Abort/recovery: uitsluitend offline.

## Experiment S11Y-AG — passief tweelaags schedulermodel

**Hypothese:** de waargenomen basisring en aanvullende service/publicatieverzoeken zijn twee orthogonale observatielagen. **Baseline:** 47/64 uit AF, 321/10 `085F`, 13/13 `0884`. **Exacte wijziging:** alleen host-model/replay met expliciete `BASE_RING`, `SERVICE_PENDING` en `UNKNOWN_REJOIN_OR_PARTIAL`, bron- en FC23-epochgrenzen, ontbrekende-ACK- en CRC-foutinjecties.

- `BASE_RING_STRICT_OBSERVED` uitsluitend voor **daadwerkelijk** in één capture ACK-gematchte negenpaginavolgorde.
- `SERVICE_PENDING` registreert `085F`/`0884`, voorafgaande andere pagina en de laatste *werkelijk beantwoorde* W4-selector, maar verzint geen interne queue-head.
- `UNKNOWN_REJOIN_OR_PARTIAL` bij onverwachte pagina, ontbrekende ACK, onvolledig venster, FC23-grens, stale selector, CRC of chronologische fout.

**Resultaat:** **86/86** offline tests PASS; exact 47 strikte en 64 niet-gekwalificeerde intervallen gereproduceerd, zonder fictieve pagina's of overgedragen controller-owner. Geen live ESPHome-validatie. Alle labels = `CAPTURE_ONLY`.

## Experiment S11Y-AH — fusie met lokale XTR-logclassifier

**Hypothese:** combineer AD's ESPHome-loglabels met AG's tweelaagse offline model zodat een **zichtbare retained servicecontext** herkenbaar is, maar niet als unieke interne XTR-owner of replypermission wordt geïnterpreteerd.

**Baseline:** vier historische lokale logvensters (S11B, S11Y-Y FIX2, twee S11Y-AA), de vijf hierboven gebruikte captures, H012/H013. **Exacte wijziging:** alleen host-only classifierfusie, afzonderlijke bewijs-/epoch-assen en fail-closed health-gates; geen AD/AG productiecode of hardware aangeraakt.

**Laatst waargenomen XTR (AA, op 8 oktober rond 23:09–23:15):**
- Repeated FC16 `085F/count5`, W2 `0800`, plus FC03 `0708/count6` **polls**; `0662` absent, fysieke ESP TX=0.
- In het laatste periodieke logvenster: W2 komt uit samenvattingen; niet alle vijf originele woorden zijn opnieuw als zelfstandige raw-frame-dump bewezen.
- De parser was stabiel. Laatste ARM op 23:15:21.637 **REFUSED** (`0662=0`, `tx=0/0/0`).
- `BASE_RING = UNKNOWN_REJOIN_NO_MATCHED_CURRENT_EPOCH_BASE_RING`.
- `SERVICE_PENDING = RETAINED_085F0800_WITH_POLL_ONLY_W4_UNKNOWN`.
- `PROVENANCE = UNKNOWN_UNOBSERVED_CURRENT_EPOCH_PREDECESSOR`.
- `last ACTUALLY answered 0708 W4 = UNAVAILABLE`. Een **poll ≠ beantwoord zeswoordbeeld**, dus noch W4=`0000` noch W4=`0100` kan voor AA worden aangenomen.
- `authorize_ack=false`; `authorize_mailbox_reply=false`; `authorize_semantic_write=false`; `dynamic_next_owner=null`; `CAPTURE_ONLY`.

**Resultaat:** **65/65** AH offline regressietests PASS op lokale loggevallen, AG-bronhashes, synthetische drops/integriteitsfouten, resync-delta's, eerdere TX, onbekende voorgeschiedenis en stale W4. Geen ESPHome-compile, live TX of volledig geïdentificeerde controller-epoch. Positief voor diagnose, INCONCLUSIVE voor unieke owner en ACK-admission; recovery offline niet nodig.

## Bewijsclassificatie — projectbreed

**PROVEN / lokaal XTR:** uitsluitend eerdere daadwerkelijk uitgevoerde, specifieke S11-ACK/mailbox-overgangen en de AA-weigering/no-TX; geen AE–AH-live proef. **OBSERVED genuine cross-model:** 47 strikte ACK-gekoppelde cycli in Eco5/ATEC, 64 overige intervallen, service-/history-overlays, 321/10 `085F` en echte W4-tegenvoorbeelden. **STRONGLY SUPPORTED:** separate basispublicatie en overlays; zichtbare retained servicecontext van AA zonder bewezen actuele runtime-owner. **HYPOTHESIS:** echte interne pending-work-prioriteit en job/epoch-provenance. **OPEN / UNKNOWN:** H011 `085F` ACK-recht, huidige XTR-interne owner, actuele mailbox W4 na OTA, betrouwbare autonome Online hot-rejoin, readback-bevestigde writes. **DISPROVEN AS UNIVERSAL:** W4 is vaste FIFO, W4=0 sluit overlay uit, all-zero 085F of recente ACK geeft replypermission, ESP OTA reset de controller, AA actieve ACK-test werd uitgevoerd.

## Volgende onderzoek / administratieve status

**S11Y-AI — OFFLINE candidate / NOT RUN:** probeer de originele S7-, S11V- en S11Y-M-logs of hun bestaande bronlocaties in één ononderbroken epoch te correleren voor een gedateerd *werkelijk beantwoord* `0708`-beeld, de voorgaande eigenaar en eerste `085F`-verandering. De ruwe logs ontbreken in sommige H013-bronsets: vermeld dat als **ontbrekend bewijs, niet een negatief experiment**. Bij ontbreken is uitsluitend een *apart voorbereide passieve* loguitbreiding te overwegen, zonder ACK.

**S11Y-AA active = PREPARED / NOT RUN; eerdere ARM = COMPLETE / INCONCLUSIVE. FIX8K semantische correlatie = RUNNING / PARTIAL. Formele firmware-rebuild S8 = NOT RUN (S7 laatst uitgevoerd).** Geen gewone ACK is bewijs van semantische writeacceptatie. Behoud productie-HA, bus-health-boekhouding, alle onbekende owners `CAPTURE_ONLY`; geen room-sensor-ontkoppeling, DCM-hardwarevereiste, geforceerde `0662` of actieve writes.

## Bronrapporten (ongewijzigde lokaal gegenereerde exemplaren)
- `S11Y_AE_OFFLINE_PENDING_WORK_ORDER_20261008.md` — SHA-256 `50f86d2279f3e1b2a6e06e6a518e1bcbb7723a04172eea3b1131f782db10ad7b`
- `S11Y_AF_OFFLINE_COMPLETE_RUNTIME_CYCLES_20261008.md` — SHA-256 `4e14543f39bb648cf79336d76f46faeacfd3b642f00923bfc4571224aef4cff8`
- `S11Y_AG_OFFLINE_TWO_LAYER_SCHEDULER_20261009.md` — SHA-256 `7aff667d61cc78acecb561d9a2f6a31a3b45c3a9666e7ad915ebfcf62a021091`
- `S11Y_AH_OFFLINE_FUSED_SESSION_CLASSIFIER_20261009.md` — SHA-256 `97b7b037089e901a1de5db1f46e88508b4a0713b05ed822a0eb3d3011278ac65`

The four source report hashes identify **external offline research artifacts**, not other GitHub files. Executable host replay source and all original captures remain **outside this public repository**.
