# PDV Simulated Data Generator

This Jupyter notebook (`PDV_gen_run.ipynb`) generates simulated Photonic Doppler Velocimetry (PDV) data from synthetic velocity time histories. It simulates various shot types (velocity, HEL, spall, HEL-spall), computes the corresponding voltage signals, adds noise, and produces spectrograms for analysis.

## Features

- **Synthetic Velocity Profiles**: Defines piecewise linear velocity time histories for different experimental scenarios.
- **PDV Signal Simulation**: Converts velocity data to phase differences and voltage signals using PDV principles.
- **Noise Addition**: Incorporates Gaussian noise to simulate real-world measurements.
- **Spectrogram Generation**: Computes Short-Time Fourier Transform (STFT) spectrograms for frequency analysis over time.
- **Data Export**: Outputs voltage-time data to CSV files for further processing.

## Dependencies

- Python 3.x
- NumPy
- Matplotlib
- SciPy

Install dependencies using pip:

```bash
pip install numpy matplotlib scipy
```

## Usage

1. Open the notebook in Jupyter Lab or Jupyter Notebook.
2. Modify parameters as needed (e.g., `shot_type`, `sample_rate`, `noise_sd`).
3. Execute the cells sequentially.
4. View generated plots and spectrograms inline.
5. Check output CSV files: `waveform.csv` and `waveform_multi.csv`.

## Parameters

- `shot_type`: Choose from "velocity", "HEL", "spall", or "HEL-spall".
- `sample_rate`: Sampling frequency (default: 128 GHz).
- `lambda_ref` and `lambda_tar`: Reference and target wavelengths (default: 1550 nm variants).
- `noise_sd`: Standard deviation of added Gaussian noise (default: 0.1).

## Output Files

- `waveform.csv`: Single-channel voltage-time data.
- `waveform_multi.csv`: Multi-channel voltage-time data (if applicable).
- Inline plots: Velocity profile, voltage signal, and spectrogram.

## Notes

- The notebook uses SciPy's ShortTimeFFT for spectrogram computation, ensuring compatibility with modern SciPy versions.
- Time arrays are adjusted to match legacy STFT behavior for consistency.

## Troubleshooting

- Ensure all dependencies are installed.
- If plots do not display, check Matplotlib backend configuration.
- For large datasets, increase memory allocation or reduce `sample_rate`.

## License

[Add license information if applicable]
