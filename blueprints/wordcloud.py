# _*_ coding : utf-8 _*_
# @Time : 2023/4/20 19:37
# @Author : sup1neCat
# @File : wordcloud
# @Project : tiebaOpinionAnalysis
from flask import Blueprint, render_template
from pyecharts.charts import WordCloud
from pyecharts import options as opts

import textAnalysis
from decorators import login_required

# /words
bp = Blueprint("wordcloud", __name__, url_prefix="/wordcloud")


@bp.route("/")
@login_required
def index():
    return render_template("./wordcloud.html")


def get_wordcloud(res):
    c = (
        WordCloud()
        .add(
            "关键词",
            res,
            word_size_range=[20, 100],
            textstyle_opts=opts.TextStyleOpts(font_family="monospace"),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="热词展示"),
        )
    )
    return c.dump_options_with_quotes()


@bp.route("/1")
def get_wordcloud_1():
    res = textAnalysis.word_frequency('./data/cdut/text_filter.txt', 100)
    return get_wordcloud(res)


@bp.route("/2")
def get_wordcloud_2():
    res = textAnalysis.word_frequency('./data/uestc/text_filter.txt', 100)
    return get_wordcloud(res)


@bp.route("/3")
def get_wordcloud_3():
    res = textAnalysis.word_frequency('./data/scu/text_filter.txt', 100)
    return get_wordcloud(res)


@bp.route("/4")
def get_wordcloud_4():
    res = textAnalysis.word_frequency('./data/swpu/text_filter.txt', 100)
    return get_wordcloud(res)


@bp.route("/5")
def get_wordcloud_5():
    res = textAnalysis.word_frequency('./data/sau/text_filter.txt', 100)
    return get_wordcloud(res)
