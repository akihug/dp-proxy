from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_allowed_aggregate_query():
    response = client.post("/get_dp_result", json={"query": "SELECT COUNT(*) AS totalCount FROM PUMS.PUMS;"})
    assert response.status_code == 200
    assert response.json() == {"result": [["total"],[5]]}

def test_disallowed_aggregate_query():
    response = client.post("/get_dp_result", json={"query": "SELECT AVG(age) AS avgAge FROM PUMS.PUMS;"})
    assert response.status_code == 400
    assert response.json() == {"detail": "Only COUNT,SUM aggregate queries are allowed!"}

def test_disallowed_query():
    response = client.post("/get_dp_result", json={"query": "DROP TABLE PUMS;"})
    assert response.status_code == 400
    assert response.json() == {"detail": "Only SELECT queries are allowed!"}
