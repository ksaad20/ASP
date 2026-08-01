![CI Status](https://github.com/ksaad20/ASP/actions/workflows/ci.yml/badge.svg)
## Status

[![CI Status](https://github.com/ksaad20/ASP/actions/workflows/ci.yml/badge.svg)](https://github.com/ksaad20/ASP/actions/workflows/ci.yml)

[![Python](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12-blue.svg)](https://www.python.org/)

[![License](https://img.shields.io/github/license/ksaad20/ASP)](https://github.com/ksaad20/ASP/blob/main/LICENSE)

[![GitHub Issues](https://img.shields.io/github/issues/ksaad20/ASP)](https://github.com/ksaad20/ASP/issues)

[![GitHub Last Commit](https://img.shields.io/github/last-commit/ksaad20/ASP)](https://github.com/ksaad20/ASP/commits/main)

[![Repository Size](https://img.shields.io/github/repo-size/ksaad20/ASP)](https://github.com/ksaad20/ASP)

# Autonomous Synthesis Planner

**An open-source software framework for autonomous synthesis planning, enabling AI-driven retrosynthesis, reaction prediction, synthesis route optimization, and reproducible computational chemistry workflows.**

---

## Overview

Autonomous Synthesis Planner (ASP) is a modular scientific software platform designed to automate the planning of chemical synthesis. It combines cheminformatics, machine learning, graph algorithms, and optimization techniques to generate efficient synthetic routes from commercially available starting materials.

The project aims to provide an extensible foundation for researchers, computational chemists, and software engineers developing next-generation AI systems for molecular synthesis.

---

## Features

* AI-assisted retrosynthetic analysis
* Forward reaction prediction
* Multi-step synthesis route generation
* Route ranking and optimization
* Molecular graph processing
* Reaction template matching
* Commercial building-block search
* Synthetic accessibility estimation
* Cost-aware synthesis planning
* Route visualization
* Batch synthesis planning
* Plugin-based architecture
* Reproducible computational workflows
* Command-line interface (CLI)
* Python API
* Extensible model framework

---

## Planned Architecture

```text
Target Molecule
        │
        ▼
 Molecular Parser
        │
        ▼
 Molecular Representation
        │
        ▼
 Retrosynthesis Engine
        │
        ├──────────────┐
        ▼              ▼
Reaction Prediction   Template Search
        │              │
        └──────┬───────┘
               ▼
     Route Generation
               │
               ▼
 Route Optimization Engine
               │
               ▼
Synthetic Accessibility
               │
               ▼
     Ranked Pathways
               │
               ▼
 Export / Visualization
```

---

# Project Structure

```text
autonomous-synthesis-planner/

├── LICENSE
├── README.md
├── pyproject.toml
├── requirements.txt
├── .gitignore
├── docs/
├── examples/
├── notebooks/
├── datasets/
├── models/
├── tests/
├── scripts/
├── src/
│   └── asp/
│       ├── cli.py
│       ├── api.py
│       ├── config.py
│       ├── parser.py
│       ├── molecule.py
│       ├── reactions.py
│       ├── retrosynthesis.py
│       ├── planner.py
│       ├── optimizer.py
│       ├── templates.py
│       ├── search.py
│       ├── scoring.py
│       ├── graph.py
│       ├── datasets.py
│       ├── visualization.py
│       ├── export.py
│       └── utils.py
```

---

# Installation

```bash
git clone https://github.com/yourusername/autonomous-synthesis-planner.git

cd autonomous-synthesis-planner

pip install -e .
```

---

# Quick Start

Python

```python
from asp import Planner

planner = Planner()

routes = planner.plan(
    target="CC(=O)OC1=CC=CC=C1C(=O)O"
)

print(routes)
```

CLI

```bash
asp plan aspirin.smi
```

---

# Core Modules

| Module         | Purpose                     |
| -------------- | --------------------------- |
| parser         | Molecular parsing           |
| molecule       | Molecular representations   |
| retrosynthesis | Backward synthesis planning |
| reactions      | Forward reaction prediction |
| planner        | High-level planning engine  |
| optimizer      | Route optimization          |
| scoring        | Pathway scoring             |
| templates      | Reaction templates          |
| search         | Graph search algorithms     |
| visualization  | Route visualization         |
| export         | JSON, CSV, PDF export       |

---

# Roadmap

## MVP

* Molecule parser
* Retrosynthesis engine
* CLI
* Route search
* Route scoring
* Visualization

## Version 0.2

* Transformer-based reaction prediction
* Template extraction
* Batch planning
* Route optimization

## Version 0.5

* Reinforcement learning planner
* Cost-aware optimization
* Multi-objective search
* Commercial reagent database

## Version 1.0

* Autonomous planning engine
* Laboratory workflow generation
* Robotic execution interface
* API server
* Web dashboard
* Distributed planning

---

# Scientific Applications

* Drug discovery
* Medicinal chemistry
* Organic synthesis
* Catalyst development
* Battery materials
* Polymer design
* Green chemistry
* Chemical process development
* Computational chemistry education

---

# Design Principles

* Modular
* Reproducible
* Extensible
* Research-grade
* Production-ready
* Open-source
* Well-tested
* Documented
* Scalable

---

# Contributing

Contributions are welcome. Please submit issues, feature requests, or pull requests. Before contributing, ensure all tests pass and code follows the project's formatting and linting standards.

---

# License

Released under the Apache License 2.0.

---

## Vision

Autonomous Synthesis Planner aims to become a foundational open-source software platform for AI-assisted synthesis planning, enabling reproducible, extensible, and scalable computational workflows that accelerate chemical discovery and bridge the gap between molecular design and practical synthesis.
