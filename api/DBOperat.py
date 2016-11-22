#!/usr/bin/env python
#encoding:utf8
#
# 提供操作DB的方法,支持增删改查
# 
from config import db_config, table_thead
from methods import DB

class DBOPERAT:

    def __init__(self, table):
        self.db = DB(host=db_config["host"],user=db_config["user"],password=db_config["passwd"],db=db_config["db"])
        self.table = table

    def insert(self, values):
        values_num = len(values)
        keys_num = len(table_thead[self.table])
        if values_num != keys_num:         # 将后端穿入的值与数据库表key的数量做验证,匹配即可继续
            print "传入的值%s" % (str(values))
            print "传入的值与表键数量不匹配应传%s,实传%s" % (len(table_thead[self.table]), len(values))
            return False

        sqlkeys = table_thead[self.table]              # 往数据库增加的表的key
        sqlkeys.insert(0,self.table)
        #
        temp_arr = []
        for val in values:
            if type(val) == unicode:
                sqlkeys.append(val.encode("utf-8"))
            else:
                sqlkeys.append(val)

        tmp_sql = 'insert into %s (' + ",".join(['%s'] * keys_num) + ') values (' + ",".join(['"%s"'] * values_num) + ')'
        print tmp_sql
        print sqlkeys
        sql = tmp_sql % (tuple(sqlkeys))
        print sql
        try:
            self.db.execute(sql)            # 执行添加数据的sql
        except Exception as error:
            print "数据添加失败."
            print error
            return False
        else:
            print "数据添加成功."
            return True

    def delete(self, id_arr):
        print id_arr
        for _id in id_arr:
            sql = "delete from %s where id=%s" % (self.table, _id)
            print sql
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
        if len(values) != (len(table_thead[self.table])-1):         # 将后端穿入的值与数据库表key的数量做验证,匹配即可继续
            print "传入的值%s" % (str(values))
            print "传入的值与表键数量不匹配应传%s,实传%s" % (len(table_thead[self.table]), len(values))
            return False

        # 拼接sql中key=value部分,这里将key锁定,下面拼接value的值
        keysjoin = str(table_thead[self.table]).replace("[","").replace("]","").replace("'","").replace("username,","").replace(",","='%s',") + "='%s'"

        # 拼接上面需要的value的值
        kvalues = tuple(str(values).replace("[","").replace("]","").replace("'","").replace("u","").replace(" ","").split(','))
        kvalues = tuple(str(values).replace("u'","").replace("]","").replace("[","").replace("'","").replace(" ","").split(','))

        # 将sql中key=value部分拼接完毕
        keysjoin = keysjoin % (kvalues)
        # 开始格式化可用的sql
        sql = "update %s set %s where id='%s'" % (self.table, keysjoin, _id)
        print "执行数据库操作%s" % (sql)
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
        values = []
        tmp = ""
        seakeys = str(table_thead[self.table]).replace("[","").replace("]","").replace("'","")      # 定义需要查询的keys作为sql拼接的格式化的值
        keys_num = len(table_thead[self.table])
        values += table_thead[self.table]
        # values.insert(0,"id")
        values.append(self.table)
        print values
        tmp_sql = "select id," + ",".join(['%s'] * keys_num) + " from %s"       # 格式化出查询的sql
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