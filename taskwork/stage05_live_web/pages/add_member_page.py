# -*- coding: utf-8 -*-
# @File : add_memeber_page.py
# @Author : Elf
# @Time : 2021/2/28 9:51

import allure
from selenium.webdriver.common.by import By
from HogwartsLG6.taskwork.stage5_live_web.pages.base_page import BasePage


@allure.feature("添加联系人页面PO")
class AddMemberPage(BasePage):
    @allure.story("添加联系人")
    def add_member(self, username, account, phonenum):
        """
        添加联系人
        :param username: 姓名
        :param account: 账号
        :param phonenum: 手机
        :return:
        """
        with allure.step(f"输入用户名{username}"):
            self.find(By.ID, 'username').send_keys(username)
        with allure.step(f"输入账户{account}"):
            self.find(By.ID, 'memberAdd_acctid').send_keys(account)
        with allure.step(f"输入手机号码{phonenum}"):
            self.find(By.ID, 'memberAdd_phone').send_keys(phonenum)
        with allure.step("点击保存按钮"):
            self.find(By.CSS_SELECTOR, '.js_btn_save').click()
        return True

    @allure.story("获取联系人列表")
    def get_members(self):
        """
        获取所有已添加联系人姓名
        :return: 联系人姓名列表
        """
        locator = (By.CSS_SELECTOR, '.member_colRight_memberTable_th_Checkbox')
        with allure.step("等待联系人复选框出现"):
            self.wait_to_click(10, locator)
        elements_list = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
        names_list = []
        with allure.step("获取已添加联系人姓名列表"):
            for element in elements_list:
                names_list.append(element.get_attribute('title'))
        return names_list



