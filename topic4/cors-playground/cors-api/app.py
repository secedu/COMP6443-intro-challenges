from flask import Flask, request, make_response
from pyquocca.logging import setup_dev_server_logging

app = Flask(__name__)

@app.route("/note", methods=["GET"])
def get_note():
    note = request.cookies.get("note") or "Cannot read note from the cookie. Perhaps the cookie was missing from the request?"
    resp = make_response(note)
    resp.headers.add('Access-Control-Allow-Origin', request.args.get("cors-allow-origin"))
    resp.headers.add('Access-Control-Allow-Credentials', 'true')
    return resp

@app.route("/set-note", methods=["POST"])
def set_note():
    resp = make_response("success")
    resp.headers.add('Access-Control-Allow-Origin', request.args.get("cors-allow-origin"))
    resp.headers.add('Access-Control-Allow-Credentials', 'true')
    resp.set_cookie("note", request.form.get("note") or "EMPTY NOTE")
    return resp

if __name__ == "__main__":
    setup_dev_server_logging()
    app.run(debug=True, host="0.0.0.0", port=8000)
