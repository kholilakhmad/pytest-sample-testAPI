import requests
import json
from pprint import pprint  # for prettier JSON output
from utils.helpers import build_login_payload
from fixtures.auth_token import auth_url, headers_auth, auth_headers, token

def test_print_request_details(auth_url,auth_headers):
    payload = {
        "name": "Jane Doe",
        "job": "QA Engineer"
    }
    response = requests.post((f"{auth_url}/users"), json=payload, headers=auth_headers)
    # 🔍 Print Request Headers
    print("\n🔍 Request Headers:")
    for k, v in response.request.headers.items():
        print(f"{k}: {v}")

    # 📤 Print Request Body (decoded if JSON)
    print("\n📤 Request Body:")
    try:
        body = json.loads(response.request.body.decode()) if isinstance(response.request.body, bytes) else json.loads(response.request.body)
        print(json.dumps(body, indent=2))
    except Exception:
        print(response.request.body)  # fallback for non-JSON

    # 📥 Print Response (optional)
    print("\n📥 Response:")
    print(f"Status Code: {response.status_code}")
    print(response.text)

    assert response.status_code in [200, 201]


def test_user_create_show_token(auth_url, auth_headers):
    payload = {
        "name": "John Doe",
        "job": "Software Engineer"
    }  
    response = requests.post((f"{auth_url}/users"), json=payload, headers=auth_headers)
    assert response.status_code in [200, 201]
    pprint(response.json())

def test_login(auth_url, headers_auth):
    payload = build_login_payload("eve.holt@reqres.in", "cityslicka")
    response = requests.post((f"{auth_url}/login"), json=payload, headers=headers_auth)

    print("\n✅ TEST: Valid Login")
    print(f"📥 Status Code: {response.status_code}")
    print("📦 Response Body:")
    pprint(response.json())

    assert response.status_code == 200, f"Login failed: {response.text}"
    assert "token" in response.json(), "Token not found in response"

def test_login_invalid(auth_url, headers_auth):
    payload = build_login_payload("invalid_user", "invalid_pass")
    response = requests.post((f"{auth_url}/login"), json=payload, headers=headers_auth)

    print("\n❌ TEST: Invalid Login")
    print(f"📥 Status Code: {response.status_code}")
    print("📦 Response Body:")
    pprint(response.json())

    assert response.status_code == 400, f"Expected 400 Bad Request, got {response.status_code}"
    assert "error" in response.json(), "Error message not found in response"

def test_login_missing_fields(auth_url, headers_auth):
    payload = build_login_payload("", "")
    response = requests.post((f"{auth_url}/login"), json=payload, headers=headers_auth)

    print("\n⚠️ TEST: Missing Fields")
    print(f"📥 Status Code: {response.status_code}")
    print("📦 Response Body:")
    pprint(response.json())

    assert response.status_code == 400, f"Expected 400 Bad Request, got {response.status_code}"
    assert "error" in response.json(), "Error message not found in response"

def test_login_empty_payload(auth_url, headers_auth):
    payload = {}
    response = requests.post((f"{auth_url}/login"), json=payload, headers=headers_auth)

    print("\n⚠️ TEST: Empty Payload")
    print(f"📥 Status Code: {response.status_code}")
    print("📦 Response Body:")
    pprint(response.json())

    assert response.status_code == 400, f"Expected 400 Bad Request, got {response.status_code}"
    assert "error" in response.json(), "Error message not found in response"
