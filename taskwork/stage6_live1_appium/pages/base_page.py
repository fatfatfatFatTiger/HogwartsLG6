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
    # 私有变量，存放sendkeys中的值
    _member_info = {}

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find(self, by, locator):
        """
        找到元素
        :param by: 查找方式，如id、xpath
        :param locator: 定位元素
        :return: 找到的元素
        """
        return self.driver.find_element(by, locator)

    def find_click(self, by, locator):
        """
        找到元素并点击
        :param by: yaml中传入的点击方式，如id、xpath
        :param locator: 元素位置
        :return:
        """
        self.find(by, locator).click()

    def find_input(self, by, locator, text):
        """
        找到元素并输入内容
        :param by: 点击方式，如id、xpath
        :param locator: 元素位置
        :param text: 待输入的内容
        :return:
        """
        self.find(by, locator).send_keys(text)

    def wait_for_click(self, time, locator):
        """
        显示等待元素出现
        :param time: 等待时间
        :param locator: 定位元素
        :return:
        """
        loc = (MobileBy.XPATH, locator)
        WebDriverWait(self.driver, time).until(expected_conditions.element_to_be_clickable(loc))

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
                self.find_click(step["by"], step["locator"])
            elif step["action"] == "find_input":
                # 获取addmember_page.yaml文件中待输入元素的value，此处已参数化，需要从members.yaml文件中读取待录入成员数据
                input_value: str = step["input_value"]    # {name}、{phone}
                for key in self._member_info:
                    # 判断addmember_page.yaml中各个操作的元素参数化格式名与members.yaml中自定义的用户信息key值，如果相同，则替换为输入值，并直接输入该值
                    if "{%s}" % key == input_value:
                        input_value = input_value.replace("{%s}" % key, self._member_info[key])
                        # 找到元素并输入内容
                        self.find_input(step["by"], step["locator"], input_value)
                        break
            elif step["action"] == "wait_for_click":
                # 显示等待元素出现
                self.wait_for_click(step["time"], step["locator"])
            elif step["action"] == "find_click_get":
                # 找到元素并获取文字
                return self.find(step["by"], step["locator"]).text

