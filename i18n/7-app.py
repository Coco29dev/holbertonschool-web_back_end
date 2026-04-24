#!/usr/bin/env python3
"""Flask app with mocked user login, locale, and timezone support."""
from typing import Dict, Optional

import pytz
from flask import Flask, g, render_template, request
from flask_babel import Babel
from pytz.exceptions import UnknownTimeZoneError


class Config:
    """Application configuration."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

app = Flask(__name__)
app.config.from_object(Config)
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
    return render_template("7-index.html")


def get_locale() -> str:
    """Select the best matching locale for the current request."""
    locale = request.args.get("locale")
    if locale in app.config["LANGUAGES"]:
        return locale

    user = getattr(g, "user", None)
    if user is not None:
        locale = user.get("locale")
        if locale in app.config["LANGUAGES"]:
            return locale

    locale = request.accept_languages.best_match(app.config["LANGUAGES"])
    if locale is not None:
        return locale

    return app.config["BABEL_DEFAULT_LOCALE"]


def get_timezone() -> str:
    """Select the best matching timezone for the current request."""
    timezone = request.args.get("timezone")
    if timezone is not None:
        try:
            pytz.timezone(timezone)
            return timezone
        except UnknownTimeZoneError:
            pass

    user = getattr(g, "user", None)
    if user is not None:
        timezone = user.get("timezone")
        if timezone is not None:
            try:
                pytz.timezone(timezone)
                return timezone
            except UnknownTimeZoneError:
                pass

    return app.config["BABEL_DEFAULT_TIMEZONE"]


babel.init_app(
    app,
    locale_selector=get_locale,
    timezone_selector=get_timezone,
)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
