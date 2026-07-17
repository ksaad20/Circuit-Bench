# DOI Dataset Card

## Dataset Name

DOIs

---

## Version

v1.0.0

---

## Description

The DOIs dataset is a curated collection of Digital Object Identifiers (DOIs) associated with datasets, benchmark suites, circuit models, scientific publications, software releases, and supplementary research materials used throughout Circuit-Bench. It provides persistent references to external resources, ensuring reproducibility, traceability, and long-term accessibility.

---

## Purpose

This dataset is designed to:

- Provide permanent references to research artifacts
- Improve reproducibility of benchmark results
- Track dataset and software provenance
- Enable citation of external resources
- Support FAIR (Findable, Accessible, Interoperable, Reusable) research principles

---

## Domain

- Electronic Design Automation (EDA)
- Circuit Simulation
- Analog Electronics
- Digital Electronics
- Mixed-Signal Design
- RF Engineering
- Power Electronics
- Scientific Software
- Benchmarking
- Machine Learning for Circuits

---

## Data Contents

Each record may contain:

- DOI
- Title
- Authors
- Publication Year
- Publisher
- Resource Type
- Repository
- URL
- Citation Information
- License
- Version
- Associated Benchmark
- Notes

---

## Supported Resource Types

Examples include:

- Scientific papers
- Datasets
- Software releases
- GitHub archives
- Zenodo records
- Figshare datasets
- Dryad datasets
- Conference proceedings
- Journal articles
- Technical reports
- Supplementary materials

---

## File Formats

Supported formats may include:

- `.csv`
- `.json`
- `.yaml`
- `.bib`
- `.txt`
- `.md`

---

## Directory Structure

```text
dois/
├── datasets.csv
├── publications.csv
├── software.csv
├── benchmarks.csv
├── citations.bib
├── metadata/
└── README.md
```

---

## Example Fields

| Field | Description |
|--------|-------------|
| doi | Digital Object Identifier |
| title | Resource title |
| authors | Author list |
| year | Publication year |
| publisher | Publishing organization |
| resource_type | Dataset, Paper, Software, etc. |
| repository | Hosting repository |
| url | Landing page |
| version | Resource version |
| license | Distribution license |

---

## Applications

- Research reproducibility
- Citation management
- Provenance tracking
- Benchmark documentation
- Literature review
- Dataset discovery
- Software version tracking
- Automated reference generation

---

## Evaluation

Quality may be assessed using:

- DOI validity
- Metadata completeness
- Citation accuracy
- Link availability
- Version consistency
- Duplicate detection

---

## Limitations

- External resources may change over time.
- Some DOIs may resolve to updated versions.
- Access restrictions may apply to certain publishers.
- Metadata quality depends on the source repository.

---

## Reproducibility

For each referenced resource, document:

- DOI
- Version
- Access date
- Citation
- Repository
- License
- Checksum (if available)

---

## FAIR Compliance

This dataset supports FAIR principles by promoting:

- **Findability** through persistent DOIs
- **Accessibility** via standardized identifiers
- **Interoperability** using structured metadata
- **Reusability** through complete citation information

---

## Citation

If you use this dataset, please cite the corresponding Circuit-Bench publication and repository. Individual external resources should also be cited according to their respective DOI records.

---

## License

Specify the applicable license (e.g., MIT, Apache-2.0, CC BY 4.0).

---

## Maintainers

Circuit-Bench Contributors

---

## Contact

Please open an issue or discussion in the repository for questions, corrections, or contributions.

---

## Changelog

### v1.0.0

- Initial release
- Added support for DOI metadata
- Included references to datasets, publications, software, and benchmark resources
- Structured metadata for reproducible research
