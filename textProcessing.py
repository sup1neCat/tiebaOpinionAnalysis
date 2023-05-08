# _*_ coding : utf-8 _*_
# @Time : 2023/4/17 18:17
# @Author : sup1neCat
# @File : textProcessing
# @Project : tiebaOpinionAnalysis

"""文本数据清洗"""
import codecs
import json
import jieba
import pymysql


# def query_to_json(file_path):
#     """查询数据库并保存为json格式(未完善)"""
#     db = pymysql.connect(host="localhost", user="root", password="root", database="tieba", charset='utf8mb4')
#     cursor = db.cursor()
#     sql = "SELECT * FROM postcard,school WHERE postcard.school_id = school.name"
#     cursor.execute(sql)
#     postcards = cursor.fetchall()
#     postcard_list = []
#     for postcard in postcards:
#         postcard_dict = {'title': postcard[1], 'creator': postcard[2], 'content': postcard[3],
#                          'create_time': str(postcard[4]), 'school': "电子科技大学", "link": postcard[6]}
#         postcard_list.append(postcard_dict)
#     with open(file_path, 'w', encoding='utf-8') as f:
#         json.dump(postcard_list, f, ensure_ascii=False)


def write_value_to_txt(file_name, value1, value2, output_file):
    """将指定json文件中指定的key对应的value按行写入txt文本中"""
    with open(file_name, encoding='utf-8') as f:
        setting = json.load(f)
    with open(output_file, 'w', encoding='utf-8') as f:
        for item in setting:
            item_value1 = str(item[value1]).strip()
            item_value2 = str(item[value2]).strip()
            if item_value1 != '' and item_value2 != '':
                f.write(item_value1 + '\n')
                f.write(item_value2 + '\n')


def filter_text(file_name, output_file):
    """对文本进行清洗"""

    # 构建停用词表
    with open('./data/stopwords.txt', 'r', encoding='utf-8') as f:
        stopwords = [word.strip('\n') for word in f.readlines()]

    source = open(file_name, 'r', encoding='utf-8')
    result = codecs.open(output_file, 'w', 'utf-8')
    line = source.readline().rstrip('\n')
    content = []  # 完整文本

    while line != "":
        seg_list = jieba.cut(line, cut_all=False)  # 精确模式
        final = []  # 存储去除停用词内容
        for seg in seg_list:
            if seg not in stopwords:
                final.append(seg)
        output = ' '.join(list(final))  # 空格拼接
        # print(output)
        content.append(output)
        result.write(output + '\r\n')
        line = source.readline().rstrip('\n')
    else:
        source.close()
        result.close()


if __name__ == '__main__':
    write_value_to_txt('./data/swpu/swpu_tieba_items.json', 'title', 'content',
                       './data/swpu/text.txt')
    filter_text('./data/swpu/text.txt', './data/swpu/text_filter.txt')
