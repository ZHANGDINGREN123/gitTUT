#static文件夹存放.ccs .js .img文件
#tempalates文件夹存放.html文件
from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def index():
    class Person(object):
        name = u'吉晨晨'
        age = 19

    p = Person()

    context = {
        'username': u'张鼎鼎',
        'gender': u'男',
        'age': 18,

        #key:person value:p
        'person': p,

        #字典中嵌套字典
        'websites': {
            'baidu': 'www.baidu.com',
            'google': 'www.google.com'
        }
    }

    #无需写成./templates/another/index.html。因为flask会自动在项目templates下搜索index.html
    return render_template('another/index.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
