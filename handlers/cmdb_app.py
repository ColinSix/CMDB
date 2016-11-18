#!/usr/bin/env python
#encoding:utf8
#
import sys, os
from flask import Flask, redirect, render_template, session, url_for, g, request
from api import DBOPERAT
from handlers import RequestProcess as RP

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
    res = DBOPERAT(table="user").select()
    return render_template("/user/user.html", user_info=res)

@app.route("/user/<option>", methods=["POST"])
def user_option(option):
    insert_val = request.form.get("insert_val", None)
    arr_id = request.form.get("arr_id", None)
    update_val = request.form.get("update_val", None)
    _id = request.form.get("_id", None)
    RP(table="user", option=option, insert_val=insert_val, arr_id=arr_id, update_val=update_val, _id=_id).response()

    


@app.route("/assets/<kind>/<name>", methods=["GET"])
def assets(kind,name):

    return render_template("/assets/"+kind+"/"+name+".html")


if __name__ == "__main__":
    app.run(host=app_config['host'], port=app_config['port'], debug=app_config['debug'])

