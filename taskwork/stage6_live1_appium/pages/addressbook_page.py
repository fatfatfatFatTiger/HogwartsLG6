# -*- coding: utf-8 -*-
# @File : workbench_page.py
# @Author : Elf
# @Time : 2021/3/7 17:38

from HogwartsLG6.taskwork.stage6_live1_appium.pages.base_page import BasePage
from HogwartsLG6.taskwork.stage6_live1_appium.pages.addmember_page import AddmemberPage


class AddressbookPage(BasePage):
    def goto_addmember_page(self):
        """
        链式调用跳转到添加成员页面
        :return: 添加成员页面
        """
        # 当前类继承BasePage类，可直接调用基类中解析配置文件方法
        # 1.若[通讯录]页面成员较多，滑动页面，直到出现“添加成员”按钮，并点击
        # 2.点击“手动输入添加”按钮，跳转到[添加成员]页面
        self.parse_configfile('../datas/addressbook_page.yaml', 'goto_addmember_page')
        return AddmemberPage(self.driver)

