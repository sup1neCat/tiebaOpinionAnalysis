# _*_ coding : utf-8 _*_
# @Time : 2023/4/25 0:25
# @Author : sup1neCat
# @File : senta
# @Project : tiebaOpinionAnalysis
import paddlehub as hub
import pymysql
from functools import reduce
import operator


def unpack_tuple(my_tup):
    """解压元组"""
    return reduce(operator.add, my_tup)


def get_index():
    """从数据库中查询学校对应的帖子标题，并放入待分析数组中，将分析结果存入数据库"""
    db = pymysql.connect(host="localhost", user="root", password="root", database="tieba", charset='utf8mb4')
    cursor = db.cursor()
    school_name = input("请输入学校名称：")
    sql1 = f"select title from postcard where school_id = (SELECT id FROM school WHERE name = '{school_name}')"
    cursor.execute(sql1)
    texts = list(unpack_tuple(cursor.fetchall()))  # 将元组转换为列表
    senta = hub.Module(name="senta_bilstm")  # 情感分析模型
    input_dict = {"text": texts}  # 传入的是列表
    results = senta.sentiment_classify(data=input_dict)
    # 存入数据库
    for result in results:
        # print(result)
        sql2 = f"INSERT INTO `index` (text, sentiment_label, sentiment_key, positive_probs, negative_probs) VALUES ('{result['text']}','{result['sentiment_label']}', '{result['sentiment_key']}' ,'{result['positive_probs']}', '{result['negative_probs']}')"
        try:
            cursor.execute(sql2)
            db.commit()
        except Exception as e:
            print(e)
            db.rollback()

    sql3 = f"UPDATE postcard p JOIN `index` i ON i.text = p.title SET p.index_id = i.id WHERE p.school_id = (SELECT id FROM school WHERE name = '{school_name}')"
    try:
        cursor.execute(sql3)
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()
    db.close()


if __name__ == '__main__':
    get_index()
