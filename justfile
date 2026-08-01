# List the available recipes.
[group('Utility')]
default:
    @just --list

# Install the project and development dependencies.
[group('Setup')]
setup:
    pip install --upgrade pip
    pip install -e ".[dev]"

# Run the test suite.
[group('Testing')]
test:
    pytest tests/

# Check code quality with Ruff.
[group('Quality')]
lint:
    ruff check .

# Check types with mypy.
[group('Quality')]
mypy:
    mypy syllapy

# Apply Ruff formatting.
[group('Quality')]
format:
    ruff format .

# Check formatting without modifying files.
[group('Quality')]
format-check:
    ruff format --check .

# Format, lint, test, and build the package for agent validation.
[group('Agent')]
agent-validate:
    just format
    just lint
    just test
    python -m build
