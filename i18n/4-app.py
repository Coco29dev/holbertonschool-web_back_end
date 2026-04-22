#!/usr/bin/env python3
"""Basic Flask app."""
from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


@app.route('/')
def index():
    """Render the index page."""
    return render_template('4-index.html')


def get_locale():
    """Get the locale for the request."""

    locale = request.args.get('locale')

    if locale in ['fr', 'en']:
        return locale

    return request.accept_languages.best_match(['fr', 'en'])


babel.init_app(app, locale_selector=get_locale)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
