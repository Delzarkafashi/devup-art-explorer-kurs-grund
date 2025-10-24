import re
import main
from unittest.mock import Mock

def test_shiba_button_shows_shiba(monkeypatch):
    fake = Mock()
    fake.status_code = 200
    fake.raise_for_status = lambda: None
    fake.json.return_value = {
        "status": "success",
        "message": [
            "https://images.dog.ceo/breeds/shiba/n02113023_1234.jpg",
            "https://images.dog.ceo/breeds/shiba/n02113023_5678.jpg",
        ],
    }

    def fake_get(url, *args, **kwargs):
        assert "breed/shiba/images" in url, "Ska hämta shiba-API:t"
        return fake

    monkeypatch.setattr(main, "requests", Mock(get=fake_get))

    client = main.app.test_client()
    resp = client.post("/shiba")
    assert resp.status_code == 200

    html = resp.data.decode("utf-8")
    m = re.search(r'<img[^>]*id="dog-pic"[^>]*src="([^"]+)"', html)
    assert m, "Ingen bild renderades"
    assert "shiba" in m.group(1), "Bilden ser inte ut att vara en shiba"
