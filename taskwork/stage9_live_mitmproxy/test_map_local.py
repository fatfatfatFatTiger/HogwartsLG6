# -*- coding: utf-8 -*-
# @File : test_map_local.py
# @Author : Elf
# @Time : 2021/3/21 15:33


import json


class Counter:
    def __init__(self):
        self.num = 0

    def response(self, flow):
        first_stock_symbol = "SZ000651"
        second_stock_symbol = "SH600036"
        third_stock_symbol = "SZ002475"
        # 判断是否是想要的请求信息，通过url进行判断
        # 此处相同的请求有两个，新增判断条件，只筛选股票的接口，不筛选包含大盘的接口
        if ("https://stock.xueqiu.com/v5/stock/batch/quote.json?_t" in flow.request.pretty_url) \
                and ((first_stock_symbol in flow.request.pretty_url)
                     or (second_stock_symbol in flow.request.pretty_url)
                     or (third_stock_symbol in flow.request.pretty_url)):

            # 打开文件，读取文件数据，作为响应，给返回
            with open("map_local.json", encoding="utf-8") as f:
                data = json.load(f)
            # 赋值给响应信息
            flow.response.text = json.dumps(data)


addons = [
    Counter()
]


