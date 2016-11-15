#!/usr/bin/env python
#encoding:utf8
#
# from flask import Flask, redirect, render_template, session, url_for, g, request
# from config import app_config
# import os
# app = Flask(__name__)
# app.secret_key = os.urandom(24)


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


# @app.route("/export", methods=['GET'])
# def export():
#     return data_export()

# @app.route('/hello', methods=['GET'])
# def hello():    
#     # session['user'] = 'ming'
#     # print session.items()
#     # g['user'] = 'aaron'
#     # print g.get('user')
#     print dir(g)
#     # print request.url
#     return 'hello'
# @app.route('/world', methods=['GET'])
# def world():
#     # print session.items()
#     # print request.url
#     return 'world'

# if __name__ == '__main__':
#     app.run(host=app_config['host'], port=app_config['port'], debug=app_config['debug'])

def bootapp_test():
    from config import app_config
    from handlers.cmdb_app import app
    webrun = app
    webrun.run(host=app_config['host'], port=app_config['port'], debug=app_config['debug'])

bootapp_test()

