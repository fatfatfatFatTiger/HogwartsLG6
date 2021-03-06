# -*- coding: utf-8 -*-
# @File : test_wework.py
# @Author : Elf
# @Time : 2021/3/6 17:13
import time

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
# from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWework:
    def setup(self):
        caps = {
            "platformName": "android",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "com.tencent.wework",
            "appActivity": ".launch.LaunchSplashActivity",
            "noReset": "true",
            "settings[waitForIdleTimeout]": 0,
            "automationName": "uiautomator2"
        }

        # 客户端和appium建立连接
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_addmember(self):
        # 点击首页“通讯录”
        self.driver.find_element(MobileBy.XPATH, '//*[@text="通讯录"]').click()

        # 滑动页面找到“添加成员”并点击
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().'
                                 'scrollable(true).instance(0)).'
                                 'scrollIntoView(new UiSelector(). '
                                 'text("添加成员").instance(0));').click()

        # 点击“手动输入添加”
        self.driver.find_element(MobileBy.XPATH, '//*[@text="手动输入添加"]').click()

        # 验证是否进入添加页面
        page_name = self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/gua').text
        if page_name == "添加成员":
            # 输入姓名
            self.driver.find_element(MobileBy.XPATH,
                                     '//*[@resource-id="com.tencent.wework:id/au1"]/..'
                                     '//*[@resource-id="com.tencent.wework:id/au0"]').send_keys("tester")

            # 点击性别
            self.driver.find_element(MobileBy.XPATH, '//*[@text="性别"]/..//*[@resource-id="com.tencent.wework:id/dux"]').click()
            # 添加显示等待，等待性别选项加载出来后再点击选择
            locator = (MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/b9z"]')
            WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
            # 点击性别“女”
            self.driver.find_element(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/b9z"]//*[@index="1"]').click()

            # 输入手机号
            self.driver.find_element(MobileBy.XPATH, '//*[@text="手机号"]').send_keys("18912312345")

            # 点击保存
            self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/gur').click()

            # print(self.driver.find_element(MobileBy.XPATH, '//*[@class="android.widget.Toast"]').text)
            # print(self.driver.find_element(MobileBy.XPATH, '/hierarchy/android.widget.Toast').text)
            # print(self.driver.find_element(MobileBy.XPATH, '//*[contains(@text, "添加成功")]').text)

            success_text = self.driver.find_element(MobileBy.XPATH, '//*[@class="android.widget.Toast"]').text
            assert "添加成功" == success_text

        else:
            print("未进入添加成员页面")
