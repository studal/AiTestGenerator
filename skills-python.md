# Python Pytest Requests API Testing Framework

## Overview

This framework is designed for automated API testing using **Python**, **Pytest**, and the **Requests** library. It helps QA engineers create scalable, maintainable, and reusable API tests.

---

## Tech Stack

* **Python** – Core programming language
* **Pytest** – Test runner and assertion framework
* **Requests** – HTTP client for API calls
* **Allure / HTML Reports** – Reporting
* **Pytest Fixtures** – Reusable setup and teardown
* **JSON / YAML** – Test data and configuration
* **Pydantic / JSONSchema** – Response schema validation
* **Logging** – Debugging and traceability

---

## Typical Folder Structure

```text
project/
│
├── tests/
│   ├── test_login.py
│   ├── test_users.py
│
├── utils/
│   ├── api_client.py
│   ├── logger.py
│   ├── helpers.py
│
├── data/
│   ├── test_data.json
│
├── config/
│   ├── config.yaml
│
├── conftest.py
├── requirements.txt
└── pytest.ini
```

---

## Core Concepts

### 1. API Client Layer

Encapsulates HTTP methods for reusability.

```python
import requests

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint, **kwargs):
        return requests.get(f"{self.base_url}{endpoint}", **kwargs)

    def post(self, endpoint, **kwargs):
        return requests.post(f"{self.base_url}{endpoint}", **kwargs)
```

---

### 2. Fixtures in `conftest.py`

Used for setup like auth token, base URL, or client object.

```python
import pytest
from utils.api_client import APIClient

@pytest.fixture
def api_client():
    return APIClient("https://reqres.in")
```

---

### 3. Writing Tests

```python
def test_get_users(api_client):
    response = api_client.get("/api/users?page=2")
    assert response.status_code == 200
    assert "data" in response.json()
```

---

### 4. Parameterization

Run same test with multiple inputs.

```python
import pytest

@pytest.mark.parametrize("user_id", [1, 2, 3])
def test_get_user(api_client, user_id):
    response = api_client.get(f"/api/users/{user_id}")
    assert response.status_code == 200
```

---

### 5. Schema Validation

Validate API response structure.

```python
from jsonschema import validate

schema = {
    "type": "object",
    "properties": {
        "data": {"type": "array"}
    }
}

validate(instance=response.json(), schema=schema)
```

---

## Best Practices

* Keep test logic separate from API request logic.
* Use fixtures for authentication/session reuse.
* Store environment configs externally.
* Validate status code, body, headers, and schema.
* Use markers like `smoke`, `regression`, `sanity`.
* Generate reports after execution.

---

## Common Commands

```bash
pytest -v
pytest -m smoke
pytest --html=report.html
allure serve allure-results
```

---

## Use Cases

* REST API functional testing
* Regression testing
* Smoke/Sanity checks
* Contract/schema validation
* Authentication/authorization testing
* Data-driven API testing
