#!/usr/bin/env python
#encoding:utf8
#
import sys
from methods import DB
from config import db_config, table_thead

reload(sys)
sys.setdefaultencoding("utf-8")

class UserAuth:

    def __init__(self,user,passwd):
        self.db = DB(host=db_config["host"],user=db_config["user"],password=db_config["passwd"],db=db_config["db"])
        self.user = user
        self.passwd = passwd

    # 从数据库中获取用户/密码,结构[{},{},{}]
    def sql_data(self):
        sql = "select username, password from user"
        try:
            res = self.db.execute(sql)
        except Exception as error:
            print "从数据库获取用户信息失败"
            print error
        # 返回用户密码信息
        return res

    # 将用户/密码做验证
    def user_auth(self):
        user_info = {}          # 用来存放用户名密码如{"John":"123456","Aaron":"23456"}
        for one in self.sql_data():
            user_info[one["username"]] = one["password"]    # 处理数据库获取的信息并放入user_info中

        if self.user in user_info:                          # 开始认证判断
            if user_info[self.user] == self.passwd:
                print "用户认证成功."
                return True
            else:
                print "认证密码错误."
                return False
        else:
            print "用户名不存在."
            return False

class GetData:

    def __init__(self,table):
        self.db = DB(host=db_config["host"],user=db_config["user"],password=db_config["passwd"],db=db_config["db"])
        self.num = len(table_thead[table])
        self.thead = table_thead[table]
        self.table = table

    def getdata(self):
        values = []
        print "table_thead:"
        print table_thead
        # seakeys = str(table_thead[self.table]).replace("[","").replace("]","").replace("'","")      # 定义需要查询的keys作为sql拼接的格式化的值
        # print table_thead[table]
        # keys_num = len(table_thead[table])
        # print "keys_num:"
        # print keys_num
        # values += table_thead[table]
        values += self.thead
        print values
        # values.insert(0,"id")
        values.append(self.table)
        print values
        tmp_sql = "select id," + ",".join(['%s'] * self.num) + " from %s"       # 格式化出查询的sql
        print tmp_sql
        sql = tmp_sql % tuple(values)
        print sql
        try:
            res = self.db.execute(sql)            # 执行查询数据的sql
        except Exception as error:
            print "数据查询失败."
            print error
            # return False
        else:
            print "数据查询成功."
            return res

if __name__ == "__main__":

    pass