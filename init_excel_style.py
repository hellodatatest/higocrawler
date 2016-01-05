# -*- coding:utf-8 -*-

__auth__ = 'liuzhuang'
__date__ = '20151118'

import xlwt

def get_excel_style():
    # 有边框
    borders = xlwt.Borders()
    borders.left = 1
    borders.right = 1
    borders.top = 1
    borders.bottom = 1

    # 头 标题 加粗 居中
    head_style = xlwt.XFStyle()
    head_alig = xlwt.Alignment()
    head_alig.horz = xlwt.Alignment.HORZ_CENTER
    head_font = xlwt.Font()
    head_font.name = u'微软雅黑'
    #head_font.bold = True
    head_font.height = 300
    head_style.alignment = head_alig
    head_style.font = head_font

    # 设置 通用 格式
    general_style = xlwt.XFStyle()
    general_alig = xlwt.Alignment()
    general_alig.horz = xlwt.Alignment.HORZ_CENTER
    general_alig.vert = xlwt.Alignment.VERT_CENTER
    general_font = xlwt.Font()
    general_font.name = u'微软雅黑'
    general_font.height = 200
    general_style.font = general_font
    general_style.alignment = general_alig
    #general_style.borders = borders
    general_style.num_format_str = '0'
    #general_style.alignment = 'warp on'

    general_style2 = xlwt.XFStyle()
    general_alig2 = xlwt.Alignment()
    general_alig2.vert = xlwt.Alignment.VERT_CENTER
    general_alig2.wrap = True
    general_font = xlwt.Font()
    general_font.name = u'微软雅黑'
    general_font.height = 200
    general_style2.font = general_font
    general_style2.alignment = general_alig2
    #general_style2.borders = borders
    general_style2.num_format_str = '0'

    # 浮点型数据样式
    digital_style = xlwt.XFStyle()
    digital_font = xlwt.Font()
    digital_font.name = u'微软雅黑'
    digital_font.height = 200
    digital_style.font = general_font
    digital_style.borders = borders
    digital_style.num_format_str = '0.0000'

    #百分数格式
    percent_style = xlwt.XFStyle()
    percent_alig = xlwt.Alignment()
    percent_alig.horz = xlwt.Alignment.HORZ_CENTER
    percent_font = xlwt.Font()
    percent_font.name = u'微软雅黑'
    percent_font.height = 200
    percent_style.font = general_font
    percent_style.borders = borders
    percent_style.alignment = percent_alig
    percent_style.num_format_str = '0.00%'

    # 设置 加粗 格式
    bold_style = xlwt.XFStyle()
    bold_style.borders = borders
    bold_font = xlwt.Font()
    bold_font.name = u'微软雅黑'
    bold_font.bold = True
    bold_style.font = bold_font
    bold_style.alignment = head_alig

    # 设置 日期 格式
    date_style = xlwt.XFStyle()
    date_style.num_format_str = 'YYYY-MM-DD hh:mm:ss'
    date_style.borders = borders
    date_alig = xlwt.Alignment()
    date_alig.horz = xlwt.Alignment.HORZ_CENTER
    date_font = xlwt.Font()
    date_font.name = u'微软雅黑'
    date_font.height = 200
    date_style.font = date_font
    date_style.alignment = date_alig

    # 设置 货币 格式
    currency_style = xlwt.XFStyle()
    currency_style.num_format_str = '0.00'
    currency_style.borders = borders


    simple_style = xlwt.XFStyle()
    simple_style.font = general_font
    simple_style.num_format_str = '0'

    excel_style = {'head_style': head_style, 'general_style': general_style, 'date_style': date_style,
                 'currency_style': currency_style, 'bold_style': bold_style, 'digital_style': digital_style,
                 'percent_style': percent_style, 'simple_style': simple_style, "general_style2": general_style2}

    return excel_style

