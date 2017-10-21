#coding=utf-8

from flask import Flask
from exts import db
from models import Article
import config

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)# app已经入栈


#
# with app.app_context():# 将本app推至栈顶
#     # 若对Article表有后续操作，db.create_all()并不能更新对表的后续操作
#     db.create_all()


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
