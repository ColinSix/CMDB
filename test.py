#!/usr/bin/env python
#encoding:utf8
#
# from flask import Flask, redirect, render_template, session, url_for, g, request
# from config import app_config
# import os
# app = Flask(__name__)
# app.secret_key = os.urandom(24)

def dbexcute():
    from methods import DB
    from config import db_config
    db = DB(host=db_config["host"],user=db_config["user"],password=db_config["passwd"],db=db_config["db"])

    # temp_arr = ['\xe6\x88\x91', '\xe6\x88\x91', 'user', '\xe6\x88\x91']
    # sql = "insert into user (username, password, role, email) values (%s, %s, %s, %s)" % ('"\xe5\xa5\xbd"', '"\xe5\xa5\xbd"', '"user"', '"\xe5\xa5\xbd"')
    # sql = 'insert into user (username, password, role, email) values ('"\xe4\xb8\xad\xe5\x9b\xbd"', '"\xe4\xb8\xad\xe5\x9b\xbd"', '"user"', '"\xe4\xb8\xad\xe5\x9b\xbd"')'
    # print sql
    values = [u"坏人",u"坏人",u"坏人",u"坏人"]
    temp_arr = []
    for val in values:
        if type(val) == unicode:
            temp_arr.append(val.encode("utf-8"))
        else:
            temp_arr.append(val)
    print temp_arr
    print tuple(temp_arr)
    sql = 'insert into user (username, password, role, email) values ("%s","%s","%s","%s")' % (tuple(temp_arr))
    print sql
    db.execute(sql)

# dbexcute()

def db_insert():
    from api import DBOPERAT
    dbop = DBOPERAT(table="user")
    print dbop.insert(values=["xxx","xxx","admin","xxx@admin"])
# db_insert()

# def db_select():
#     from api import DBOPERAT
#     dbop = DBOPERAT(table="user")
#     print dbop.select()
# db_select()

def db_delete():
    from api import DBOPERAT
    dbop = DBOPERAT(table="user")
    print dbop.delete(id_arr=[9,10])

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

