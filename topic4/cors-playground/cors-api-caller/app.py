from flask import Flask, render_template
from pyquocca.logging import setup_dev_server_logging

import os

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", api_domain=os.getenv("API_DOMAIN"), my_domain=os.getenv("MY_DOMAIN"))

if __name__ == "__main__":
    setup_dev_server_logging()
    app.run(debug=True, host="0.0.0.0", port=8000)
