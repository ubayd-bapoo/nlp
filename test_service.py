import pytest
from fastapi.testclient import TestClient
from service import app, startup_events

client = TestClient(app)

# Run the startup events to register routes before running tests
startup_events()


# Test GET request for /api/v1/match_users endpoint
def test_match_users_endpoint():
    response = client.get("/api/v1/match_users?transaction_id='NEYo6vu'")
    assert response.status_code == 200
    assert len(response.json()["users"]) == 1


# Test GET request for /api/v1/similar_transactions endpoint
def test_similar_transactions_endpoint():
    response = client.get("/api/v1/similar_transactions?input_string=grocery%20shopping")
    assert response.status_code == 200
    assert len(response.json()) > 0


# Test invalid input for /api/v1/match_users endpoint
def test_match_users_invalid_input():
    response = client.get("/api/v1/match_users?transaction_id=")
    assert response.status_code == 422


# Test invalid input for /api/v1/similar_transactions endpoint
def test_similar_transactions_invalid_input():
    response = client.get("/api/v1/similar_transactions?input_string=")
    assert response.status_code == 422


# Test GET request for /docs endpoint
def test_docs_endpoint():
    response = client.get("/docs")
    assert response.status_code == 200


# Run tests
if __name__ == "__main__":
    pytest.main(["-v", "-s", __file__])
