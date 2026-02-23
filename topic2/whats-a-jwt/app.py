from flask import Flask, render_template, make_response, request
from pyquocca import get_flag
from pyquocca.logging import setup_dev_server_logging

import jwt

app = Flask(__name__)

JWT_SECRET_KEY = 'weak_example_key_for_intro_challenge'

@app.route("/")
def index():
    r = make_response(render_template("index.html"))

    sess = request.cookies.get("session")
    if sess is None:
        # Add the JWT to the cookies if it doesn't exist
        sess = jwt.encode({
            "flag": get_flag('whats-a-jwt') # Normally a JWT will contain information such as a user id, but in this case just add the flag
        }, JWT_SECRET_KEY, algorithm='HS256')
        r.set_cookie("session", sess)

    # Try to decode the token
    try:
        data = jwt.decode(sess, JWT_SECRET_KEY, algorithms=["HS256"])
        # Normally you would use stuff inside the data variable (eg the user id), but in this example we don't

    except jwt.exceptions.PyJWTError as e:
        return f"An error occurred decoding the JWT: {e}"

    return r

if __name__ == "__main__":
    setup_dev_server_logging()
    app.run(debug=True, host="0.0.0.0", port=8000)
