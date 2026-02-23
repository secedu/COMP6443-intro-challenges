from flask import Flask, render_template, request
from pyquocca.logging import setup_dev_server_logging
from pyquocca.postgres import FlaskPostgres

import secrets
import os

app = Flask(__name__)

db = FlaskPostgres(app=app)

AUTH_PROVIDER_PUBLIC_URL = os.getenv("AUTH_PROVIDER_PUBLIC_URL")
CLIENT_APP_PUBLIC_URL = os.getenv("CLIENT_APP_PUBLIC_URL")

@app.route("/")
def index():
    return render_template("index.html", auth_provider_url=AUTH_PROVIDER_PUBLIC_URL, client_app_url=CLIENT_APP_PUBLIC_URL)

@app.route("/authorize")
def authorize():
    return render_template("authorize.html")

@app.route("/code")
def generate_code():
    code = secrets.randbelow(9999999999)
    username = request.args.get('user') or 'placeholderuser'

    db.execute("INSERT INTO authentication_codes (code, username) VALUES (%s, %s)", (code, username))

    return str(code)

@app.route("/oauth/token")
def get_user_info():
    # Note: Normally this would return a token that could be used for many more queries.
    # To keep this simple, we will just return the username for this code rather than a token.
    return db.fetch_one("SELECT username FROM authentication_codes WHERE code = %s", (request.args.get('code'), ))["username"]

if __name__ == "__main__":
    setup_dev_server_logging()
    app.run(debug=True, host="0.0.0.0", port=8001)
