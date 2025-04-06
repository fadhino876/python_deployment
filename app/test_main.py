from fastapi.testclient import TestClient
from main import app


testClient = TestClient(app)


def test_prefex_endpoint_url():
    response = testClient.get(url="/")
    assert response.status_code == 200


