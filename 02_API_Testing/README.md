# REST API Test Project

Uses Python, requests and pytest to validate response codes, JSON data shapes, filtering, missing resources and a loose response-time smoke check.

## Live service
```bash
pip install -r requirements.txt
pytest -v test_posts_api.py
```
Live tests require access to `https://jsonplaceholder.typicode.com`.

## Offline demonstration
Terminal 1:
```bash
python local_mock_server.py
```
Terminal 2:
```bash
QA_API_BASE_URL=http://127.0.0.1:8765 pytest -v test_posts_api.py
```

The previous 5/5 result is **mock-only**, not evidence that the real service works.
