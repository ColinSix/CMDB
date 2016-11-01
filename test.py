#!/usr/bin/env python
#encoding:utf8
#
from flask import Flask, redirect, render_template, session, url_for, g, request
from config import app_config

# app = Flask(__name__)



# def db_select():
#     from api import DBOPERAT
#     dbop = DBOPERAT(table="user")
#     print dbop.select()
# db_select()

# def db_delete():
#     from api import DBOPERAT
#     dbop = DBOPERAT(table="user")
#     print dbop.delete(_id=6)

# db_delete()

# def data_import():
#     from methods.data import DATAIMPORT
#     instance = DATAIMPORT(excel="G:\\python\\test_file\\user.xlsx",table="user")
#     instance.data_import()

# data_import()
# 
# def data_export():
#     from methods.data import DataExport
#     instance = DATAEXPORT(table="user")
#     return instance.data_export()

# print data_export()
# 
# def excval_join():
#     from api import ExcJoint
#     inst = ExcJoint(table="user")
#     return inst.data_tailor()

# print excval_join()

# @app.route("/", methods=['GET'])
# def index():
#     return "hello"

# @app.route("/export", methods=['GET'])
# def export():
#     return data_export()


# if __name__ == '__main__':
    # app.run(host=app_config['host'], port=app_config['port'], debug=app_config['debug'])