from flask import Flask, render_template, request
from pyquocca import get_flag
from pyquocca.logging import setup_dev_server_logging

import requests

import os

app = Flask(__name__)

AUTH_PROVIDER_PUBLIC_URL = os.getenv("AUTH_PROVIDER_PUBLIC_URL")
CLIENT_APP_PUBLIC_URL = os.getenv("CLIENT_APP_PUBLIC_URL")
AUTH_PROVIDER_BACKEND_URL = os.getenv("AUTH_PROVIDER_BACKEND_URL")

@app.route("/")
def index():
    return render_template("index.html", auth_provider_url=AUTH_PROVIDER_PUBLIC_URL, client_app_url=CLIENT_APP_PUBLIC_URL)

@app.route("/callback")
def callback():
    # Typically we would retrieve a token here, but for simplicity sake this route only returns the username (instead of token)
    username = requests.get(AUTH_PROVIDER_BACKEND_URL + f"/oauth/token?code={request.args.get('code')}").text

    if username == "admin":
        username = get_flag("oauth-demo")

    return render_template("callback.html", username=username)

if __name__ == "__main__":
    setup_dev_server_logging()
    app.run(debug=True, host="0.0.0.0", port=8000)
