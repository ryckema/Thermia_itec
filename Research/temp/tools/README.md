# Offline Thermia research tools

These tools are intentionally **offline-only**. They do not open a serial port, drive RS485, manipulate GPIO, or transmit anything to a heat pump.

## thermia_capture_analyzer.py

Extracts the decisive topology events needed for EXP208/EXP214 from timestamped bus captures:

- A5/A4/05 service activity;
- slave 0x04 activity;
- 0x0F FC03 0708/count6 scheduler;
- 07D0..0884 runtime FC16 publisher;
- first 0x0F FC16 ACK / FC03 response;
- 0x02 A811/A812 fingerprint;
- an overall extended-topology YES/NO classification.

Example:

```bash
python3 Research/tools/thermia_capture_analyzer.py capture.log
```

Use `--json` for machine-readable output.

The topology classifier deliberately requires at least two of the three independent families A5, 0708, and runtime FC16. A single stray probe is therefore not enough to declare the topology active.

## thermia_dcm_reference_model.py

Pure in-memory, fail-closed model of the currently observed genuine DCM slave-0x0F role.

Implemented:

- ACK of observed FC16 write shapes;
- FC03 0708/count6 mailbox response;
- FC03 03E8/count13 heating desired-state page;
- FC03 0546/count20 system desired-state page;
- one-shot selector semantics from EXP212;
- convenience setters for Heat Curve, Room Target and Operation Mode.

Not implemented:

- serial/RS485 transport;
- scheduler activation;
- unknown FC03 pages;
- arbitrary register writes;
- 0410/count21 DHW page until its selector/command path is proven.

Run its built-in self-test:

```bash
python3 Research/tools/thermia_dcm_reference_model.py
```

## test_offline_tools.py

Runs synthetic positive/negative analyzer tests plus exact captured-frame response tests.

```bash
cd Research/tools
python3 test_offline_tools.py
```

## Safety rule

These tools are research aids only. Do not add a serial transport or connect the reference model to the local XTR until the controller itself has been shown to instantiate the genuine Online/DCM scheduler or a separately proven bootstrap mechanism exists.


## compare_0546_page.py

Offline helper for EXP219. It parses the full 20-word `0546/count20` lines emitted by the EXP219 YAML, checks local frame stability, and compares the local page word-for-word with the stable genuine reference image observed in three independent captures.

Reference page:

```text
0546..0559 = [2,0,2,0,0,0,0,0,0,0,0,0,0,4,0,0,0,0,0,0]
```

Known fields are `0553 = Operation Mode` and `0559 = Link Integration`. The tool explicitly reports whether any differences remain outside `0553`.

Example:

```bash
python3 Research/tools/compare_0546_page.py exp219.log
```

This tool is offline-only and has no transport code.
