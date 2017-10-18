#coding=utf-8

from flask import Flask,render_template

app = Flask(__name__)

class Person(object):
    name = ''
    age = 0

    # 为子类留下接口down_page(self)，以便子类调用父类方法
    def down_page(self):
        pass

 # 继承自Person所以无需定义name, age
class Student(Person):
    #实现父类接口down_page(self)
    def down_page(self):
        print '实现父类Person接口功能：学习'

class Teacher(Person):
    def down_page(self):
        print '实现父类Person接口功能：教书'




@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login/')
def login():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
