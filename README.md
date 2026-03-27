# PDV Simulated Data

Tools for generating synthetic **Photonic Doppler Velocimetry (PDV)** signals from user-supplied velocity-time histories.

## File Overview

| File | Purpose |
|------|---------|
| `pdv_synthesis.py` | Core library — velocity → PDV voltage conversion functions |
| `run_pdv_synthesis.py` | Entry-point script — run synthesis from the command line |
| `PDV_gen_run.ipynb` | Interactive notebook — exploration, visualization, and spectrograms |
| `output/waveform.csv` | Output: single-point PDV voltage vs. time |
| `output/waveform_multi.csv` | Output: multi-point (composite) PDV voltage vs. time |

---

## Quick Start

### Command-line

```bash
python run_pdv_synthesis.py
```

Edit `SHOT_TYPE`, `SAMPLE_RATE`, and `NOISE_SD` at the top of that file to change parameters.  Outputs are written to `waveform.csv` and `waveform_multi.csv`.

### In your own script

```python
from pdv_synthesis import generate_velocity_profile, velocity_to_pdv_voltage

time, velocity = generate_velocity_profile("HEL", sample_rate=128e9)

voltage = velocity_to_pdv_voltage(
    time,
    velocity,
    noise_sd=0.1,
    output_csv="waveform.csv",   # omit to skip saving
)
```

Bring your own velocity array instead of using `generate_velocity_profile`:

```python
import numpy as np
from pdv_synthesis import velocity_to_pdv_voltage

time = np.arange(0, 1e-6, 1 / 128e9)   # 1 µs at 128 GHz
velocity = np.linspace(0, 500, len(time))  # ramp to 500 m/s

voltage = velocity_to_pdv_voltage(time, velocity, output_csv="my_waveform.csv")
```

---

## `pdv_synthesis.py` API

### `generate_velocity_profile(shot_type, sample_rate, **kwargs)`
Returns `(time, velocity)` arrays for a named shot type.
Supported `shot_type` values: `"velocity"`, `"HEL"`, `"HEL-spall"`.
Pass keyword arguments to override any default parameter (e.g., `vel_peak=400`).

### `velocity_to_pdv_voltage(time, velocity, ...)`
Converts a velocity-time history to a **single-point** heterodyne PDV beat signal.

| Parameter | Default | Description |
|-----------|---------|-------------|
| `lambda_ref` | 1550 nm | Reference laser wavelength |
| `lambda_tar` | 1550.016 nm | Target laser wavelength |
| `power_ref_dbm` | 0 dBm | Reference beam power |
| `power_signal_dbm` | −1 dBm | Return signal power |
| `noise_sd` | 0.1 | Multiplicative Gaussian noise std dev |
| `output_csv` | `None` | Path to save CSV (skipped if `None`) |

Returns: `voltage` (`np.ndarray`)

### `velocity_to_multipoint_pdv_voltage(time, velocity, ...)`
Same as above but synthesizes `num_points` independent PDV channels and sums them into a single composite waveform.

| Parameter | Default | Description |
|-----------|---------|-------------|
| `num_points` | 2 | Number of PDV channels |
| `ref_lambdas_nm` | `[1531.116, 1537.397, 1543.730]` | Per-channel reference wavelengths (nm) |
| `beat_freqs_ghz` | `[3, 7, 10]` | Per-channel heterodyne beat frequencies (GHz) |
| `output_csv` | `None` | Path to save CSV |

Returns: `voltage_multi` (`np.ndarray`)

### `compute_stft(voltage, fs, ...)`
Wrapper around SciPy `ShortTimeFFT` with zero-padded boundaries and legacy-compatible time axis.
Returns `(f, t, Zxx)`.

### `load_waveform_csv(filepath)`
Loads a previously saved CSV.
Returns `(time, voltage)`.

---

## Dependencies

- Python 3.x
- NumPy
- Matplotlib
- SciPy

```bash
pip install numpy matplotlib scipy
```

---

## Notes

- Phase calculations follow heterodyne PDV principles: the beat signal encodes the round-trip Doppler phase $\phi(t) = 4\pi L(t)/\lambda$.
- Noise is multiplicative Gaussian, scaled to signal amplitude.
- STFT parameters (`nperseg`, `noverlap`, `nfft`) are tunable in the notebook or via `compute_stft`.

## License

[Add license information if applicable]
