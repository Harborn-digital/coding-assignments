from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_task():
    payload = {"title": "x", "description": "y"}
    r = client.post("/api/v1/tasks/?owner_id=1", json=payload)
    assert r.status_code == 201
