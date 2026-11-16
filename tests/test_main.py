from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    assert client.get("/health").json()["status"] == "healthy"

def test_ready():
    assert client.get("/ready").json()["status"] == "ready"

def test_instance():
    assert client.get("/instance").json()["version"] == "1.0.0"