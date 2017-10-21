#coding=utf-8
from flask_script import Manager
from flask_script_demo import app
from db_scripts import DBManager

manager = Manager(app)

# 和数据库相关的文件都放在一起

# 装饰器
@manager.command
def runserver():
    print "服务器跑起来了"

manager.add_command('db', DBManager)

if __name__ == '__main__':
    manager.run()