#!/usr/bin/env python3
"""Offline reference model for the observed Thermia DCM slave-0x0F role.

SAFETY
------
This module contains NO serial, GPIO, socket, or ESPHome code. It cannot transmit
on a Thermia bus. It only maps request bytes to response bytes in memory and is
intended for replay/unit testing before any hardware emulator is considered.

Scope is deliberately fail-closed:
- FC16: ACK only syntactically valid slave-0x0F writes whose start/count shape is
  on the observed allow-list.
- FC03: answer only the observed mailbox pages 0708/count6, 03E8/count13 and
  0546/count20.
- all other requests return None.

The model implements EXP212 selector semantics:
- mailbox word1 selects 03E8/count13 and clears after that page is fetched;
- mailbox word0 selects 0546/count20 and clears after that page is fetched.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional


OBSERVED_FC16_SHAPES = {
    (0x03E8, 13), (0x03FC, 11), (0x0410, 21), (0x042E, 15),
    (0x0442, 13), (0x0456, 12), (0x046A, 18), (0x047E, 19),
    (0x0492, 9), (0x04A6, 13), (0x04BA, 22), (0x04D8, 27),
    (0x04F6, 14), (0x050A, 19), (0x051E, 9), (0x0532, 18),
    (0x0546, 20), (0x055A, 33), (0x057B, 33), (0x059C, 33),
    (0x05BD, 33), (0x05DE, 33), (0x05FF, 33), (0x0620, 33),
    (0x0641, 33), (0x06EA, 7), (0x06F1, 3), (0x06F4, 19),
    (0x07D0, 19), (0x07E4, 17), (0x07F8, 17), (0x080C, 18),
    (0x0820, 18), (0x0834, 18), (0x0848, 23), (0x085F, 5),
    (0x0864, 4), (0x0870, 17), (0x0884, 60),
}


def modbus_crc(data: bytes) -> int:
    crc = 0xFFFF
    for b in data:
        crc ^= b
        for _ in range(8):
            if crc & 1:
                crc = (crc >> 1) ^ 0xA001
            else:
                crc >>= 1
    return crc & 0xFFFF


def add_crc(payload: bytes) -> bytes:
    crc = modbus_crc(payload)
    return payload + bytes((crc & 0xFF, (crc >> 8) & 0xFF))


def crc_ok(frame: bytes) -> bool:
    if len(frame) < 4:
        return False
    got = frame[-2] | (frame[-1] << 8)
    return modbus_crc(frame[:-2]) == got


def be16(v: int) -> bytes:
    return bytes(((v >> 8) & 0xFF, v & 0xFF))


def u16(frame: bytes, pos: int) -> int:
    return (frame[pos] << 8) | frame[pos + 1]


def words_to_bytes(words: list[int]) -> bytes:
    return b"".join(be16(v & 0xFFFF) for v in words)


@dataclass
class DCMReferenceModel:
    mailbox_words: list[int] = field(default_factory=lambda: [0, 0, 0, 0, 0, 6])
    heating_page: list[int] = field(
        default_factory=lambda: [22, 20, 40, 0, 1, 1, 18, 18, 2, 40, 30, 60, 21]
    )
    system_page: list[int] = field(
        default_factory=lambda: [
            2, 0, 2, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 4, 0, 0, 0, 0, 0, 0,
        ]
    )

    def set_heating_dirty(self, dirty: bool = True) -> None:
        self.mailbox_words[1] = 1 if dirty else 0

    def set_system_dirty(self, dirty: bool = True) -> None:
        self.mailbox_words[0] = 1 if dirty else 0

    @property
    def operation_mode(self) -> int:
        return self.system_page[13]

    @operation_mode.setter
    def operation_mode(self, value: int) -> None:
        self.system_page[13] = value & 0xFFFF
        self.set_system_dirty(True)

    @property
    def link_integration(self) -> int:
        return self.system_page[19]

    @link_integration.setter
    def link_integration(self, value: int) -> None:
        self.system_page[19] = value & 0xFFFF
        self.set_system_dirty(True)

    @property
    def heat_curve(self) -> int:
        return self.heating_page[0]

    @heat_curve.setter
    def heat_curve(self, value: int) -> None:
        self.heating_page[0] = value & 0xFFFF
        self.set_heating_dirty(True)

    @property
    def room_target(self) -> int:
        return self.heating_page[12]

    @room_target.setter
    def room_target(self, value: int) -> None:
        self.heating_page[12] = value & 0xFFFF
        self.set_heating_dirty(True)

    def handle(self, request: bytes) -> Optional[bytes]:
        """Return an offline response frame, or None for unsupported input."""
        if not crc_ok(request) or len(request) < 4 or request[0] != 0x0F:
            return None

        fn = request[1]
        if fn == 0x10:
            return self._handle_fc16(request)
        if fn == 0x03:
            return self._handle_fc03(request)
        return None

    def _handle_fc16(self, request: bytes) -> Optional[bytes]:
        if len(request) < 9:
            return None
        start, count, byte_count = u16(request, 2), u16(request, 4), request[6]
        if len(request) != 9 + byte_count or byte_count != count * 2:
            return None
        if (start, count) not in OBSERVED_FC16_SHAPES:
            return None
        return add_crc(bytes((0x0F, 0x10)) + be16(start) + be16(count))

    def _handle_fc03(self, request: bytes) -> Optional[bytes]:
        if len(request) != 8:
            return None
        start, count = u16(request, 2), u16(request, 4)

        if (start, count) == (0x0708, 6):
            data = words_to_bytes(self.mailbox_words)
            return add_crc(bytes((0x0F, 0x03, len(data))) + data)

        if (start, count) == (0x03E8, 13):
            data = words_to_bytes(self.heating_page)
            response = add_crc(bytes((0x0F, 0x03, len(data))) + data)
            self.set_heating_dirty(False)
            return response

        if (start, count) == (0x0546, 20):
            data = words_to_bytes(self.system_page)
            response = add_crc(bytes((0x0F, 0x03, len(data))) + data)
            self.set_system_dirty(False)
            return response

        return None


def _selftest() -> None:
    m = DCMReferenceModel()

    req_0708 = bytes.fromhex("0f03070800064450")
    assert m.handle(req_0708).hex() == "0f030c0000000000000000000000069d76"

    m.set_heating_dirty(True)
    assert m.handle(req_0708).hex() == "0f030c00000001000000000000000690e6"
    req_heat = bytes.fromhex("0f0303e8000d0551")
    heat_resp = m.handle(req_heat)
    assert heat_resp is not None and heat_resp[2] == 26
    assert m.mailbox_words[1] == 0

    m.set_system_dirty(True)
    system_poll = m.handle(req_0708)
    assert system_poll is not None and system_poll[3:5] == b"\x00\x01"
    req_system = add_crc(bytes.fromhex("0f0305460014"))
    sys_resp = m.handle(req_system)
    assert sys_resp is not None and sys_resp[2] == 40
    assert m.mailbox_words[0] == 0

    req_0864 = bytes.fromhex("0f1008640004080000000000000016d7b7")
    assert m.handle(req_0864).hex() == "0f1008640004835b"

    unknown = add_crc(bytes.fromhex("0f1001230001020001"))
    assert m.handle(unknown) is None

    print("selftest: OK")


if __name__ == "__main__":
    _selftest()
