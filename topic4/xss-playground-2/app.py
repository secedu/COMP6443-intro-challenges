from flask import Flask, redirect, render_template, request, url_for
from pyquocca import get_flag
from pyquocca.logging import setup_dev_server_logging

from pyquocca.postgres import FlaskPostgres

from pyquocca.xssbot import visit

import uuid

app = Flask(__name__)
db = FlaskPostgres(app=app)

@app.route("/", methods=["GET"])
def index():
    if request.args.get("paste"):
        paste_row = db.fetch_one("SELECT data FROM pastes WHERE id = %s", [request.args.get("paste")])
        if paste_row is None:
            paste = "Paste not found!"
        else:
            paste = paste_row["data"]
        return render_template("paste.html", paste=paste)
    return render_template("index.html")

@app.route("/", methods=["POST"])
def create_paste():
    content = request.form.get('paste') or ''
    paste_id = uuid.uuid4()

    db.execute("INSERT INTO pastes (id, data) VALUES (%s, %s)", [paste_id, content])

    return redirect(url_for("index", paste=paste_id))


@app.route("/admin", methods=["GET"])
def admin():
    return render_template("admin.html")

@app.route("/report", methods=["POST"])
def report():
    try:
        visit(
            request.form.get("url"), [{"name": "flag", "value": get_flag("xss-playground-2"), "domain": "xss-playground-2.quoccacorp.com"}]
        )
    except Exception as e:
        print(e)
        return "An unexpected error occurred."
    return "Successfully reported the page! An admin should visit shortly."

if __name__ == "__main__":
    setup_dev_server_logging()
    app.run(debug=True, host="0.0.0.0", port=8000)
