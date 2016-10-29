#!/usr/bin/env python
#encoding:utf8
#
#
from api import ExcAnaly, ExcJoint, UserAuth


# excjoint = ExcJoint(table="user")
# excanaly = ExcAnaly(excel="G:\\python\\test_file\\user.xlsx",table="user")
# print excjoint.data_tailor()
# print excanaly.excel_analy()


instan = UserAuth(user="Lisa", passwd="123456")

print instan.user_auth()
