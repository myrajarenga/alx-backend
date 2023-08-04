#!/usr/bin/env python3
"""
Simple flask app
"""
from flask import Flask, render_template
from flask_babel import Babel


"""
Create a Config class with available languages
"""


class Config(object):
    """_summary_

    Returns:
            _type_: _description_
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


"""
Instantiate the Babel object and use Config as the app's config
"""
app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """ function to return the locale """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """"function  to render index file"""
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(port="5000", host="0.0.0.0", debug=True)
