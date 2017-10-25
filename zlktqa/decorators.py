# coding=utf-8

# 登录限制的装饰器
from functools import wraps
from flask import session,redirect,url_for

def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # 在question装饰器处实现限制登录的操作：如果未登录则返回登录界面
        # 因为question有return所以wrapper也需要有return
        if session.get('user_id'):
            return func(*args, **kwargs)
        else:
            return redirect(url_for('login'))
    return wrapper
