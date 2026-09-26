#!/usr/bin/env python3
"""Self-tests for offline Thermia research tooling."""

from pathlib import Path
from tempfile import TemporaryDirectory

from thermia_capture_analyzer import analyze
from thermia_dcm_reference_model import DCMReferenceModel, add_crc


def test_model() -> None:
    m = DCMReferenceModel()
    req_0708 = bytes.fromhex("0f03070800064450")
    assert m.handle(req_0708).hex() == "0f030c0000000000000000000000069d76"

    m.heat_curve = 23
    assert m.mailbox_words[1] == 1
    assert m.handle(req_0708).hex() == "0f030c00000001000000000000000690e6"
    heat_req = bytes.fromhex("0f0303e8000d0551")
    heat_response = m.handle(heat_req)
    assert heat_response is not None and heat_response[2] == 26
    assert m.mailbox_words[1] == 0

    m.operation_mode = 1
    assert m.mailbox_words[0] == 1
    system_req = add_crc(bytes.fromhex("0f0305460014"))
    system_response = m.handle(system_req)
    assert system_response is not None and system_response[2] == 40
    assert m.mailbox_words[0] == 0

    write_0864 = bytes.fromhex("0f1008640004080000000000000016d7b7")
    assert m.handle(write_0864).hex() == "0f1008640004835b"


def test_analyzer() -> None:
    with TemporaryDirectory() as td:
        p = Path(td) / "positive.log"
        p.write_text(
            "0.031 0217a7f8000da80c00070e00400000002800050005000c05005cf9\n"
            "1.179 a50300000012dce3\n"
            "33.180 0f03070800064450\n"
            "33.204 0f030c0000000000000000008000069c9e\n"
            "33.915 0f1007d00013260016001aff9c002f0026ff9cff9cff9cff9cff9c000e0024000a004000000028000a000a000c277c\n"
        )
        a = analyze(p)
        assert a.extended_topology_seen
        assert a.a811 == 0x000C and a.a812 == 0x0500
        assert a.first_a5 == 1.179
        assert a.first_0708_poll == 33.180
        assert a.first_runtime_fc16 == 33.915

    with TemporaryDirectory() as td:
        p = Path(td) / "negative.log"
        p.write_text("1.000 0a17b3b00003b3c4000306000e001400004d92\n")
        a = analyze(p)
        assert not a.extended_topology_seen
        assert a.evidence_count == 0


def main() -> None:
    test_model()
    test_analyzer()
    print("offline tool tests: OK")


if __name__ == "__main__":
    main()
