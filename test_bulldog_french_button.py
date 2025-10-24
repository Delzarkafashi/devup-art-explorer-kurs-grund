import re
import main
from unittest.mock import Mock

def test_bulldog_french_button_shows_bulldog_french(monkeypatch):
    fake = Mock()
    fake.status_code = 200
    fake.raise_for_status = lambda: None
    fake.json.return_value = {
        "status": "success",
        "message": [
            "https://images.dog.ceo/breeds/bulldog-french/n02108915_1111.jpg",
            "https://images.dog.ceo/breeds/bulldog-french/n02108915_2222.jpg",
        ],
    }

    def fake_get(url, *args, **kwargs):
        assert "breed/bulldog/french/images" in url, "Ska hämta bulldog/french-API:t"
        return fake

    monkeypatch.setattr(main, "requests", Mock(get=fake_get))

    client = main.app.test_client()
    resp = client.post("/bulldog-french")
    assert resp.status_code == 200

    html = resp.data.decode("utf-8")
    m = re.search(r'<img[^>]*id="dog-pic"[^>]*src="([^"]+)"', html)
    assert m, "Ingen bild renderades"
    src = m.group(1)
    assert "bulldog" in src and "french" in src, "Bilden ser inte ut att vara bulldog/french"
