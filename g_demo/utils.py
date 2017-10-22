# coding=utf-8
from flask import g

# 写一些工具类的函数

def login_log():
    print u'当前登录用户是：%s' % g.username

def login_ip_log():
    print u'当前用户的ip是：%s' % g.ip
