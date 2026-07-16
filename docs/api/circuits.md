# Circuits API Reference

## Overview

The Circuits API provides a standardized interface for creating, loading, validating, querying, analyzing, and exporting electronic circuits within the Circuit-Bench ecosystem. It enables researchers, educators, and developers to interact with circuit definitions in a consistent and reproducible manner across analog, digital, RF, mixed-signal, power electronics, passive, and sensor applications.

The API is designed to support interoperability between simulation tools, benchmark pipelines, machine learning workflows, and dataset management utilities.

---

# Purpose

The Circuits API enables users to:

* Create circuit objects
* Load existing circuits
* Validate circuit definitions
* Inspect circuit metadata
* Analyze circuit topology
* Export circuit descriptions
* Integrate circuits into benchmark workflows

---

# Supported Circuit Categories

The API supports circuits including:

* Analog circuits
* Digital circuits
* Mixed-signal circuits
* RF circuits
* Power electronics
* Passive networks
* Sensor interfaces
* Communication circuits
* Educational example circuits
* Reference benchmark circuits

---

# Core Workflow

A typical workflow consists of:

1. Load a circuit
2. Validate its structure
3. Inspect metadata
4. Analyze connectivity
5. Simulate or benchmark
6. Export results

---

# Circuit Representation

A circuit may contain:

* Components
* Nets
* Nodes
* Pins
* Connections
* Power rails
* Ground references
* Subcircuits
* Parameters
* Metadata

The API abstracts these elements into a consistent data model.

---

# Supported File Formats

Circuit descriptions may be imported or exported in formats such as:

* SPICE netlists
* Verilog
* VHDL (structural representations)
* JSON
* YAML
* Graph formats
* CSV (component tables)

Support for additional formats may be added in future releases.

---

# Component Access

Each circuit component may expose information such as:

* Identifier
* Component type
* Value
* Units
* Model
* Pins
* Position (if available)
* Parameters

Components can be queried individually or collectively.

---

# Connectivity Analysis

The API supports inspection of circuit topology, including:

* Node connectivity
* Net traversal
* Connected components
* Signal paths
* Power distribution
* Ground connectivity
* Subcircuit hierarchy

These capabilities support analysis and visualization.

---

# Metadata Access

Circuit metadata may include:

* Circuit name
* Version
* Author
* Description
* License
* Source
* Tags
* Category
* Date created
* Revision history

Metadata facilitates organization and reproducibility.

---

# Validation

The Circuits API should verify:

* Required metadata
* Valid component definitions
* Net consistency
* Missing connections
* Duplicate identifiers
* Unsupported component types
* Structural integrity

Validation helps detect common design issues before simulation or benchmarking.

---

# Export Functions

Supported export targets may include:

* JSON
* YAML
* SPICE
* CSV
* Graph representations
* Visualization-ready formats

Export functions simplify integration with external analysis tools.

---

# Integration with Circuit-Bench

The Circuits API integrates with:

* Dataset management
* Simulation workflows
* Metrics evaluation
* Visualization tools
* Machine learning pipelines
* Benchmark leaderboards
* Reporting utilities

This integration enables end-to-end benchmarking workflows.

---

# Error Handling

The API should detect and report issues such as:

* Missing components
* Invalid netlists
* Broken connections
* Duplicate node names
* Unsupported formats
* Missing metadata
* Invalid parameter values

Errors should include descriptive messages to aid debugging.

---

# Best Practices

When using the Circuits API:

* Keep circuit metadata complete.
* Use descriptive component identifiers.
* Validate circuits before simulation.
* Maintain consistent naming conventions.
* Preserve original netlists.
* Archive revisions using version control.
* Document assumptions and operating conditions.

---

# Related Documentation

Additional documentation includes:

* Theory: Analog Circuits
* Theory: Digital Circuits
* Theory: Simulation
* API: Datasets
* API: Metrics
* API: Reports
* Developer Guide: Adding Circuits

---

# Summary

The Circuits API provides a unified interface for representing and managing electronic circuits within Circuit-Bench. By standardizing circuit definitions, validation, metadata, topology analysis, and export capabilities, it enables reproducible research, interoperable tooling, and scalable benchmarking across diverse electronic design domains.
