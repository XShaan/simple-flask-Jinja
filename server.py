from flask import Flask, render_template
import requests

app = Flask(__name__)

posts = requests.get("https://api.npoint.io/59b90c48a6e56a515635").json()


@app.route("/")
def home():
    return render_template("index.html", all_posts=posts)

@app.route("/single/<int:id>")
def get_single(id):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == id:
            requested_post = blog_post
    return render_template("single.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)