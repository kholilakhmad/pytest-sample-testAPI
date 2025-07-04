import requests
from pprint import pprint
from fixtures.auth_token import auth_url

def test_get_users(auth_url):
    response = requests.get(f"{auth_url}/users?page=2")

    # Debug: Print request headers
    print("\n🔍 Request Headers:")
    for k, v in response.request.headers.items():
        print(f"{k}: {v}")
    
    # Status code assertion
    assert response.status_code == 200, f"Unexpected status: {response.status_code}"

    # Parse response
    response_data = response.json()

    # Top-level structure validation
    assert "page" in response_data
    assert "data" in response_data
    assert response_data["page"] == 2, f"Expected page 2, got {response_data['page']}"

    users = response_data["data"]
    assert isinstance(users, list), "Expected 'data' to be a list of users"
    assert len(users) > 0, "No users returned"

    # Print user details
    print("\n📦 Users on page 2:")
    for user in users:
        print(f"- {user['id']}: {user['first_name']} {user['last_name']} ({user['email']})")

    # Field validation with MAX LENGTH checks
    for user in users:
        # Required fields
        assert "id" in user
        assert "email" in user
        assert "first_name" in user
        assert "last_name" in user
        
        # Format validation
        assert user["email"].endswith("@reqres.in"), f"Invalid email format: {user['email']}"
        
        # Max length validation (adjust values as needed)
        assert len(user["email"]) <= 254, f"Email too long: {user['email']}"
        assert len(user["first_name"]) <= 50, f"First name too long: {user['first_name']}"
        assert len(user["last_name"]) <= 50, f"Last name too long: {user['last_name']}"
        
        # Additional: Check for empty strings
        assert user["first_name"].strip() != "", "First name is empty"
        assert user["last_name"].strip() != "", "Last name is empty"

    print("\n✅ All users validated successfully with length constraints!")