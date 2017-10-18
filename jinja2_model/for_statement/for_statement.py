#coding=utf-8
from flask import Flask,render_template

app = Flask(__name__)

# eg.1
# for 遍历字典与列表
#
# @app.route('/')
# def index():
#     user = {
#         'username': u'张鼎鼎',
#         'age': 18
#     }
#
#     for k, v in user.items():
#         #k: key  v:values
#         print k
#         print v
#     websites = ['baidu.com', 'google.com']
#     for i in websites:
#         print i
#     return render_template('index.html',user=user, websites=websites)


# eg.2
@app.route('/')
def index():
    books = [
    {
        'name': u'西游记',
        'author': u'吴承恩',
        'price': 109
    },
    {
        'name': u'红楼梦',
        'author': u'曹雪芹',
        'price': '200'
    },
    {
        'name': u'三国演义',
        'author': u'罗贯中',
        'price': 120
    },
    {
        'name': u'水浒传',
        'author': u'施耐庵',
        'price': 130
    }
    ]
    return render_template('index.html', books = books)



if __name__ == '__main__':
    app.run(debug=True)
