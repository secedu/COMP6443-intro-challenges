from flask import Flask, redirect, render_template, request, url_for
from pyquocca import get_flag
from pyquocca.logging import setup_dev_server_logging

from pyquocca.xssbot import visit

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/admin", methods=["GET"])
def admin():
    return render_template("admin.html")

@app.route("/report", methods=["POST"])
def report():
    try:
        visit(
            request.form.get("url"), [{"name": "flag", "value": get_flag("xss-playground-3"), "domain": "xss-playground-3.quoccacorp.com"}]
        )
    except Exception as e:
        print(e)
        return "An unexpected error occurred."
    return "Successfully reported the page! An admin should visit shortly."

if __name__ == "__main__":
    setup_dev_server_logging()
    app.run(debug=True, host="0.0.0.0", port=8000)
