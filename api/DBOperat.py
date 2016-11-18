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
        if len(values) != len(table_thead[self.table]):         # 将后端穿入的值与数据库表key的数量做验证,匹配即可继续
            print "传入的值与表键数量不匹配"
            return False

        sqlkeys = str(tuple(table_thead[self.table])).replace("'","")              # 往数据库增加的表的key
        sqlvalues = str(tuple((values)))                                           # 往数据库增加的表的值
        sql = "insert into %s %s values %s" % (self.table, sqlkeys, sqlvalues)     # 拼接sql
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
        for _id in id_arr:
            sql = "delete from %s where id=%s" % (self.table, _id)
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
        if len(values) != len(table_thead[self.table]):         # 将后端穿入的值与数据库表key的数量做验证,匹配即可继续
            print "传入的值与表键数量不匹配"
            return False
        # 拼接sql中key=value部分,这里将key锁定,下面拼接value的值
        keysjoin = str(table_thead[self.table]).replace("[","").replace("]","").replace("'","").replace(",","='%s',") + "='%s'"
        # 拼接上面需要的value的值
        kvalues = tuple(str(values).replace("[","").replace("]","").replace("'","").replace(" ","").split(','))
        # 将sql中key=value部分拼接完毕
        keysjoin = keysjoin % (kvalues)
        # 开始格式化可用的sql
        sql = "update %s set %s where id='%s'" % (self.table, keysjoin, _id)

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
        seakeys = str(table_thead[self.table]).replace("[","").replace("]","").replace("'","")      # 定义需要查询的keys作为sql拼接的格式化的值
        sql = "select id,%s from %s" % (seakeys, self.table)       # 格式化出查询的sql
        print sql
        try:
            res = self.db.execute(sql)            # 执行查询数据的sql
        except Exception as error:
            print "数据查询失败."
            print error
            return False
        else:
            print "数据查询成功."
            return res

if __name__ == "__main__":

    pass