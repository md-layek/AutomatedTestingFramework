# Automated Testing Framework

This project is an automated testing framework built using Playwright and pytest, designed for cross-browser testing and comprehensive report generation using Allure.

## Table of Contents

1. Project Overview
2. Prerequisites
3. Installation
4. Project Structure
5. Running Tests
6. Github Actions Integration
7. Troubleshooting
8. Contributing
9. License


## Project Overview

This project aims to automate testing of web applications across multiple browsers using Playwright. It provides reliable retry mechanisms, logs, and failure screenshots for easier debugging. The framework supports continuous integration with GitHub Actions, and test results are visualized using Allure Reports.

Key Features:
Cross-browser testing: Support for Chromium, Firefox, and WebKit browsers.
Allure reporting: Comprehensive test reports with failure screenshots.
Retry Mechanism: Automated retries on failures to handle flaky tests.
CI Integration: Runs tests on push and pull requests using GitHub Actions.


## Prerequisites

Before you begin, ensure that you have the following installed on your system:

- **Python 3.12+**
- **Node.js** (v20.x.x or higher)
- **pip** (Python package manager)
- **Allure CLI** for generating test reports


## Installation

To install and set up the project, follow these steps:

Clone the repository:

git clone https://github.com/yourusername/automated-testing-framework.git

cd automated-testing-framework

Create a virtual environment:

`python -m venv .venv
`

`source .venv/bin/activate`  # On Windows: .venv\Scripts\activate

Install dependencies:

`pip install --upgrade pip`

`pip install pytest pytest-playwright allure-pytest pytest-rerunfailures pytest-timeout`

`playwright install --with-deps`

or you can install dependencies by running this command

`pip install -r requirements.txt`

Set up Playwright: Install the required browsers by running:
`playwright install`

Install Allure CLI:
`pip install allure-commandline`

Running Tests
Basic Test Run: You can run all tests using:
`pytest`

Run Cross-browser Tests: You can specify the browser to run the tests:

`pytest --browser=chromium`

`pytest --browser=firefox`

`pytest --browser=webkit`

Run with Allure Report Generation: To run tests and generate Allure reports:

`pytest --alluredir=reports/allure-results`

View Allure Report: After running the tests, generate the Allure report:

`allure generate reports/allure-results --clean`

`allure open`

## Project Structure
`
AutomatedTestingFramework/
│
├── .github/
│   └── workflows/
│       └── ci.yml                # CI configuration for GitHub Actions
│
├── .venv/                         # Virtual environment directory (not part of version control)
│
├── logs/                          # Log files generated during test runs
│
├── reports/
│   └── allure-results/            # Allure test reports generated after the tests
│
├── tests/
│   ├── files/
│   │   └── testfile.txt           # Example test file for file upload
│   ├── conftest.py                # Pytest configuration and fixtures
│   ├── test_ci_integration.py     # Test case for CI integration
│   ├── test_cross_browser.py      # Test cases for cross-browser testing
│   ├── test_dropdown_and_alerts.py# Test cases for dropdowns and JavaScript alerts
│   ├── test_dynamic_content.py    # Test case for dynamic content page
│   ├── test_file_upload.py        # Test case for file upload
│   ├── test_user_auth.py          # Test cases for user authentication (login)
│
├── utils/
│   ├── __init__.py                # Init file for utils module
│   └── test_utilities.py          # Utility functions like retry actions, login, etc.
│
├── .gitignore                     # Files and directories to ignore in version control
├── failure_firefox_success.png    # Screenshot taken on Firefox during a successful login
├── failure_javascript_alert_chromium.png  # Screenshot taken on Chromium during JavaScript alert test
├── failure_login_chromium.png     # Screenshot taken on login failure in Chromium
├── failure_login_firefox.png      # Screenshot taken on login failure in Firefox
├── pytest.ini                     # Pytest configuration file
├── README.md                      # Project documentation
├── requirements.txt               # Python dependencies
`

## Running Tests Locally

Running the Full Test Suite
To run the full test suite across all supported browsers (Chromium, Firefox, WebKit), use the following command:

`pytest --alluredir=reports/allure-results --browser=chromium --reruns 2 --timeout=180000 -vv
`

Command Breakdown:

--alluredir=reports/allure-results: Specifies the directory where Allure will store test results.

--browser=chromium: Run the tests in the Chromium browser (can be changed to firefox or webkit).

--reruns 2: Retry any failed tests up to 2 times.

--timeout=180000: Set a timeout for each test.

-vv: Verbose mode for more detailed test output.

Running Tests in Specific Browsers
To run tests in a specific browser, update the --browser option. For example, to run tests in Firefox:

pytest --alluredir=reports/allure-results --browser=firefox --reruns 2 --timeout=180000 -vv
Viewing Allure Reports
After running the tests, generate and view the Allure report with:

allure serve reports/allure-results
This command will start a local server and open the Allure report in your browser.

## GitHub Actions Integration

This project is integrated with GitHub Actions for continuous integration. The tests run automatically on every push to the main branch or when a pull request is opened.

CI Features
Multiple Browsers: Tests run on Chromium, Firefox, and WebKit.
Allure Reports: Generated after the test run and uploaded as artifacts.
Automatic Retries: Failed tests are retried up to 2 times.


## Troubleshooting

Common Issues
Allure Reports Not Generating:

Ensure Allure is installed correctly and referenced in the test command.
Verify the --alluredir option is set.

Timeouts:
Increase the timeout value if tests are failing due to timeouts. For example:

pytest --timeout=240000

GitHub Actions Failures:
Check the logs in the Actions tab for detailed error messages.

## Contributing

We welcome contributions to this project. To contribute:

Fork this repository.
Create a new branch (git checkout -b feature-branch).
Make your changes and commit them (git commit -m 'Add some feature').
Push to the branch (git push origin feature-branch).
Open a pull request.

Code Style
Ensure all Python code is formatted with black. You can run:
black .

Tests should follow the structure and conventions used in the existing tests.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

This version of the `README.md` is complete and detailed, covering the setup, running 

