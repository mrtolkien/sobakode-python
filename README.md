# sobakode-python

[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v1.json)](https://github.com/charliermarsh/ruff)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![pre-commit enabled][pre-commit badge]][pre-commit project]

[pre-commit badge]: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
[pre-commit project]: https://pre-commit.com/

Python cookie cutter template

## Philosophy

Don't write spahetti code, write [sobakode](https://blog.tolki.dev/sobakode/). It tastes better.

This template is optimized for use with [VS Code](https://github.com/python/mypy) and provides an `extensions.json` and `settings.json` for the workspace.

## Tooling

- [Ruff](https://github.com/charliermarsh/ruff): Insanely fast Python linter
- [MyPy](https://github.com/python/mypy): Static typing for python
- [Black](https://github.com/psf/black): Python code formatter
- [Pre-commit](https://pre-commit.com/): Ensures that committed code passes `ruff` and `black`
- [MkDocs Material](https://squidfunk.github.io/mkdocs-material/): Superb documentation made simple

## Pre-requisites

- [Git](https://git-scm.com/)
- [Poetry](https://python-poetry.org/)

## TODO

- Configuration files for Ruff, MyPy, and Black
- Add Markdown linter
- Add template configuration options (python version, enabling MyPy in pre-commit and CI/CD, ...)
