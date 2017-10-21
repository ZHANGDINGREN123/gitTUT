#coding=utf-8
# 此文件将被引用到manage.py文件运行

from flask_script import Manager

DBManager = Manager()

@DBManager.command
def init():
    print '数据库初始化完成'

@DBManager.command
def migrate():
    print '数据表重新迁移成功'

