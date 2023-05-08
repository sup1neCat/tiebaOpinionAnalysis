# _*_ coding : utf-8 _*_
# @Time : 2023/4/20 19:37
# @Author : sup1neCat
# @File : data
# @Project : tiebaOpinionAnalysis
from decorators import login_required
from flask import Blueprint, render_template
from pyecharts import options as opts
from pyecharts.charts import Bar, Calendar, Pie, Line
from pyecharts.globals import ThemeType
from models import PostCardModel, SchoolModel
import textAnalysis

# /data
bp = Blueprint("data", __name__, url_prefix="/data")


@bp.route("/publish_time")
@login_required
def publish_time():
    return render_template("./publish_time.html")


@bp.route("/comments")
@login_required
def comments():
    return render_template("./comments.html")


def get_date_count(threads):
    thread_list = []
    for thread in threads:
        thread_list.append(str(thread.publish_time))
    result = {}
    for date in thread_list:
        if result.get(date) is None:
            result[date] = 1
        else:
            result[date] += 1
    return result


def get_bar(school, date):
    c = (
        Line(init_opts=opts.InitOpts(theme=ThemeType.WHITE))
        .add_xaxis(list(date.keys()))
        .add_yaxis("帖子数量", list(date.values()))
        .set_global_opts(
            xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-15)),
            title_opts=opts.TitleOpts(title=f"{school.name}吧上半年发帖数"),
            datazoom_opts=[opts.DataZoomOpts()],
            toolbox_opts=opts.ToolboxOpts(),
            legend_opts=opts.LegendOpts(is_show=False),
        )
    )
    return c.dump_options_with_quotes()


def get_calendar(school, data):
    c = (
        Calendar()
        .add(
            "",
            list(data.items()),
            calendar_opts=opts.CalendarOpts(
                range_="2023",
                daylabel_opts=opts.CalendarDayLabelOpts(name_map="cn"),
                monthlabel_opts=opts.CalendarMonthLabelOpts(name_map="cn"),
            ),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title=f"2023{school.name}吧发帖情况"),
            visualmap_opts=opts.VisualMapOpts(
                max_=50,
                min_=0,
                orient="horizontal",
                is_piecewise=True,
                pos_top="230px",
                pos_left="100px",
            ),
        )
    )
    return c.dump_options_with_quotes()


def get_comments_bar(school, res):
    res_k, res_v = zip(*res)  # zip(*)解压函数
    c = (
        Bar({"theme": ThemeType.WHITE})
        .add_xaxis(res_k)
        .add_yaxis("话题热度", res_v)
        .set_global_opts(
            xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-30)),
            title_opts=opts.TitleOpts(title=f"{school.name}吧话题排行"),
            toolbox_opts=opts.ToolboxOpts(),
            legend_opts=opts.LegendOpts(is_show=False),
        )
    )
    return c.dump_options_with_quotes()


def get_comments_pie(res):
    c = (
        Pie()
        .add(
            "话题",
            res,
            radius=["25%", "75%"],
            center=["40%", "50%"],
            rosetype="area",
            label_line_opts=opts.PieLabelLineOpts(smooth=True),
            label_opts=opts.LabelOpts(formatter='{b}:{d}%')
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="话题占比"),
            legend_opts=opts.LegendOpts(type_="scroll", pos_left="80%", orient="vertical")
        )
    )
    return c.dump_options_with_quotes()


@bp.route("/publish_time/bar/1")
def get_bar_cdut():
    threads = PostCardModel.query.filter_by(school_id=22).order_by(PostCardModel.publish_time.desc()).all()
    school = SchoolModel.query.filter_by(id=22).first()
    date = get_date_count(threads)
    return get_bar(school, date)


@bp.route("/publish_time/bar/2")
def get_bar_uestc():
    threads = PostCardModel.query.filter_by(school_id=21).order_by(PostCardModel.publish_time.desc()).all()
    school = SchoolModel.query.filter_by(id=21).first()
    date = get_date_count(threads)
    return get_bar(school, date)


@bp.route("/publish_time/bar/3")
def get_bar_scu():
    threads = PostCardModel.query.filter_by(school_id=23).order_by(PostCardModel.publish_time.desc()).all()
    school = SchoolModel.query.filter_by(id=23).first()
    date = get_date_count(threads)
    return get_bar(school, date)


@bp.route("/publish_time/bar/4")
def get_bar_swpu():
    threads = PostCardModel.query.filter_by(school_id=24).order_by(PostCardModel.publish_time.desc()).all()
    school = SchoolModel.query.filter_by(id=24).first()
    date = get_date_count(threads)
    return get_bar(school, date)


@bp.route("/publish_time/bar/5")
def get_bar_sau():
    threads = PostCardModel.query.filter_by(school_id=25).order_by(PostCardModel.publish_time.desc()).all()
    school = SchoolModel.query.filter_by(id=25).first()
    date = get_date_count(threads)
    return get_bar(school, date)


@bp.route("/publish_time/calendar/1")
def get_calendar_1():
    threads = PostCardModel.query.filter_by(school_id=22).order_by(PostCardModel.publish_time.desc()).all()
    school = SchoolModel.query.filter_by(id=22).first()
    data = get_date_count(threads)
    return get_calendar(school, data)


@bp.route("/publish_time/calendar/2")
def get_calendar_2():
    threads = PostCardModel.query.filter_by(school_id=21).order_by(PostCardModel.publish_time.desc()).all()
    school = SchoolModel.query.filter_by(id=21).first()
    data = get_date_count(threads)
    return get_calendar(school, data)


@bp.route("/publish_time/calendar/3")
def get_calendar_3():
    threads = PostCardModel.query.filter_by(school_id=23).order_by(PostCardModel.publish_time.desc()).all()
    school = SchoolModel.query.filter_by(id=23).first()
    data = get_date_count(threads)
    return get_calendar(school, data)


@bp.route("/publish_time/calendar/4")
def get_calendar_4():
    threads = PostCardModel.query.filter_by(school_id=24).order_by(PostCardModel.publish_time.desc()).all()
    school = SchoolModel.query.filter_by(id=24).first()
    data = get_date_count(threads)
    return get_calendar(school, data)


@bp.route("/publish_time/calendar/5")
def get_calendar_5():
    threads = PostCardModel.query.filter_by(school_id=25).order_by(PostCardModel.publish_time.desc()).all()
    school = SchoolModel.query.filter_by(id=25).first()
    data = get_date_count(threads)
    return get_calendar(school, data)


@bp.route("/comments/bar/1")
def get_comments_bar_1():
    school = SchoolModel.query.filter_by(id=22).first()
    res = textAnalysis.word_frequency('./data/cdut/text_filter.txt', 30)
    return get_comments_bar(school, res)


@bp.route("/comments/bar/2")
def get_comments_bar_2():
    school = SchoolModel.query.filter_by(id=21).first()
    res = textAnalysis.word_frequency('./data/uestc/text_filter.txt', 30)
    return get_comments_bar(school, res)


@bp.route("/comments/bar/3")
def get_comments_bar_3():
    school = SchoolModel.query.filter_by(id=23).first()
    res = textAnalysis.word_frequency('./data/scu/text_filter.txt', 30)
    return get_comments_bar(school, res)


@bp.route("/comments/bar/4")
def get_comments_bar_4():
    school = SchoolModel.query.filter_by(id=24).first()
    res = textAnalysis.word_frequency('./data/swpu/text_filter.txt', 30)
    return get_comments_bar(school, res)


@bp.route("/comments/bar/5")
def get_comments_bar_5():
    school = SchoolModel.query.filter_by(id=25).first()
    res = textAnalysis.word_frequency('./data/sau/text_filter.txt', 30)
    return get_comments_bar(school, res)


@bp.route("/comments/pie/1")
def get_comments_pie_1():
    res = textAnalysis.word_frequency('./data/cdut/text_filter.txt', 30)
    return get_comments_pie(res)


@bp.route("/comments/pie/2")
def get_comments_pie_2():
    res = textAnalysis.word_frequency('./data/uestc/text_filter.txt', 30)
    return get_comments_pie(res)


@bp.route("/comments/pie/3")
def get_comments_pie_3():
    res = textAnalysis.word_frequency('./data/scu/text_filter.txt', 30)
    return get_comments_pie(res)


@bp.route("/comments/pie/4")
def get_comments_pie_4():
    res = textAnalysis.word_frequency('./data/swpu/text_filter.txt', 30)
    return get_comments_pie(res)


@bp.route("/comments/pie/5")
def get_comments_pie_5():
    res = textAnalysis.word_frequency('./data/sau/text_filter.txt', 30)
    return get_comments_pie(res)
