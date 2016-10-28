#!/usr/bin/env python
#encoding:utf8
import json
import time,random
import datetime
import MySQLdb
import MySQLdb.cursors
# 引入了mysqldb返回({},{})格式的值MySQLdb.cursors.DictCursor
class DB:
 
    conn = None
    # db = None
    # host = None

    def __init__(self, host, user, password, db):
        self.host = host
        self.user = user
        self.password = password
        self.db = db

    # 新建一个连接
    def connect(self):
        self.conn = MySQLdb.connect(host=self.host, user=self.user, passwd=self.password, db=self.db, charset="utf8", connect_timeout=600, compress=True, cursorclass = MySQLdb.cursors.DictCursor)
        self.conn.autocommit(True)          # 设置自动提交

    # 定义sql执行函数
    def execute(self, sql):
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql)
        except (AttributeError, MySQLdb.OperationalError):
            try:
                cursor.close()
                self.conn.close()
            except:
                pass
            time.sleep(1)
            try:
                self.connect()
                print "reconnect DB"
                cursor = self.conn.cursor()
                cursor.execute(sql)
            except (AttributeError, MySQLdb.OperationalError):
                time.sleep(2)
                self.connect()
                print "reconnect DB"
                cursor = self.conn.cursor()
                cursor.execute(sql)
        return cursor.fetchall()        # 返回格式为字典({},{},{},)

if __name__ == "__main__":

    # 测试
    db = DB(host='101.200.125.9',user='root',password='123456',db='mingguangzhen')
    sql = 'select * from user'
    print db.execute(sql)