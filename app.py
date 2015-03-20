#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template
from sh import git

app = Flask(__name__)

version = git("rev-parse", "--short", "HEAD").strip()


@app.route("/", methods=["GET"])
def status():
    """
    Status check. Display the current version of heatlamp, some basic
    diagnostics, and a simple form that may be used to manually trigger
    a deployment.
    """

    return render_template("status.html", version=version)


@app.route("/", methods=["POST", "PUT"])
def refresh():
    """
    Webhook accepted. Perform the configured action.
    """

    return "yes"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10100)
