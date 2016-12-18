#!/usr/bin/env python
#encoding:utf8
#
import sys
from api import DBOPERAT

reload(sys)
sys.setdefaultencoding('utf-8')

class RequestProcess:

    def __init__(self, table):
        self.table = table

    def response(self, option=None, insert_val=None, arr_id=None, update_val=None, _id=None):
        if option == "None":
            print "没有任何可用操作选项。"
            return False
        try:
            if option == "select":
                res = DBOPERAT(table=self.table).select()
                return res

            elif option == "delete":
                if DBOPERAT(table=self.table).delete(id_arr=arr_id):
                    pass
                    return True
                else:
                    pass
                    return False
            elif option == "insert":
                if DBOPERAT(table=self.table).insert(values=insert_val):
                    pass
                    return True
                else:
                    pass
                    return False
            elif option == "update":
                if DBOPERAT(table=self.table).update(values=update_val, _id=_id):
                    return True
                else:
                    return False

        except Exception as error:
            print "执行%s操作失败。" % (option)
            print error
            return False
        return True

    