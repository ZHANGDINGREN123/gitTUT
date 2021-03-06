# coding=utf-8
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from exts import db
from zlktqa import app
from models import User,Question,Answer #循环引用中的引用模型操作

# 专门用来些写各种命令(终端db init ),以及数据迁移

# 使用Manager绑定app
manager = Manager(app)

# 使用migrate绑定app和db
migrate = Migrate(app, db)

# 添加迁移脚本的命令到manager中
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
