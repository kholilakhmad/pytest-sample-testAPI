import pytest
import requests
from config import config

@pytest.fixture(scope="session")
def base_url():
    return config.BASE_URL

@pytest.fixture
def headers():
    return config.HEADERS
