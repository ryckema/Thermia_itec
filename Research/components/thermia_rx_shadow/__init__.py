"""Passive RX-only frame CRC shadow for ESPHome. No native emulation or TX."""
import esphome.codegen as cg
import esphome.config_validation as cv

CONFIG_SCHEMA = cv.Schema({})

async def to_code(config):
    cg.add_global(cg.RawStatement('#include "esphome/components/thermia_rx_shadow/thermia_rx_shadow.hpp"'))
