#!/usr/bin/env python
#encoding:utf8
#
# 提供操作DB的方法,支持增删改查
# 
from config import db_config, table_thead
from methods import DB
import copy

class DBOPERAT:

    def __init__(self, table):
        self.db = DB(host=db_config["host"],user=db_config["user"],password=db_config["passwd"],db=db_config["db"])
        self.table = table

    def insert(self, values):
        values_num = len(values)
        keys_num = len(table_thead[self.table])
        if values_num != keys_num:         # 将后端穿入的值与数据库表key的数量做验证,匹配即可继续
            print "传入的值%s" % (str(values))
            print "传入的值与表键数量不匹配应传%s,实传%s" % (keys_num, values_num)
            return False

        sqlvals = copy.deepcopy(table_thead[self.table])    # 定义格式化sql所需要的值的列表
        sqlvals.insert(0,self.table)
        
        temp_arr = []       # 临时list
        for val in values:          # 遍历插入的数据,遍历完成sqlval就完整了
            if type(val) == unicode:        # 判断元素是否为unicode字符
                sqlvals.append(val.encode("utf-8"))         # 将unicode字符转换为utf-8类型字符串并添加到sqlval中
            else:
                sqlvals.append(val)
        # 拼接出需要格式化的sql模型
        tmp_sql = 'insert into %s (' + ",".join(['%s'] * keys_num) + ') values (' + ",".join(['"%s"'] * values_num) + ')'
        # 格式化sql语句
        sql = tmp_sql % (tuple(sqlvals))
        print "执行数据库操作: %s" % (sql)
        try:
            self.db.execute(sql)            # 执行添加数据的sql
        except Exception as error:
            print "数据添加失败.%s" % (sql)
            print error
            return False
        else:
            print "数据添加成功."
            return True

    def delete(self, id_arr):
        for _id in id_arr:
            sql = "delete from %s where id=%s" % (self.table, _id)
            print "执行数据库操作: %s" % (sql)
            try:
                self.db.execute(sql)            # 执行删除数据的sql
            except Exception as error:
                print "数据删除失败,id:%s" % (_id)
                print error
                continue
            else:
                print "数据删除成功,id:%s" % (_id)
        return True

    def update(self, values, _id):
        values_num = len(values)
        if self.table == "user":        # user表只更新数据不更新用户名
            keys_num = len(table_thead[self.table])-1
            tmp_thead = copy.deepcopy(table_thead[self.table])
            tmp_thead.pop(0)
        else:                           # 其余表字段全部可以更新
            keys_num = len(table_thead[self.table])
            tmp_thead = copy.deepcopy(table_thead[self.table])

        if values_num != keys_num:                        # 将后端传入的值与数据库表key的数量做验证,匹配即可继续
            print "传入的值%s" % (str(values))
            print "传入的值与表键数量不匹配应传%s,实传%s" % (keys_num, values_num)
            return False
        # 拼接出需要格式化的sql模型
        tmp_sql = "update %s set" + ",".join([" %s='%s'"] * keys_num) + " where id='%s'"
        sqlvals = [self.table]          # 定义格式化sql所需要的值的列表  

        au_val = []         # 将sql的key和对应的value作为一个元祖插入到此列表作为格式化的值用
        for i in range(keys_num):
            au_val.append((tmp_thead[i],values[i].encode("utf-8")))
        # 遍历au_val,添加到sqlval里
        for x,y in au_val:
            sqlvals.append(x)
            sqlvals.append(y)
        sqlvals.append(_id)
        # 格式化sql语句
        sql = tmp_sql % (tuple(sqlvals))
        print "执行数据库操作: %s" % (sql)
        try:
            self.db.execute(sql)            # 执行更新数据的sql
        except Exception as error:
            print "数据更新失败."
            print error
            return False
        else:
            print "数据更新成功."
            return True

    def select(self):
        num = len(table_thead[self.table])
        values = copy.deepcopy(table_thead[self.table])
        values.append(self.table)

        tmp_sql = "select id," + ",".join(['%s'] * num) + " from %s"       # 格式化出查询的sql

        sql = tmp_sql % tuple(values)
        print "执行数据库操作: %s" % (sql)
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