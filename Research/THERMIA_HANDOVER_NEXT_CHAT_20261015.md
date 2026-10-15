# THERMIA iTec XTR M — handover voor volgend gesprek (15 oktober 2026)

## LEES DIT EERST
Actuele status: **GAP-19 COMPLETE/POSITIVE voor firmwarebron- en captureanalyse, NEGATIVE voor de veronderstelling dat interne firmware-ACCEPTED altijd RESPONSE_SENT vereist, INCONCLUSIVE voor fysieke native TX-veiligheid.** GAP-19 tests **29/29**. **GAP-18 DEFERRED / NOT RUN** omdat GPIO18 fysiek niet bereikbaar is. **Volgende: GAP-20 PREPARED / NOT RUN**, volledig offline. Op ESP32 draait nog steeds de door gebruiker bevestigde GAP-08 RX-only-build; native TX HARD_DENY. GAP-11 t/m GAP-15 zijn alleen lokaal offline gecorrigeerde C++-kandidaten, niet op de ESP32 geïnstalleerd.

## Belangrijkste bronnen
Lees vóór antwoord op vragen over actuele status deze GitHub-bestanden, newest-first:
1. [THERMIA_PROJECT_STATE.md](THERMIA_PROJECT_STATE.md)
2. [EXPERIMENT_LOG.md](EXPERIMENT_LOG.md)
3. [PROTOCOL_FINDINGS.md](PROTOCOL_FINDINGS.md)
4. [GAP-11–19 update](V41V5_GAP11_TO_19_AUDIT_20261015.md)

De oude paragrafen in de drie canonieke bestanden blijven bewaarde historische momentopnamen. Prefer newest dated overlay.

Firmwarekennis: https://github.com/ryckema/Thermia_Connect_Firmware ; vooral `findings/CM930_NATIVE_DCM_STATE_MACHINE.md`, `XTR focus/CM930_NATIVE_SESSION_RECONSTRUCTION.md`, `findings/CONNECT_2.0.18_VS_2.1.105_PROTOCOL_DIFF.md`, `findings/NATIVE_SESSION_EPOCH_CONTINUITY_AUDIT_20261010.md` en `findings/NATIVE_SESSION_MVP_TIMESTAMP_RECONSTRUCTION_20261010.md`. Projectbestanden omvatten originele Connect RAUC 2.0.18/2.1.105, `device_client.zip`, `appfs_2018.zip`, XTR logs, ATEC/Eco5 collaboratordumps en eerdere YAML.

## Doel en hardware
Native Thermia Online/Connect/DCM integratie van Thermia iTec XTR M, Danfoss DHP-AQ, met Waveshare ESP32-S3 ESPHome / Home Assistant. Controller is Modbus master; Connect firmware ondersteunt slave 0x0F; paginabeheer en mailbox zijn contextafhankelijk. Geen echt Online/DCM-apparaat beschikbaar, dus geen capturevoorstel dat zo'n module vereist. Room sensor verbonden laten; niet omleiden naar roomsensoremulatie.
Huidige UART-configuratie in voorbereid GAP-08 YAML: 9600/8E1, RX GPIO18, TX GPIO17, DE GPIO21 (LOW). **GPIO18 fysiek niet bereikbaar**: gebruiker heeft GAP-18 passieve Saleae-synchronisatiemeting uitgesteld; geen nieuwe aansluitsuggestie zonder nieuwe expliciete wens. B11C en B11D zijn afzonderlijke RX-only observatoren, geen bewezen gedeelde controller-epoch. Laat de productieconfig en HA-entiteiten onaangeroerd. Gebruiker wil geen routineverzoek om compilerlog; compile eerlijk onbevestigd vermelden waar van toepassing.

## Experimenten in één overzicht
- GAP-08B: ESPHome compile bevestigd door gebruiker; GAP-08 RX-only met OTA geïnstalleerd.
- GAP-09: live RX-only vergelijking op XTR >15k frames, geen byte- of framediff, geen output; sessieovergang niet live aangetoond.
- GAP-10: offline 23/23 checks, NEGATIVE: oude cache-writebase herstelt na mailbox/runtime toggle.
- GAP-11: offline core revoke-fix POSITIVE 326/326 gerichte tests; conservatieve mailbox/runtime loss revoke.
- GAP-12: adapter transport-fault revoke POSITIVE 79/79; NEGATIVE: oude externe Decision kan over nieuwe epoch worden aangeboden.
- GAP-13: Decision provenance/tickets POSITIVE 361/361; oude Decision afgewezen; gekopieerde staged state nog open.
- GAP-14: staged snapshot adoption POSITIVE 175/175; synchroon adaptermodel, niet elektrische live TX.
- GAP-15: wachtlease/mock API-guard POSITIVE 188/188; zes historische suites en GAP11–15 samen 1670/1670 checks. Single-threaded hostmodel, geen productiecode geïnstalleerd.
- GAP-16: zeven historische echte buslogs, 25.031/25.031 CRC-goed; 35/35 tests. Binnen vier historische XTR-samples 2.451 frames, 415 op native slave 0x0F. Logger-ms ≠ fysiek wire EOF. ATEC/Eco5 164 FC23-verzoeken, zeven nabije antwoordvormen.
- GAP-17: 47/47 provenance/negatieve synchronisatietests. Drie oorspronkelijke Saleae-opnames 4 september; 1.258 goede frames was uit eerdere G03-audit, niet opnieuw in GAP-17 gedecodeerd; geen match met gelijktijdige ESPHome-log of gedeeld klokanker. Digital(1).csv alleen D2.
- GAP-18: **DEFERRED/NOT RUN op verzoek gebruiker**; RX GPIO18 fysiek ontoegankelijk; geen meten/OTA.
- GAP-19: 29/29 Python-tests. Originele `device_client/cm/modbus_server15.py` toont dat interne handshake ACCEPTED na in aanmerking komende FC16 niet noodzakelijk een voorafgaande RESPONSE_SENT-status verifieert. Dat is firmwarebronbewijs, NIET lokaal bewezen bus-acceptatie zonder eerdere handshake. Onafhankelijk 25.031 originele raw CRC-goede frames; 2.500 FC16 vormen, 2.125 voldoen slechts aan geïsoleerde code-startadresvoorwaarde, 164 FC23, 7 nabije antwoordvormen. Geen nieuwe TX. Binnen de twee Eco5-fragmenten staan 55/67 in aanmerking komende FC16 voor de eerste **zichtbare** FC23, maar status vóór logstart onbekend.

## Kritieke bewijsgrenzen en historie
Historisch S11F documenteert lokale verse handshake + 32/32 bootstrap in één experiment. S11W/X/Y en R5 zijn andere episodes met ESP-herstarts en onbekende controller-continuïteit; NOOIT samenvoegen tot één bewezen epoch. GAP-06 gebruikte twaalf rapport-afgeleide fixtures, geen 1:1 volledig ruwe busreplay. Standaard FC16 ACK is geen semantische acceptatie. FC03 pull / selectorbit wissen / FC16 teruglezing / semantische bevestiging zijn verschillende gebeurtenissen. Een interne firmwarehandshake ACCEPTED is geen fysieke owner/epoch-witness.
Evidentieniveaus steeds apart: lokaal XTR gemeten; echte cross-model gatewaycaptures; originele Connect-firmware; synthetisch hostmodel; hypotheses/open.

## Onopgeloste veiligheidsvoorwaarden
G01: videoverankerde herstart historisch bevestigd, actuele autonome controller-epoch niet onafhankelijk bewezen.
G02: conditional positive voor bestaande bekende externe DCM-poort, geen absolute elektrische exclusiviteit.
G03: fysiek laatste stopbit naar huidige RX-callback OPEN.
G04: exclusief native responsslot OPEN.
G05: UART/DE/FIFO elektrisch slechts PARTIAL/HOST.
G06: DE fail-low bij reset/brownout OPEN.
Native TX hard geweigerd; geen automatisch nieuwe ACK, handshake, mailbox response, actuatorwrite of OTA toestaan.
Geen secrets, private emulatiecode, beveiligingsherleiding of ruwe vertrouwelijke commandopayloads op openbare GitHub publiceren.

## GAP-20 plan — offline
Nummer GAP-20, PREPARED / NOT RUN. Hypothese: firmware-source-codepaden plus historische captures kunnen request-bit cleared, ontvangst van controllerpagina, wire ACK-vorm, gewenste paginaread en semantisch bevestigde waarde als aparte gebeurtenissen classificeren. Baseline GAP-19, oorspronkelijke Connect-appcode, echte ATEC/Eco5 en lokale XTR-logfragmenten, niet over sessies mixen. Exacte gecontroleerde wijziging: uitsluitend offline classificatietabel/test, geen wijziging aan productiecode, UART of HA. Positief: per klasse direct brononderbouwd bewijs. Negatief: succesclaim die alleen op ACK of oude firmwareflag steunt. Inconclusief: semantische teruglezing niet aanwezig. Abort: ontbrekende herkomst, onverwachte bronconflicten of noodzaak tot bus-TX. Recovery: bestaande GAP-08 RX-only blijft onaangeroerd. Vraag alleen kleinste nog ontbrekende bestaande capturefragment wanneer essentieel.

## Procesafspraken
Experimentele statussen strikt houden: PREPARED/NOT RUN, RUNNING/PARTIAL, COMPLETE/POSITIVE/NEGATIVE/INCONCLUSIVE en SUPERSEDED/NOT RUN. Nooit uitvoering claimen zonder testresultaat. Elke test baseline, één variabele, relevante frames, positief/negatief/abort/recovery. GitHub `Thermia_itec` mag enkel gewijzigd met actuele expliciete toestemming; deze handover is door gebruiker op 15 okt gevraagd. Laat historische Research-loginhoud intact en update drie canonieke docs bij materieel bewijs, minstens elke vijf experimenten.
