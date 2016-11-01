#!/usr/bin/env python
#encoding:utf8
#
# 本api为导入导出提供数据基础
#
import sys, xlrd, copy
from config import table_thead, excel_thead, db_config
from methods import DB

reload(sys)
sys.setdefaultencoding("utf-8")

#
# 处理上传的excel并返回值
class ExcAnaly:

    def __init__(self,excel,table):
        self.excel = excel
        self.table = table

    def open_excel(self):
        workbook = xlrd.open_workbook(self.excel)   # 打开传入的excel文件
        try:
            selectsheet = workbook.sheets()[0]      # 实例化一个sheet
        except Exception as error:
            print "选中表格sheet失败,处理文件中止."
            print error
        # 返回选中sheet
        return selectsheet

    # 处理选中的sheet
    def excel_analy(self):
        exc_sheet = self.open_excel()          # 创建被处理的excel sheet
        table_rows = exc_sheet.nrows           # sheet所有行数
        table_columns = exc_sheet.ncols        # sheet所有列数
        table_key = table_thead[self.table]    # 一个列表包含表中所有的键名
        res = []

        for rownum in range(1,table_rows):          # 从第二行开始循环sheet中每一行
            tmp = {}                                # 临时存储字典,每一行循环完毕都会刷新
            for colnum in range(1,table_columns):            # 从第二列起循环sheet每一列
                cell = exc_sheet.cell_value(rownum,colnum)   # 取出当前行列锁定的值(即取出逐行的值)
                tmp[table_key[colnum-1]] = cell        # 将取出的值按照表中的key存储到临时字典中(每一行代表一个字典)
            res.append(tmp)                   # 将每一行的数据添加到列表中直到所有行循环完毕
        return res                            # 返回[{},{},{},{}]格式


# 拼接要导出的excel基础数据并返回值
class ExcJoint:

    def __init__(self,table):
        self.db = DB(host=db_config["host"],user=db_config["user"],password=db_config["passwd"],db=db_config["db"])
        self.table = table

    # 主要从数据库获取需要的值并返回,格式[{},{},{}]
    def sql_data(self):
        num = len(table_thead[self.table])               # %s需要拼接多少次 
        split_sql = ','.join(['%s'] * num)               # 计算出%s的个数供sql拼接使用
        tmp_sql = "select " + split_sql + " from %s"     # 拼接出待格式化的sql
                              
        format_sqlval = copy.deepcopy(table_thead[self.table])    # 添加需要导出数据表的key作为查询的key(copy.deepcopy作用为复制出一份独立而不是指向的列表)
        format_sqlval.append(self.table)                          # 添加需要到处的数据表的名称(sql语句需要的格式化数据准备完毕)
        return self.db.execute(tmp_sql % tuple(format_sqlval))    # 获取数据库指定表的指定key的值作为返回值

    # 处理数据库中返回的值为[[],[],[]]格式,为导出excel做准备
    def data_tailor(self):
        res = []                                      # 结果返回列表
        exc_head = excel_thead[self.table]            # 引入excel表头文件
        tab_head = table_thead[self.table]            # 引入db表头文件
        res.append(exc_head)                          # 将excel中第一行定义出来
        for i in range(len(self.sql_data())):         # 按索引循环数据库返回值
            tmp = [i+1]                               # 每次循环索引+1(即excel中首列序号),tmp为excel每行值的容器
            for key in tab_head:                      # 循环数据库表中的key
                tmp.append(self.sql_data()[i][key])   # 完成excel每行数据的生成(即除了首列序号其它excel中每行的数据来自sql_data)
            res.append(tmp)                           # 循环完成时就是excel数据生成完毕的时候
        return res                                    # 将数据值返回给函数,供excel生成使用



if __name__ == "__main__":
    
    # 测试
    # EXC = ExcAnaly(excel="G:\\python\\test_file\\user.xlsx",table="user")
    # print EXC.excel_analy()
    pass










