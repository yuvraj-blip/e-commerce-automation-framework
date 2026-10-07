# 🛒 E-Commerce Web Automation Framework

[![Python](https://img.shields.io/badge/Python-3.12%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Selenium-4.x-43B02A.svg?logo=selenium&logoColor=white)](https://www.selenium.dev/)
[![Pytest](https://img.shields.io/badge/Pytest-8.x-0A9EDC.svg?logo=pytest&logoColor=white)](https://docs.pytest.org/)
[![Design Pattern](https://img.shields.io/badge/Pattern-Page%20Object%20Model-orange.svg)]()
[![Automation](https://img.shields.io/badge/Target-Automation%20Exercise-purple.svg)](https://automationexercise.com/)
[![CI Ready](https://img.shields.io/badge/CI-Ready%20(Headless)-brightgreen.svg)]()

A production-grade, scalable End-to-End (E2E) Web UI Automation Testing framework designed using **Python**, **Selenium WebDriver**, and **Pytest**. Built on top of the **Page Object Model (POM)** design pattern, this framework automates critical user workflows on the [Automation Exercise](https://automationexercise.com/) e-commerce platform.

---

## 🌟 Key Highlights & Architectural Strengths

* **Page Object Model (POM) Design**: Strictly decouples web element locators and page interactions from test assertions, maximizing code reusability and reducing maintenance overhead when UI changes occur.
* **Resilient Synchronization**: Zero hardcoded `sleep` pauses. Features a centralized `BasePage` leveraging Selenium `WebDriverWait` and `expected_conditions` for dynamic synchronization against real-world network latency.
* **Driver Factory Pattern**: Centralized browser lifecycle management (`utils/driver_factory.py`) with support for Chrome configuration, options flags, maximized windows, and seamless headless mode for CI/CD pipelines.
* **Data-Driven Testing (DDT)**: Decouples test data from test scripts using external JSON data files (`test_data/user_data.json`) with `pytest.mark.parametrize`.
* **Idempotent & Self-Cleaning Tests**: Employs timestamped unique user generation combined with end-to-end account deletion to ensure tests can run indefinitely without database collisions or test state pollution.
* **Automated HTML Reporting**: Out-of-the-box integration with `pytest-html` generating self-contained, interactive test reports detailing execution status, duration, and stack traces.

---

## 🏗️ Architecture & Project Structure

```text
e-commerce-automation-framework/
│
├── pages/                      # Page Object Model layer
│   ├── __init__.py
│   ├── base_page.py            # Generic wrapper with explicit waits and driver helpers
│   ├── home_page.py            # Home page actions and locators
│   ├── signup_page.py          # User signup and login form interactions
│   ├── enter_acct_info_page.py # Detailed account profile & address submission
│   ├── acct_created_page.py    # Account creation confirmation & continue navigation
│   ├── account_delete_page.py  # Account deletion verification
│   └── nav_bar.py              # Navigation bar elements and session verification
│
├── tests/                      # Automated Test Suites
│   ├── __init__.py
│   └── test_user_registration.py # E2E Test Case 1: Register User & Delete Account
│
├── test_data/                  # Externalized Test Datasets
│   └── user_data.json          # Parameterized user credentials and profile inputs
│
├── utils/                      # Utilities & Infrastructure
│   ├── __init__.py
│   └── driver_factory.py       # WebDriver initialization with headless & options support
│
├── .gitignore                  # Git ignore rules for environments, caches, and reports
├── conftest.py                 # Pytest root configuration, fixtures, and custom CLI options
├── pytest.ini                  # Pytest runner settings, markers, and report defaults
├── requirements.txt            # Project dependencies manifest
└── README.md                   # Framework documentation
```

---

## 🛠️ Technology Stack

| Technology | Purpose |
| :--- | :--- |
| **Python 3.12+** | Core programming language |
| **Selenium WebDriver 4.x** | Browser automation engine |
| **Pytest** | Test execution framework, fixtures, and parameterization |
| **pytest-html** | Interactive HTML reporting |
| **pytest-xdist** | Multi-threaded parallel test execution |
| **python-dotenv** | Environment configuration management |

---

## 🚀 Getting Started

### 1. Prerequisites
Ensure you have the following installed:
* **Python 3.10+** (Python 3.12 recommended): [python.org](https://www.python.org/downloads/)
* **Google Chrome**: Latest stable version (ChromeDriver is managed automatically by Selenium 4 Manager).

### 2. Clone the Repository
```bash
git clone https://github.com/yuvraj-blip/e-commerce-automation-framework.git
cd e-commerce-automation-framework
```

### 3. Create and Activate a Virtual Environment
```bash
# Windows (PowerShell / Command Prompt)
python -m venv .venv
.venv\Scripts\activate

# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🧪 Test Execution

### Run All Tests (Headed Mode)
```bash
pytest
```

### Run Tests in Headless Mode (Ideal for CI/CD)
```bash
pytest --headless
```

### Run Specific Test Suite or File
```bash
pytest tests/test_user_registration.py -v
```

### Run by Pytest Marker
```bash
# Run Smoke Suite
pytest -m smoke

# Run End-to-End Suite
pytest -m e2e
```

### Parallel Execution (Accelerate Execution)
```bash
pytest -n 2
```

### Generate Self-Contained HTML Report
```bash
pytest --html=reports/report.html --self-contained-html
```
The resulting test report will be available at `reports/report.html`.

---

## 📋 Test Scenarios Covered

### **Test Case 1: Register User and Delete Account (Full Lifecycle)**
* **Target**: `https://automationexercise.com/`
* **Workflow**:
  1. Launch browser and navigate to home page.
  2. Verify home page title is `"Automation Exercise"`.
  3. Navigate to **Signup / Login** page.
  4. Verify visibility of **'New User Signup!'**.
  5. Fill user name and unique email address, then submit.
  6. Verify **'ENTER ACCOUNT INFORMATION'** section is displayed.
  7. Fill title, password, date of birth, and opt-in checkboxes.
  8. Fill address information (name, company, street, state, city, zipcode, phone).
  9. Click **'Create Account'** and verify **'ACCOUNT CREATED!'** confirmation.
  10. Click **'Continue'** and verify header displays **'Logged in as username'**.
  11. Click **'Delete Account'** and verify **'ACCOUNT DELETED!'** confirmation.
  12. Click **'Continue'** to complete teardown and return to clean state.

---

## 📈 Engineering Best Practices Applied

1. **Locators with Custom Attributes**: Primary locators utilize stable `data-qa` attributes to ensure test resiliency against CSS/design refactors.
2. **Dynamic Data Generation**: Prevents brittle tests by generating unique emails on the fly, eliminating reliance on static test state.
3. **Automated Teardown**: Deleting created test accounts at the end of execution guarantees an idempotent database state.
4. **Zero Flakiness Policy**: Replaced arbitrary pauses with explicit conditional waits on interactive states (`element_to_be_clickable`, `visibility_of_element_located`).

---

## 👤 Author
* **Yuvraj** — [GitHub Profile](https://github.com/yuvraj-blip)
* Feel free to submit issues or pull requests for framework extensions!
