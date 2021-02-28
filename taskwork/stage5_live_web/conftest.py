# -*- coding: utf-8 -*-
# @File : conftest.py
# @Author : Elf
# @Time : 2021/2/28 11:03

import yaml
import pytest

# 从yml文件中读取待添加的联系人信息
with open("../datas/members.yml") as f:
    f = yaml.safe_load(f)
    member_datas = f["members"]["info"]
    member_ids = f["members"]["ids"]


@pytest.fixture(scope="module", params=member_datas, ids=member_ids)
def get_member_datas(request):
    """
    获取联系人信息
    :param request:
    :return:
    """
    data = request.param
    print(f"测试数据为：{data}")
    yield data

