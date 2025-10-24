import re
import app.main as main
from unittest.mock import Mock


def test_pug_button_shows_pug(monkeypatch):
    fake = Mock()
    fake.status_code = 200
    fake.raise_for_status = lambda: None
    fake.json.return_value = {
        "status": "success",
        "message": [
            "https://images.dog.ceo/breeds/pug/n02110958_1234.jpg",
            "https://images.dog.ceo/breeds/pug/n02110958_5678.jpg",
        ],
    }

    def fake_get(url, *args, **kwargs):
        assert "breed/pug/images" in url, "Ska hämta pug-API:t"
        return fake

    monkeypatch.setattr(main, "requests", Mock(get=fake_get))

    client = main.app.test_client()
    resp = client.post("/pug")
    assert resp.status_code == 200

    html = resp.data.decode("utf-8")
    m = re.search(r'<img[^>]*id="dog-pic"[^>]*src="([^"]+)"', html)
    assert m, "Ingen bild renderades"
    assert "pug" in m.group(1), "Bilden ser inte ut att vara en pug"
