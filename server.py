from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route("/")
def home():
    post_url = "https://api.npoint.io/59b90c48a6e56a515635"
    response = requests.get(post_url)
    all_posts = response.json()
    return render_template("index.html", posts=all_posts)

@app.route("/single/<int:id>")
def get_single(id):
    post_url = "https://api.npoint.io/59b90c48a6e56a515635"
    response = requests.get(post_url)
    single_post = response.json()
    return render_template("single.html", post=single_post[id -1])

if __name__ == "__main__":
    app.run(debug=True)