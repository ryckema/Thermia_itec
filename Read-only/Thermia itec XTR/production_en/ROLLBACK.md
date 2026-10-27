# ABORT / rollback

This ZIP deliberately contains **no private OEM or native write-firmware source**. Prior to flash, back up the actual currently installed, independently locally verified YAML/firmware and secrets. If essential readings, network connectivity, frame counts or bus integrity regress, stop this candidate and use ordinary ESPHome OTA/USB to restore that backup. Leave the Thermia controller and room sensor connected and operating. GPIO21 must remain DE LOW during passive mode. Never treat bus CRC alone as semantic validation.
