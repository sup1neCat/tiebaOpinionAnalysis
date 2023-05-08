# _*_ coding : utf-8 _*_
# @Time : 2023/4/19 21:40
# @Author : sup1neCat
# @File : auth
# @Project : tiebaOpinionAnalysis
from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from .forms import RegisterForm, LoginForm
from werkzeug.security import generate_password_hash, check_password_hash  # 哈希加密
from models import UserModel
from exts import db

# /auth
bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'GET':
        return render_template('login.html', form=form)
    else:
        if form.validate():
            phone_number = form.phone_number.data
            password = form.password.data
            user = UserModel.query.filter_by(phone_number=phone_number).first()
            if not user:
                flash("该用户不存在！")
                return redirect(url_for('auth.login'))
            if check_password_hash(user.password, password):  # 登陆成功
                session['user_id'] = user.id
                flash("登录成功！", user.username)
                return redirect("/")
            else:
                flash("密码错误！")
                return redirect(url_for('auth.login'))
        else:
            print(form.errors)
            return render_template('login.html', form=form)


@bp.route("/logout")
def logout():
    session.clear()
    return redirect("/")


@bp.route("/register", methods=['GET', 'POST'])
def register():
    # 表单验证：flask-wtf：wtforms
    form = RegisterForm(request.form)
    if request.method == 'GET':
        return render_template('register.html', form=form)
    else:
        if form.validate():
            phone_number = form.phone_number.data
            user_name = form.user_name.data
            password = form.password.data
            user = UserModel(phone_number=phone_number, username=user_name, password=generate_password_hash(password))
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("auth.login"))
        else:
            print(form.errors)
            return render_template('register.html', form=form)
