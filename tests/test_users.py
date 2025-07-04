import requests
from utils.helpers import build_user_payload
from config.config import BASE_URL, HEADERS
from fixtures.conftest import base_url, headers

def test_create_user(base_url, headers):
    payload = build_user_payload("Test User", "testuser", "testuser@example.com")
    response = requests.post(f"{base_url}/users", json=payload, headers=headers)
    
    assert response.status_code == 201  # Check if the user was created successfully
    
    user_data = response.json()
    assert user_data["name"] == "Test User"  # Verify the name in the response
    assert user_data["username"] == "testuser"  # Verify the username in the response

def test_get_user(base_url):
    response = requests.get(f"{base_url}/users/1")
    assert response.status_code == 200  # Check if the user was retrieved successfully
    
    user_data = response.json()
    assert user_data["id"] == 1  # Verify the user ID in the response
    assert "name" in user_data  # Ensure the name field exists
    assert "username" in user_data  # Ensure the username field exists
    
