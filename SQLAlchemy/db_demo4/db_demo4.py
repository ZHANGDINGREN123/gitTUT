#coding=utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config


app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)
db.create_all()

# 标签表
# create table tag(
#     id int primary key autoincrement,
#     name varchar(50) not null,
# )
# 文章表
# create table article(
#     id int primary key autoincrement,
#     title varchar(100) not null,
# )
# 关联表(多对多)
# create table article_tag(
#     article_id int,
#     tag_id int,
#     primary key('article', 'tag_id'),
#     foreign key 'article_id' reference 'article.id',
#     foreign key 'tag_id' reference 'tag.id',
# )



#实现上述功能
article_tag = db.Table('article_tag',
                       db.Column('article_id', db.Integer, db.ForeignKey('article.id'),primary_key=True),
                       db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'),primary_key=True),
                       )


class Tag(db.Model):
    __tablename__ = 'tag'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)

class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    tags = db.relationship('Tag', secondary=article_tag, backref=db.backref('articles'))



db.create_all()


@app.route('/')
def index():
    article1 = Article(title='aaa')
    article2 = Article(title='bbb')
    tag1 = Tag(name='111')
    tag2 = Tag(name='222')

    article1.tags.append(tag1)
    article1.tags.append(tag2)
    article2.tags.append(tag1)
    article2.tags.append(tag2)

    db.session.add(article1)
    db.session.add(article2)
    db.session.add(tag1)
    db.session.add(tag2)

    db.session.commit()


    article3 = Article.query.filter(Article.title == 'aaa').first()
    tags = article3.tags
    for tag in tags:
        print tag.name

    return 'index'


if __name__ == '__main__':
    app.run()
