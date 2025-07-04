from utils.helpers import build_login_payload
import requests
import pytest
from config import config

@pytest.fixture(scope="session")
def auth_url():
    return config.AUTH_URL
    
@pytest.fixture()
def headers_auth():
    return config.AUTH_HEADERS