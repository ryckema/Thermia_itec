# V5DCM96 — offline onboarding provenance

Status: COMPLETE / POSITIVE (original Connect source comparison only), 2026-10-20.

Baseline: FAS1 user-verified RX_ONLY/HARD_DENY, EXP388 RUNNING/PARTIAL; original V49 rollback, old B11D initial anomaly still open. No bus transmission or flash.

The original device_client MQTT dispatcher subscribes to external SetDeviceInfo messages, and etlib exposes distinct optional `onboarding_completed` and `serial_number_config` fields. The CM930 handler accepts the message only in its waiting-for-info state, distinguishes completed onboarding from a desired eight-character serial update, and returns to information gathering on an absent response. Generic client publishes info and schedules a check after 60 seconds. Shared ApplicationState holds a separately received MasterSettings serial value. Hence controller-derived serial, externally requested serial and master-settings serial must not be conflated. External ATEC V3 remains third-party source, not local XTR proof. These source facts do not show that cloud onboarding is needed for purely local native access or that local write acceptance has occurred.

12 of 12 exact source-path checks passed offline. No ESPHome compilation. Unresolved: authorization, current native session, electrical role, native accepted writes. Next V97 offline analyze nonsecret state gates; keep current RX-only baseline and EXP388 partial.
