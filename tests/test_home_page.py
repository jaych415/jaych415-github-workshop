from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_home_page_renders() -> None:
    response = client.get("/")

    assert response.status_code == 200
    assert "CSE120 GitHub Workshop" in response.text
    assert "Average Calculator" in response.text