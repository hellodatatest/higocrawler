# -*- coding:utf-8 -*-

__auth__ = 'liuzhuang'
__date__ = '20151117'

import json
import logging
import re
import time
import requests
from lxml import etree

LOGGING_FILE = 'higo_crawler.log'
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s %(message)s',
    filename=LOGGING_FILE,
    filemode='a+'
)

_cookies = {'JSESSIONID': '849B6F45BFDA7BE669E501987C5A0652'}

HIGO_URL = "http://www.higo-express.cn/toHigoTraking.action?waybillID={0}"
PACKAGE_NO_URL = "http://www.higo-express.cn/queryExpress.action?pageNumber={0}&pageSize={1}"


def get_cookies():
    post_data = {"userNO": "", "password": ""}
    try:
        r = requests.post("http://www.higo-express.cn/login.action", post_data)
        cookies = requests.utils.dict_from_cookiejar(r.cookies)
        logging.debug("get cookies success.")
        return cookies
    except Exception, e:
        logging.error("get cookies error. error: {0}", e)
        return ""


def get_html(url, cookies, headers):
    times = 0
    logging.debug('request to href: {0}'.format(url))
    while times < 3:
        try:
            r = requests.post(url=url, cookies=cookies, headers=headers, timeout=20)
            return r.text
        except Exception, e:
            times += 1
            logging.error('{0} requests error:{1}: {2}, try_times: {3}'.format(url, Exception, e, times))
    logging.debug("{0} response is none".format(url))
    return ""


def html_fragment_slim(html_fragment):
    html_fragment = re.sub(r"<br />", "", html_fragment)
    html_fragment = re.sub(r"\r|\t|\n", "", html_fragment)
    html_fragment = re.sub(r" ", "", html_fragment)
    return html_fragment


def get_express_detail(cookies, package_no):
    express_detail = []

    url = HIGO_URL.format(package_no)
    text = get_html(url, cookies, headers="")
    if not text:
        return ""

    page = etree.HTML(text)
    nodes = page.xpath("//div[@id='info']/div[@class='_content']/text()")
    for fragment in nodes:
        html_fragment = html_fragment_slim(fragment)
        res = html_fragment.encode("utf-8").strip()
        express_detail.append(res)

    return "&".join(express_detail)


def get_package_no(cookies, page_no, page_size):
    package_no_dic = {}

    url = PACKAGE_NO_URL.format(page_no, page_size)
    text = get_html(url, cookies, headers="")
    if not text:
        return ""

    page = etree.HTML(text)
    nodes = page.xpath("//form[@id='ff0']/table[@id='dg']/tbody/tr")
    for node in nodes:
        id = node.xpath("./td[1]/text()")
        package_no = node.xpath("./td[2]/label/a/text()")
        if len(package_no) == 0 or len(id) == 0:
            continue

        package_no = html_fragment_slim(package_no[0])
        id = id[0]

        if not package_no:
            logging.debug("the package no is none or id is none")
            continue

        if isinstance(package_no, unicode):
            package_no = package_no.encode("utf-8")
        if isinstance(id, unicode):
            id = id.encode("utf-8")

        package_no_dic[int(id)] = int(package_no)
        # status = node.xpath("./td[14]/a/label/text()")
        # status_code = node.xpath("./td[14]/a/@onclick")

        # status_note = html_fragment_slim(status[0])
        # status_code = status_code[0].split(",")[2]
    return package_no_dic


def process(page_no, page_size):
    cookies = get_cookies()
    if not cookies:
        cookies = _cookies
    package_no_dic = get_package_no(cookies, page_no, page_size)
    if not package_no_dic:
        logging.debug("get the package no is none.")
        return

    package_no_list = sorted(package_no_dic.items(), key=lambda d: d[0], reverse=True)

    express_detail_list = []
    for each in package_no_list:

        id = each[0]
        package_no = each[1]

        express_detail = get_express_detail(cookies, package_no)
        if not express_detail:
            continue
        express_detail_list.append({"package_no": package_no, "express_detail": express_detail})
        time.sleep(1)
    return express_detail_list


