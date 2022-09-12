from flask import Flask, render_template, request
import requests
import smtplib

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


@app.route("/contact", methods=['GET', 'POST'])
def contact_us():
    if request.method == 'POST':
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", alert=True)
    else:
        return render_template("contact.html")

def send_email(name, email, phone, message):
    sender = "Private Person <from@example.com>"
    text = f"""\
Subject:New mail from contact-us
To: {email}
From: {sender}

Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"""

## You can use Gmail SMTP service for now i use mailtrap.io
    with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
        server.login("YOUR USERNAME", "YOUR PASSWORD")
        server.sendmail(sender, email, text)
        print(server)

if __name__ == "__main__":
    app.run(debug=True)