#pragma once
// Public passive, RX-only shadow. Never writes, emits, or responds on a bus.
// This is NOT the full original proprietary portable engine.
#include <cstddef>
#include <cstdint>
#include <vector>

namespace thermia_public {
class RxShadow {
 public:
  struct Result {
    bool valid;
    bool crc_ok;
    std::size_t size;
  };
  static uint16_t crc16(const uint8_t *p, size_t n) {
    uint16_t crc = 0xFFFF;
    for (size_t i = 0; i < n; ++i) {
      crc ^= p[i];
      for (unsigned b = 0; b < 8; ++b)
        crc = (crc & 1u) ? uint16_t((crc >> 1) ^ 0xA001u) : uint16_t(crc >> 1);
    }
    return crc;
  }
  Result inspect(const std::vector<uint8_t> &frame) const {
    if (frame.size() < 4) return {false, false, frame.size()};
    const uint16_t received = uint16_t(frame[frame.size()-2]) |
                              (uint16_t(frame.back()) << 8);
    const bool crc_ok = (crc16(frame.data(), frame.size()-2) == received);
    return {crc_ok, crc_ok, frame.size()};
  }
};
}  // namespace thermia_public
