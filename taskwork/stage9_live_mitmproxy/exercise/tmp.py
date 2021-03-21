# -*- coding: utf-8 -*-
# @File : ttt.py
# @Author : Elf
# @Time : 2021/3/21 16:30
import json
import os


def tes_aa():
    file_path = os.path.realpath(__file__)
    folder_path = os.path.dirname(file_path)
    json_path = os.path.join(folder_path, "recursion.json")

    with open(json_path, "r", encoding="utf-8") as f:
        filedata = json.load(f)
    # print(filedata)
    data = filedata["data"]
    # print(data)
    items = data["items"]
    # print(items)
    for item in items:
        # print(item)
        market = item["market"]
        # print(market)
        quote = item["quote"]
        print(quote["name"])


if __name__ == '__main__':
    tes_aa()
