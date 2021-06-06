# -*- coding: utf-8 -*-
# @File : test_.py
# @Author : Elf
# @Time : 2021/3/21 11:58

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
            # 获取的text是str类型，如果要对数据进行操作，需要进行数据转换
            data = json.loads(flow.response.text)
            first_stock_name = data["data"]["items"][0]["quote"]["name"]
            second_stock_name = data["data"]["items"][1]["quote"]["name"]
            third_stock_name = data["data"]["items"][2]["quote"]["name"]

            # 修改原始数据
            data["data"]["items"][1]["quote"]["name"] = second_stock_name * 2
            data["data"]["items"][2]["quote"]["name"] = ""
            # 赋值给响应信息
            flow.response.text = json.dumps(data)


addons = [
    Counter()
]


