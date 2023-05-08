# _*_ coding : utf-8 _*_
# @Time : 2023/4/20 19:37
# @Author : sup1neCat
# @File : words
# @Project : tiebaOpinionAnalysis
from flask import Blueprint, render_template
from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.faker import Faker
import textAnalysis

from decorators import login_required

# /words
bp = Blueprint("words", __name__, url_prefix="/words")


@bp.route("/")
@login_required
def index():
    return render_template("./words.html")


def get_tfpie(k, v):
    c = (
        Pie()
        .add(
            "关键词",
            [list(z) for z in zip(k, v)],
            radius=["20%", "95%"],
            center=["50%", "50%"],
            rosetype="radius",
            label_opts=opts.LabelOpts(is_show=False),
            label_line_opts=opts.PieLabelLineOpts(is_show=False),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="TF-IDF关键词抽取"),
        )
    )
    return c.dump_options_with_quotes()


def get_trpie(k, v):
    c = (
        Pie()
        .add(
            "关键词",
            [list(z) for z in zip(k, v)],
            radius=["20%", "95%"],
            center=["50%", "50%"],
            rosetype="radius",
            label_opts=opts.LabelOpts(is_show=False),
            label_line_opts=opts.PieLabelLineOpts(is_show=False),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Textrank关键词抽取"),
        )
    )
    return c.dump_options_with_quotes()


@bp.route("/tfpie/1")
def get_tfpie_1():
    w_k_list, w_v_list = textAnalysis.get_tfidf('./data/cdut/text.txt')
    return get_tfpie(w_k_list, w_v_list)


@bp.route("/tfpie/2")
def get_tfpie_2():
    w_k_list, w_v_list = textAnalysis.get_tfidf('./data/uestc/text.txt')
    return get_tfpie(w_k_list, w_v_list)


@bp.route("/tfpie/3")
def get_tfpie_3():
    w_k_list, w_v_list = textAnalysis.get_tfidf('./data/scu/text.txt')
    return get_tfpie(w_k_list, w_v_list)


@bp.route("/tfpie/4")
def get_tfpie_4():
    w_k_list, w_v_list = textAnalysis.get_tfidf('./data/swpu/text.txt')
    return get_tfpie(w_k_list, w_v_list)


@bp.route("/tfpie/5")
def get_tfpie_5():
    w_k_list, w_v_list = textAnalysis.get_tfidf('./data/sau/text.txt')
    return get_tfpie(w_k_list, w_v_list)


@bp.route("/trpie/1")
def get_trpie_1():
    w_k_list, w_v_list = textAnalysis.get_textrank('./data/cdut/text.txt')
    return get_trpie(w_k_list, w_v_list)


@bp.route("/trpie/2")
def get_trpie_2():
    w_k_list, w_v_list = textAnalysis.get_textrank('./data/uestc/text.txt')
    return get_trpie(w_k_list, w_v_list)


@bp.route("/trpie/3")
def get_trpie_3():
    w_k_list, w_v_list = textAnalysis.get_textrank('./data/scu/text.txt')
    return get_trpie(w_k_list, w_v_list)


@bp.route("/trpie/4")
def get_trpie_4():
    w_k_list, w_v_list = textAnalysis.get_textrank('./data/swpu/text.txt')
    return get_trpie(w_k_list, w_v_list)


@bp.route("/trpie/5")
def get_trpie_5():
    w_k_list, w_v_list = textAnalysis.get_textrank('./data/sau/text.txt')
    return get_trpie(w_k_list, w_v_list)
