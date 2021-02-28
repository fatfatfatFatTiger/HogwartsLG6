# -*- coding: utf-8 -*-
# @File : test_contact.py
# @Author : Elf
# @Time : 2021/2/28 9:51

import allure
from HogwartsLG6.taskwork.stage5_live_web.pages.main_page import MainPage


@allure.feature("测试联系人添加")
class TestContact:
    def setup(self):
        self.mp = MainPage()

    @allure.story("测试添加联系人并判断是否添加成功")
    def test_addmember(self, get_member_datas):
        # 读取测试数据
        username = get_member_datas[0]
        account = get_member_datas[1]
        phonenum = get_member_datas[2]

        # 进入添加联系人页面，提取出来，供多次使用
        page = self.mp.goto_add_member()
        # 添加联系人
        page.add_member(username, account, phonenum)
        # 获取测试数据中的联系人姓名
        username = get_member_datas[0]
        # 获取已添加联系人列表
        names = page.get_members()
        assert username in names

