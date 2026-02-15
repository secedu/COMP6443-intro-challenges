from flask import Flask, abort, Response, render_template, request
from pyquocca import get_flag
from pyquocca.logging import setup_dev_server_logging

import socket
import os

app = Flask(__name__)

KB_ADDR = (os.getenv("HAAS_HOST"), int(os.getenv("HAAS_PORT")))
FLAG_PLACEHOLDER = os.getenv("HAAS_FLAG_PLACEHOLDER")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def send():
    req = request.form.get("requestBox")
    if req is None:
        return abort(
            400, "No requestBox value found in POST data. You need to submit a request!"
        )

    # Send payload to kb.quoccacorp.com
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(KB_ADDR)
    sock.send(req.encode("utf-8"))

    # Return the output
    received = sock.recv(4096) + sock.recv(4096)  # Headers
    sock.close()

    text = received.decode()
    if FLAG_PLACEHOLDER in text:
        text = text.replace(FLAG_PLACEHOLDER, get_flag("haas-v1"))

    return Response(text, mimetype="text/plain")

if __name__ == "__main__":
    setup_dev_server_logging()
    app.run(debug=True, host="0.0.0.0", port=8000)

# This is haas-v1! the first chal. Ok docker cache?