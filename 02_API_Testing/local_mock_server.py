"""Deterministic offline practice fixture, not the live JSONPlaceholder API."""
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse, parse_qs
import json

POSTS = [
    {"userId": 1, "id": 1, "title": "sample one", "body": "sample body one"},
    {"userId": 1, "id": 2, "title": "sample two", "body": "sample body two"},
    {"userId": 2, "id": 3, "title": "sample three", "body": "sample body three"},
]

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        route = urlparse(self.path)
        if route.path == "/posts":
            uid = parse_qs(route.query).get("userId", [None])[0]
            items = [p for p in POSTS if uid is None or str(p["userId"]) == uid]
            self.reply(200, items)
        elif route.path.startswith("/posts/"):
            item = next((p for p in POSTS if str(p["id"]) == route.path.split("/")[-1]), None)
            self.reply(200 if item else 404, item if item else {})
        else:
            self.reply(404, {})

    def reply(self, status, payload):
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *args):
        pass

if __name__ == "__main__":
    ThreadingHTTPServer(("127.0.0.1", 8765), Handler).serve_forever()
