# Automated Testing Framework

This project is an automated testing framework built using Playwright and pytest, designed for cross-browser testing and comprehensive report generation using Allure.

## Table of Contents

1. Project Overview
2. Prerequisites
3. Installation
4. Running Tests
5. Github Actions Integration
6. Troubleshooting
7. Contributing
8. License

## Project Overview

This project aims to automate testing of web applications across multiple browsers using Playwright. It provides reliable retry mechanisms, logs, and failure screenshots for easier debugging. The framework supports continuous integration with GitHub Actions, and test results are visualized using Allure Reports.

Key Features:
- Cross-browser testing: Support for Chromium, Firefox, and WebKit browsers.
- Allure reporting: Comprehensive test reports with failure screenshots.
- Retry Mechanism: Automated retries on failures to handle flaky tests.
- CI Integration: Runs tests on push and pull requests using GitHub Actions.

## Prerequisites

Before you begin, ensure that you have the following installed on your system:

- **Python 3.12+**
- **pip** (Python package manager)
- **Allure CLI** for generating test reports

## Installation

To install and set up the project, follow these steps:

Clone the repository:

```
git clone https://github.com/yourusername/automated-testing-framework.git
cd automated-testing-framework
```

Create a virtual environment:

```
python -m venv .venv
```

Activate the virtual environment:

```
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

Install dependencies:

```
pip install --upgrade pip
pip install pytest pytest-playwright allure-pytest pytest-rerunfailures pytest-timeout
playwright install --with-deps
```

Or install dependencies by running:

```
pip install -r requirements.txt
```

Set up Playwright by installing the required browsers:

```
playwright install
```

Install Allure CLI:

```
pip install allure-pytest
```

## Running Tests

### Basic Test Run

To run all tests:

```
pytest
```

### Run Cross-browser Tests

Specify the browser to run the tests:

```
pytest --browser=chromium
pytest --browser=firefox
pytest --browser=webkit
```

### Run with Allure Report Generation

To run tests and generate Allure reports:

```
pytest --alluredir=reports/allure-results
```

### Viewing Allure Reports

After running the tests, generate and view the Allure report with:

```
allure serve reports/allure-results
```

## Running Tests Locally

To run the full test suite across all supported browsers (Chromium, Firefox, WebKit), use the following command:

```
pytest --alluredir=reports/allure-results --browser=chromium --reruns 2 --timeout=180000 -vv
```

### Command Breakdown:

- `--alluredir=reports/allure-results`: Specifies the directory where Allure will store test results.
- `--browser=chromium`: Run the tests in the Chromium browser (can be changed to firefox or webkit).
- `--reruns 2`: Retry any failed tests up to 2 times.
- `--timeout=180000`: Set a timeout for each test.
- `-vv`: Verbose mode for more detailed test output.

## GitHub Actions Integration

This project is integrated with GitHub Actions for continuous integration. The tests run automatically on every push to the main branch or when a pull request is opened.

### CI Features

- **Multiple Browsers**: Tests run on Chromium, Firefox, and WebKit.
- **Allure Reports**: Generated after the test run and uploaded as artifacts.
- **Automatic Retries**: Failed tests are retried up to 2 times.

## Troubleshooting

### Common Issues

**Allure Reports Not Generating**:
- Ensure Allure is installed correctly and referenced in the test command.
- Verify the `--alluredir` option is set.

**Timeouts**:
- Increase the timeout value if tests are failing due to timeouts. For example:

```
pytest --timeout=240000
```

**GitHub Actions Failures**:
- Check the logs in the Actions tab for detailed error messages.

## Contributing

I welcome contributions to this project. To contribute:

1. Fork this repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

### Code Style

Ensure all Python code is formatted with black. You can run:

```
black .
```

Tests should follow the structure and conventions used in the existing tests.

## License

This project is licensed under the MIT License.
