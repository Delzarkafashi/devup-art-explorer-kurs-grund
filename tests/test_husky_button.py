import re
import app.main as main
from unittest.mock import Mock


def test_husky_button_shows_husky(monkeypatch):
    # Fejka Dog API-svar för husky (lista -> appen väljer en)
    fake = Mock()
    fake.status_code = 200
    fake.raise_for_status = lambda: None
    fake.json.return_value = {
        "status": "success",
        "message": [
            "https://images.dog.ceo/breeds/husky/n02110185_1469.jpg",
            "https://images.dog.ceo/breeds/husky/n02110185_5678.jpg",
        ],
    }

    # Säkerställ att koden verkligen anropar husky-endpointen
    def fake_get(url, *args, **kwargs):
        assert "breed/husky/images" in url, (
            "Ska hämta husky-API:t"
        )
        return fake

    monkeypatch.setattr(main, "requests", Mock(get=fake_get))

    client = main.app.test_client()
    resp = client.post("/husky")
    assert resp.status_code == 200

    html = resp.data.decode("utf-8")
    m = re.search(r'<img[^>]*id="dog-pic"[^>]*src="([^"]+)"', html)
    assert m, "Ingen hundbild renderades"
    src = m.group(1)
    assert "husky" in src, "Bilden ser inte ut att vara en husky"
