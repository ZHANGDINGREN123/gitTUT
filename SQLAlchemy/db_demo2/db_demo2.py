#coding=utf-8

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config


app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)

# article表
# create table article(
#     id int primary key autoincrement,
#     title varchar(100) not null,
#     content text not null
# )

#类同上述(article表)功能
#实现模型与表的映射
class Article(db.Model):
    __tablename__ = 'article'#设置表名
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.TEXT, nullable=False)

db.create_all()#测试是否能运行到数据库当中

@app.route('/')
def index():
    # 数据的增删改查
    # 1.增加
    article1 = Article(title = 'aaa', content = 'bbb')
    db.session.add(article1)#数据的增删改查都是通过session完成的（本操作为事务操作）
    db.session.commit()#提交事务

    # 2.查（select * from article where title='aaa';）
    article2 =  Article.query.filter(Article.title == 'aaa').first()# .first()为返回第一行数据。  .all()为返回所有数据（使用all()时输出对应article2[数字]）
    print 'title:%s' % article2.title
    print 'content:%s' % article2.content

    # 3.改
        # 第一步：先把你要更改的数据查找出来
    article3 = Article.query.filter(Article.title == 'aaa').first()#找到含有'aaa'的第一条数据
        # 第二步：对这条数据数据需要修改的地方进行修改
    article3.title = 'new title'
        # 第三步：提交事务
    db.session.commit()

    # 4.删
        # 第一步:把需要删除的数据查找出来
    article4 = Article.query.filter(Article.title == 'aaa').first()
        # 第二步:把这条数据删除掉
    db.session.delete(article4)
        # 第三不:做事务提交
    db.session.commit()



    return 'index'


if __name__ == '__main__':
    app.run()
