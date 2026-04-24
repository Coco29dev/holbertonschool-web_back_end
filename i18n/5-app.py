#!/usr/bin/env python3
"""Flask app with mocked user login support."""
from typing import Dict, Optional

from flask import Flask, g, render_template, request
from flask_babel import Babel


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

app = Flask(__name__)
babel = Babel(app)


def get_user() -> Optional[Dict]:
    """Return the mocked user from the login_as URL parameter."""
    login_as = request.args.get("login_as")

    if login_as is None:
        return None

    try:
        return users.get(int(login_as))
    except (TypeError, ValueError):
        return None


@app.before_request
def before_request() -> None:
    """Find a user if any and store it on flask.g."""
    g.user = get_user()


@app.route("/")
def index() -> str:
    """Render the index page."""
    return render_template("5-index.html")


def get_locale() -> str:
    """Get the locale for the request."""
    locale = request.args.get("locale")

    if locale in ["fr", "en"]:
        return locale

    return request.accept_languages.best_match(["fr", "en"])


babel.init_app(app, locale_selector=get_locale)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
