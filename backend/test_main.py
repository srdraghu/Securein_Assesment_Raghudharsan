from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_list_cves():
    response = client.get("/cves/list")
    assert response.status_code == 200
