from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_user_minimal():
    payload = {"email": "jane@example.com", "name": "J", "password": "pw"}
    r = client.post("/api/v1/users/", json=payload)
    assert r.status_code == 200
