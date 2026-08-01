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

