# coding=utf-8

from flask import Flask,render_template,request,redirect,url_for,session,g
import config
from models import User,Question,Answer
from exts import db
from decorators import login_required
from sqlalchemy import or_
from werkzeug.security import check_password_hash


app = Flask(__name__)

# 导入配置文件
app.config.from_object(config)

db.init_app(app)






@app.route('/')
def index():
    context = {
        'questions':Question.query.order_by('-create_time').all()

    }
    return render_template('index.html', **context)



@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method == 'GET':
         return render_template('login.html')
    else:
        telephone = request.form.get('telephone')
        password = request.form.get('password')

        user = User.query.filter(User.telephone == telephone).first()
        if user and user.check_password(password):# 如果存在，即手机号码与密码正确，则可以登录
            # 将用户相关信息保存到cookie和session
            session['user_id'] = user.id
            # 如果想在31天内都保存cookie，添加下行代码
            session.permanent = True
            return redirect(url_for('index'))
        else:
            return u'手机号码或密码错误，请确认后重新登录'


@app.route('/regist/',methods=['GET','POST'])
def regist():
    if request.method == 'GET':
         return render_template('regist.html')
    else:
        telephone = request.form.get('telephone')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        # 手机号码验证，如果被注册了，就不能再注册了
        user = User.query.filter(User.telephone == telephone).first()
        if user: # 如果有值，即改账号已经被注册
            return u'该手机号码已经被注册，请更换手机号码'
        else:
            # password1与password2相等才可以
            if password1 != password2:
                return u'两次密码不一致，请核对后重新输入'
            else:
                # 密码两次输入一致,则将数据保存到数据库当中
                user = User(telephone=telephone,username=username,password=password1)
                db.session.add(user)
                db.session.commit()
                # 如果注册成功，就让页面跳转到登录页面
                return redirect(url_for('login'))

@app.route('/logout/')
def logout():
    # 删除session数据：以下三行代码都可以完成该功能
    # session.pop('user_id')
    # del session['user_id']
    session.clear()
    return redirect(url_for('login'))



# question => login_required(question) => wrapper(*args,**kwargs)
# 即执行index()就是执行wrapper()
@app.route('/question/', methods=['GET', 'POST'])
@login_required
def question():
    if request.method == 'GET':
        return render_template('question.html')
    else:
        title = request.form.get('title')
        content = request.form.get('content')
        question = Question(title=title, content=content)

        # 从数据库读取用户数据，确认是那个作者在发布问题

        question.author = g.user
        question.content = content
        db.session.add(question)
        db.session.commit()

        #完成后返回首页
        return redirect(url_for('index'))


@app.route('/detail/<question_id>')
def detail(question_id):
    question_model =  Question.query.filter(Question.id == question_id).first()
    return render_template('detail.html', question=question_model)

@app.route('/add_answer/',methods=['POST'])
@login_required
def add_answer():
    # 从form标签中拿到评论内容
    content = request.form.get('answer_content')
    question_id = request.form.get('question_id')

    # 将评论内容添加到数据库当中
    answer = Answer(content=content)
    answer.author = g.user
    question = Question.query.filter(Question.id == question_id).first()
    answer.question = question
    db.session.add(answer)
    db.session.commit()
    return redirect(url_for('detail',question_id=question_id))


@app.route('/search/')
def search():
    q = request.args.get('q')

    #查找的关键字在title或content当中
    questions = Question.query.filter(or_(Question.title.contains(q),
                              Question.content.contains(q))).order_by('-create_time')
    return render_template('index.html',questions = questions)


@app.before_request
def my_before_request():
    user_id = session.get('user_id')
    if user_id:
        user = User.query.filter(User.id == user_id).first()
        if user:
            g.user = user




@app.context_processor
def my_context_processor():
    # hasattr：判断g对象有误'user'属性
    if hasattr(g,'user'):
        return {'user':g.user}
    # 未登录的话也要返回一个空字典
    return {}

# before_request->视图函数->context_processor


if __name__ == '__main__':
    app.run()
