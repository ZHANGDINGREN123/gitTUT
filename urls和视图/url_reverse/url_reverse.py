# coding=utf-8
from flask import Flask,url_for

app = Flask(__name__)


@app.route('/')
def index():
    print(url_for('my_list'))#从视图函数反转得到url
    print(url_for('article', id='abc'))#从视图函数反转得到url
    return 'Hello World!'

@app.route('/list/')
def my_list():
    return 'list'

@app.route('/article/<id>/')
def article(id):
    return u'您请求的id是:%s' % id




if __name__ == '__main__':
    app.run(debug=True)
