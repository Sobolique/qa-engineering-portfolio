"""API smoke checks; change QA_API_BASE_URL for local test fixture."""
import os
import requests

BASE_URL = os.getenv("QA_API_BASE_URL", "https://jsonplaceholder.typicode.com")
TIMEOUT = 15

def test_get_single_post():
    r = requests.get(f"{BASE_URL}/posts/1", timeout=TIMEOUT)
    assert r.status_code == 200
    assert "application/json" in r.headers.get("Content-Type", "")
    body = r.json()
    assert body["id"] == 1
    assert isinstance(body["userId"], int)
    assert isinstance(body["title"], str) and body["title"]
    assert isinstance(body["body"], str) and body["body"]

def test_list_posts():
    r = requests.get(f"{BASE_URL}/posts", timeout=TIMEOUT)
    assert r.status_code == 200
    posts = r.json()
    assert isinstance(posts, list) and len(posts) > 0
    assert all(isinstance(post.get("id"), int) for post in posts)

def test_filter_posts_by_user_id():
    r = requests.get(f"{BASE_URL}/posts", params={"userId": 1}, timeout=TIMEOUT)
    assert r.status_code == 200
    posts = r.json()
    assert posts
    assert all(post["userId"] == 1 for post in posts)

def test_nonexistent_post_returns_404():
    r = requests.get(f"{BASE_URL}/posts/999999", timeout=TIMEOUT)
    assert r.status_code == 404

def test_response_time_smoke():
    r = requests.get(f"{BASE_URL}/posts/1", timeout=TIMEOUT)
    assert r.status_code == 200
    assert r.elapsed.total_seconds() < 10
