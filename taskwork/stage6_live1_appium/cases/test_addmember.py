# -*- coding: utf-8 -*-
# @File : test_addmember.py
# @Author : Elf
# @Time : 2021/3/7 19:23

from HogwartsLG6.taskwork.stage6_live1_appium.pages.app_init import AppInit


class TestAddmember:
    def setup(self):
        self.app = AppInit()

    def test_add(self):
        self.app.goto_info_page().goto_addressbook_page().goto_addmember_page().add_member_and_assert()


