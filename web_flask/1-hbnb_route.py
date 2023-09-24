#!/usr/bin/python3
"""A script that starts web application with two routings
"""

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    """Return Hello HBNB
    """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """Return HBNB
    """
    return 'HBNB'

if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
