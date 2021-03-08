# -*- coding: utf-8 -*-
# @File : message_page.py
# @Author : Elf
# @Time : 2021/3/7 17:31

from HogwartsLG6.taskwork.stage6_live1_appium.pages.base_page import BasePage
from HogwartsLG6.taskwork.stage6_live1_appium.pages.addressbook_page import AddressbookPage


class InformationPage(BasePage):
    def goto_addressbook_page(self):
        """
        链式调用跳转到通讯录页面
        :return: 通讯录页面
        """
        # 当前类继承BasePage类，可直接调用基类中解析配置文件方法
        # 点击通讯录按钮，跳转到通讯录页面
        self.parse_configfile('../datas/information_page.yaml', 'goto_addressbook_page')
        return AddressbookPage(self.driver)


