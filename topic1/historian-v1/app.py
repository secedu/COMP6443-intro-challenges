from flask import Flask, render_template, Response
from pyquocca import get_flag
from pyquocca.logging import setup_dev_server_logging

from hashlib import sha256

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/<p>")
def flag(p):
    if sha256(p.encode()).hexdigest() == "788232278ec6496ad6c544828bf8e957f368b37b2d3b5386fc0e9d26d151d235":
        return Response(get_flag("historian-v1"), content_type="text/plain")
    else:
        return "nope"

if __name__ == "__main__":
    setup_dev_server_logging()
    app.run(debug=True, host="0.0.0.0", port=8000)
