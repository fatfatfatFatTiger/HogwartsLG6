# -*- coding: utf-8 -*-
# @File : main_page.py
# @Author : Elf
# @Time : 2021/2/28 9:51

from selenium.webdriver.common.by import By
from HogwartsLG6.taskwork.stage5_live_web.pages.add_member_page import AddMemberPage
from HogwartsLG6.taskwork.stage5_live_web.pages.base_page import BasePage


class MainPage(BasePage):
    base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    def goto_add_member(self):
        """
        跳转到添加联系人页面
        :return: 添加联系人页面PO
        """
        self.find(By.CSS_SELECTOR, '.index_service_cnt_itemWrap:nth-child(1)').click()
        return AddMemberPage(self.driver)

