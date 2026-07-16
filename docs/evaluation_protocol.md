# Circuit-Bench Evaluation Protocol

## Purpose

This document defines the standardized evaluation procedure for all benchmark tasks in Circuit-Bench. The protocol ensures that benchmark results are reproducible, comparable and scientifically rigorous across different machine learning methods and software implementations.

## Standard Evaluation Workflow

1. Select benchmark task.
2. Load benchmark dataset.
3. Preprocess input data.
4. Train the machine learning model.
5. Evaluate on benchmark data.
6. Compute benchmark metrics.
7. Record runtime and resource usage.
8. Export benchmark report.

## Dataset Splits

Every benchmark dataset should define:

- Training dataset
- Validation dataset
- Test dataset

Unless otherwise specified, benchmark results must only be reported using the official test dataset.

## Reproducibility Requirements

Benchmark evaluations should report:

- Random seed
- Python version
- Circuit-Bench version
- Operating system
- Hardware specification
- Software dependencies

## Official Performance Metrics

Depending on the benchmark task, one or more of the following metrics should be reported:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- Mean Absolute Percentage Error (MAPE)
- R² Score
- Runtime
- Peak memory usage

## Required Benchmark Report

Every benchmark result should include:

- Benchmark task
- Dataset version
- Circuit category
- Model name
- Hyperparameters
- Evaluation metrics
- Runtime
- Date
- Circuit-Bench version

## Prohibited Practices

The following practices are not permitted for official benchmark results:

- Training on the official test set
- Modifying benchmark labels
- Reporting incomplete metrics
- Omitting benchmark version information
- Selectively reporting successful experiments

## Benchmark Success Criteria

Benchmark submissions should satisfy the following requirements:

- Reproducible results
- Complete metadata
- Official evaluation protocol
- Required performance metrics
- Version compatibility

## Version 

Git commit: Add standardized benchmark evaluation protocol
