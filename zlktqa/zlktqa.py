# coding=utf-8

from flask import Flask,render_template
import config

app = Flask(__name__)

# 导入配置文件
app.config.from_object(config)

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
