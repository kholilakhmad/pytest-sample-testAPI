import pytest
import requests
from utils.helpers import build_login_payload

# This returns the base URL and headers from config
from config.config import AUTH_URL, AUTH_HEADERS

@pytest.fixture(scope="session")
def auth_url():
    return AUTH_URL

@pytest.fixture(scope="session")
def headers_auth():
    return AUTH_HEADERS

@pytest.fixture(scope="session")
def token(auth_url, headers_auth):
    payload = build_login_payload("eve.holt@reqres.in", "cityslicka")
    response = requests.post((f"{auth_url}/login"), json=payload, headers=headers_auth)

    assert response.status_code == 200, f"Login failed: {response.text}"
    token = response.json().get("token")
    assert token is not None, "No token found in response"
    print(f"\n🔐 Stored Token: {token}")  # optional: print token

    return token

@pytest.fixture
def auth_headers(token):
    return {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "x-api-key": "reqres-free-v1"
    }
