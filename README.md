# 🧪 API Testing Project with Pytest

This project is a structured API test suite using [`pytest`](https://docs.pytest.org/) and [`requests`](https://docs.python-requests.org/), focused on token-based authentication.

---

## 📌 Features

- ✅ Login API testing with token extraction
- 🔐 Reusable authentication token using pytest fixtures
- 👤 Create user with token-based authorization
- 🧪 Organized project structure for scalability
- 📥 Console logging for status and response details

---

## 📁 Project Structure
api_test_project/
├── config/ # Configs (base URLs, headers)
│ └── config.py
├── fixtures/ # Reusable pytest fixtures
│ └── auth_token.py
├── tests/ # All API test cases
│ ├── test_auth.py # Login tests
│ └── test_users.py # Authenticated user actions
├── utils/ # Payload builders & helpers
│ └── helpers.py
├── README.md
├── requirements.txt
└── pytest.ini

Run All tests
pytest -v -s


