from flask import Flask, render_template, request
import requests
import random


app = Flask(__name__)


def get_random_image() -> str:
    r = requests.get("https://dog.ceo/api/breeds/image/random", timeout=10)
    r.raise_for_status()
    data = r.json()
    return data["message"]


@app.route("/", methods=["GET", "POST"])
def index():
    img_url = None
    error = None
    if request.method == "POST":
        try:
            img_url = get_random_image()
        except Exception as e:
            error = str(e)
    return render_template("index.html", image_url=img_url, error=error)


@app.post("/pug")
def pug():
    try:
        r = requests.get("https://dog.ceo/api/breed/pug/images", timeout=10)
        r.raise_for_status()
        pics = r.json().get("message", [])
        img_url = random.choice(pics) if pics else None
        return render_template("index.html", image_url=img_url, error=None)
    except Exception as e:
        return render_template("index.html", image_url=None, error=str(e))


@app.post("/shiba")
def shiba():
    try:
        r = requests.get("https://dog.ceo/api/breed/shiba/images", timeout=10)
        r.raise_for_status()
        pics = r.json().get("message", [])
        img_url = random.choice(pics) if pics else None
        return render_template("index.html", image_url=img_url, error=None)
    except Exception as e:
        return render_template("index.html", image_url=None, error=str(e))


@app.post("/bulldog-french")
def bulldog_french():
    try:
        r = requests.get(
            "https://dog.ceo/api/breed/bulldog/french/images",
            timeout=10
        )
        r.raise_for_status()
        pics = r.json().get("message", [])
        img_url = random.choice(pics) if pics else None
        return render_template("index.html", image_url=img_url, error=None)
    except Exception as e:
        return render_template("index.html", image_url=None, error=str(e))


@app.post("/husky")
def husky():
    try:
        r = requests.get("https://dog.ceo/api/breed/husky/images", timeout=10)
        r.raise_for_status()
        pics = r.json().get("message", [])
        img_url = random.choice(pics) if pics else None
        return render_template("index.html", image_url=img_url, error=None)
    except Exception as e:
        return render_template("index.html", image_url=None, error=str(e))


if __name__ == "__main__":
    app.run(debug=True)
