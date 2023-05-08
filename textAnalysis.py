# _*_ coding : utf-8 _*_
# @Time : 2023/4/18 18:19
# @Author : sup1neCat
# @File : textAnalysis
# @Project : tiebaOpinionAnalysis

"""文本数据分析"""

import textProcessing
import re
import jieba.analyse
from collections import Counter

stopwords = {"rt", "成都", "理工", "工大", "理工大", "理工大学", "大学", "成理", "没有", "有没有", "学校", "真的",
             "感觉", "西南", "石油大学", "石油", "四川", "四川大学", "川大", "电子", "电子科技", "电子科大", "电子科",
             "科技", "成电", "川农", "农业", "农业大学", "农大", "业大", "女生", "男生", "学生", "学院", "学长",
             "学姐", "学弟", "学妹", "老师", "同学", "教授"}


def word_frequency(file_name, num):
    """统计词频"""
    with open(file_name, "r", encoding='utf-8') as f:
        s = f.read()
        f.close()
    s = re.sub(r'[\W]', '', s)
    word_list = jieba.lcut(s)
    new_word_list = []
    for word in word_list:
        if word not in stopwords and len(word) > 1:
            new_word_list.append(word)
    res = Counter(new_word_list).most_common(num)
    return res


def get_tfidf(file_path):
    """得到tfidf分词结果"""
    f = open(file_path, 'r', encoding='utf-8').readlines(5000)
    w_k_list = []
    w_v_list = []
    for w in f:
        w_list = jieba.analyse.extract_tags(topK=5, sentence=w, withWeight=True, allowPOS=('vn', 'n'))
        if not w_list:  # w_list为空
            pass
        else:
            w_k, w_v = zip(*w_list)
            w_k_list.append(w_k)
            w_v_list.append(w_v)
    # print([list(z) for z in zip(w_k_list, w_v_list)])
    return w_k_list, w_v_list


def get_textrank(file_path):
    """得到textrank分词结果"""
    f = open(file_path, 'r', encoding='utf-8').readlines(5000)
    w_k_list = []
    w_v_list = []
    for w in f:
        # w_list = jieba.analyse.extract_tags(topK=10, sentence=w, withWeight=True, allowPOS=('vn', 'n'))
        w_list = jieba.analyse.textrank(topK=5, sentence=w, withWeight=True, allowPOS=('vn', 'n'))
        if not w_list:  # w_list为空
            pass
        else:
            w_k, w_v = zip(*w_list)
            w_k_list.append(w_k)
            w_v_list.append(w_v)
    # print(w_k_list, w_v_list)
    return w_k_list, w_v_list


if __name__ == '__main__':
    get_tfidf('./data/cdut/text.txt')
