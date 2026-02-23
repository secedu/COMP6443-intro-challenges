import re

from flask import Flask, abort, g, make_response, redirect, render_template, request
from pyquocca.header_utils import get_username
from pyquocca.logging import setup_dev_server_logging
from pyquocca.postgres import FlaskPostgres
from pyquocca import get_flag

app = Flask(__name__)
app.config["TITLE"] = "Support Ticket System"
app.config["NAVBAR"] = [["Home", "/"], ["New Ticket", "/new"]]

db = FlaskPostgres("postgres", app)

TICKET_FORMAT = """Support Ticket - User: {user_id} - {title}

{contents}

A quoccacorp employee will reply soon."""


@app.before_request
def before_request():
    g.username = get_username()
    if g.username is None:
        g.username = "Anonymous User"
        g.user_id = 1511
    else:
        m = re.match(r"^z([0-9]{7,8})$", g.username)
        if m is not None:
            g.user_id = int(m.group(1)) % 2048
        else:
            g.user_id = 1511


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/new")
def new():
    return render_template("new.html")


@app.route("/new", methods=["POST"])
def create_ticket():
    title = request.form.get("title")
    contents = request.form.get("content")

    if title is None or contents is None:
        abort(400, "missing post data")

    ticket = db.execute(
        "INSERT INTO tickets (user_id, title, contents) VALUES (%s, %s, %s) RETURNING id",
        (g.user_id, title, contents),
    ).fetchone()
    assert ticket is not None, "missing inserted ticket"

    return redirect(f"/raw/{ticket['id']}")


@app.route("/raw/<int:ticket_id>/")
def view_ticket(ticket_id: int):
    ticket = db.fetch_one(
        "SELECT user_id, title, contents FROM tickets WHERE id=%s", (ticket_id,)
    )
    if ticket is None:
        abort(404, "Ticket not found.")
    
    ticket["contents"] = ticket["contents"].replace("INTRO{this_is_an_intro_flag}", get_flag("support_v0"))

    resp = make_response(TICKET_FORMAT.format(**ticket))
    resp.headers["Content-Type"] = "text/plain"
    return resp


if __name__ == "__main__":
    setup_dev_server_logging()
    app.run(debug=True, host="0.0.0.0", port=8000)
