#coding=utf-8

# 介绍全局变量g
from flask import Flask,g,render_template,request
from utils import login_log,login_ip_log
app = Flask(__name__)


@app.route('/')
def index():
    return 'index'




@app.route('/login/',methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'zhiliao' and password == '111111':
            #就认为用户名和密码正确
            g.username = 'zhiliao'#将'zhiliao'绑定到全局变量g.username当中去
            g.ip = 'xxx.xxx.xxx.xxx'#将'xxx.xxx.xxx.xxx'绑定到全局变量g.ip当中去
            login_log()
            login_ip_log()
            return u'登陆成功'
        else:
            return u'您的用户名或密码错误！'


if __name__ == '__main__':
    app.run()
