#!/usr/bin/env python
#encoding:utf8
#
import sys
from api import DBOPERAT

reload(sys)
sys.setdefaultencoding('utf-8')

class RequestProcess:

    def __init__(self, table, option, insert_val=None, arr_id=None, update_val=None, _id=None):
        self.table = table
        self.option = option
        self.insert_val = insert_val
        self.arr_id = arr_id
        self.update_val = update.val
        self.id = _id

    def response(self):
        
    