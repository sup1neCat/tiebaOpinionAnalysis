from collections import Counter

from flask import Blueprint, render_template
from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.faker import Faker

from models import PostCardModel

bp = Blueprint("index", __name__, url_prefix="/")


@bp.route("/")
def index():
    threads = PostCardModel.query.order_by(PostCardModel.publish_time.desc()).limit(500)
    return render_template("./index.html", threads=threads)


@bp.route("/pie")
def get_pie():
    school_list = []
    thread_list = []
    for i in range(21, 26):
        school_name = PostCardModel.query.filter_by(school_id=i).first().school.name
        threads = PostCardModel.query.filter_by(school_id=i).all()
        school_list.append(school_name)
        thread_list.append(len(threads))
    # print(school_list, thread_list)
    c = (
        Pie()
        .add(
            series_name="高校名称",
            data_pair=[list(z) for z in zip(school_list, thread_list)],
            radius=["40%", "55%"],
            label_opts=opts.LabelOpts(
                position="outside",
                formatter="{a|{a}}{abg|}\n{hr|}\n {b|{b}: }{c}  {per|{d}%}  ",
                background_color="#eee",
                border_color="#aaa",
                border_width=1,
                border_radius=4,
                rich={
                    "a": {"color": "#999", "lineHeight": 22, "align": "center"},
                    "abg": {
                        "backgroundColor": "#e3e3e3",
                        "width": "100%",
                        "align": "right",
                        "height": 22,
                        "borderRadius": [4, 4, 0, 0],
                    },
                    "hr": {
                        "borderColor": "#aaa",
                        "width": "100%",
                        "borderWidth": 0.5,
                        "height": 0,
                    },
                    "b": {"fontSize": 16, "lineHeight": 33},
                    "per": {
                        "color": "#eee",
                        "backgroundColor": "#334455",
                        "padding": [2, 4],
                        "borderRadius": 2,
                    },
                },
            ),
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="2023年四川各高校发帖量占比"))
    )
    return c.dump_options_with_quotes()
