# -*- coding: utf-8 -*-
# @File : test_deletemember.py
# @Author : Elf
# @Time : 2021/3/14 9:02

from HogwartsLG6.taskwork.stage6_live2_frame.pages.app_init import AppInit


class TestContact:
    def setup(self):
        self.app = AppInit()

    def test_deletemember(self):
        # 搜索关键字
        search_keyword = "hogwards"
        # 待删除用户名
        username = "hogwards_100"
        # 待删除用户名
        department = "elf测试企业/财务部"

        searchpage = self.app.goto_infomation_page().goto_addresslist().click_search()
        # 搜索页面输入关键字
        searchpage.input_search_words(search_keyword)
        # 删除会员前，获取按关键字搜索出来的结果个数
        before_del_num = searchpage.get_before_del_results(search_keyword)
        # 删除会员，并获取当前关键字剩余的结果个数
        after_del_num = searchpage.click_search_result(username, department).click_setup().click_edit().delete_member().get_after_del_results(search_keyword)

        # print(f"before_del_num: {before_del_num}")
        # print(f"after_del_num: {after_del_num}")

        # 如果删除后的个数和删除前的个数差1，表名删除成功
        assert before_del_num - after_del_num == 1



