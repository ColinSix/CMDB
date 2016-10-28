#encoding=utf-8
#

db_config = {
    'host':'101.200.125.9',
    'user':'root',
    'passwd':"123456",
    'db':'mingguangzhen'
            }

app_config = {
    'host':'0.0.0.0',
    'port':8080,
    'debug':True,
    'linux_dir':'/tmp/cmdb-file/',
    'windows_dir':'E:\\tmp\\cmdb-file\\'
             }

# 数据库表头
table_thead = {'user':['username',
                       'password',
                       'role',
                       'email'],

              'vmassets':['ip_addr',
                          'app_name',
                          'hostname',
                          'vc_name',
                          'cpu',
                          'memory',
                          'disk',
                          'os',
                          'status',
                          'office_name',
                          'office_contact',
                          'office_phone',
                          'object_contact',
                          'object_phone',
                          'create_date',
                          'end_date',
                          'notes']
              }

# excel文件表头
excel_thead = {'user':['USE',
                      '用户名',
                      '密码',
                      '角色',
                      '邮箱'],

              'vmassets':['USE',
                          'IP地址',
                          '应用系统名称',
                          '主机名',
                          'vCenter名称',
                          'CPU',
                          '内存',
                          '硬盘',
                          '操作系统',
                          '使用状态',
                          '负责处室',
                          '行方负责人',
                          '行方电话',
                          '项目组联系人',
                          '项目组联系方式',
                          '创建日期',
                          '拟定回收日期',
                          '备注']
              }
