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

    temp_arr = ['\xe6\x88\x91', '\xe6\x88\x91', 'user', '\xe6\x88\x91']
    sql = "insert into user (username, password, role, email) values (%s, %s, %s, %s)" % ('"\xe5\xa5\xbd"', '"\xe5\xa5\xbd"', '"user"', '"\xe5\xa5\xbd"')
    sql = 'insert into user (username, password, role, email) values ('"\xe4\xb8\xad\xe5\x9b\xbd"', '"\xe4\xb8\xad\xe5\x9b\xbd"', '"user"', '"\xe4\xb8\xad\xe5\x9b\xbd"')'

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

def db_select():
    from api import DBOPERAT
    dbop = DBOPERAT(table="user")
    print dbop.select()
# db_select()

def db_delete():
    from api import DBOPERAT
    dbop = DBOPERAT(table="user")
    print dbop.delete(id_arr=[9,10])

# db_delete()

# 测试处理excel文件,返回值
def excanaly():
    from api import ExcAnaly
    inst = ExcAnaly(table="user", excel="C:\\Users\\GZ\\Downloads\\export_user.xlsx")
    return inst.excel_analy()
# print excanaly()

def importdata():
    from methods.data import DataImport
    inst = DataImport(table="user", excel="C:\\Users\\GZ\\Downloads\\export_user.xlsx")
    inst.data_import()
# importdata()

def exportdata():
    from methods.data import DataExport
    inst = DataExport(table="user")
    # return inst.get_data()
    inst.data_export()
# print exportdata()


def bootapp_test():
    from config import app_config
    from handlers.cmdb_app import app
    webrun = app
    webrun.run(host=app_config['host'], port=app_config['port'], debug=app_config['debug'])

bootapp_test()
# 
# 



# test_excel()

