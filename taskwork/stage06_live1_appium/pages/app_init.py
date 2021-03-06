# -*- coding: utf-8 -*-
# @File : app_init.py
# @Author : Elf
# @Time : 2021/3/7 17:26

from appium import webdriver
from HogwartsLG6.taskwork.stage6_live1_appium.pages.information_page import InformationPage


class AppInit:
    def __init__(self):
        self.driver = None
        self.start()

    def start(self):
        caps = {
            "platformName": "android",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "com.tencent.wework",
            "appActivity": ".launch.LaunchSplashActivity",
            "noReset": "true",  # 不清除session信息，如果上一个测试用例登陆成功了，下一个测试用例，在打开app时，进来的页面是登录成功后的页面，会保持登录状态
            "settings[waitForIdleTimeout]": 0,
            "automationName": "uiautomator2",
            "skipDeviceInitialization": "true"  # 跳过设备初始化
        }

        # 客户端和appium建立连接
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def goto_info_page(self):
        """
        链式调用跳转到消息页面
        :return: 消息页面
        """
        return InformationPage(self.driver)


