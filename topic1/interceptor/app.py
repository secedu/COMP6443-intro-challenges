from flask import Flask, render_template, request
from pyquocca import get_flag
from pyquocca.logging import setup_dev_server_logging

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/flag", methods=["POST"])
def flag():
    shouldgetflag = request.form.get("shouldgetflag")
    if shouldgetflag is None:
        txt = "shouldgetflag was not supplied. What did you do? 🤔"
    elif shouldgetflag == "false":
        txt = "shouldgetflag was false. No flag for you!"
    else:
        txt = get_flag("interceptor")
    return render_template("flag.html", txt=txt, favcolour=request.form.get("favcolour"))

if __name__ == "__main__":
    setup_dev_server_logging()
    app.run(debug=True, host="0.0.0.0", port=8000)
