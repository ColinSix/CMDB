#!/usr/bin/env python
#encoding:utf8
#
# 主要提供数据导入导出功能
# 
from config import table_thead, excel_thead, db_config
from methods import DB
from api import ExcAnaly, ExcJoint
from flask.ext import excel
import copy

# 提供excel数据导入
class DataImport:

    def __init__(self, excel, table):
        self.db = DB(host=db_config["host"],user=db_config["user"],password=db_config["passwd"],db=db_config["db"])
        self.table = table              # 定义表名
        self.excel = excel              # 定义excel

    # 拼接sql
    def join_sql(self):
        num = len(table_thead[self.table])      # %s需要拼接多少次
        keys_sql = ",".join(["%s"] * num)       # 拼接好的sql的keys
        values_sql = ",".join(["'%s'"] * num)   # 拼接好的sql的values
        sql = "insert into %s (" + keys_sql + ") values (" + values_sql + ")"   # 拼接完整的sql等待格式化
        return sql

    # 数据插入数据库
    def data_import(self):
        tmp_sql = self.join_sql()       # 定义待格式化的sql
        # 实例化处理过的excel的返回值
        exc_data = ExcAnaly(excel=self.excel,table=self.table).excel_analy()
        tmp_sqlval = [self.table]       # 定义需要格式化的sql所需要的值的临时容器
        # 循环数据表的keys,添加值格式化的临时容器中
        for key in table_thead[self.table]:
            tmp_sqlval.append(key)
        #print exc_data
        for data in exc_data:       # 循环excel的值
            #print data
            sqlval = copy.deepcopy(tmp_sqlval)      # 定义真正的格式化sql所需要的值(目前已经有了表名/表keys,每循环一次都会重置一次)
            for key in table_thead[self.table]:     # 循环表的key
                sqlval.append(data[key])            # 将表的key所对应的value添加至sqlval容器中(此时需要的值已经全了)
            sql = tmp_sql % tuple(sqlval)           # 完成可用的sql
            #print sql
            try:
                self.db.execute(sql)                    # 执行数据插入的sql
            except Exception as error:
                print error
                print "数据导入失败"
                print sql
                return False
        return True

# 提供数据导出
class DataExport:

    def __init__(self,table):
        self.table = table

    # 获取要导出的数据
    def get_data(self):
        res = ExcJoint(table=self.table).data_tailor()
        return res

    # 数据导出action需要和flask.ext.excel结合使用
    def data_export(self):
        data = self.get_data()
        return excel.make_response_from_array(data, "xlsx", file_name="export_" + self.table)

