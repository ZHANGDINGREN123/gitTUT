#coding=utf-8
from flask import Flask
from exts import db

from models import Article#不能切断此链条，因为models_sep必须调用Article

import config

app = Flask(__name__)

# 调用config文件
app.config.from_object(config)

#由于需要切断循环链条，所以需要db来绑定app。
db.init_app(app)



@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
