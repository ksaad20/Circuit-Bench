# Circuit-Bench Baseline Models

## Purpose

Baseline models provide reference performance for Circuit-Bench benchmark tasks. They establish reproducible performance levels against which future machine learning methods can be compared.

## Baseline Selection Strategy

Circuit-Bench includes representative baseline models spanning different levels of model complexity.

The objective is not to identify the best-performing model, but to provide reproducible reference points for benchmark evaluation.

## Baseline Categories

| Category | Purpose |
|----------|---------|
| Statistical | Simple reference methods |
| Classical Machine Learning | Traditional predictive models |
| Ensemble Learning | Strong tabular baselines |
| Deep Learning | Neural network baselines |
| Physics-informed Models | Hybrid AI approaches |

## Official Baseline Models

| Model | Category | Status |
|--------|----------|--------|
| Linear Regression | Statistical | Official |
| Ridge Regression | Statistical | Official |
| Random Forest | Ensemble | Official |
| XGBoost | Ensemble | Official |
| Support Vector Regression | Classical ML | Official |
| Multi-layer Perceptron | Deep Learning | Official |

## Baseline Evaluation Requirements

All baseline models should:

- Follow the official evaluation protocol
- Use official benchmark datasets
- Report all required metrics
- Report runtime
- Record software versions
- Use fixed random seeds where applicable

## Standard Reporting Format

Every baseline result should include:

- Benchmark task
- Circuit category
- Dataset version
- Model
- Hyperparameters
- Metrics
- Runtime
- Benchmark version

## Future Baseline Models

Future benchmark releases may include:

- Graph Neural Networks
- Physics-Informed Neural Networks
- Transformer architectures
- Bayesian optimization methods
- Reinforcement learning methods

## Baseline Principles

Baseline models are intended to:

- Provide reproducible reference performance
- Enable fair comparison
- Support future benchmarking
- Encourage transparent reporting

## Version 

Git commit: Add official benchmark baseline framework
