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
                           avatar = 'http://avatar.csdn.net/7/0/9/1_qq_33852877.jpg',
                           comments = comments)


if __name__ == '__main__':
    app.run(debug=True)
