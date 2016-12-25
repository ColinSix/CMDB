#!/usr/bin/env python
#encoding:utf8
#
import sys,platform,os
# from api import DBOPERAT
from methods import DB
from config import db_config, table_thead, excel_thead
from werkzeug import secure_filename
# from handlers import RequestProcess as RP

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
                return 1
            else:
                print "认证密码错误."
                return 2
        else:
            print "用户名不存在."
            return 3

#
class GetFile:

    def __init__(self,file=None,use="upload"):
        self.excelf = file
        self.os_type = platform.system()
        if self.os_type == "Windows":
            self.usedir = os.getcwd() + "\\handlers\\static\\" + use + "_file\\"
        elif self.os_type == "Linux":
            self.usedir = os.getcwd() + "/handlers/static/" + use + "_file/"
        else:
            print "本程序不适用此系统.支持Windows和Redhat"
            return False
        if (os.path.exists(self.usedir)) == False:
            os.makedirs(self.usedir)

    # 保存上传文件
    def savefile(self):
        self.excelf.save(self.usedir + secure_filename(self.excelf.filename))

    # 返回上传文件所保存路径
    def filepath(self):
        os_type = platform.system()
        return self.usedir + secure_filename(self.excelf.filename)

    # 返回导出文件所保存路径
    def exportpath(self):
        return self.usedir



if __name__ == "__main__":

    pass