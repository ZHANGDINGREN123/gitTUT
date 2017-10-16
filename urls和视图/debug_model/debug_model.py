#coding=utf-8
from flask import Flask
### 使用配置文件：
# 1.新建一个'config.py'文件
# 2.在主app文件中导入这个文件，并且配置到'app'中，示例代码如下

import config

app = Flask(__name__)
app.config.from_object(config)

@app.route('/')
def hello_world():
    return '我是啦啦啦呵呵'


if __name__ == '__main__':
    app.run()
    # 1. app.run()中传入一个关键字参数debug:app.run(debug=True),即可设置当前项目为debug模式
    # 2. debug模式中的两大功能：
        # 当程序出现问题的时候，可以在页面中看到错误信息和出错的位置。
        # 只要修改了项目中的'python'文件，程序会自动加载，不需要重新启动服务器。
