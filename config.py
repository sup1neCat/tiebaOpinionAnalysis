# _*_ coding : utf-8 _*_
# @Time : 2023/4/11 16:57
# @Author : sup1neCat
# @File : config
# @Project : tiebaOpinionAnalysis

# cookie
SECRET_KEY = 'abcdefghijk'

# 数据库配置信息
HOSTNAME = "localhost"
PORT = 3306
DATABASE = "tieba"
USERNAME = "root"
PASSWORD = "root"
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI
