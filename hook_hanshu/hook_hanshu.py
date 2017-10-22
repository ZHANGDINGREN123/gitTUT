#coding=utf-8
#hook_hanshu:钩子函数，作用：eg:
# a函数执行完后征程应该执行b函数，如果执行了钩子函数c，则钩子函数c会插队,在a函数之心完后先执行钩子函数c，在执行函数b

import os
from flask import Flask,render_template,request,session,redirect,url_for,g


app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

@app.route('/')
def index():
    print 'index'
    return render_template('index.html')

@app.route('/login/', methods=['GET', 'POST'])
def login():
    print 'login'
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'zhiliao' and password == '111111':
            session['username'] = 'zhiliao'
            return u'登录成功'
        else:
            return u'用户名或密码错误'

# 模拟修改用户信息视图
@app.route('/edit/')
def edit():
    # if hasattr(g, 'username'):
    #     return u'修改成功'
    # else:# 若cookie到期或者被删除,则在访问/edit/时自动跳转到登录页面
    #     return redirect(url_for('login'))
    return render_template('edit.html')



# before_request:在请求之前执行的，即before_request是在视图函数执行之前执行的
# before_request这个函数只是一个装饰器，它可以把需要设置为钩子函数的代码放置其中，以便在试图函数执行之前执行它
# before_request可以理解为构造函数，每个装饰器为一个对象，每个装饰器执行以前，都需要执行构造函数即执行before_request

@app.before_request
def my_before_request():
    # 每次访问装饰器前都判断session是否有'username'
    if session.get('username'):
        # 有的话说明已经登录，则使用全局变量记录'username'信息，
        # 这样可以将username绑定到
        g.username = session.get('username', username='zhiliao')
    # print 'my_before_request'


#context_processor:的返回值如果成功返回username，那么所有模板当中都会有username的值：'zhiliao'
@app.context_processor
def my_context_processor():
    username = session.get('username')
    # return {'username': username}#未实现
    return {'username': 111111}
    # 日后补充该逻辑
    # if  username:
    #     return {'username':username}
    # else:
    #     pass




if __name__ == '__main__':
    app.run(debug=True)
