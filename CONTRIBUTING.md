# Contributing to CircuitBench

First and foremost, thank you for your interest in contributing to **CircuitBench**.

CircuitBench is an open-source benchmark designed to establish a reproducible, standardized framework for evaluating machine learning methods in electrical circuit design, simulation, optimization, and surrogate modeling. Our goal is to provide the research community with transparent datasets, simulation pipelines, benchmark tasks, and evaluation protocols that can be reproduced across different computing environments.

We welcome contributions from researchers, students, engineers, and software developers.

---

# Table of Contents

- Code of Conduct
- Ways to Contribute
- Before You Start
- Development Workflow
- Repository Structure
- Coding Standards
- Documentation Standards
- Benchmark Requirements
- Dataset Contributions
- Pull Request Process
- Issue Reporting
- Licensing
- Citation

---

# Code of Conduct

We are committed to maintaining a respectful, inclusive, and collaborative research environment.

Please:

- Be respectful.
- Discuss ideas scientifically.
- Welcome constructive criticism.
- Focus discussions on technical merit.
- Avoid personal attacks.

---

# Ways to Contribute

Contributions may include:

- New electrical circuit topologies
- SPICE simulation files
- PySpice automation
- Benchmark datasets
- Machine learning models
- Evaluation metrics
- Documentation
- Bug fixes
- Performance improvements
- Reproducibility improvements
- Visualization tools
- Tutorials
- Unit tests

---

# Before You Start

Before beginning substantial work, please:

1. Search existing Issues.
2. Open a Discussion if your contribution changes the benchmark structure.
3. Explain your proposed contribution.
4. Wait for feedback before implementing large changes.

---

# Development Workflow

1. Fork the repository.

2. Clone your fork.

```bash
git clone https://github.com/your_username/CircuitBench.git
```

3. Create a new branch.

```bash
git checkout -b feature/my-feature
```

4. Make changes.

5. Run tests.

6. Commit using descriptive commit messages.

Example:

```
Add op-amp benchmark dataset
```

7. Push your branch.

```bash
git push origin feature/my-feature
```

8. Submit a Pull Request.

---

# Repository Structure

```
CircuitBench/

circuits/
datasets/
benchmarks/
simulations/
src/
tests/
notebooks/
docs/
paper/
```

Please place new files in their appropriate directories.

---

# Coding Standards

Python code should follow:

- PEP 8
- Meaningful variable names
- Type hints where appropriate
- Docstrings for public functions
- Clear comments for non-trivial algorithms

Example:

```python
def simulate_circuit(netlist: str) -> SimulationResult:
    """
    Executes a SPICE simulation and returns the parsed results.
    """
```

---

# Simulation Standards

Supported simulation tools include:

- ngspice
- PySpice
- Xyce
- OpenModelica (where applicable)

Every simulation should include:

- Circuit schematic
- Netlist
- Component values
- Simulation parameters
- Expected outputs

Simulation scripts should execute without manual intervention.

---

# Benchmark Requirements

Every benchmark contribution should include:

- Scientific motivation
- Problem description
- Dataset source
- Circuit description
- Evaluation protocol
- Performance metrics
- Runtime information
- Hardware specifications

Benchmarks must be reproducible.

---

# Dataset Contributions

Datasets should include:

- Description
- License
- Source
- Citation
- Variables
- Units
- Data dictionary

Avoid proprietary datasets whenever possible.

Open datasets are strongly encouraged.

---

# Machine Learning Contributions

Models should include:

- Training script
- Evaluation script
- Hyperparameters
- Dependencies
- Random seed
- Hardware information

Whenever possible, include pretrained weights.

---

# Documentation

Documentation should be written clearly and technically.

Every new feature should include:

- Description
- Example usage
- Expected outputs
- Limitations

---

# Testing

All contributions should include appropriate tests.

Examples include:

- Unit tests
- Integration tests
- Simulation verification
- Dataset integrity checks

---

# Pull Request Checklist

Before submitting a Pull Request, ensure:

- [ ] Code compiles
- [ ] Tests pass
- [ ] Documentation updated
- [ ] Benchmark results reproduced
- [ ] No unnecessary files committed
- [ ] Commit history is clean

---

# Reporting Issues

When reporting issues, include:

- Operating system
- Python version
- Package versions
- Error messages
- Minimal reproducible example

Bug reports should be as detailed as possible.

---

# Feature Requests

Feature requests should explain:

- The problem
- Proposed solution
- Expected benefits
- Possible implementation

---

# Citation

If you use CircuitBench in your research, please cite the repository using the provided `CITATION.cff` file.

---

# License

By contributing to CircuitBench, you agree that your contributions will be released under the repository's open-source license.

---

# Acknowledgements

We sincerely appreciate every contribution that improves CircuitBench.

Whether you contribute code, documentation, datasets, simulations, or ideas, your efforts help build a transparent and reproducible benchmark for the electrical engineering and machine learning communities.
