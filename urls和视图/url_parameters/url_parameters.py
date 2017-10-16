from flask import Flask

app = Flask(__name__)


@app.route('/')#视图函数
def hello_world():
    return 'Hello World!'

#视图函数中需要放和url中的参数同名的
@app.route('/article/<id>')
def article(id):
    return u'您请求的参数的:%s' % id


if __name__ == '__main__':
    app.run()
