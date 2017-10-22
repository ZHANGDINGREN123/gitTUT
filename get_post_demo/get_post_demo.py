# coding=utf-8
from flask import Flask,render_template,request
# 通过request方法调用get和post请求

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search/')
def search():
    # args:是arguments的简写,request.args返回/search/所有的参数的字典
    # {
    #     'q': 'hello'
    # }
    q = request.args.get('q')
    print request.args
    return u'用户提交的查询参数是：%s' % q


# 默认的视图函数，只能采用get请求
# 如果你想采用post请求，那么要写明methods=['GET', 'POST']
# render_template('login.html')：需要用到GET请求
# login.html内部需要用到post请求，即将用户输入的账户名密码信息发送给试视图函数，则需要用到POST请求
@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:#肯定为POST请求
        #从login.html中的form标签通过post请求获取用户数据
        username =  request.form.get('username')
        password = request.form.get('password')
        print 'username',username
        print 'password',password
        return 'post request'



if __name__ == '__main__':
    app.run(debug=True)
