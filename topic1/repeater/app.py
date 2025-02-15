from flask import Flask, session, render_template
from pyquocca import get_flag
from pyquocca.logging import setup_dev_server_logging

app = Flask(__name__)

app.secret_key = "not_secure_because_this_is_an_intro_challenge"

def init_session():
    if not "balance" in session:
        session["balance"] = 100
        session["quoccas"] = 0

def display_page():
    return render_template("index.html", balance=session["balance"], quoccas=session["quoccas"])

@app.route("/")
def index():
    init_session()

    return display_page()

@app.route("/buy", methods=["POST"])
def buy():
    init_session()

    session["quoccas"] += 1
    session["balance"] -= 10

    return display_page()

@app.route("/sell", methods=["POST"])
def sell():
    init_session()

    session["quoccas"] -= 1
    session["balance"] += 10

    return display_page()

@app.route("/flag", methods=["POST"])
def flag():
    init_session()

    if session["balance"] >= 300:
        return get_flag("repeater")
    else:
        return "Not enough funds! <a href='/'>Back</a>"

if __name__ == "__main__":
    setup_dev_server_logging()
    app.run(debug=True, host="0.0.0.0", port=8000)
