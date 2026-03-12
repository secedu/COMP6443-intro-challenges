from flask import Flask, render_template, Response, render_template_string, request
from pyquocca import get_flag
from pyquocca.logging import setup_dev_server_logging

import hashlib

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def create_email():
    content = render_template_string(request.form.get('content'), name=request.form.get('name'), author=request.form.get('author'))
    return render_template("email.html", content=content)

@app.route("/admin", methods=["GET"])
def admin():
    return render_template("admin.html")

@app.route("/admin", methods=["POST"])
def flag():
    with open("/.password.txt.md5", "r") as f:
        p = f.read().strip()
    if hashlib.md5(request.form.get('password').encode()).hexdigest() == p:
        return get_flag("jinja-ninja")
    else:
        return render_template("admin.html", err="Invalid password")

if __name__ == "__main__":
    setup_dev_server_logging()
    app.run(debug=True, host="0.0.0.0", port=8000)
