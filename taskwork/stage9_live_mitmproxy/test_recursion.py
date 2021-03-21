# -*- coding: utf-8 -*-
# @File : test_recursion.py
# @Author : Elf
# @Time : 2021/3/21 17:06

import json
from mitmproxy import http
import sys
from mitmproxy.tools._main import mitmdump


class Counter:
    def __init__(self):
        self.num = 0

    def response(self, flow: http.HTTPFlow):
        first_stock_symbol = "SZ000651"
        second_stock_symbol = "SH600036"
        third_stock_symbol = "SZ002475"

        # 判断是否是想要的请求信息，通过url进行判断
        # 此处相同的请求有两个，新增判断条件，只筛选股票的接口，不筛选包含大盘的接口
        if ("https://stock.xueqiu.com/v5/stock/batch/quote.json?_t" in flow.request.pretty_url) \
                and ((first_stock_symbol in flow.request.pretty_url)
                     or (second_stock_symbol in flow.request.pretty_url)
                     or (third_stock_symbol in flow.request.pretty_url)):
            # 获取响应结果
            data = json.loads(flow.response.text)
            # 将结果递归，批量处理后返回；返回结果不接收Python类型，只接收字符串
            flow.response.text = json.dumps(self.json_travel(data))

    def json_travel(self, response_data):
        first_stock_symbol = "SZ000651"
        second_stock_symbol = "SH600036"
        third_stock_symbol = "SZ002475"
        # 判断传入的数据类型
        if isinstance(response_data, dict):  # {"a":{"b":{"c":1}}}
            # 当字典格式，递归value值
            for key, value in response_data.items():
                if key == "quote":
                    if response_data[key]["symbol"] == second_stock_symbol:
                        response_data[key]["name"] = response_data[key]["name"] * 2
                    elif response_data[key]["symbol"] == third_stock_symbol:
                        response_data[key]["name"] = ""
                # 字典key值不可变，肯定不是可迭代对象，不停往下遍历value值
                response_data[key] = self.json_travel(value)
        elif isinstance(response_data, list):  # [[1, 2, 3], [1, 4, 7]]
            # 当数据类型为 list 的时候，添加到结构内，并继续递归遍历，直到数据类型不为可迭代对象
            # 列表推导式
            response_data = [self.json_travel(value) for value in response_data]
        elif isinstance(response_data, bool):
            # 如果原json文件中的值是bool类型，则保持原类型，否则会识别为1
            response_data = response_data
        elif isinstance(response_data, int) or isinstance(response_data, float):
            response_data = response_data
        elif isinstance(response_data, str):
            response_data = response_data
        else:
            response_data = response_data

        return response_data


addons = [
    Counter()
]


if __name__ == '__main__':
    sys.argv = [__file__, "-p 8889", "-s", __file__]
    # 官方要求必须主线程
    mitmdump()

