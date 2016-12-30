#!/usr/bin/env python
#encoding:utf8
#
import sys, os, json
from flask import Flask, redirect, render_template, session, url_for, g, request
from handlers import RequestProcess as RP
from handlers import ForHtmlVal
from api import UserAuth, GetFile
from config import table_thead, excel_thead

reload(sys)
sys.setdefaultencoding("utf-8")

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
    if request.method == 'GET':
        return render_template("/login/login.html", res=None)
    elif request.method == 'POST':
        user = request.form.get('username')
        pwd = request.form.get('password')
        login_status = UserAuth(user=user,passwd=pwd).user_auth()
        if login_status == 1:
            return redirect(url_for('user'))
        elif login_status == 2:
            return "密码错误"
        elif login_status == 3:
            return "用户名不存在"

@app.route("/user", methods=["GET"])
def user():
    res = RP(table="user").response(option="select")
    return render_template("/user/user.html", users=res)

@app.route("/user/<option>", methods=["GET", "POST"])
def user_option(option):
    val_dict = {"insert_val":request.form.get("insert_val", None),
                "arr_id":request.form.get("arr_id", None),
                "update_val":request.form.get("update_val", None),
                "_id":request.form.get("_id", None)
               }
    for key in val_dict.keys():
        if val_dict[key] != None:
            val_dict[key] = json.loads(val_dict[key])
            
    if option == "export":
        if RP(table="user").response(option=option):
            return redirect(url_for("download", filename="static/export_file/export_user.xlsx"))

    elif option == "import":
        getfile = request.files["upload-excel"]
        GetFile(file=getfile,use="upload").savefile()
        excelf = GetFile(file=getfile).filepath()

        RP(table="user").response(option=option,excel=excelf)
        return redirect(url_for("user"))

    elif RP(table="user").response(option=option, insert_val=val_dict["insert_val"], arr_id=val_dict["arr_id"], update_val=val_dict["update_val"], _id=val_dict["_id"]):
        return "ok"
    else:
        return "error"

@app.route("/<filename>")
def download(filename):
    return None

@app.route("/assets/<kind>/<name>", methods=["GET"])
def assets(kind,name):
    res = ForHtmlVal(table=name).res_val()
    return render_template("/assets/"+kind+"/"+name+".html", assetdata=res["assetdata"], theads=res["theads"], modalval=res["modalval"])

# @app.route("/assets/<option>", methods=["GET", "POST"])
@app.route("/assets/<kind>/<name>/<option>", methods=["GET", "POST"])
def vmassets_option(kind,name,option):
    val_dict = {"insert_val":request.form.get("insert_val", None),
                "arr_id":request.form.get("arr_id", None),
                "update_val":request.form.get("update_val", None),
                "_id":request.form.get("_id", None)
               }
    for key in val_dict.keys():
        if val_dict[key] != None:
            val_dict[key] = json.loads(val_dict[key])
            
    if option == "export":
        if RP(table=name).response(option=option):
            return redirect(url_for("download", filename="static/export_file/export_"+name+".xlsx"))

    elif option == "import":
        getfile = request.files["upload-excel"]
        GetFile(file=getfile,use="upload").savefile()
        excelf = GetFile(file=getfile).filepath()

        RP(table=name).response(option=option,excel=excelf)
        return redirect(url_for("assets",kind=kind,name=name))

    elif RP(table=name).response(option=option, insert_val=val_dict["insert_val"], arr_id=val_dict["arr_id"], update_val=val_dict["update_val"], _id=val_dict["_id"]):
        return "ok"
    else:
        return "error"
if __name__ == "__main__":
    app.run(host=app_config['host'], port=app_config['port'], debug=app_config['debug'])

