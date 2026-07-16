# Tutorial 02: Creating Your First Dataset

## Overview

This tutorial demonstrates how to create a dataset that follows the Circuit-Bench conventions. Well-organized datasets improve reproducibility, simplify benchmarking, and make it easier for other researchers to reuse and validate your work.

By the end of this tutorial, you will understand the recommended dataset structure, required documentation, metadata, validation steps, and best practices for dataset management.

---

# Learning Objectives

After completing this tutorial, you will be able to:

* Create a new dataset.
* Organize dataset files.
* Write dataset metadata.
* Document provenance and licensing.
* Validate dataset integrity.
* Prepare datasets for benchmarking.

---

# Prerequisites

Before starting, ensure that you have:

* Installed Circuit-Bench.
* Cloned the repository.
* Reviewed the "Adding Datasets" developer guide.
* Selected a dataset that is appropriate for benchmarking.

---

# Step 1: Create a Dataset Directory

Choose the appropriate category and create a directory for your dataset.

Example:

```text id="yr5fne"
datasets/
└── analog/
    └── example_dataset/
```

---

# Step 2: Create the Recommended Structure

Organize the dataset using the recommended layout.

```text id="ixm1vb"
example_dataset/
├── README.md
├── metadata.yaml
├── citation.bib
├── LICENSE
├── checksums.sha256
├── preprocessing.md
├── tasks.md
├── statistics.json
├── download.sh
├── raw/
├── interim/
├── processed/
├── expected/
└── validation/
```

This structure separates documentation, metadata, raw data, processed data, and validation artifacts.

---

# Step 3: Document the Dataset

Create a `README.md` describing:

* Dataset purpose
* Circuit category
* Source
* Version
* Contents
* Supported benchmark tasks
* File organization
* Usage notes

---

# Step 4: Add Metadata

Create a `metadata.yaml` file that records information such as:

* Dataset name
* Version
* Maintainer
* Source
* License
* Citation
* Supported tasks
* File formats
* Date added

Complete metadata improves discoverability and reproducibility.

---

# Step 5: Record Licensing and Citation

Include:

* A `LICENSE` file or reference to the official license.
* A `citation.bib` file containing the recommended academic citation.

Always respect the original dataset license and provide appropriate attribution.

---

# Step 6: Organize Data

Store files according to their role:

* `raw/` for original, unmodified data.
* `interim/` for intermediate processing outputs.
* `processed/` for benchmark-ready data.
* `expected/` for reference outputs.
* `validation/` for validation artifacts and reports.

Keeping these stages separate helps preserve provenance and reproducibility.

---

# Step 7: Document Preprocessing

Describe any preprocessing steps in `preprocessing.md`, including:

* Data cleaning
* Normalization
* Feature extraction
* File conversion
* Quality control

These instructions should enable another researcher to reproduce the processed dataset.

---

# Step 8: Define Supported Tasks

In `tasks.md`, list the benchmark tasks supported by the dataset, such as:

* Classification
* Regression
* Fault diagnosis
* Parameter estimation
* Simulation
* Graph learning

---

# Step 9: Validate the Dataset

Before using the dataset in a benchmark, verify that:

* Required files are present.
* Metadata is complete.
* Citations are accurate.
* Licenses are documented.
* Checksums (when available) match.
* Directory names follow project conventions.

---

# Step 10: Use the Dataset

Once validated, the dataset can be referenced by benchmark configurations and used in benchmark workflows.

Document any benchmark-specific assumptions or configuration requirements.

---

# Best Practices

* Prefer official dataset sources.
* Preserve raw data.
* Document every processing step.
* Maintain complete metadata.
* Use consistent naming conventions.
* Keep licensing information current.
* Update documentation whenever the dataset changes.

---

# Troubleshooting

Common issues include:

* Missing metadata
* Incorrect directory structure
* Incomplete documentation
* Invalid citations
* Missing licenses
* Unsupported file formats

Review validation results and update the dataset before submission.

---

# Summary

In this tutorial, you learned how to:

* Create a dataset structure.
* Organize files.
* Record metadata.
* Document licensing and citations.
* Prepare data for benchmarking.
* Validate dataset integrity.

These practices help ensure that Circuit-Bench datasets remain reproducible, maintainable, and useful to the research community.

