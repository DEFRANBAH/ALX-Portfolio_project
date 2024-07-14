#!/usr/bin/python3 

"""defines the route and initiate the server"""

from flask import Flask
app = Flask(__name__)


@app.route('/garerinit/', strict_slashes=False)
def hello_garer():
    """displays hello park garer"""
    return "hello park garrer!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
