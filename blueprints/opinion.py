# _*_ coding : utf-8 _*_
# @Time : 2023/4/20 19:38
# @Author : sup1neCat
# @File : opinion
# @Project : tiebaOpinionAnalysis
from flask import Blueprint, render_template
from decorators import login_required
from models import PostCardModel
from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.faker import Faker

from collections import Counter

# /opinion
bp = Blueprint("opinion", __name__, url_prefix="/opinion")


def get_pie(school, res):
    c = (
        Pie()
        .add(
            f"{school}",
            res,
        )
        .set_colors(['red', 'green'])
        .set_global_opts(title_opts=opts.TitleOpts(title="舆情分析占比"))
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {d}%({c})"))
    )
    return c.dump_options_with_quotes()


@bp.route("/")
@login_required
def index():
    threads_1 = PostCardModel.query.filter_by(school_id=22).order_by(PostCardModel.publish_time.desc()).all()
    threads_2 = PostCardModel.query.filter_by(school_id=21).order_by(PostCardModel.publish_time.desc()).all()
    threads_3 = PostCardModel.query.filter_by(school_id=23).order_by(PostCardModel.publish_time.desc()).all()
    threads_4 = PostCardModel.query.filter_by(school_id=24).order_by(PostCardModel.publish_time.desc()).all()
    threads_5 = PostCardModel.query.filter_by(school_id=25).order_by(PostCardModel.publish_time.desc()).all()

    return render_template("./opinion.html",
                           threads_1=threads_1,
                           threads_2=threads_2,
                           threads_3=threads_3,
                           threads_4=threads_4,
                           threads_5=threads_5,
                           )


@bp.route("/pie/1")
def get_pie_1():
    school_name = PostCardModel.query.filter_by(school_id=22).first().school.name
    threads = PostCardModel.query.filter_by(school_id=22)
    index_list = []
    for t in threads:
        index_list.append(t.index.sentiment_key)
    res = Counter(index_list).most_common(2)
    return get_pie(school_name, res)


@bp.route("/pie/2")
def get_pie_2():
    school_name = PostCardModel.query.filter_by(school_id=21).first().school.name
    threads = PostCardModel.query.filter_by(school_id=21)
    index_list = []
    for t in threads:
        index_list.append(t.index.sentiment_key)
    res = Counter(index_list).most_common(2)
    return get_pie(school_name, res)


@bp.route("/pie/3")
def get_pie_3():
    school_name = PostCardModel.query.filter_by(school_id=23).first().school.name
    threads = PostCardModel.query.filter_by(school_id=23)
    index_list = []
    for t in threads:
        index_list.append(t.index.sentiment_key)
    res = Counter(index_list).most_common(2)
    return get_pie(school_name, res)


@bp.route("/pie/4")
def get_pie_4():
    school_name = PostCardModel.query.filter_by(school_id=24).first().school.name
    threads = PostCardModel.query.filter_by(school_id=24)
    index_list = []
    for t in threads:
        index_list.append(t.index.sentiment_key)
    res = Counter(index_list).most_common(2)
    return get_pie(school_name, res)


@bp.route("/pie/5")
def get_pie_5():
    school_name = PostCardModel.query.filter_by(school_id=25).first().school.name
    threads = PostCardModel.query.filter_by(school_id=25)
    index_list = []
    for t in threads:
        index_list.append(t.index.sentiment_key)
    res = Counter(index_list).most_common(2)
    return get_pie(school_name, res)
