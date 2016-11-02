#!/usr/bin/env python
#encoding:utf8
#
import sys, os
from flask import Flask, redirect, render_template, session, url_for, g, request


reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route("/", methods=["GET"])
def index():

    return render_template("/index/index.html", res=None)
@app.route("/base", methods=["GET"])
def base():
    return render_template("/base/base.html")

@app.route("/login", methods=["GET", "POST"])
def login():

    return render_template("/login/login.html", res=None)

@app.route("/user", methods=["GET"])
def user():

    return "user"

@app.route("/assets", methods=["GET"])
def assets():

    return "assets"


if __name__ == "__main__":
    app.run(host=app_config['host'], port=app_config['port'], debug=app_config['debug'])

