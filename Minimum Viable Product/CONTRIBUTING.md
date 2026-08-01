# Contributing to Autonomous Synthesis Planner

First off, thank you for considering contributing to **Autonomous Synthesis Planner (ASP)**.

The goal of this project is to build an open, modular, and reproducible software platform for autonomous chemical synthesis planning. Contributions from researchers, developers, students, and the broader open-source community are greatly appreciated.

---

# Table of Contents

* Code of Conduct
* Ways to Contribute
* Development Setup
* Project Structure
* Development Workflow
* Coding Standards
* Testing
* Documentation
* Pull Requests
* Reporting Issues
* Feature Requests
* Community

---

# Code of Conduct

By participating in this project, you agree to abide by the project's **Code of Conduct**.

Please help create a welcoming, inclusive, and respectful environment for everyone.

---

# Ways to Contribute

There are many ways to contribute to ASP, including:

## Software Development

* Implement new features
* Improve existing modules
* Fix bugs
* Optimize performance
* Improve architecture

---

## Chemistry

* Reaction templates
* Molecular utilities
* Validation algorithms
* Route scoring strategies

---

## Documentation

* Tutorials
* Examples
* API documentation
* User guides

---

## Testing

* Unit tests
* Integration tests
* Performance benchmarks
* Regression tests

---

## Research

* Novel planning algorithms
* Search strategies
* Optimization techniques
* Benchmark datasets

---

# Development Setup

## Clone the Repository

```bash
git clone https://github.com/<username>/autonomous-synthesis-planner.git

cd autonomous-synthesis-planner
```

---

## Create a Virtual Environment

```bash
python -m venv .venv
```

Linux/macOS

```bash
source .venv/bin/activate
```

Windows

```powershell
.venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -e .

pip install -r requirements.txt
```

---

# Project Structure

```text
src/
tests/
docs/
examples/
datasets/
scripts/
```

Please place new code in the appropriate module rather than creating new top-level directories.

---

# Development Workflow

1. Fork the repository.
2. Create a new branch.

```bash
git checkout -b feature/my-feature
```

3. Implement your changes.
4. Add or update tests.
5. Update documentation if needed.
6. Ensure all checks pass.
7. Commit your changes.
8. Open a Pull Request.

---

# Coding Standards

ASP follows modern Python best practices.

## Formatting

```bash
black src tests
```

---

## Linting

```bash
ruff check src tests
```

---

## Type Checking

```bash
mypy src
```

---

## General Guidelines

* Write readable code.
* Prefer small functions.
* Use descriptive names.
* Add type hints.
* Keep modules focused.
* Avoid duplicated logic.
* Document public APIs.

---

# Testing

Run all tests before submitting a Pull Request.

```bash
pytest
```

Generate coverage

```bash
pytest --cov=asp
```

All new features should include appropriate tests.

---

# Documentation

Documentation is considered part of the software.

Please update documentation whenever:

* New features are added.
* APIs change.
* CLI commands change.
* Configuration changes.

---

# Commit Messages

Use concise, descriptive commit messages.

Examples:

```text
Add beam search planner

Improve route scoring

Fix parser validation bug

Add visualization tests

Update API documentation
```

---

# Pull Requests

Before opening a Pull Request, ensure:

* All tests pass.
* Code is formatted.
* Linting passes.
* Type checking passes.
* Documentation is updated.
* No unnecessary files are included.

Please include:

* A summary of the change
* Motivation
* Implementation details
* Testing performed

---

# Reporting Bugs

When reporting a bug, please include:

* Python version
* Operating system
* ASP version
* Steps to reproduce
* Expected behavior
* Actual behavior
* Error messages
* Stack trace (if applicable)

Minimal reproducible examples are highly encouraged.

---

# Feature Requests

Feature requests should include:

* Motivation
* Proposed solution
* Alternative approaches (if any)
* Expected impact

The more context provided, the easier it is to evaluate and discuss the proposal.

---

# Questions and Discussions

General questions, design discussions, and ideas are welcome through GitHub Discussions or Issues.

Constructive feedback from the community helps improve the project for everyone.

---

# Recognition

All contributors—whether through code, documentation, testing, design, or discussion—are valued members of the project.

Every contribution helps advance open scientific software.

---

# Thank You

Thank you for helping build **Autonomous Synthesis Planner**.

Together, we can create an open, extensible, and reproducible software platform for autonomous synthesis planning.

