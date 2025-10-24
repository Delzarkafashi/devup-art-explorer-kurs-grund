# app/main.py
from flask import Flask, render_template, request
import requests

app = Flask(__name__)  # funkar direkt om mapparna ligger i app/

def get_random_image() -> str:
    r = requests.get("https://dog.ceo/api/breeds/image/random", timeout=10)
    r.raise_for_status()
    return r.json()["message"]

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

if __name__ == "__main__":
    app.run(debug=True)
