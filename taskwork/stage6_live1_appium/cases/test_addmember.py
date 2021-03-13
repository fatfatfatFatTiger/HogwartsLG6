# -*- coding: utf-8 -*-
# @File : test_addmember.py
# @Author : Elf
# @Time : 2021/3/7 19:23

import yaml
from HogwartsLG6.taskwork.stage6_live1_appium.pages.app_init import AppInit


class TestAddmember:
    def setup(self):
        self.app = AppInit()

    def test_add(self):
        with open("../datas/members.yaml", "r", encoding="utf-8") as f:
            # 获取待添加的用户信息，格式为List[dict, dict, dict...]，一个dict代表一个用户的信息
            member_info = yaml.safe_load(f)["info"]
        self.app.goto_info_page().goto_addressbook_page().goto_addmember_page().add_member_and_assert(member_info)

