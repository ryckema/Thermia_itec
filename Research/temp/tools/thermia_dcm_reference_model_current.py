#!/usr/bin/env python3
"""Current offline reference model for the genuine Eco5/Thermia Online slave-0x0F role.

Evidence baseline:
- PROTO-OFFLINE-10: full-page desired-state pull/apply/confirm for 03E8 and 042E.
- PROTO-OFFLINE-17/18: approval accepted and page-service ready are separate states;
  no 120 s timer is encoded here because the delay is gateway/session behavior, not a
  proven universal controller requirement.
- PROTO-OFFLINE-19: fixed 32-page ACK-gated bootstrap through 06F4 before first 0708;
  later W2/W3 refresh is a separate 26-page worklist; W0 has never been observed non-zero;
  W4 is state/refresh metadata, not an exclusive next-page selector; Eco5 W5 is 0000.

SAFETY:
- Pure in-memory model. No serial, GPIO, socket, ESPHome, or network code.
- Unknown/unsupported requests return None.
- Desired-state responses are built only from a cached controller page, never guessed defaults.
- Only the two genuine desired selectors actually observed in captures are implemented:
  W1 bit0 -> 03E8 and W1 bit3 -> 042E.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Optional

SLAVE = 0x0F

ECO5_BOOTSTRAP = [
    (0x03E8, 14), (0x03FC, 11), (0x0410, 22), (0x042E, 15),
    (0x0442, 13), (0x0456, 12), (0x046A, 18), (0x047E, 19),
    (0x0492, 11), (0x04A6, 13), (0x04BA, 22), (0x04D8, 27),
    (0x04F6, 14), (0x050A, 19), (0x051E, 10), (0x0532, 18),
    (0x0546, 20), (0x055A, 33), (0x057B, 33), (0x059C, 33),
    (0x05BD, 33), (0x05DE, 33), (0x05FF, 33), (0x0620, 33),
    (0x0641, 33), (0x0662, 33), (0x0683, 33), (0x06A4, 33),
    (0x06C5, 33), (0x06EA, 7), (0x06F1, 3), (0x06F4, 19),
]
ECO5_BOOTSTRAP_COUNTS = dict(ECO5_BOOTSTRAP)
CONFIG_PAGE_INDEX = {start: i for i, (start, _) in enumerate(ECO5_BOOTSTRAP)}

ECO5_REFRESHABLE = {
    0x03E8, 0x03FC, 0x0410, 0x042E, 0x0442, 0x0456, 0x046A,
    0x04A6, 0x04BA, 0x0532,
    0x0546, 0x055A, 0x057B, 0x059C, 0x05BD, 0x05DE, 0x05FF, 0x0620,
    0x0641, 0x0662, 0x0683, 0x06A4, 0x06C5, 0x06EA, 0x06F1, 0x06F4,
}

DESIRED_W1_BITS = {
    0x03E8: 0,
    0x042E: 3,
}


class Phase(Enum):
    WAIT_APPROVAL = auto()
    WAIT_PAGE_SERVICE = auto()
    BOOTSTRAP = auto()
    RUNTIME = auto()


def modbus_crc(data: bytes) -> int:
    crc = 0xFFFF
    for b in data:
        crc ^= b
        for _ in range(8):
            crc = (crc >> 1) ^ 0xA001 if (crc & 1) else (crc >> 1)
    return crc & 0xFFFF


def add_crc(payload: bytes) -> bytes:
    crc = modbus_crc(payload)
    return payload + bytes((crc & 0xFF, (crc >> 8) & 0xFF))


def crc_ok(frame: bytes) -> bool:
    return len(frame) >= 4 and (frame[-2] | (frame[-1] << 8)) == modbus_crc(frame[:-2])


def be16(v: int) -> bytes:
    return bytes(((v >> 8) & 0xFF, v & 0xFF))


def u16(frame: bytes, pos: int) -> int:
    return (frame[pos] << 8) | frame[pos + 1]


def words_to_bytes(words: list[int]) -> bytes:
    return b"".join(be16(v & 0xFFFF) for v in words)


def bytes_to_words(data: bytes) -> list[int]:
    if len(data) % 2:
        raise ValueError("word data must have even byte length")
    return [u16(data, i) for i in range(0, len(data), 2)]


def build_fc16_request(start: int, words: list[int]) -> bytes:
    data = words_to_bytes(words)
    payload = bytes((SLAVE, 0x10)) + be16(start) + be16(len(words)) + bytes((len(data),)) + data
    return add_crc(payload)


@dataclass
class PendingDesired:
    page_start: int
    target_addr: int
    desired_words: list[int]
    pulled: bool = False
    confirmed: bool = False


@dataclass
class DCMReferenceModelCurrent:
    phase: Phase = Phase.WAIT_APPROVAL
    bootstrap_index: int = 0
    page_cache: dict[int, list[int]] = field(default_factory=dict)
    refresh_pending: set[int] = field(default_factory=set)
    pending_desired: Optional[PendingDesired] = None
    w4: int = 0
    w5: int = 0

    def accept_approval(self) -> None:
        if self.phase is not Phase.WAIT_APPROVAL:
            raise RuntimeError(f"approval not valid in phase {self.phase.name}")
        self.phase = Phase.WAIT_PAGE_SERVICE

    def set_page_service_ready(self) -> None:
        if self.phase is not Phase.WAIT_PAGE_SERVICE:
            raise RuntimeError(f"page service not valid in phase {self.phase.name}")
        self.bootstrap_index = 0
        self.phase = Phase.BOOTSTRAP

    @property
    def expected_bootstrap(self) -> Optional[tuple[int, int]]:
        if self.phase is not Phase.BOOTSTRAP:
            return None
        return ECO5_BOOTSTRAP[self.bootstrap_index]

    def request_refresh(self, page_starts: set[int]) -> None:
        if self.phase is not Phase.RUNTIME:
            raise RuntimeError("refresh may be requested only in RUNTIME")
        unsupported = set(page_starts) - ECO5_REFRESHABLE
        if unsupported:
            bad = ", ".join(f"{x:04X}" for x in sorted(unsupported))
            raise ValueError(f"not proven Eco5 refreshable: {bad}")
        self.refresh_pending |= set(page_starts)

    def queue_desired_word(self, page_start: int, target_addr: int, value: int) -> None:
        if self.phase is not Phase.RUNTIME:
            raise RuntimeError("desired command may be queued only in RUNTIME")
        if self.pending_desired is not None:
            raise RuntimeError("one desired transaction at a time")
        if page_start not in DESIRED_W1_BITS:
            raise ValueError("desired selector not proven in genuine corpus")
        current = self.page_cache.get(page_start)
        if current is None:
            raise RuntimeError("no current controller page cached")
        offset = target_addr - page_start
        if offset < 0 or offset >= len(current):
            raise ValueError("target address outside cached page")
        desired = list(current)
        desired[offset] = value & 0xFFFF
        self.pending_desired = PendingDesired(page_start, target_addr, desired)
        self.refresh_pending.add(page_start)

    def mailbox_words(self) -> list[int]:
        w0 = 0
        w1 = 0
        if self.pending_desired is not None and not self.pending_desired.pulled:
            w1 |= 1 << DESIRED_W1_BITS[self.pending_desired.page_start]

        w2 = 0
        w3 = 0
        for start in self.refresh_pending:
            idx = CONFIG_PAGE_INDEX[start]
            if idx < 16:
                w3 |= 1 << idx
            else:
                w2 |= 1 << (idx - 16)
        return [w0, w1, w2, w3, self.w4 & 0xFFFF, self.w5 & 0xFFFF]

    def handle(self, request: bytes) -> Optional[bytes]:
        if not crc_ok(request) or len(request) < 4 or request[0] != SLAVE:
            return None
        if request[1] == 0x10:
            return self._handle_fc16(request)
        if request[1] == 0x03:
            return self._handle_fc03(request)
        return None

    def _handle_fc16(self, request: bytes) -> Optional[bytes]:
        if len(request) < 9:
            return None
        start, count, byte_count = u16(request, 2), u16(request, 4), request[6]
        if byte_count != count * 2 or len(request) != 9 + byte_count:
            return None
        words = bytes_to_words(request[7:7 + byte_count])

        if self.phase is Phase.BOOTSTRAP:
            expected = ECO5_BOOTSTRAP[self.bootstrap_index]
            if (start, count) != expected:
                return None
            self.page_cache[start] = words
            ack = add_crc(bytes((SLAVE, 0x10)) + be16(start) + be16(count))
            self.bootstrap_index += 1
            if self.bootstrap_index == len(ECO5_BOOTSTRAP):
                self.phase = Phase.RUNTIME
            return ack

        if self.phase is not Phase.RUNTIME:
            return None

        expected_count = ECO5_BOOTSTRAP_COUNTS.get(start)
        if expected_count != count:
            return None

        if self.pending_desired is not None and start == self.pending_desired.page_start:
            self.page_cache[start] = words
            self.pending_desired.confirmed = words == self.pending_desired.desired_words
            self.refresh_pending.discard(start)
            return add_crc(bytes((SLAVE, 0x10)) + be16(start) + be16(count))

        if start in self.refresh_pending:
            self.page_cache[start] = words
            self.refresh_pending.discard(start)
            return add_crc(bytes((SLAVE, 0x10)) + be16(start) + be16(count))

        return None

    def clear_confirmed_desired(self) -> None:
        if self.pending_desired is None:
            return
        if not self.pending_desired.confirmed:
            raise RuntimeError("desired transaction is not confirmed")
        self.pending_desired = None

    def _handle_fc03(self, request: bytes) -> Optional[bytes]:
        if len(request) != 8 or self.phase is not Phase.RUNTIME:
            return None
        start, count = u16(request, 2), u16(request, 4)

        if (start, count) == (0x0708, 6):
            data = words_to_bytes(self.mailbox_words())
            return add_crc(bytes((SLAVE, 0x03, len(data))) + data)

        if self.pending_desired is not None and start == self.pending_desired.page_start:
            desired = self.pending_desired.desired_words
            if count != len(desired):
                return None
            data = words_to_bytes(desired)
            response = add_crc(bytes((SLAVE, 0x03, len(data))) + data)
            self.pending_desired.pulled = True
            return response

        return None


def _selftest() -> None:
    m = DCMReferenceModelCurrent()
    poll = bytes.fromhex("0f03070800064450")

    assert m.handle(poll) is None
    m.accept_approval()
    assert m.handle(poll) is None
    m.set_page_service_ready()

    for start, count in ECO5_BOOTSTRAP:
        words = [0] * count
        if start == 0x03E8:
            words[12] = 20
        assert m.handle(build_fc16_request(start, words)) is not None
    assert m.phase is Phase.RUNTIME

    idle = m.handle(poll)
    assert idle is not None
    assert idle[3:15] == bytes(12)

    m.queue_desired_word(0x03E8, 0x03F4, 30)
    mb = m.mailbox_words()
    assert mb[0] == 0 and mb[1] == 0x0001 and mb[3] & 0x0001
    desired_req = add_crc(bytes.fromhex("0f0303e8000e"))
    desired_resp = m.handle(desired_req)
    assert desired_resp is not None and desired_resp[2] == 28
    assert m.mailbox_words()[1] == 0
    assert m.mailbox_words()[3] & 0x0001

    result_words = list(m.pending_desired.desired_words)
    assert m.handle(build_fc16_request(0x03E8, result_words)) is not None
    assert m.pending_desired.confirmed
    assert 0x03E8 not in m.refresh_pending
    m.clear_confirmed_desired()

    try:
        m.queue_desired_word(0x0546, 0x0553, 1)
    except ValueError:
        pass
    else:
        raise AssertionError("0546 desired selector must remain unproven")

    print("current reference-model selftest: OK")


if __name__ == "__main__":
    _selftest()
