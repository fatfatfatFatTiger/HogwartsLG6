# -*- coding: utf-8 -*-
# @File : information_page.py
# @Author : Elf
# @Time : 2021/3/13 22:07

from HogwartsLG6.taskwork.stage6_live2_frame.conftest import root_log
from HogwartsLG6.taskwork.stage6_live2_frame.pages.addresslist_page import AddressListPage
from HogwartsLG6.taskwork.stage6_live2_frame.pages.base_page import BasePage


class InformationPage(BasePage):
    def goto_addresslist(self):
        """
        [消息]页面点击底部通讯录进入[通讯录]页面
        :return:
        """
        self.parse_action('../datas/information_page.yaml', 'goto_addresslist')
        root_log.info("【Step2: [消息]页面点击底部通讯录进入[通讯录]页面】")
        return AddressListPage(self.driver)
