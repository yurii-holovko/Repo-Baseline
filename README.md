# Repo-Baseline

![CI Status](https://github.com/yurii-holovko/Repo-Baseline/actions/workflows/ci.yml/badge.svg)

A robust Python 3.14 project template featuring automated linting, formatting, and CI/CD.

## Getting Started

### Prerequisites
* **Python 3.14+**
* **Git**

### Installation
1. **Clone the repository**:
```bash
git clone [https://github.com/yurii-holovko/Repo-Baseline.git](https://github.com/yurii-holovko/Repo-Baseline.git)
cd Repo-Baseline
```

2. **Setup environment**:
```bash
python -m venv venv
.\venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux
```


3. **Install tools**:
```bash
make setup
```



## Development Tools

* **Formatter**: `black` & `isort`
* **Linter**: `flake8`
* **Tests**: `pytest`
* **Security**: `detect-secrets`

## Configuration

Initialize your local environment variables:

```bash
cp .env.example .env
```

## Commands

Use the following `make` commands for a standardized workflow:

| Command | Description |
| --- | --- |
| `make run` | Executes the main application (`src/main.py`) |
| `make test` | Runs the full `pytest` suite |
| `make check` | Runs the full suite: formatting (black/isort), linting (flake8), and tests |
| `make setup` | Installs dependencies and sets up pre-commit hooks |
