from flask import Flask, render_template, request
from pyquocca import get_flag
from pyquocca.logging import setup_dev_server_logging

import os

from pyquocca.xssbot import visit, BadRequestError

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    if request.args.get("name"):
        return render_template("introduce.html", name=request.args.get('name'))
    return render_template("index.html", api_caller_domain=os.getenv("API_CALLER_DOMAIN"))

@app.route("/admin", methods=["GET"])
def admin():
    return render_template("admin.html")

@app.route("/report", methods=["POST"])
def report():
    try:
        visit(
            request.form.get("url"), [{"name": "note", "value": get_flag("cors-playground"), "domain": "cors-api.quoccacorp.com"}]
        )
    except BadRequestError:
        return "The URL was invalid.", 400
    except Exception as e:
        print(e)
        return "An unexpected error occurred.", 500
    return "Successfully reported the page! An admin should visit shortly."

if __name__ == "__main__":
    setup_dev_server_logging()
    app.run(debug=True, host="0.0.0.0", port=8000)
