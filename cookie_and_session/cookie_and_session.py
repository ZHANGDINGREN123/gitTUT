#coding=utf-8

from flask import Flask,session
import config
import os

app = Flask(__name__)

# 9行（app.config['SECRET_KEY'] = 'xxx'）与10行（app.config.from_object(config)）代码作用相同
# app.config['SECRET_KEY'] = '24个字符的字符串'
# app.config.from_object(config)
print os.urandom(24)
# app.config['SECRET_KEY'] = os.urandom(24) #对应30行注释，把如果不把盐写死，这样即使重新执行服务器，网页刷新/get/会报错
app.config['SECRET_KEY'] = 'abc' #对应30行注释，把盐写死，这样即使重新执行服务器，网页刷新/get/一样能有结果

# 盐
# SECRET_KEY = 'abc'
# 'ausernameb:zhiliaoc'


#  添加数据到session中
#  操作session与操作字典基本相同

@app.route('/')
def hello_world():
    session['username'] = 'zhiliao'

    return 'Hello World!'

# 通过session获取用户名,没重新执行一遍服务器,盐都会发生改变，所以需要把盐写死。
@app.route('/get/')
def get():
    return session.get('username')

# 删除session(删除'username')
@app.route('/delete/')
def delete():
    print session.get('username')
    session.pop('username')
    print session.get('username')
    return 'success'

@app.route('/clear/')
def clear():
    print session.get('username')
    session.clear()
    print session.get('username')
    return 'successful'

if __name__ == '__main__':
    app.run()
