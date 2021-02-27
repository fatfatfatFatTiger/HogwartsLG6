# -*- coding: utf-8 -*-
# @File : test_cookie_wechat.py
# @Author : Elf
# @Time : 2021/2/27 12:53

import shelve
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestWeb1:
    def setup(self):
        option = Options()
        option.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=option)

    def teardown(self):
        self.driver.quit()

    # 前提：已通过命令行开启远程浏览器调试
    def test_reuse_browser_get_cookies(self):
        """
        验证是否已复用浏览器，并获取登录成功后的cookies保存到db
        :return:
        """
        # 获取页面登录成功后的cookies
        page_cookies = self.driver.get_cookies()
        print(page_cookies)

        # 将cookies存入python自带的小型数据库
        db = shelve.open('./mydbs/cookies')
        db['cookies'] = page_cookies
        db.close()

        # 验证 index 页面企业名称
        assert "elf测试企业" == self.driver.find_element_by_css_selector('.index_info_name').text
        sleep(1)
