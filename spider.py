# _*_ coding : utf-8 _*_
# @Time : 2023/4/13 11:20
# @Author : sup1neCat
# @File : spider
# @Project : tiebaOpinionAnalysis

"""爬取百度贴吧数据"""
import random
import time
import datetime
import json
import re
import requests
import pymysql
from lxml import etree

base_url = 'https://tieba.baidu.com/f?'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36",
    "Cookie": "BIDUPSID=59AC834DE8BB21496B0303D67C0266B7",
    "PSTM": "1615363394",
    "BDUSS": "lNvUVZ1S1VhVDZHOHpySEdac0dBQ0d0ZFowLXBMb2lYZU5LNmt5UVFJRjRodXRoRVFBQUFBJCQAAAAAAAAAAAEAAABHz0M-ZmF2b3JpdGXB1jEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHj5w2F4-cNhT",
    "BDUSS_BFESS": "lNvUVZ1S1VhVDZHOHpySEdac0dBQ0d0ZFowLXBMb2lYZU5LNmt5UVFJRjRodXRoRVFBQUFBJCQAAAAAAAAAAAEAAABHz0M-ZmF2b3JpdGXB1jEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHj5w2F4-cNhT",
    "BAIDUID": "202E839C006D869F7E9B5CBE10749486:FG=1",
    "STOKEN": "8ef93062f42c87ca7526d9e9fffd75e9b94b7a4702820df9cc3fdecdf2c3cf72",
    "BAIDUID_BFESS": "202E839C006D869F7E9B5CBE10749486:FG=1",
    "ZFY": "T:BBvs1aDVWeE9iGAaahLT2MfFy7k6SXGXCRHA2K4e1s:C",
    "FPTOKEN": "i1WTbb0dDRvilC+Uys7Ss9Vj9ZbVMuRIitpolojsokpDGh1LBCay7QUBGrJh88kpgB7rkY3md6pBiTmzcrXAu1yu5SImuvl0bP1PyIlfsqwPZ0cpypY4nfpw/JFAg+fb+bNuINpQY39Bu8EAn59UGxzqPH+jAnVcydf02vOdr56pxZEhfska6/T2a9ZfKDwQ1Qfih2EhyI6pkOztaz1dhM4ORQgTMngXhxB3OcjJ4vEe9W+NBpBubiFaVJBtC8rB1GDORRJ1dQpXwCJo9P+Md/wm+bdQ8utPHcyY9tLltBIxBLHeIPDUFlFIonSbw1DVGH1kGNOaUDusK1GWnLhvkh4FvtGGeWoEmYqQc7pXmy8CEOKqcRZAtA8uWIB4yulVTlHGzIWcyK/GOQhEXwLBIw==|yK2giIEWnvA1UUr2EZeOs5mR5My3SMcA94qhltneWps=|10|beba0343d0f9b89a80c167f2321cccdd",
    "BAIDU_WISE_UID": "wapp_1681747281957_783",
    "__bid_n": "18750d13386c8df7a34207",
    "arialoadData": "false",
    "H_PS_PSSID": "38516_36554_38470_38368_38468_38379_36803_38486_37933_37709_38356_26350_22159",
    "delPer": "0",
    "PSINO": "1",
    "USER_JUMP": "-1",
    "Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948": "1681524048,1681621232,1681746939,1681747574",
    "st_key_id": "17",
    "BDORZ": "B490B5EBF6F3CD402E515D22BCDA1598",
    "tb_as_data": "5d268e499fa22e86e5692d14876c12125e424364f78414c09aeea39ec88cd3f0ca6d53b99f6df2fd17145d4f7745dcd72e5b63bb056ae770a3f9a60031a3692920a18c1437e777194cf180103564f0b671c4aaad519bd053713236b0f93e3714ace5aae725c6f4919f1b978a81e74009",
    "wise_device": "0",
    "Hm_lpvt_98b9d8c2fd6608d564bf2ac2ae642948": "1681747997",
    "XFI": "c3975570-dd3a-11ed-937c-8fe1d4ec9493",
    "BA_HECTOR": "85a4a4210h2k842ga405004n1i3qs0u1n",
    "ab_sr": "1.0.1_NjkyODMxMzgwN2Y1ODE1OWMyMWQ5NGMxMThmZDQ4NzA4MTMwOGE4OWI2ZTVjZjNmNTI5MzI2ZDFiOTFhZTZhZGFlZmM5ZTUwNTU0OTVjOWVlMjE0YzU0ZjZlOWI1NjFiM2JiNzMwYWU3NmNiOWE0MTA4NWNlZDE5NTcyZmVjMTU1NDgzZjQ5NDVlM2Q0OTYyYjg0ODA0ZWJlY2UyZDYwZmVlNDFjOWRiMWQwMDJkMzdjYmYwYjA2N2MwN2ExZmJm",
    "st_data": "ab1bfb394200702f1185f03d3a0d19c18ec6b214a519257b5cea4d6a80d9c7d386212ed3b06e4f382ad9e5c12b3f6ff84df037605ef501184a6df264c048de52d6af5f952bfbc566924b8d918d0a73e22cd291f705402b89e21abc7b36e88339",
    "st_sign": "c4b2da69",
    "XFCS": "20993E8E111DFDEA42BCA429B2471A84E0AED5F5A08655995F681BD9E3EBFFB4",
    "XFT": "lc9ZtuEiicaodrtZiThIrsnhCBTMnEvRoMo3ugeOCik=",
    "RT": "\"z=1&dm=baidu.com&si=47a96041-5a09-4687-8c44-e1c841b9158f&ss=lgl0pd05&sl=2c&tt=2lb8&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=muit&ul=mzwq\""
}
data = {
    "ie": "utf-8",
    "kw": "四川农业大学",
    "fr": "search"
}


class TiebaSpider:

    data = data

    def __init__(self, tieba_name):
        self.tieba_name = tieba_name
        self.tieba_items = []
        # self.saver = open('./data/sau/sau_tieba_items.json', 'w', encoding='utf-8')

    def filter_emoji(self, desstr, restr=''):
        """过滤emoji表情"""
        res = re.compile(u'[\U00010000-\U0010ffff\uD800-\uDBFF\uDC00-\uDFFF]')
        return res.sub(restr, desstr)

    def get_time_convert(self, input_str):
        """格式化时间"""
        today = datetime.date.today()
        if '-' in input_str:
            if len(input_str) == 7:
                return datetime.datetime.strptime(input_str, '%Y-%m').strftime('%Y-%m')
            elif len(input_str) == 3 or 4:
                year = today.year
                return datetime.datetime.strptime(f'{year}-{input_str}', '%Y-%m-%d').strftime('%Y-%m-%d')
        elif ':' in input_str:
            return today.strftime('%Y-%m-%d')
        else:
            return input_str

    def get_html(self, url):
        """获取网页解析后的对象，并进行反反爬处理"""
        response = requests.get(url=url, params=data, headers=headers)
        try:
            response_txt = str(response.content, 'utf-8')
        except Exception as e:
            response_txt = str(response.content, 'gbk')
        bs64_str = re.findall(
            '<code class="pagelet_html" id="pagelet_html_frs-list/pagelet/thread_list" style="display:none;">[.\n\S\s]*?</code>',
            response_txt)

        bs64_str = ''.join(bs64_str).replace(
            '<code class="pagelet_html" id="pagelet_html_frs-list/pagelet/thread_list" style="display:none;"><!--', '')
        bs64_str = bs64_str.replace('--></code>', '')
        html = etree.HTML(bs64_str)
        return html

    def save_to_db(self, tieba_items):
        """保存到数据库"""
        db = pymysql.connect(host="localhost", user="root", password="root", database="tieba", charset='utf8mb4')
        cursor = db.cursor()
        school_name = self.tieba_name
        _sql = f"INSERT INTO school (name) VALUES ('{school_name}')"  # 插入学校名称
        try:
            cursor.execute(_sql)
            db.commit()
        except Exception as e:
            print(e)
            db.rollback()
        for tieba_item in tieba_items:
            sql = f"INSERT INTO postcard (title, content, link, author, publish_time, school_id) VALUES ('{tieba_item['title']}', '{tieba_item['content']}', '{tieba_item['link']}', '{tieba_item['creator']}', '{tieba_item['create_time']}', (SELECT id FROM school WHERE name = '{school_name}'))"
            try:
                cursor.execute(sql)
                db.commit()
            except Exception as e:
                print(e)
                db.rollback()
        db.close()

    def query_to_json(self, file_path):
        """查询数据库并保存为json格式"""
        db = pymysql.connect(host="localhost", user="root", password="root", database="tieba", charset='utf8mb4')
        cursor = db.cursor()
        school_name = self.tieba_name
        sql = f"SELECT * FROM postcard WHERE school_id = (SELECT id FROM school WHERE name = '{school_name}')"
        cursor.execute(sql)
        postcards = cursor.fetchall()
        db.close()
        postcard_list = []
        for postcard in postcards:
            postcard_dict = {'title': postcard[1], 'creator': postcard[2], 'content': postcard[3],
                             'create_time': str(postcard[4]), 'school': self.tieba_name, "link": postcard[6]}
            postcard_list.append(postcard_dict)
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(postcard_list, f, ensure_ascii=False)

    def spider_tieba_list(self, url):
        """爬虫主体函数"""
        html = self.get_html(url)
        # 标题列表
        title_list = html.xpath('//div[@class="threadlist_title pull_left j_th_tit "]/a[1]/@title')
        # 内容列表
        content_list = html.xpath('//div[@class="threadlist_abs threadlist_abs_onlyline "]/text()')
        # 链接列表
        link_list = html.xpath('//div[@class="threadlist_title pull_left j_th_tit "]/a[1]/@href')
        # 发帖人
        creator_list = html.xpath('//div[@class="threadlist_author pull_right"]/span[@class="tb_icon_author "]/@title')
        # 发帖时间
        create_time_list = html.xpath(
            '//div[@class="threadlist_author pull_right"]/span[@class="pull-right is_show_create_time"]/text()')

        for i in range(len(title_list)):
            item = dict()
            item['title'] = self.filter_emoji(title_list[i])
            comment_url = 'https://tieba.baidu.com' + link_list[i]
            item['create_time'] = create_time_list[i]
            if item['create_time'] == '广告':
                continue
            item['create_time'] = self.get_time_convert(item['create_time'])
            item['link'] = comment_url
            item['creator'] = self.filter_emoji(creator_list[i]).replace('主题作者: ', '')
            if len(content_list) > i:
                item['content'] = self.filter_emoji(content_list[i])
            else:
                item['content'] = ""
            item['school'] = self.tieba_name
            self.tieba_items.append(item)

        # 如果有下一页继续采集下一页
        next_page = html.xpath('//a[@class="next pagination-item "]/@href')
        if len(next_page) > 0:
            next_url = 'https:' + next_page[0]
            # 抓取 ** 条数据
            if float(next_url.split('=')[-1]) < 500:
                time.sleep(random.uniform(1, 5))
                self.spider_tieba_list(next_url)


if __name__ == '__main__':
    s = TiebaSpider(data.get('kw'))
    s.spider_tieba_list(base_url)
    # # 保存帖子数据
    # s.saver.write(json.dumps(s.tieba_items, ensure_ascii=False))
    # s.saver.flush()
    # 存入数据库
    s.save_to_db(s.tieba_items)
    s.query_to_json('./data/sau/sau_tieba_items.json')
