from flask import Flask, session, render_template
from pyquocca import get_flag
from pyquocca.logging import setup_dev_server_logging
import secrets

app = Flask(__name__)

app.secret_key = "not_secure_because_this_is_an_intro_challenge"

balances = {}

def get_balance():
    if not "uid" in session:
        session["uid"] = secrets.token_hex(16)
    
    if not session["uid"] in balances:
        balances[session["uid"]] = {
            "balance": 100,
            "quoccas": 0
        }
    
    return balances[session["uid"]]
    

def display_page(balance):
    return render_template("index.html", balance=balance["balance"], quoccas=balance["quoccas"])

@app.route("/")
def index():
    balance = get_balance()

    return display_page(balance)

@app.route("/buy", methods=["POST"])
def buy():
    balance = get_balance()

    balance["quoccas"] += 1
    balance["balance"] -= 10

    return display_page(balance)

@app.route("/sell", methods=["POST"])
def sell():
    balance = get_balance()

    balance["quoccas"] -= 1
    balance["balance"] += 10

    return display_page(balance)

@app.route("/flag", methods=["POST"])
def flag():
    balance = get_balance()

    if balance["balance"] >= 300:
        return get_flag("repeater")
    else:
        return "Not enough funds! <a href='/'>Back</a>"

if __name__ == "__main__":
    setup_dev_server_logging()
    app.run(debug=True, host="0.0.0.0", port=8000)
