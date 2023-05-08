# _*_ coding : utf-8 _*_
# @Time : 2023/4/11 21:52
# @Author : sup1neCat
# @File : models
# @Project : tiebaOpinionAnalysis

from exts import db
from datetime import datetime


class PostCardModel(db.Model):
    __tablename__ = "postcard"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=True)
    link = db.Column(db.String(100), nullable=False, unique=True)
    publish_time = db.Column(db.Date, default=datetime.now)

    # 学校表外键
    school_id = db.Column(db.Integer, db.ForeignKey("school.id"))
    # 关系
    school = db.relationship("SchoolModel", backref="postcards")

    # 指数表外键
    index_id = db.Column(db.Integer, db.ForeignKey("index.id"))
    # 关系
    index = db.relationship("IndexModel", backref="postcards")


class SchoolModel(db.Model):
    __tablename__ = "school"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False, unique=True)


class IndexModel(db.Model):
    __tablename__ = "index"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text = db.Column(db.String(200), nullable=False, unique=True)
    sentiment_label = db.Column(db.Integer, nullable=False)
    sentiment_key = db.Column(db.String(100), nullable=False)
    positive_probs = db.Column(db.Float, nullable=False)
    negative_probs = db.Column(db.Float, nullable=False)


class UserModel(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    phone_number = db.Column(db.String(100), nullable=False, unique=True)
