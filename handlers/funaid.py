#!/usr/bin/env python
#encoding:utf8
#
import sys, copy
from api import DBOPERAT
from methods.data import DataImport, DataExport
from config import excel_thead, table_thead

reload(sys)
sys.setdefaultencoding('utf-8')

class RequestProcess:

    def __init__(self, table):
        self.table = table

    def response(self, option=None, insert_val=None, arr_id=None, update_val=None, _id=None, excel=None):
        if option == "None":
            print "没有任何可用操作选项。"
            return False
        try:
            if option == "select":
                res = DBOPERAT(table=self.table).select()
                return res

            elif option == "delete":
                if DBOPERAT(table=self.table).delete(id_arr=arr_id):
                    return True
                else:
                    return False
            elif option == "insert":
                if DBOPERAT(table=self.table).insert(values=insert_val):
                    return True
                else:
                    return False
            elif option == "update":
                if DBOPERAT(table=self.table).update(values=update_val, _id=_id):
                    return True
                else:
                    return False
            elif option == "import":
                if DataImport(excel=excel,table=self.table).data_import():
                    return True
                else:
                    return False

            elif option == "export":
                if DataExport(table=self.table).data_export():
                    return True

        except Exception as error:
            print "执行%s操作失败。" % (option)
            print error
            return False
        return True

class ForHtmlVal:

    def __init__(self, table):
        self.table = table

    def res_val(self):
        res = {}
        res["assetdata"] = DBOPERAT(table=self.table).select()
        res["theads"] = excel_thead[self.table]
        tmp = []
        excel_keys = copy.deepcopy(excel_thead[self.table]) 
        excel_keys.pop(0)

        for i in range(len(excel_keys)):
            tmp.append((table_thead[self.table][i], excel_keys[i]))

        res["modalval"] = tmp  
        return res