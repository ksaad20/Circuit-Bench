# Adding Datasets

## Overview

This guide describes the recommended process for adding new datasets to Circuit-Bench. The goal is to ensure that all datasets are reproducible, well documented, legally distributable (or properly referenced), and consistent with the repository structure.

---

# Guiding Principles

Every dataset should be:

* Reproducible
* Well documented
* Properly licensed
* Versioned
* Validated
* Easily discoverable
* Suitable for benchmarking

Datasets should include sufficient metadata for other researchers to understand and reproduce benchmark results.

---

# Before Adding a Dataset

Verify the following:

* The dataset has a clearly identified source.
* The license permits its intended use.
* Citation information is available.
* The dataset is relevant to Circuit-Bench.
* The dataset has stable identifiers or version information.

Whenever possible, reference the official source instead of redistributing third-party data.

---

# Recommended Directory Structure

Each dataset should follow a consistent layout.

```text
datasets/
└── <category>/
    └── <dataset_name>/
        ├── README.md
        ├── metadata.yaml
        ├── citation.bib
        ├── LICENSE
        ├── checksums.sha256
        ├── preprocessing.md
        ├── tasks.md
        ├── statistics.json
        ├── download.sh
        ├── expected/
        ├── raw/
        ├── interim/
        ├── processed/
        └── validation/
```

---

# Required Documentation

Every dataset should include:

## README.md

Describe:

* Dataset purpose
* Source
* Contents
* Version
* Directory structure
* Intended benchmark tasks
* Usage notes

---

## metadata.yaml

Recommended metadata includes:

* Dataset name
* Version
* Source
* Maintainer
* License
* Citation
* Categories
* File formats
* Number of samples
* Supported tasks
* Date added

---

## citation.bib

Provide a BibTeX entry for the original publication whenever available.

---

## LICENSE

Include the applicable license or clearly reference the official license if redistribution is not permitted.

---

## preprocessing.md

Document:

* Download procedure
* Cleaning steps
* Normalization
* Feature extraction
* File conversions
* Quality control procedures

---

## tasks.md

Document benchmark tasks supported by the dataset, such as:

* Classification
* Regression
* Fault diagnosis
* Circuit recognition
* Parameter estimation
* Graph learning
* Simulation

---

## statistics.json

Summarize useful dataset statistics, for example:

* Number of circuits
* Number of classes
* Average component count
* Supported technologies
* File types

---

# Validation

Before committing a dataset:

* Verify required files exist.
* Validate metadata.
* Confirm citation accuracy.
* Verify checksums when available.
* Ensure directory names follow project conventions.
* Confirm licensing requirements are satisfied.

---

# Naming Conventions

Use lowercase directory names with underscores.

Examples:

* analog_filters
* buck_converter
* cmos_inverter

Avoid spaces and special characters.

---

# Versioning

Record dataset versions whenever possible.

If a dataset changes substantially, update:

* Metadata
* Statistics
* Documentation
* Version information

---

# Large Files

Avoid committing very large third-party datasets directly to the repository unless redistribution is explicitly permitted and appropriate.

Prefer:

* Official download links
* Download scripts
* Metadata
* Checksums
* Documentation

---

# Testing

New datasets should pass:

* Metadata validation
* Schema validation
* Integrity checks
* Benchmark compatibility tests
* Documentation review

---

# Pull Requests

Dataset contributions should include:

* Documentation
* Metadata
* Citation
* Licensing information
* Validation results
* Any required preprocessing scripts

---

# Best Practices

* Prefer official sources.
* Keep metadata complete.
* Maintain reproducibility.
* Preserve provenance.
* Cite original authors.
* Avoid duplicate datasets.
* Clearly document preprocessing.

Following these practices helps ensure that Circuit-Bench remains a reliable, reproducible, and maintainable benchmark for the research community.
