from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_user():
    response = client.post(
        "/users",
        json={
            "email": "lodhiya123@gmail.com",
            "password": "testpassword"
    }
    )
    print(response.json())