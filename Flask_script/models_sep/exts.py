# coding=utf-8
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()#原本属于models_sep，由于需要切断链条所以单独拿出来，这样models_sep和models都需要调用db，从而切断了循环调用