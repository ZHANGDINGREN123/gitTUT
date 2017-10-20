#coding=utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config


app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)
db.create_all()

# 用户表
# create table user(
#     id int primary key autoincrement,
#     username varchar(100) not null,
# )
# 文章表
# create table article(
#     id int primary key autoincrement,
#     title carchar(100) not null,
#     content text not null,
#     author_id int,
#     foreign key 'author_id' references 'users.id' #引用user的id作为外键
# )

#实现上述功能
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False)

class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    # 外键 author_id
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    # relationship：根据关联的模型名（User）,找到与之关联的外键（author_id）
    # backref: 反向引用
    author = db.relationship('User', backref=db.backref('articles'))

db.create_all()


@app.route('/')
def index():
    # 实现添加一篇文章（因为文章必须依赖用户而存在，所以首先要添加一个用户）
    # user1 = User(username = 'zhiliao')
    # db.session.add(user1)
    # db.session.commit()
    #
    # article = Article(title='aaa', content='bbb', author_id=1)
    # db.session.add(article)
    # db.session.commit()

    # 上述代码实现完成后后，实现找到文章标题为'aaa'的这个作者
    # article1 = Article.query.filter(Article.title == 'aaa').first()
    # author_id = article1.author_id
    # user = User.query.filter(User.id == author_id).first()
    # print user.username

    # 上述代码实现比较麻烦，通过建立relationship，实现根据作者(eg.'zhiliao')找到其全部文章的功能
    # article.author:正向引用
    # author = User.query.filter(User.username == 'zhiliao').first()
    # author.articles:反向引用
    # article2 = Article.query.filter(Article.title == 'aaa').first()
    # print 'username: %s' % article2.author.username
    # 要找到zhiliao用户写过的所有文章，需要添加一些数据
    # article3 = Article(title='111', content='222', author_id = 1)
    # db.session.add(article3)
    # db.session.commit()
    # 添加完毕
    user = User.query.filter(User.username == 'zhiliao').first()
    result = user.articles
    for article in result:
        print '-'*10
        print article.title

    return 'index'


if __name__ == '__main__':
    app.run()
