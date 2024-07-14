#!/usr/bin/python3

"""defines the route and initiate the server"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hellogarer():
    """displays hello park garer"""
    return "hello park garer!"
@app.route('/garer', strict_slashes=False)
def garer():
    """displays park garer"""
    return "bout to be onborded!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
