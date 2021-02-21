# -*- coding: utf-8 -*-

import pytest
import yaml
from HogwartsLG6.taskwork.stage4_live_pytest.common.calc import Calculator


@pytest.fixture(scope="module")
def get_calc1():
    print("获取计算器实例")
    calc = Calculator()
    return calc


# 分别从yml文件中读取测试数据
with open("./datas/calc.yml") as f:
    f = yaml.safe_load(f)
    add_datas = f["add"]["datas"]
    add_ids = f["add"]["ids"]
    sub_datas = f["sub"]["datas"]
    sub_ids = f["sub"]["ids"]
    mul_datas = f["mul"]["datas"]
    mul_ids = f["mul"]["ids"]
    div_datas = f["div"]["datas"]
    div_ids = f["div"]["ids"]


@pytest.fixture(scope="module", params=add_datas, ids=add_ids)
def get_add_datas(request):
    """
    获取加法测试数据
    """
    print("开始计算加法")
    data = request.param
    print(f"测试数据为：{data}")
    yield data
    print("结束计算加法")


@pytest.fixture(scope="module", params=sub_datas, ids=sub_ids)
def get_sub_datas(request):
    print("开始计算减法")
    data = request.param
    print(f"测试数据为：{data}")
    yield data
    print("结束计算减法")


@pytest.fixture(scope="module", params=mul_datas, ids=mul_ids)
def get_mul_datas(request):
    print("开始计算乘法")
    data = request.param
    print(f"测试数据为：{data}")
    yield data
    print("结束计算乘法")


@pytest.fixture(scope="module", params=div_datas, ids=div_ids)
def get_div_datas(request):
    print("开始计算除法")
    data = request.param
    print(f"测试数据为：{data}")
    yield data
    print("结束计算除法")

