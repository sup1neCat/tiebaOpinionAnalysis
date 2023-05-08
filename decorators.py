# _*_ coding : utf-8 _*_
# @Time : 2023/4/20 17:38
# @Author : sup1neCat
# @File : decorators
# @Project : tiebaOpinionAnalysis
from functools import wraps
from flask import g, redirect, url_for


# 装饰器函数的写法
def login_required(func):
    # 保留func的信息
    @wraps(func)
    def inner(*args, **kwargs):
        if g.user:  # 如果用户已登录，则继续执行func
            return func(*args, **kwargs)
        else:
            return redirect(url_for("auth.login"))

    return inner