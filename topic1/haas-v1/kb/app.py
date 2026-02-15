from flask import Flask, abort, render_template, request

import os

app = Flask(__name__)

FLAG_PLACEHOLDER = os.getenv("HAAS_FLAG_PLACEHOLDER")

@app.before_request
def before_request_hook():
    if request.headers.get("Host", None) != "kb.quoccacorp.com":
        return abort(404)

@app.route("/")
def root():
    return render_template("index.html")

@app.route("/simple")
@app.route("/simple/<id>")
def simple(id=None):
    if not id:
        return render_template("simple.html")
    elif id == "loans":
        return "Well done!\n" + FLAG_PLACEHOLDER
    else:
        return "No flag here!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
