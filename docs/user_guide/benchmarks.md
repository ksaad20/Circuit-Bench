# CircuitBench Benchmarks

## Overview

CircuitBench benchmarks provide standardized evaluation tasks for machine learning, optimization algorithms, and simulation tools in electrical engineering.

Each benchmark consists of:

- Circuit definitions
- Simulation protocols
- Training and testing datasets
- Evaluation metrics
- Baseline models
- Reference results

The goal is to ensure reproducible and fair comparisons between algorithms.

---

# Benchmark Structure

```
benchmark/
│
├── benchmark.yaml
├── README.md
├── evaluate.py
├── metrics.py
├── baseline_results.csv
├── leaderboard.csv
└── datasets/
```

---

# Benchmark Categories

## Passive Circuits

- RC Filters
- RL Filters
- RLC Networks
- Voltage Dividers

---

## Analog Circuits

- Operational Amplifiers
- Differential Amplifiers
- Current Mirrors
- Cascode Amplifiers
- Oscillators

---

## Digital Circuits

- Logic Gates
- Flip-Flops
- Counters
- Multiplexers
- Adders

---

## Power Electronics

- Buck Converters
- Boost Converters
- Inverters
- Rectifiers
- Battery Chargers

---

## RF

- LNAs
- Mixers
- Matching Networks
- Oscillators
- Power Amplifiers

---

# Supported Tasks

CircuitBench currently supports

- Regression
- Classification
- Fault Detection
- Optimization
- Circuit Parameter Prediction
- Transfer Learning
- Out-of-Distribution Evaluation

---

# Running a Benchmark

```bash
python benchmark.py --benchmark rc_lowpass
```

---

# Evaluation Metrics

Regression

- RMSE
- MAE
- MSE
- R²

Classification

- Accuracy
- Precision
- Recall
- F1 Score
- ROC AUC

---

# Baseline Models

Examples include

- Linear Regression
- Random Forest
- XGBoost
- CatBoost
- MLP
- Graph Neural Networks

---

# Leaderboards

Each benchmark maintains a leaderboard containing

- Model Name
- Version
- Evaluation Metric
- Submission Date

---

# Creating New Benchmarks

1. Create a new folder
2. Add benchmark.yaml
3. Add datasets
4. Define evaluation metrics
5. Implement evaluate.py
6. Run validation

---

# Best Practices

- Use reproducible random seeds.
- Keep training and testing data separate.
- Report all required metrics.
- Include model configuration.
- Cite CircuitBench when publishing results.
