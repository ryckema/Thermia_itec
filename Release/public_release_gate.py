#!/usr/bin/env python3
"""Conservative LOCAL source audit: never authenticates, flashes or opens network sockets.
Use before submitting Thermia firmware code for public review.
Passing does NOT establish rights, safety, or controller compatibility.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import re
from pathlib import Path

REVIEW_RULES = {
    "recorded_challenge_response": [
        r"\bknown_challenge\b",
        r"\bknown_response\b",
        r"\bbuild_native_fc23_response\b",
        r"\bFC23_R1_REPLAY\b",
    ],
    "historical_private_session_paths": [
        r"\bxxtea\b", r"\bC5DE\b", r"\bC5CG\b",
        r"\bC5BB\b", r"\bc5cv_export_join_tx_enabled\b",
    ],
    "native_tx_needs_provenance_and_scope_review": [
        r"\bs92_tx_owner_send\s*\(", r"\bwrite_array\s*\(",
        r"\btx_pin\s*:", r"\b0x0708\b",
    ],
    "unverified_calendar_writes": [
        r"\bcal32_new_domain_apply\b",
        r"\bCAL32_TRIAL_ARMED\b",
        r"\bcal32_arm_targets\b",
    ],
    "inline_credentials": [
        r"(?im)^\s*(?:password|api_key|encryption_key)\s*:\s*(?!\s*!secret\b)[^\s#][^\n]*$",
    ],
}

def audit(path: Path) -> dict:
    data = path.read_bytes()
    source = data.decode("utf-8")
    findings = {
        kind: sum(len(re.findall(pattern, source, re.I)) for pattern in patterns)
        for kind, patterns in REVIEW_RULES.items()
    }
    findings = {key: value for key, value in findings.items() if value}
    if path.suffix.lower() in {".bin", ".elf", ".raucb", ".log"}:
        findings["binary_or_live_capture"] = 1
    return {
        "sha256": hashlib.sha256(data).hexdigest(),
        "bytes": len(data),
        "static_gate": "HOLD" if findings else "PASS_STATIC_ONLY",
        "review_categories": findings,
        "manual_rights_and_provenance_review_required": True,
        "manual_model_scoped_target_and_live_validation_required": True,
        "authorized_for_public_firmware_release": False,
    }

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("candidate", type=Path)
    arguments = parser.parse_args()
    if not arguments.candidate.is_file():
        parser.error("candidate must be a file")
    result = audit(arguments.candidate)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 2 if result["review_categories"] else 0

if __name__ == "__main__":
    raise SystemExit(main())
