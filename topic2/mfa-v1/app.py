import base64
from hashlib import sha256

import mintotp
from flask import Flask, redirect, render_template, request, session
from psycopg import IntegrityError
from pyquocca import get_flag
from pyquocca.logging import setup_dev_server_logging
from pyquocca.postgres import FlaskPostgres

app = Flask(__name__)
app.config.from_prefixed_env()
db = FlaskPostgres("postgres", app)


@app.route("/")
def index():
    if "username" in session:
        if session.get("username") == "admin":
            return render_template("flag.html", flag=get_flag("mfa"))
        return render_template("flag.html", flag="Flag is only available to admins.")
    return redirect("/login")


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/register", methods=["POST"])
def register_post():
    username = request.form.get("username")
    password = request.form.get("password")
    if type(username) is not str or type(password) is not str:
        return (
            render_template("register.html", error="invalid username or password"),
            400,
        )

    if len(username) > 64:
        return (
            render_template(
                "register.html", error="username must be less than 64 characters"
            ),
            400,
        )

    try:
        db.execute(
            "INSERT INTO users (username, password_hash) VALUES (%s, %s);",
            (username, sha256(password.encode()).hexdigest()),
        )
    except IntegrityError:
        return render_template("register.html", error="user already exists"), 409

    session["username"] = username

    return render_template(
        "qr.html",
        username=username,
        secret=base64.b32encode(username.encode()).decode().replace("=", ""),
    )


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login_post():
    username = request.form.get("username")
    password = request.form.get("password")
    if type(username) is not str or type(password) is not str:
        return (
            render_template("login.html", error="invalid username or password field"),
            400,
        )

    user = db.fetch_one(
        "SELECT username FROM users WHERE username=%s AND password_hash=%s",
        (username, sha256(password.encode()).hexdigest()),
    )
    if user is None:
        return (
            render_template("login.html", error="incorrect username or password"),
            403,
        )

    session["mfa_check_for"] = user["username"]
    return redirect("/mfa")


@app.route("/mfa")
def mfa():
    if "mfa_check_for" not in session:
        return redirect("/login")
    return render_template("mfa.html")


@app.route("/mfa", methods=["POST"])
def mfa_post():
    if "mfa_check_for" not in session:
        return redirect("/login")

    username = session["mfa_check_for"]
    code = request.form.get("code")
    if type(code) is not str:
        return render_template("mfa.html", error="invalid code")

    expected_code = mintotp.totp(
        base64.b32encode(username.encode()).decode().replace("=", "")
    )
    if code.strip().replace(" ", "") != expected_code:
        return render_template("mfa.html", error="incorrect TOTP code")

    session["username"] = username
    del session["mfa_check_for"]
    return redirect("/")


@app.route("/logout")
def logout():
    if "username" in session:
        del session["username"]
    if "mfa_check_for" in session:
        del session["mfa_check_for"]
    return redirect("/login")


if __name__ == "__main__":
    setup_dev_server_logging()
    app.run(debug=True, host="0.0.0.0", port=8000)
