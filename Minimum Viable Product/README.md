# Autonomous Synthesis Planner

<p align="center">
  <img src="docs/assets/logo.png" alt="Autonomous Synthesis Planner Logo" width="220">
</p>

<h3 align="center">
Open-Source Software for AI-Powered Autonomous Chemical Synthesis Planning
</h3>

<p align="center">
Generate retrosynthetic pathways, optimize synthesis routes, and build reproducible computational chemistry workflows.
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)
![License](https://img.shields.io/badge/License-Apache%202.0-green.svg)
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey)
![Status](https://img.shields.io/badge/Status-MVP-orange)
![Tests](https://img.shields.io/badge/Tests-Pytest-success)
![Code%20Style](https://img.shields.io/badge/Code%20Style-Black-black)
![Lint](https://img.shields.io/badge/Lint-Ruff-red)
![Typing](https://img.shields.io/badge/Typing-Mypy-blueviolet)

</p>

---

## Overview

**Autonomous Synthesis Planner (ASP)** is an open-source scientific software framework for autonomous chemical synthesis planning. It enables researchers and developers to generate, evaluate, and optimize synthetic pathways from target molecules using modern computational methods.

ASP is designed around three core principles:

* **Autonomy** — automate synthesis planning with minimal user intervention.
* **Reproducibility** — produce deterministic, transparent, and reusable planning workflows.
* **Extensibility** — provide a modular architecture for integrating new planning algorithms, scoring strategies, reaction databases, and machine learning models.

Rather than being a single-purpose application, ASP serves as a reusable software foundation for research in computational chemistry, cheminformatics, scientific machine learning, and laboratory automation.

---

## Why Autonomous Synthesis Planner?

Designing practical synthetic routes is one of the central challenges in chemistry. Traditional synthesis planning often requires extensive expert knowledge, iterative experimentation, and manual exploration of reaction pathways.

ASP aims to accelerate this process by providing software that can:

* Generate candidate retrosynthetic pathways
* Search alternative synthesis routes
* Rank pathways using configurable scoring strategies
* Support reproducible computational experiments
* Provide a foundation for next-generation AI-driven synthesis planning

The project is intended for academic research, industrial R&D, scientific software development, and educational use.

---

## Vision

Our long-term vision is to build a modular, open-source software ecosystem for autonomous synthesis planning that bridges computational chemistry, artificial intelligence, optimization, and laboratory automation.

As the project evolves, ASP will support increasingly sophisticated capabilities—including advanced route planning, reaction prediction, intelligent optimization, and integration with autonomous laboratory systems—while maintaining a transparent, extensible architecture for the scientific community.

---

> **Project Status:** MVP under active development. Core planning capabilities are being implemented with an emphasis on modular design, reproducibility, and production-quality software engineering.
>
> ---

# Features

Autonomous Synthesis Planner is designed as a modular scientific software platform for computational chemistry and autonomous synthesis planning.

## Core Features

* Molecular structure parsing
* Retrosynthetic route generation
* Multi-step synthesis planning
* Reaction template matching
* Pathway search algorithms
* Route scoring and ranking
* Synthetic accessibility estimation
* Route visualization
* Python API
* Command-line interface (CLI)
* Extensible plugin architecture
* Reproducible computational workflows

---

# Design Goals

The project is guided by the following engineering principles.

## Modular

Every major component is isolated behind clean interfaces, enabling researchers to replace planning algorithms, reaction databases, or scoring functions without affecting the rest of the system.

## Extensible

ASP is designed as a platform rather than a monolithic application. New reaction predictors, search strategies, optimization methods, and visualization tools can be integrated with minimal effort.

## Reproducible

Planning results should be deterministic, transparent, and easy to reproduce. Configuration, datasets, and generated synthesis routes are intended to be portable across environments.

## Research-Ready

The software is built to support experimentation with new algorithms while maintaining production-quality engineering practices.

## Production-Oriented

Although initially released as an MVP, the architecture emphasizes maintainability, testing, documentation, and scalability from the outset.

---

# Core Capabilities

## Molecular Processing

* Parse molecular representations
* Validate molecular structures
* Canonicalize molecular inputs
* Support common chemistry data formats
* Generate molecular graph representations

---

## Retrosynthesis

* Target-driven retrosynthetic analysis
* Recursive pathway generation
* Multi-step synthesis planning
* Alternative route discovery
* Search-space exploration

---

## Reaction Planning

* Reaction template matching
* Candidate reaction generation
* Intermediate compound identification
* Route expansion
* Planning graph construction

---

## Route Evaluation

Generated synthesis pathways can be evaluated using configurable metrics such as:

* Number of synthetic steps
* Overall pathway complexity
* Reaction confidence
* Template confidence
* Estimated synthetic accessibility
* User-defined scoring functions

---

## Visualization

ASP provides tools for visualizing synthesis pathways through:

* Reaction trees
* Planning graphs
* Route summaries
* Exportable planning reports

---

# Intended Users

Autonomous Synthesis Planner is designed for:

* Computational chemists
* Organic chemists
* Medicinal chemists
* Pharmaceutical researchers
* Scientific software developers
* Machine learning researchers
* Cheminformatics researchers
* Graduate students
* Educators

---

# Use Cases

Typical applications include:

* Drug discovery
* Medicinal chemistry
* Organic synthesis planning
* Materials discovery
* Battery materials research
* Catalyst development
* Green chemistry
* Reaction pathway exploration
* Scientific benchmarking
* Computational chemistry education

---

# Engineering Principles

The software follows modern software engineering practices, including:

* Modular architecture
* Type-safe Python
* Automated testing
* Continuous integration
* Static analysis
* Code formatting
* Comprehensive documentation
* Semantic versioning
* Reproducible releases
* Open-source development workflow

---

---

# Project Structure

The repository is organized into modular components that separate chemistry, planning, data management, visualization, and user interfaces. This architecture promotes maintainability, extensibility, and reproducible scientific software development.

```text
autonomous-synthesis-planner/
│
├── LICENSE
├── README.md
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── SECURITY.md
├── CHANGELOG.md
├── pyproject.toml
├── requirements.txt
├── .gitignore
├── Makefile
│
├── docs/
│   ├── architecture.md
│   ├── api.md
│   └── cli.md
│
├── examples/
│   ├── aspirin.py
│   ├── caffeine.py
│   └── ibuprofen.py
│
├── datasets/
│   ├── reactions/
│   └── templates/
│
├── models/
│
├── tests/
│   ├── test_api.py
│   ├── test_cli.py
│   ├── test_parser.py
│   ├── test_planner.py
│   ├── test_retrosynthesis.py
│   ├── test_scoring.py
│   └── test_visualization.py
│
├── scripts/
│   ├── download_data.py
│   └── build_templates.py
│
└── src/
    └── asp/
        │
        ├── __init__.py
        ├── cli.py
        ├── api.py
        ├── config.py
        ├── constants.py
        │
        ├── chemistry/
        │   ├── __init__.py
        │   ├── molecule.py
        │   ├── parser.py
        │   ├── reaction.py
        │   └── templates.py
        │
        ├── planning/
        │   ├── __init__.py
        │   ├── planner.py
        │   ├── retrosynthesis.py
        │   ├── search.py
        │   ├── scoring.py
        │   └── optimizer.py
        │
        ├── data/
        │   ├── __init__.py
        │   ├── loader.py
        │   └── repository.py
        │
        ├── visualization/
        │   ├── __init__.py
        │   └── routes.py
        │
        ├── io/
        │   ├── __init__.py
        │   ├── export.py
        │   └── importers.py
        │
        └── utils/
            ├── __init__.py
            ├── logging.py
            ├── validation.py
            └── helpers.py
```

---

# Repository Organization

## Root Directory

The root directory contains project metadata, build configuration, community guidelines, and development tooling.

| File                 | Purpose                                |
| -------------------- | -------------------------------------- |
| `README.md`          | Project overview and documentation     |
| `LICENSE`            | Apache 2.0 license                     |
| `CONTRIBUTING.md`    | Contribution guidelines                |
| `CODE_OF_CONDUCT.md` | Community standards                    |
| `SECURITY.md`        | Vulnerability disclosure policy        |
| `CHANGELOG.md`       | Release history                        |
| `pyproject.toml`     | Build system and project configuration |
| `requirements.txt`   | Runtime dependencies                   |
| `.gitignore`         | Git ignore rules                       |
| `Makefile`           | Common development commands            |

---

## Documentation (`docs/`)

Comprehensive technical documentation for developers and users.

| File              | Description                          |
| ----------------- | ------------------------------------ |
| `architecture.md` | System architecture and design       |
| `api.md`          | Python API reference                 |
| `cli.md`          | Command-line interface documentation |

---

## Examples (`examples/`)

Self-contained examples demonstrating end-to-end synthesis planning workflows for representative molecules.

* `aspirin.py`
* `caffeine.py`
* `ibuprofen.py`

These examples serve as executable tutorials and integration tests for the public API.

---

## Datasets (`datasets/`)

Contains reaction knowledge used by the planning engine.

```
datasets/
├── reactions/
└── templates/
```

Future releases may include curated reaction datasets, reaction templates, and benchmark planning tasks.

---

## Models (`models/`)

Reserved for pretrained machine learning models, checkpoints, and future neural planning components.

The MVP does not require pretrained models, but the directory provides a standardized location for future AI capabilities.

---

## Tests (`tests/`)

Automated unit and integration tests covering all major software components.

```
tests/
├── test_api.py
├── test_cli.py
├── test_parser.py
├── test_planner.py
├── test_retrosynthesis.py
├── test_scoring.py
└── test_visualization.py
```

Continuous integration executes the test suite to ensure correctness and maintain software quality.

---

## Scripts (`scripts/`)

Development utilities and dataset preparation scripts.

| Script               | Purpose                     |
| -------------------- | --------------------------- |
| `download_data.py`   | Download reaction datasets  |
| `build_templates.py` | Generate reaction templates |

---

# Source Code Layout

The `src/asp` package contains the implementation of Autonomous Synthesis Planner.

## `chemistry/`

Provides the chemistry foundation of the software.

Responsibilities include:

* Molecular representations
* Molecular parsing
* Reaction objects
* Reaction templates
* Chemical utility functions

---

## `planning/`

Implements the autonomous synthesis planning engine.

Responsibilities include:

* Retrosynthetic planning
* Search algorithms
* Route generation
* Route optimization
* Pathway scoring

This package forms the computational core of the project.

---

## `data/`

Provides a unified interface for loading and managing reaction datasets and template repositories.

Responsibilities include:

* Dataset loading
* Repository abstraction
* Data access
* Dataset validation

---

## `visualization/`

Responsible for rendering synthesis routes and planning results.

Planned outputs include:

* Reaction trees
* Route diagrams
* Planning graphs
* Publication-quality visualizations

---

## `io/`

Handles import and export of molecular data and planning results.

Supported formats will expand over time to include structured scientific data exchange formats.

---

## `utils/`

Shared infrastructure used throughout the project.

Includes:

* Logging
* Validation
* Helper functions
* Common utilities

---

# Architectural Philosophy

Autonomous Synthesis Planner follows a layered architecture in which chemistry, planning, visualization, and interfaces remain loosely coupled.

```text
+--------------------------------------------------------+
|                 CLI & Python API                       |
+--------------------------------------------------------+
|              Autonomous Planning Engine                |
+--------------------------------------------------------+
| Search • Retrosynthesis • Optimization • Scoring       |
+--------------------------------------------------------+
| Chemistry • Molecules • Reactions • Templates          |
+--------------------------------------------------------+
|        Datasets • Storage • Import • Export            |
+--------------------------------------------------------+
```

Each layer communicates through stable interfaces, enabling independent development, testing, and future integration of advanced planning algorithms, machine learning models, and autonomous laboratory workflows without disrupting the rest of the system.

---

---

# Installation

## Requirements

Autonomous Synthesis Planner currently supports:

* Python 3.10 or later
* Linux, macOS, or Windows
* `pip` or another PEP 517–compatible package manager

---

## Clone the Repository

```bash
git clone https://github.com/<username>/autonomous-synthesis-planner.git

cd autonomous-synthesis-planner
```

---

## Create a Virtual Environment

### Linux / macOS

```bash
python -m venv .venv

source .venv/bin/activate
```

### Windows

```powershell
python -m venv .venv

.venv\Scripts\activate
```

---

## Install the Project

### Development Installation (Recommended)

```bash
pip install -e .
```

This installs the package in editable mode so local source code changes are immediately reflected without reinstalling.

---

### Install Development Dependencies

```bash
pip install -r requirements.txt
```

---

## Verify the Installation

```bash
python -c "import asp; print('Autonomous Synthesis Planner installed successfully.')"
```

or

```bash
asp --help
```

---

# Quick Start

The simplest workflow is to create a planner instance, provide a target molecule, and request candidate synthesis routes.

```python
from asp import Planner

planner = Planner()

routes = planner.plan(
    target="CC(=O)OC1=CC=CC=C1C(=O)O"
)

print(routes)
```

---

## Planning a Molecule

```python
from asp import Planner

planner = Planner()

result = planner.plan(
    target="CCO"
)

print(result.routes)
print(result.best_route)
```

---

## Configuring the Planner

Planning behaviour can be customized through configuration parameters.

```python
from asp import Planner

planner = Planner(
    max_depth=5,
    max_routes=20,
    beam_width=10
)

result = planner.plan(
    target="CCO"
)
```

---

# Command-Line Interface

The command-line interface provides a convenient way to perform synthesis planning without writing Python code.

Display available commands:

```bash
asp --help
```

---

## Plan a Molecule

```bash
asp plan aspirin.smi
```

---

## Specify Output File

```bash
asp plan aspirin.smi \
    --output routes.json
```

---

## Export Visualization

```bash
asp plan aspirin.smi \
    --plot route.png
```

---

## Enable Verbose Logging

```bash
asp plan aspirin.smi \
    --verbose
```

---

# Python API

The Python API exposes the planning engine as a reusable software library.

## Create a Planner

```python
from asp import Planner

planner = Planner()
```

---

## Generate Candidate Routes

```python
routes = planner.plan(target=smiles)
```

---

## Access the Best Route

```python
best_route = routes.best_route
```

---

## Iterate Through All Routes

```python
for route in routes:
    print(route)
```

---

# Example Workflows

The repository includes complete examples demonstrating common planning tasks.

```text
examples/

├── aspirin.py
├── caffeine.py
└── ibuprofen.py
```

---

## Aspirin

```bash
python examples/aspirin.py
```

Demonstrates:

* Molecular parsing
* Retrosynthetic planning
* Route ranking
* Visualization

---

## Caffeine

```bash
python examples/caffeine.py
```

Demonstrates:

* Multi-step planning
* Alternative synthesis routes
* Candidate ranking

---

## Ibuprofen

```bash
python examples/ibuprofen.py
```

Demonstrates:

* Larger search spaces
* Route evaluation
* Planning performance

---

# Configuration

Planner behaviour is configurable through the Python API.

Example parameters include:

| Parameter     | Description                        |
| ------------- | ---------------------------------- |
| `max_depth`   | Maximum retrosynthesis depth       |
| `beam_width`  | Search beam width                  |
| `max_routes`  | Maximum number of candidate routes |
| `timeout`     | Planning timeout                   |
| `random_seed` | Reproducibility                    |
| `verbose`     | Enable detailed logging            |

---

# Development Workflow

Install dependencies

```bash
pip install -r requirements.txt
```

Run formatting

```bash
black src tests
```

Run linting

```bash
ruff check src tests
```

Run type checking

```bash
mypy src
```

Run the test suite

```bash
pytest
```

Generate coverage

```bash
pytest --cov=asp
```

---

# Building the Package

Build a distributable wheel:

```bash
python -m build
```

The generated artifacts will be placed in the `dist/` directory and can be uploaded to a package index or installed locally.

---

---

# Roadmap

The roadmap outlines the planned evolution of Autonomous Synthesis Planner from a lightweight MVP to a comprehensive autonomous synthesis planning platform.

## MVP (v0.1)

The initial release establishes the software foundation.

### Chemistry

* Molecular parsing
* Molecular validation
* Molecular graph representation
* Reaction template support

### Planning

* Retrosynthetic planning
* Graph-based route search
* Route scoring
* Candidate ranking

### Visualization

* Reaction trees
* Route summaries
* Exportable planning reports

### Software

* Python API
* Command-line interface
* Documentation
* Unit testing
* Continuous Integration

---

## Version 0.2

Expand planning capabilities.

### Planned Features

* Template management
* Configurable search strategies
* Improved scoring functions
* Route pruning
* Parallel planning
* Batch synthesis planning
* Additional export formats

---

## Version 0.5

Introduce intelligent planning capabilities.

### Planned Features

* Machine learning-assisted planning
* Learned reaction scoring
* Multi-objective optimization
* Cost-aware planning
* Synthetic accessibility prediction
* Reaction confidence estimation
* Planning benchmarks

---

## Version 1.0

Production-ready autonomous synthesis planning platform.

### Planned Features

* Plugin ecosystem
* REST API
* Web interface
* Workflow management
* Distributed planning
* Cloud deployment
* Enterprise configuration
* Stable public API

---

## Long-Term Vision

Future research directions may include:

* Transformer-based reaction prediction
* Graph neural network planning
* Reinforcement learning for synthesis planning
* Autonomous experiment planning
* Closed-loop optimization
* Laboratory robotics integration
* Scientific benchmark suite
* Large-scale reaction knowledge bases

---

# Contributing

Contributions of all sizes are welcome.

Whether you are improving documentation, fixing bugs, implementing new planning algorithms, or developing visualization tools, your contributions help advance the project.

## Development Workflow

1. Fork the repository.
2. Create a feature branch.
3. Implement your changes.
4. Run formatting, linting, and tests.
5. Commit using descriptive messages.
6. Open a Pull Request.

---

## Coding Standards

Please ensure that all contributions:

* Follow the project style guide.
* Include type annotations where appropriate.
* Pass the complete test suite.
* Include tests for new functionality.
* Update documentation when behavior changes.

---

## Reporting Issues

Please include:

* Software version
* Python version
* Operating system
* Steps to reproduce
* Expected behavior
* Actual behavior
* Relevant logs or stack traces

Clear, reproducible bug reports help us resolve issues more efficiently.

---

# Scientific Scope

Autonomous Synthesis Planner is intended as a reusable scientific software platform supporting research in:

* Computational chemistry
* Organic synthesis
* Medicinal chemistry
* Cheminformatics
* Scientific machine learning
* Materials discovery
* Green chemistry
* Chemical process development

The project emphasizes transparent algorithms, modular software design, and reproducible computational workflows.

---

# Citation

If Autonomous Synthesis Planner contributes to your research, please cite the software using the repository information or a future archived release.

A formal citation file (`CITATION.cff`) and DOI may be added in a future release to support reproducible scientific referencing.

---

# License

Autonomous Synthesis Planner is released under the **Apache License 2.0**.

This license permits commercial and academic use while providing explicit patent protection and encouraging open collaboration.

See the `LICENSE` file for the complete license text.

---

# Frequently Asked Questions

## Is this software intended for production laboratory use?

No.

The current MVP is a research software platform designed for computational synthesis planning and algorithm development. Experimental validation and laboratory execution remain outside the scope of the initial release.

---

## Does the software require machine learning?

No.

The MVP is designed to support deterministic planning algorithms. Machine learning components are planned as optional extensions in future releases.

---

## Can I integrate my own planning algorithms?

Yes.

The architecture is intentionally modular, allowing researchers to replace or extend planning, search, scoring, and visualization components without modifying the rest of the system.

---

## Which molecular formats are planned?

Support is expected to expand over time and may include formats commonly used in computational chemistry, such as SMILES, SDF, and related representations.

---

## Is this project suitable for research?

Yes.

The project is designed to support reproducible research, algorithm development, benchmarking, and education through a modular and transparent software architecture.

---

# Acknowledgements

Autonomous Synthesis Planner is inspired by advances in computational chemistry, cheminformatics, graph algorithms, optimization, and scientific software engineering.

We thank the broader open-source scientific computing community for developing the libraries, standards, and tools that make projects like this possible.

---

# Support

If you encounter a bug, have a feature request, or would like to discuss a new idea:

* Open a GitHub Issue.
* Start a GitHub Discussion.
* Submit a Pull Request.

Constructive feedback and community contributions are always welcome.

---

# Project Status

> **Status:** Active Development

Autonomous Synthesis Planner is currently in the MVP stage. The primary focus is establishing a robust, extensible software foundation for autonomous synthesis planning. Future releases will expand planning capabilities while preserving modularity, reproducibility, and production-quality engineering practices.

---

<p align="center">
<strong>Building open scientific software for the future of autonomous chemical synthesis.</strong>
</p>

