#!/usr/bin/env python
#encoding:utf8
#
#
from api import ExcAnaly, ExcJoint, UserAuth, DBOPERAT


# excjoint = ExcJoint(table="user")
# excanaly = ExcAnaly(excel="G:\\python\\test_file\\user.xlsx",table="user")
# print excjoint.data_tailor()
# print excanaly.excel_analy()


# instan = UserAuth(user="Lisa", passwd="123456")

# print instan.user_auth()
# 

dbop = DBOPERAT(table="user")
# val = ["xxxxx","!QAZ2wsx","super admin","xxx@cdb.com.cn"]

# print dbop.insert(values=val)
# _id = 1

# dbop.delete(_id=_id)
# 
print dbop.select()