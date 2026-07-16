# Circuit-Bench Official Baseline Policy

## Purpose

This document defines the official baseline models used in Circuit-Bench.

Baseline models provide reproducible reference performance for every benchmark task and establish a consistent comparison point for future machine learning methods.

## Baseline Philosophy

Circuit-Bench includes baseline methods representing increasing levels of model complexity.

Baseline models are selected based on:

- widespread use
- reproducibility
- computational efficiency
- interpretability
- relevance to electrical engineering

## Official Baseline Models

| Model | Category | Difficulty | Official |
|--------|----------|-----------|----------|
| Linear Regression | Statistical | Easy | Yes |
| Ridge Regression | Statistical | Easy | Yes |
| Random Forest | Ensemble | Medium | Yes |
| XGBoost | Ensemble | Medium | Yes |
| Support Vector Regression | Classical ML | Medium | Yes |
| Multi-layer Perceptron | Deep Learning | Hard | Yes |

## Evaluation Rules

All official baselines must:

- use the official benchmark datasets
- follow the official evaluation protocol
- report every required metric
- report runtime
- record random seed
- record software versions

## Reporting Requirements

Official benchmark publications should report:

- dataset version
- benchmark version
- model
- hyperparameters
- evaluation metrics
- runtime
- hardware specification

## Versioning

Official baseline models remain fixed for each major benchmark release.

New baseline models are introduced only in future benchmark versions to preserve comparability.

Git Commit: Define official benchmark baseline policy
