# Thermia uitlezen — overgang naar deel 19

## Startpunt
Gebruik de canonical Research-bestanden als bron van waarheid. Deze handoff is alleen een compacte overgangsnota.

## Laatste status
- EXP320 — COMPLETE / POSITIVE.
- EXP321 — COMPLETE / INCONCLUSIVE.
- Controller daarna door gebruiker herstart om zichtbare errors te wissen.
- EXP322 — COMPLETE / POSITIVE passive clean-reboot baseline.
- EXP323 — NOT YET PREPARED / NOT RUN.

## EXP322 kernresultaat
90 s strict passive, TX=0:
- 125 slave-0x0F frames;
- 83 x sparse 04A6/13;
- 42 x exact all-zero 085F/5;
- 0 x 085F(0800);
- 0 x 0708;
- 0 x alle tracked runtimepagina's;
- 04A6 payload changes=0;
- resync=0, drops=0, DE LOW.

Sparse 04A6 payload:
`0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 4020 0000 0000`.

## Belangrijk protocolresultaat
Retained branch lokaal bevestigd:
`085F(0800) --ACK--> all-zero 085F --ACK--> 0884/60 --ACK--> 07D0/19`.

Genuine XTR/DCM capture evidence:
- richer 04A6/13 configuration frames receive standard ACK `0F1004A6000DE1F1`;
- niet generaliseren naar de sparse lokale 04A6 payload zonder lokale test.

## Volgende stap — EXP323
Nog niet gegenereerd.

Hypothese: één conservatief gekwalificeerde ACK van de huidige all-zero 085F/5 kan de clean post-reboot scheduler naar zijn volgende native state brengen.

Plan:
1. wacht 2 x exact all-zero 085F/5;
2. eerste NO_TX;
3. tweede exact één ACK `0F10085F00053356`;
4. 04A6 blijft NO_TX;
5. daarna strict capture-only;
6. eerste volgende relevante non-04A6 0x0F frame RAW loggen en stoppen.

Geen overnight-run vóór deze clean-start route opnieuw aan bewezen runtime is gekoppeld.
