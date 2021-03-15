# -*- coding: utf-8 -*-
# @File : addresslist_page.py
# @Author : Elf
# @Time : 2021/3/13 22:24

from HogwartsLG6.taskwork.stage6_live2_frame.conftest import root_log
from HogwartsLG6.taskwork.stage6_live2_frame.pages.base_page import BasePage
from HogwartsLG6.taskwork.stage6_live2_frame.pages.search_page import SearchPage


class AddressListPage(BasePage):
    def click_search(self):
        """
        点击[通讯录]页面右上角放大镜，进入[搜索]页面
        :return:
        """
        self.parse_action('../datas/addresslist_page.yaml', 'click_search')
        root_log.info("【Step3: 点击[通讯录]页面右上角放大镜，进入[搜索]页面】")
        return SearchPage(self.driver)

