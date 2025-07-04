import requests
from pprint import pprint
from fixtures.auth_token import auth_url  # ✅ fixture


def test_get_users(auth_url):  # ✅ accept fixture here
    response = requests.get(f"{auth_url}/users?page=2")

    print("\n🔍 Request Headers:")
    for k, v in response.request.headers.items():
        print(f"{k}: {v}")
        
    # ✅ Assert status
    assert response.status_code == 200, f"Unexpected status: {response.status_code}"

    # ✅ Parse response body
    response_data = response.json()

    # ✅ Assert top-level keys
    assert "page" in response_data
    assert "data" in response_data

    # ✅ Check if page is 2
    assert response_data["page"] == 2, f"Expected page 2, got {response_data['page']}"

    users = response_data["data"]
    assert isinstance(users, list), "Expected 'data' to be a list of users"
    assert len(users) > 0, "No users returned"

    print("\n📦 Users on page 2:")
    for user in users:
        print(f"- {user['id']}: {user['first_name']} {user['last_name']} ({user['email']})")

    # ✅ Field validation
    for user in users:
        assert "id" in user
        assert "email" in user
        assert user["email"].endswith("@reqres.in"), f"Unexpected email format: {user['email']}"
    print("\n✅ All users validated successfully!")