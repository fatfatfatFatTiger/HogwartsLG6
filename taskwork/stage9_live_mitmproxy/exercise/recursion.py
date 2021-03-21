# -*- coding: utf-8 -*-
# @File : test_recursor.py
# @Author : Elf
# @Time : 2021/3/21 15:42

import json
import os


def json_travel(response_data):
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
            response_data[key] = json_travel(value)
    elif isinstance(response_data, list):  # [[1, 2, 3], [1, 4, 7]]
        # 当数据类型为 list 的时候，添加到结构内，并继续递归遍历，直到数据类型不为可迭代对象
        # 列表推导式
        response_data = [json_travel(value) for value in response_data]
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


if __name__ == '__main__':
    file_path = os.path.realpath(__file__)
    folder_path = os.path.dirname(file_path)
    old_json_path = os.path.join(folder_path, "recursion.json")
    new_json_path = os.path.join(folder_path, "recursion_new.json")
    # print(old_json_path, new_json_path)
    data = json.load(open(old_json_path, encoding="utf-8"))
    new_data = json_travel(data)
    with open(new_json_path, "w", encoding="utf-8") as f:
        # 缩进等于2，不进行ASCII编码
        json.dump(new_data, fp=f, indent=2, ensure_ascii=False)


