#coding=utf-8

# 以前需要从models_sep调用db，但造成了循环调用，所以现在从exts.py调用

from exts import db

class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, nullable=False)