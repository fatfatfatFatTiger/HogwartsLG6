# -*- coding: utf-8 -*-
# @File : base_page.py
# @Author : Elf
# @Time : 2021/2/28 9:51

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    base_url = ""

    def __init__(self, driver: WebDriver = None):
        # 首次初始化，无driver，此处定义一个新的，之后再调用基类初始化时，driver已经存在，直接沿用
        if driver is None:
            # 复用浏览器，需要设置 opton.debugger_address
            option = Options()
            option.debugger_address = '127.0.0.1:9222'
            self.driver = webdriver.Chrome(options=option)
            self.driver.implicitly_wait(5)
        else:
            self.driver = driver
        # 主页配置网址，进入主页，先读取变量，再初始化，此处进入网址；进入添加联系人页面，未定义变量，初始化时此处不重新进入，直接沿用之前网址
        if self.base_url != "":
            self.driver.get(self.base_url)

    def find(self, locator, value):
        """
        定位单个元素
        :param locator: 元素定位方式
        :param value: 元素定位值
        :return: 定位到的元素
        """
        return self.driver.find_element(locator, value)

    def finds(self, locator, value):
        """
        定位一组元素
        :param locator: 元素定位方式
        :param value: 元素定位值
        :return: 定位到的一组元素
        """
        return self.driver.find_elements(locator, value)

    def wait_to_click(self, timeout, locator):
        """
        显示等待元素出现后判断是否可点击
        :param timeout: 超时时间
        :param locator: 元素定位方式
        :return:
        """
        # 显示等待是局部等待
        WebDriverWait(self.driver, timeout).until(expected_conditions.element_to_be_clickable(locator))

