# Calculator Lab Project

## Description

This project is a Python-based calculator developed as part of the SCCM4910 DevOps coursework.

The original calculator supports interactive arithmetic operations. The coursework extends it with CSV batch processing, input validation, automated testing and continuous integration.

The batch-processing functionality supports normal and mixed CSV files. Invalid calculations are reported without preventing subsequent valid records from being processed.

## Acceptance Criteria

- The calculator must accept two numerical inputs.
- The calculator must support addition (+), subtraction (-), multiplication (*) and division (/).
- The calculator must correctly calculate the results of supported operations.
- The calculator must handle invalid input appropriately.
- The batch calculator must process CSV files containing multiple calculations.
- Invalid batch records must be handled without stopping subsequent calculations.
- The automated test suite must pass successfully.
- GitHub Actions must independently run the automated tests.

## Acknowledgements

- Original test files and supporting resources supplied by the university.
- Supplied batch-processing runner, CSV data and expected output examples.

## Requirements

- Python 3.
- Git, for version control and pre-commit hooks.
- pytest, for running the automated test suite.

Install the development dependencies using:

python3 -m pip install -r requirements-dev.txt

Check the pytest installation with:

python3 -m pytest --version


## Running the Calculator

To launch the interactive calculator, run:

./run.sh

Alternatively, run the Python file directly:

python3 calculator.py

The calculator supports the following operations:

- Addition (+)
- Subtraction (-)
- Multiplication (*)
- Division (/)

Stop the calculator interface using Ctrl + C.

## Running the Tests

The project contains two test-checking scripts.

### Original coursework quality gate

The original quality gate can be executed using:

./check.sh


This runs pytest and displays a QUALITY GATE PASSED message when all tests succeed.

### Common test check script

The extended coursework introduces a common test script:

./scripts/check.sh

This executes the automated test suite using pytest.

The common script is used by local development, the Git pre-commit hook and GitHub Actions, ensuring that the same test command is used across these environments.

The current test suite contains 28 tests covering the original calculator functionality and the extended batch calculator functionality.

## Git Pre-commit Hook

This project includes a Git pre-commit hook that automatically runs the test suite before a commit is created.

The hook is stored in .githooks/pre-commit and executes the common test script at ./scripts/check.sh.

If the tests pass, Git allows the commit to proceed. If any tests fail, the hook returns a non-zero exit status and Git prevents the commit from being created.

### Installation

After cloning the repository, ensure Python is installed and install the development dependencies:

python3 -m pip install -r requirements-dev.txt

Configure Git to use the version-controlled hooks directory:

git config core.hooksPath .githooks


This configuration must be performed separately for each local clone. The hook is already stored with executable permissions in the repository.

### Running the checks manually

The common test script can also be executed manually:
./scripts/check.sh

### Hook limitations

The pre-commit hook is a local quality check. It is not automatically activated when cloning the repository and can be bypassed by a user.

GitHub Actions independently runs the test script as part of the CI workflow, providing an additional quality gate through the configured push and pull-request events.

## Continuous Integration

GitHub Actions is used to automate the testing process.

The CI workflow:

- Checks out the repository.
- Sets up Python.
- Installs the development dependencies.
- Executes ./scripts/check.sh.
- Fails the workflow if the tests do not pass.