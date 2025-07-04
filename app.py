#!/usr/bin/env python3
"""
Main module for the Yahtzee game.
"""
import traceback
from flask import Flask, render_template
from src.hand import Hand

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def main():
    """ Main route """
    hand = Hand()
    return render_template("index.html", hand=hand)

@app.route("/about")
def about():
    """ About route """
    my_name = "Keshti Gyllinger"
    return render_template("about.html", name=my_name)

@app.errorhandler(404)
def page_not_found(e):
    """
    Handler for page not found 404
    """
    #pylint: disable=unused-argument
    return "Flask 404 here, but not the page you requested."

@app.errorhandler(500)
def internal_server_error(e):
    """
    Handler for internal server error 500
    """
    #pylint: disable=unused-argument
    return "<p>Flask 500<pre>" + traceback.format_exc()

if __name__ == "__main__":
    app.run(debug=True)
