from fastapi.testclient import TestClient
client = TestClient(app)

def test_fetcher():
    query = {"question": "rect??? ...."}
    # query = "rect??"
    response = client.get(f"/fetch/{query}")
    assert response.status_code == 200



test_fetcher()