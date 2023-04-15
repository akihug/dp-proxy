from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_allowed_aggregate_query():
    response = client.post("/get_dp_result", json={"query": "SELECT SUM(age) AS totalAge FROM main.users;"})
    print('response', response.json())
    assert response.status_code == 200

def test_disallowed_aggregate_query():
    response = client.post("/get_dp_result", json={"query": "SELECT AVG(age) AS avgAge FROM main.users;"})
    assert response.status_code == 400
    assert response.json() == {"detail": "Only COUNT,SUM aggregate queries are allowed!"}

def test_disallowed_query():
    response = client.post("/get_dp_result", json={"query": "DROP TABLE main.users;"})
    assert response.status_code == 400
    assert response.json() == {"detail": "Only SELECT queries are allowed!"}
