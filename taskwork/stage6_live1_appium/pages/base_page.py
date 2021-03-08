# -*- coding: utf-8 -*-
# @File : base_page.py
# @Author : Elf
# @Time : 2021/3/7 17:34

import yaml
from typing import List, Dict
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find_click(self, mode, locator):
        """
        找到元素并点击
        :param mode: 点击方式，如id、xpath
        :param locator: 元素位置
        :return:
        """
        if mode == "id":
            self.driver.find_element(MobileBy.ID, locator).click()
        elif mode == "xpath":
            self.driver.find_element(MobileBy.XPATH, locator).click()

    def find_input(self, mode, locator, text):
        """
        找到元素并输入内容
        :param mode: 点击方式，如id、xpath
        :param locator: 元素位置
        :param text: 待输入的内容
        :return:
        """
        if mode == "id":
            self.driver.find_element(MobileBy.ID, locator).send_keys(text)
        elif mode == "xpath":
            self.driver.find_element(MobileBy.XPATH, locator).send_keys(text)

    def wait_for_click(self, time, locator):
        """
        显示等待元素出现
        :param time: 等待时间
        :param locator: 定位元素
        :return:
        """
        loc = (MobileBy.XPATH, locator)
        WebDriverWait(self.driver, time).until(expected_conditions.element_to_be_clickable(loc))

    def find_get(self, mode, locator):
        """
        找到元素并获取文字
        :param mode: 查找方式，如id、xpath
        :param locator: 定位元素
        :return: 定位元素的text
        """
        if mode == "id":
            return self.driver.find_element(MobileBy.ID, locator).text
        elif mode == "xpath":
            return self.driver.find_element(MobileBy.XPATH, locator).text

    def swip_click(self, text):
        """
        滑动查找元素并点击
        :param text: 待查找元素的text
        :return:
        """
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().'
                                 'scrollable(true).instance(0)).'
                                 'scrollIntoView(new UiSelector(). '
                                 f'text("{text}").instance(0));').click()

    def parse_configfile(self, path, module_name):
        """
        解析配置文件
        :param path: 配置文件路径
        :param module_name: yaml文件中的模块名
        :return:
        """
        # 打开存储数据的yaml文件
        with open(path, "r", encoding="utf-8") as f:
            # 读取yaml文件所有内容
            contents = yaml.safe_load(f)
            # 按功能模块读取数据保存到list中
            steps: List[Dict] = contents[module_name]
        # 依次读取，根据配置中的行为和定位方式执行相应操作
        for step in steps:
            if step["action"] == "swip_click":
                # 滑动并点击
                self.swip_click(step["text"])
            elif step["action"] == "find_click":
                # 找到元素并点击
                self.find_click(step["mode"], step["locator"])
            elif step["action"] == "find_input":
                # 找到元素并输入内容
                self.find_input(step["mode"], step["locator"], step["input_value"])
            elif step["action"] == "wait_for_click":
                # 显示等待元素出现
                self.wait_for_click(step["time"], step["locator"])
            elif step["action"] == "find_click_get":
                # 找到元素并获取文字
                return self.find_get(step["mode"], step["locator"])

