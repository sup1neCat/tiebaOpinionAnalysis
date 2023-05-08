# _*_ coding : utf-8 _*_
# @Time : 2023/4/19 21:40
# @Author : sup1neCat
# @File : forms
# @Project : tiebaOpinionAnalysis
import wtforms
from wtforms.validators import DataRequired, Regexp, Length, EqualTo

from models import UserModel


# Form：主要用于验证前端提交的数据是否符合要求
class RegisterForm(wtforms.Form):
    phone_number = wtforms.StringField('phone_number',
                                       validators=[DataRequired(message="电话号码必填"),
                                                   Regexp(r'^1[35789]\d{9}$', message="请输入11位手机号")])
    user_name = wtforms.StringField('user_name',
                                    validators=[DataRequired(message="用户姓名必填"),
                                                Length(min=2, max=12, message="用户名长度必须为2至12位")])
    password = wtforms.StringField('password', validators=[Length(min=6, max=20, message="密码长度必须为6至20位")])
    password_confirm = wtforms.StringField(validators=[EqualTo('password', message="两次密码不一致")])

    # 自定义验证
    def validate_phone(self, field):
        phone_number = field.data
        user = UserModel.query.filter_by(phone_number=phone_number).first()
        if user:
            raise wtforms.ValidationError(message="该电话号码已被注册！")


class LoginForm(wtforms.Form):
    phone_number = wtforms.StringField('phone_number',
                                       validators=[DataRequired(message="电话号码必填"),
                                                   Regexp(r'^1[35789]\d{9}$', message="请输入11位手机号")])
    password = wtforms.StringField('password', validators=[Length(min=6, max=20, message="密码长度必须为6至20位")])


class ResetForm(wtforms.Form):
    password = wtforms.StringField('password', validators=[Length(min=6, max=20, message="密码长度必须为6至20位")])
    password_confirm = wtforms.StringField(validators=[EqualTo('password', message="两次密码不一致")])
