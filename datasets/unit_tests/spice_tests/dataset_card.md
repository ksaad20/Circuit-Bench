# SPICE Tests Dataset Card

## Dataset Name
SPICE Tests

## Version
v1.0.0

## Description
The SPICE Tests dataset contains automated circuit simulation test cases for validating the correctness, robustness, and reproducibility of SPICE-compatible simulators. The dataset is designed to benchmark simulation engines, verify expected circuit behavior, and support regression testing for analog, mixed-signal, and power electronic circuits.

---

## Purpose

The dataset is intended to:

- Validate SPICE simulation correctness
- Benchmark simulator performance
- Detect regression bugs
- Compare simulator outputs
- Support automated continuous integration (CI)
- Enable reproducible circuit simulation research

---

## Domain

Electronic Design Automation (EDA)

Circuit Simulation

Analog Electronics

Mixed-Signal Electronics

Power Electronics

RF Simulation

---

## Simulation Types

- DC Analysis
- AC Analysis
- Transient Analysis
- Noise Analysis
- Operating Point Analysis
- Parametric Sweep
- Temperature Sweep
- Monte Carlo Simulation
- Corner Analysis

---

## File Format

Supported files may include:

- `.cir`
- `.sp`
- `.net`
- `.raw`
- `.csv`
- `.json`
- `.yaml`

---

## Directory Structure

```
spice_tests/
├── dc/
├── ac/
├── transient/
├── noise/
├── monte_carlo/
├── corners/
├── temperature/
├── expected_outputs/
└── metadata/
```

---

## Input

Each test includes:

- Netlist
- Device models
- Simulation configuration
- Input sources
- Component values

---

## Output

Expected outputs may include:

- Voltage waveforms
- Current waveforms
- Frequency response
- Gain
- Phase
- Power
- Efficiency
- Noise spectrum
- Operating point values

---

## Evaluation Metrics

Possible metrics include:

- Root Mean Square Error (RMSE)
- Mean Absolute Error (MAE)
- Maximum Absolute Error
- Relative Error
- Simulation Runtime
- Memory Usage
- Convergence Success Rate

---

## Applications

- Simulator validation
- Regression testing
- Academic benchmarking
- CI/CD testing
- Model verification
- Circuit education
- EDA research

---

## Limitations

- Results depend on simulator implementation
- Numerical tolerances vary across simulators
- Device model support may differ

---

## Reproducibility

Each benchmark should specify:

- Simulator version
- Device model version
- Simulation settings
- Random seed (if applicable)
- Platform information

---

## Citation

If you use this dataset, please cite the associated Circuit-Bench publication and repository.

---

## License

Specify the applicable license (e.g., MIT, Apache-2.0, CC BY 4.0).

---

## Maintainers

Circuit-Bench Contributors

---

## Contact

Please open an issue or discussion in the repository for questions, bug reports, or contributions.

---

## Changelog

### v1.0.0

- Initial release
- Basic SPICE simulation test suite
- Standard benchmark organization
