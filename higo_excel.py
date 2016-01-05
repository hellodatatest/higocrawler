# -*- coding:utf-8 -*-

__auth__ = 'liuzhuang'
__date__ = '20151118'

import time
import xlwt
import datetime
from higo_crawler import process
from init_excel_style import get_excel_style

def write_sheet(oneday, result, title, sheet, book, excel_style):
    _lst = [[u'运单编号', u'快递详情']]
    _lst.extend([x['package_no'], x['express_detail']] for i, x in enumerate(result))

    top_offset = 2  # !!!! 头信息 写入偏移量 !!!!
    sheet.write_merge(0, 0, 0, len(_lst[0])-1, u'{0} {1}'.format(title, oneday), excel_style['head_style'])

    for row, line in enumerate(_lst):
        row += top_offset
        for col, data in enumerate(line):
            sheet.col(1).width = 30000
            sheet.col(0).width = 5000
            if row > top_offset and col == 0:
                sheet.write(row, col, data, excel_style['general_style'])
            elif row == top_offset:
                sheet.write(row, col, data, excel_style['bold_style'])
            else:
                sheet.write(row, col, data, excel_style['general_style2'])

    book.save(u"""黑狗物流爬虫{0}.xls""".format(oneday))


def get_excel():
    oneday = datetime.datetime.strftime(datetime.date.today(),  "%Y%m%d")
    page_size = 1000
    book = xlwt.Workbook(encoding="utf-8")
    for page_no in range(1, 5):
        result = process(page_no, page_size)
        title = u"黑狗爬虫"
        sheet = book.add_sheet(u"黑狗爬虫 第{0}页".format(page_no))
        excel_style = get_excel_style()

        write_sheet(oneday, result, title, sheet, book, excel_style)
        time.sleep(2)

get_excel()