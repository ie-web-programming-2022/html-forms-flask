from flask import Flask, render_template, request
from data import users

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    # 1. get the form from the request
    username = request.form["user"]
    password = request.form["password"]

    # 2. check if the username from the form is equal to the one in data
    # 3. check if the password from the form is equal to the one in data
    if username in users and password == users[username]:
        return render_template("private.html")
    else:
        return render_template("unauthorized.html"), 403

app.run(debug=True)