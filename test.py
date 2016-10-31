#!/usr/bin/env python
#encoding:utf8
#
#
# from api import DBOPERAT
# from methods import DATAIMPORT

# excjoint = ExcJoint(table="user")
# excanaly = ExcAnaly(excel="G:\\python\\test_file\\user.xlsx",table="user")
# print excjoint.data_tailor()
# print excanaly.excel_analy()


# instan = UserAuth(user="Lisa", passwd="123456")

# print instan.user_auth()
# 

# dbop = DBOPERAT(table="user")
# val = ["xxxxx","!QAZ2wsx","super admin","xxx@cdb.com.cn"]

# print dbop.insert(values=val)
# _id = 1

# dbop.delete(_id=_id)
#
# from api import DBOPERAT

def db_select():
    from api import DBOPERAT
    dbop = DBOPERAT(table="user")
    print dbop.select()
db_select()

def db_delete():
    from api import DBOPERAT
    dbop = DBOPERAT(table="user")
    print dbop.delete(_id=6)

db_delete()

def data_import():
    from methods.data import DATAIMPORT
    instance = DATAIMPORT(excel="G:\\python\\test_file\\user.xlsx",table="user")
    instance.data_import()

data_import()