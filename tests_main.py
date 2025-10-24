import re
import main
from unittest.mock import Mock

def test_random_dog_shown_on_button_click(monkeypatch):
    fake = Mock()
    fake.status_code = 200
    fake.raise_for_status = lambda: None
    fake.json.return_value = {
        "status": "success",
        "message": "https://example.com/dog1.jpg",  # <-- str, inte lista
    }
    monkeypatch.setattr(main, "requests", Mock(get=lambda *a, **k: fake))

    client = main.app.test_client()
    resp = client.post("/")
    assert resp.status_code == 200

    html = resp.data.decode("utf-8")
    m = re.search(r'<img[^>]*id="dog-pic"[^>]*src="([^"]+)"', html)
    assert m, "Ingen hundbild renderades"
    assert m.group(1) == "https://example.com/dog1.jpg"
