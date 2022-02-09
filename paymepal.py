from flask import Flask, request, render_template
from data import users, transactions

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    if username in users and users[username] == password:
        user_transactions = transactions[username]
        
        return render_template(
            "private.html",
            user=username,
            transactions=user_transactions
        )
    else:
        return render_template("unauthorized.html"), 403

app.run(debug=True)