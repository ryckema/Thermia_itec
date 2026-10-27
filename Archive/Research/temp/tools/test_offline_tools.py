#!/usr/bin/env python3
"""Self-tests for offline Thermia research tooling."""

from pathlib import Path
from tempfile import TemporaryDirectory

from thermia_capture_analyzer import analyze
from thermia_dcm_reference_model_current import (
    DCMReferenceModelCurrent,
    ECO5_BOOTSTRAP,
    ECO5_REFRESHABLE,
    Phase,
    add_crc,
    build_fc16_request,
)


def test_current_model() -> None:
    m = DCMReferenceModelCurrent()
    req_0708 = bytes.fromhex("0f03070800064450")

    assert m.handle(req_0708) is None
    m.accept_approval()
    assert m.phase is Phase.WAIT_PAGE_SERVICE
    assert m.handle(req_0708) is None
    m.set_page_service_ready()
    assert m.phase is Phase.BOOTSTRAP

    for start, count in ECO5_BOOTSTRAP:
        words = [0] * count
        if start == 0x03E8:
            words[12] = 20
        if start == 0x042E:
            words[0] = 1
            words[1] = 1
        assert m.handle(build_fc16_request(start, words)) is not None

    assert m.phase is Phase.RUNTIME
    idle = m.handle(req_0708)
    assert idle is not None
    assert m.mailbox_words() == [0, 0, 0, 0, 0, 0]

    m.request_refresh(set(ECO5_REFRESHABLE))
    assert m.mailbox_words()[2:4] == [0xFFFF, 0x867F]

    for start, count in ECO5_BOOTSTRAP:
        if start in ECO5_REFRESHABLE:
            assert m.handle(build_fc16_request(start, [0] * count)) is not None
    assert m.refresh_pending == set()

    m.queue_desired_word(0x03E8, 0x03F4, 30)
    words = m.mailbox_words()
    assert words[0] == 0
    assert words[1] == 0x0001
    assert words[3] & 0x0001

    desired_req = add_crc(bytes.fromhex("0f0303e8000e"))
    desired_response = m.handle(desired_req)
    assert desired_response is not None
    assert desired_response[2] == 28
    assert m.mailbox_words()[1] == 0
    assert m.mailbox_words()[3] & 0x0001

    result_words = list(m.pending_desired.desired_words)
    assert m.handle(build_fc16_request(0x03E8, result_words)) is not None
    assert m.pending_desired.confirmed
    m.clear_confirmed_desired()

    try:
        m.queue_desired_word(0x0546, 0x0553, 1)
    except ValueError:
        pass
    else:
        raise AssertionError("0546 desired selector must remain unproven")


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
    test_current_model()
    test_analyzer()
    print("offline tool tests: OK")


if __name__ == "__main__":
    main()
