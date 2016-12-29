#encoding=utf-8
#

db_config = {
    "host":"localhost",
    "user":"root",
    "passwd":"123456",
    "db":"cmdb"
            }

app_config = {
    "host":"0.0.0.0",
    "port":8080,
    "debug":True
    # "linux_dir":"/tmp/cmdb-file/",
    # "windows_dir":"E:\\tmp\\cmdb-file\\"
             }

# 数据库表头
table_thead = {"user":["username",
                       "password",
                       "role",
                       "email"],

              "vmassets":["room",
                          "pool",
                          "project",
                          "vmname",
                          "ip",
                          "cpu",
                          "memory",
                          "disk",
                          "system",
                          "hostname",
                          "user",
                          "password",
                          "contact",
                          "cphone",
                          "bank",
                          "bphone",
                          "startdate",
                          "enddate",
                          "note"]
              }

# excel文件表头
excel_thead = {"user":["USE",
                      "用户名",
                      "密码",
                      "角色",
                      "邮箱"],

              "vmassets":["USE",
                          "机房",
                          "资源池",
                          "项目组",
                          "虚机名称",
                          "IP地址",
                          "CPU",
                          "内存",
                          "硬盘",
                          "操作系统",
                          "主机名",
                          "用户名",
                          "密码",
                          "负责人",
                          "电话",
                          "行方",
                          "电话",
                          "交付日期",
                          "归还日期",
                          "备注"]
              }
