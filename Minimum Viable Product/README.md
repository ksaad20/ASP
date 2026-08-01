Autonomous Synthesis Planner (ASP)

<p align="center">

<img src="https://img.shields.io/badge/status-MVP-blue" />
<img src="https://img.shields.io/badge/python-3.10%2B-green" />
<img src="https://img.shields.io/badge/license-Apache--2.0-orange" />

</p>

## AI-Assisted Retrosynthetic Planning Framework

Autonomous Synthesis Planner (ASP) is an open-source software framework for generating, evaluating, and visualizing chemical synthesis pathways.

ASP provides a modular foundation for computational retrosynthesis workflows by combining:

- Molecular representation
- Reaction template libraries
- Retrosynthetic search
- Route scoring
- Synthesis pathway visualization

The goal of ASP is to accelerate chemical discovery by making synthesis planning workflows accessible, reproducible, and extensible.

---

# Features

## Current MVP Features

✅ SMILES-based molecular input

✅ Reaction template management

✅ Retrosynthetic planning engine

✅ Candidate route generation

✅ Route scoring framework

✅ JSON result export

✅ Command-line interface

✅ Python API

✅ Synthesis pathway visualization

---

# Architecture

```text
                 User
                  |
          +---------------+
          |  ASP CLI/API  |
          +---------------+
                  |
                  v
          +---------------+
          |    Planner    |
          +---------------+
                  |
       +----------+----------+
       |          |          |
       v          v          v

 Retrosynthesis  Scoring  Visualization

       |
       v

 Reaction Templates

       |
       v

 Molecule Representation
````

---

# Installation

## From source

```bash
git clone https://github.com/ksaad20/autonomous-synthesis-planner.git

cd autonomous-synthesis-planner

pip install -e .
```

---

# Quick Start

## Python API

```python
from asp import ASP

planner = ASP()

result = planner.plan(
    "CC(=O)OC1=CC=CC=C1C(=O)O"
)

print(
    result
)
```

---

## Command Line

Plan a molecule:

```bash
asp plan molecule "CCO"
```

Export results:

```bash
asp plan molecule "CCO" --output ethanol.json
```

Check installation:

```bash
asp version
```

---

# Examples

ASP includes example workflows:

```bash
python examples/aspirin.py

python examples/caffeine.py

python examples/ibuprofen.py
```

Example targets:

| Molecule  | Application              |
| --------- | ------------------------ |
| Aspirin   | Pharmaceutical synthesis |
| Caffeine  | Heterocyclic chemistry   |
| Ibuprofen | Drug molecule planning   |

---

# Dataset Workflow

Prepare reaction data:

```bash
python scripts/download_data.py
```

Build reaction templates:

```bash
python scripts/build_templates.py
```

Generated templates are stored in:

```text
datasets/templates/
```

---

# Project Structure

```text
autonomous-synthesis-planner/

├── examples/
├── datasets/
├── models/
├── scripts/
├── tests/
└── src/
    └── asp/
        ├── chemistry/
        ├── planning/
        ├── data/
        ├── visualization/
        ├── io/
        └── utils/
```

---

# Development

Install development dependencies:

```bash
pip install -r requirements.txt
```

Run tests:

```bash
pytest
```

Run formatting checks:

```bash
black .
ruff check .
```

---

# Scientific Scope

ASP is currently a research software MVP.

The current version focuses on:

* Software architecture
* Reproducible synthesis planning workflows
* Template-based retrosynthesis
* Extensible planning algorithms

Future versions aim to integrate:

* Machine learning reaction prediction
* Neural template extraction
* Cost-aware synthesis optimization
* Yield prediction
* Laboratory automation interfaces

---

# Roadmap

## v0.1.0 — MVP

* Core planning framework
* CLI
* Python API
* Template system
* Route scoring
* Visualization

## v0.2.0

* Expanded reaction databases
* Improved search algorithms
* ML-based ranking

## v1.0.0

* Autonomous synthesis planning platform
* Advanced AI models
* Experimental workflow integration

---

# Contributing

Contributions are welcome.

Areas of interest:

* Chemistry algorithms
* Machine learning
* Molecular representation
* Optimization methods
* Scientific visualization

---

# License

ASP is released under the Apache License 2.0.

See:

```text
LICENSE
```

for details.

---

# Citation

If you use ASP in research, please cite the repository release.

```
Autonomous Synthesis Planner (ASP)
Open-source retrosynthetic planning framework
```

---

# Acknowledgements

ASP builds on decades of progress in:

* Computational chemistry
* Retrosynthesis
* Molecular informatics
* Artificial intelligence
* Scientific software engineering

```
```
