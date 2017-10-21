# coding=utf-8
from flask_script import Manager
from flask_migrate_demo import app
from flask_migrate import Migrate,MigrateCommand
from models import Article

from exts import db

# 模型 -> 迁移文件  ->  表
# 进入项目目录
# 1. python manage.py db init (仅第一次需要运行，后两不每次更改article表结构都需要运行一遍)
# 2. python manage.py db migrate
# 3. python manage.py db upgrade


manager = Manager(app)

# 1.要使用flask_migrate,必须绑定app和db
migrate = Migrate(app, db)

# 2.把MigrateCommand命令添加到manager中
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()