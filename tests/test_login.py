import requests
from pprint import pprint  # for prettier JSON output
from utils.helpers import build_login_payload
from config.config import AUTH_URL, AUTH_HEADERS
from fixtures.auth_token import auth_url, headers_auth


def test_login(auth_url, headers_auth):
    payload = build_login_payload("eve.holt@reqres.in", "cityslicka")
    response = requests.post(auth_url, json=payload, headers=headers_auth)

    print("\n✅ TEST: Valid Login")
    print(f"📥 Status Code: {response.status_code}")
    print("📦 Response Body:")
    pprint(response.json())

    assert response.status_code == 200, f"Login failed: {response.text}"
    assert "token" in response.json(), "Token not found in response"

def test_login_invalid(auth_url, headers_auth):
    payload = build_login_payload("invalid_user", "invalid_pass")
    response = requests.post(auth_url, json=payload, headers=headers_auth)

    print("\n❌ TEST: Invalid Login")
    print(f"📥 Status Code: {response.status_code}")
    print("📦 Response Body:")
    pprint(response.json())

    assert response.status_code == 400, f"Expected 400 Bad Request, got {response.status_code}"
    assert "error" in response.json(), "Error message not found in response"

def test_login_missing_fields(auth_url, headers_auth):
    payload = build_login_payload("", "")
    response = requests.post(auth_url, json=payload, headers=headers_auth)

    print("\n⚠️ TEST: Missing Fields")
    print(f"📥 Status Code: {response.status_code}")
    print("📦 Response Body:")
    pprint(response.json())

    assert response.status_code == 400, f"Expected 400 Bad Request, got {response.status_code}"
    assert "error" in response.json(), "Error message not found in response"

def test_login_empty_payload(auth_url, headers_auth):
    payload = {}
    response = requests.post(auth_url, json=payload, headers=headers_auth)

    print("\n⚠️ TEST: Empty Payload")
    print(f"📥 Status Code: {response.status_code}")
    print("📦 Response Body:")
    pprint(response.json())

    assert response.status_code == 400, f"Expected 400 Bad Request, got {response.status_code}"
    assert "error" in response.json(), "Error message not found in response"
