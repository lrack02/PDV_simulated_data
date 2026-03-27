"""
run_pdv_synthesis.py
--------------------
Entry-point script: generates synthetic single-point and multi-point PDV
waveforms and saves them to CSV.

Edit the parameters below to change the shot type, noise level, or output paths,
then run:

    python run_pdv_synthesis.py
"""

import os

from pdv_synthesis import (
    generate_velocity_profile,
    velocity_to_pdv_voltage,
    velocity_to_multipoint_pdv_voltage,
)

# ---------------------------------------------------------------------------
# Parameters
# ---------------------------------------------------------------------------
SHOT_TYPE   = "HEL"       # "velocity" | "HEL" | "HEL-spall"
SAMPLE_RATE = 128e9        # Hz
NOISE_SD    = 0.1

OUTPUT_DIR       = "output"
SINGLE_POINT_CSV = os.path.join(OUTPUT_DIR, "waveform.csv")
MULTI_POINT_CSV  = os.path.join(OUTPUT_DIR, "waveform_multi.csv")

os.makedirs(OUTPUT_DIR, exist_ok=True)

# ---------------------------------------------------------------------------
# Single-point synthesis
# ---------------------------------------------------------------------------
time, velocity = generate_velocity_profile(SHOT_TYPE, sample_rate=SAMPLE_RATE)

voltage = velocity_to_pdv_voltage(
    time,
    velocity,
    noise_sd=NOISE_SD,
    output_csv=SINGLE_POINT_CSV,
)

print(f"Single-point waveform saved → {SINGLE_POINT_CSV}  ({len(voltage)} samples)")

# ---------------------------------------------------------------------------
# Multi-point synthesis
# ---------------------------------------------------------------------------
voltage_multi = velocity_to_multipoint_pdv_voltage(
    time,
    velocity,
    num_points=2,
    noise_sd=NOISE_SD,
    output_csv=MULTI_POINT_CSV,
)

print(f"Multi-point waveform saved  → {MULTI_POINT_CSV}  ({len(voltage_multi)} samples)")
