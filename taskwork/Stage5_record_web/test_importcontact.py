# -*- coding: utf-8 -*-
# @File : test_importcontact.py
# @Author : Elf
# @Time : 2021/2/27 13:28

import shelve
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestWeb1:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_login_import_contact(self):
        """
        使用cookie登录企业微信，并导入联系人文件
        :return:
        """
        # 从db中读取出用于登录到 index 页面的cookies
        db = shelve.open('./mydbs/cookies')
        cookies = db['cookies']

        # 首次打开 index 页面，由于是新开的driver，相当于无痕浏览，会重定向到登录页面
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")

        # 依次将cookie写入到driver用于登录
        for cookie in cookies:
            if "expiry" in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)

        # 再次访问 index 页面，验证是否已登录成功
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        sleep(1)

        # 点击 index 页面导入通讯录按钮
        self.driver.find_element(By.CSS_SELECTOR, '.index_service_cnt_itemWrap:nth-child(2)').click()
        sleep(1)

        file_path = r'E:\Python\myProjects\HogwartsLG6\taskwork\Stage5_record_web\myfriends.xlsx'
        # 上传通讯录文件
        self.driver.find_element(By.ID, 'js_upload_file_input').send_keys(file_path)
        # 断言上传文件是否正确
        assert "myfriends.xlsx" == self.driver.find_element(By.ID, 'upload_file_name').text
        sleep(2)

