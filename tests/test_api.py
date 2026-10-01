import requests
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"

@pytest.fixture
def post_response():
    return requests.get(f"{BASE_URL}/posts/1")


def test_get_post_return_200(post_response):
    assert post_response.status_code == 200

def test_get_post_has_correct_id(post_response):
    data = post_response.json()
    assert data["id"] == 1
    assert "title" in data

def test_get_post_return_404():
    response = requests.get(f"{BASE_URL}/posts/9999")
    assert response.status_code == 404

def test_has_name_LeanneGraham():
    response = requests.get(f"{BASE_URL}/users/1")
    data = response.json()
    assert data["name"] == "Leanne Graham"

def test_returns_10_posts():
    response = requests.get(f"{BASE_URL}/posts?userId=1")
    data = response.json()
    assert len(data) == 10