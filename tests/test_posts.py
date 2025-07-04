import requests
from utils.helpers import build_post_payload
from config.config import BASE_URL, HEADERS
from fixtures.conftest import base_url, headers


def test_get_post(base_url):
    response = requests.get(f"{BASE_URL}/posts/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1

def test_create_post(base_url, headers):
    payload = build_post_payload("Test Title", "Test Body", 1)
    response = requests.post(f"{base_url}/posts", json=payload, headers=headers)
    assert response.status_code == 201
    assert response.json()["title"] == "Test Title"
