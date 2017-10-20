#coding=utf-8

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    comments = [
        {
            'user': u'知了课堂',
            'content': 'xxxx'
        },
        {
            'user': u'张鼎鼎',
            'content': 'I LOVE JICHENCHEN'
        }
    ]
    return render_template('index.html',
                           # 未能实现
                           # avatar = 'http://cn.technode.com/files/2017/05/22.jpg',
                           comments = comments)


if __name__ == '__main__':
    app.run(debug=True)
