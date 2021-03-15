# -*- coding: utf-8 -*-
# @File : search_page.py
# @Author : Elf
# @Time : 2021/3/13 22:15

from HogwartsLG6.taskwork.stage6_live2_frame.conftest import root_log
from HogwartsLG6.taskwork.stage6_live2_frame.pages.base_page import BasePage
from HogwartsLG6.taskwork.stage6_live2_frame.pages.personalinfo_page import PersonalInfoPage


class SearchPage(BasePage):
    def input_search_words(self, search_keyword):
        """
        [搜索]页面输入查询关键字
        :return:
        """
        self._params['search_keyword'] = search_keyword
        self.parse_action('../datas/search_page.yaml', 'input_search_words')
        root_log.info("【Step4: [搜索]页面输入查询关键字】")

    def get_before_del_results(self, search_keyword):
        """
        搜索出关键字，选择元素删除前，统计搜索结果个数
        :param search_keyword: 搜索关键词
        :return:
        """
        self._params['search_keyword'] = search_keyword
        before_num = self.parse_action('../datas/search_page.yaml', 'get_before_del_results')
        root_log.info("【删除用户前获取搜索结果个数】")
        return before_num

    def click_search_result(self, username, department):
        """
        点击查询结果中要删除的用户，进入[个人信息]页面
        :return:
        """
        self._params['username'] = username
        self._params['department'] = department
        self.parse_action('../datas/search_page.yaml', 'click_search_result')
        root_log.info("【Step5: 点击查询结果中要删除的用户，进入[个人信息]页面】")
        return PersonalInfoPage(self.driver)
