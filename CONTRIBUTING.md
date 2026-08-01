# Contributing to Autonomous Synthesis Planner (ASP)

Thank you for your interest in contributing to **Autonomous Synthesis Planner (ASP)**.

ASP is an open-source scientific software project focused on building extensible computational frameworks for synthesis planning, retrosynthesis, molecular reasoning, and autonomous chemistry workflows.

Contributions are welcome from researchers, developers, computational chemists, machine learning practitioners, and scientific software engineers.

---

# Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Ways to Contribute](#ways-to-contribute)
- [Development Setup](#development-setup)
- [Project Structure](#project-structure)
- [Development Workflow](#development-workflow)
- [Coding Standards](#coding-standards)
- [Testing](#testing)
- [Scientific Contributions](#scientific-contributions)
- [Documentation](#documentation)
- [Pull Requests](#pull-requests)
- [Issue Guidelines](#issue-guidelines)
- [Roadmap Contributions](#roadmap-contributions)

---

# Code of Conduct

All contributors are expected to maintain a respectful, collaborative, and scientifically rigorous environment.

Please review:

```

CODE_OF_CONDUCT.md

````

before contributing.

---

# Ways to Contribute

ASP welcomes contributions in several areas.

## Software Engineering

Examples:

- Core Python development
- API improvements
- Performance optimization
- Testing infrastructure
- Developer tooling
- Packaging improvements

---

## Computational Chemistry

Examples:

- Reaction representation
- Retrosynthesis algorithms
- Molecular parsing
- Reaction templates
- Chemical validation

---

## Machine Learning

Examples:

- Reaction prediction models
- Neural retrosynthesis
- Molecular embeddings
- Route ranking models
- AI-assisted optimization

---

## Scientific Research

Examples:

- Benchmark datasets
- Algorithm evaluation
- Reproducibility studies
- Computational experiments

---

## Documentation

Examples:

- Tutorials
- API documentation
- Scientific explanations
- Example workflows

---

# Development Setup

## Clone the repository

```bash
git clone https://github.com/<username>/autonomous-synthesis-planner.git

cd autonomous-synthesis-planner
````

---

## Create an environment

Using Python virtual environments:

```bash
python -m venv .venv

source .venv/bin/activate
```

Windows:

```bash
.venv\Scripts\activate
```

---

## Install dependencies

Install the package:

```bash
pip install -e .
```

Install development tools:

```bash
pip install -r requirements.txt
```

---

# Project Structure

ASP follows a modular architecture.

```
src/
└── asp/

    ├── chemistry/
    │   Molecular and reaction representations

    ├── planning/
    │   Retrosynthesis and route generation

    ├── data/
    │   Dataset management

    ├── visualization/
    │   Route visualization

    ├── io/
    │   Import/export systems

    └── utils/
        Shared utilities
```

---

# Development Workflow

## 1. Create a branch

Use descriptive branch names:

Examples:

```
feature/neural-ranking
feature/new-parser
bugfix/template-loading
docs/api-update
```

---

## 2. Make changes

Keep commits focused.

Good:

```
Add reaction template validation
```

Avoid:

```
Update files
```

---

## 3. Run checks

Before submitting:

```bash
pytest
```

```bash
ruff check .
```

```bash
black .
```

---

# Coding Standards

ASP follows modern Python development practices.

## Python Version

Supported versions:

```
Python 3.10+
```

---

## Formatting

Code formatting:

```
black
```

Linting:

```
ruff
```

---

## Type Safety

Use type annotations wherever practical.

Example:

```python
def plan(
    molecule: str,
) -> PlanningResult:
    ...
```

---

## Documentation

Public functions and classes should include docstrings.

Example:

```python
def score(route):
    """
    Calculate synthesis route score.

    Parameters
    ----------
    route:
        Candidate synthesis route.

    Returns
    -------
    float
        Route quality score.
    """
```

---

# Testing

All new functionality should include tests.

Run:

```bash
pytest
```

Coverage should be maintained as the project grows.

Test categories include:

* API behavior
* CLI behavior
* Chemistry parsing
* Planning algorithms
* Scoring
* Visualization

---

# Scientific Contributions

Scientific contributions should include:

## Reproducibility

Provide:

* Dataset sources
* Configuration parameters
* Experimental settings
* Expected outputs

---

## Benchmarking

When proposing algorithms, include:

* Baseline comparisons
* Evaluation metrics
* Computational requirements

---

## Chemical Validation

New chemistry functionality should consider:

* Chemical correctness
* Reaction validity
* Dataset quality
* Known limitations

---

# Documentation Contributions

Documentation improvements are highly encouraged.

Examples:

* New tutorials
* Better examples
* Scientific explanations
* API references

Documentation should be:

* Accurate
* Clear
* Reproducible

---

# Pull Requests

A good pull request should contain:

## Description

Explain:

* What changed
* Why it was needed
* How it improves ASP

---

## Testing

Include:

* Tests added
* Commands executed
* Validation results

---

## Review Process

Pull requests may be reviewed for:

* Correctness
* Maintainability
* Scientific validity
* Documentation quality
* Compatibility

---

# Issue Guidelines

Before opening an issue:

* Search existing issues
* Confirm the problem is reproducible
* Provide relevant details

Include:

* ASP version
* Python version
* Operating system
* Error messages
* Minimal reproduction example

---

# Feature Requests

Feature requests should explain:

* The problem being solved
* Scientific or engineering motivation
* Proposed approach
* Expected impact

---

# Roadmap Contributions

ASP is designed to evolve toward increasingly autonomous scientific workflows.

Long-term development areas include:

* Machine learning retrosynthesis
* Molecular foundation models
* Reaction optimization
* Cost-aware planning
* Laboratory automation
* Closed-loop discovery systems

Contributors interested in these areas are encouraged to participate.

---

# License

By contributing to ASP, you agree that your contributions will be licensed under the project's license.

See:

```
LICENSE
```

for details.

---

Thank you for helping build open-source infrastructure for autonomous chemistry.

```
```

