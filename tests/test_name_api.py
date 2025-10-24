# tests/test_name_api.py
from main import app

def test_get_name(client=None):
    with app.test_client() as client:
        res = client.get("/api/name?query=van+gogh")
        assert res.status_code == 200
        data = res.get_json()
        assert "results" in data
        assert isinstance(data["results"], list)
