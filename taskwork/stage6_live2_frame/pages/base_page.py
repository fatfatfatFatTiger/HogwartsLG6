# -*- coding: utf-8 -*-
# @File : base_page.py
# @Author : Elf
# @Time : 2021/3/13 22:07

import allure
import yaml
import json
from typing import List, Dict
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from HogwartsLG6.taskwork.stage6_live2_frame.conftest import root_log


class BasePage:
    # 定义一个字典，要替换的内容放在一个字典里
    _params = {}
    # 定义黑名单列表，保存可能出现的异常弹框
    _blacklist = [(MobileBy.ID, 'com.tencent.wework:id/ig0'),
                  (MobileBy.XPATH, '//*[text="关闭"]')
                  ]
    # 设置最大查找次数
    _max_num = 3
    _error_num = 0

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find(self, by, locator):
        """
        查找元素
        :param by: 点击方式，如id、xpath
        :param locator: 元素位置
        :return: 找到的元素
        """
        root_log.info(f"find: by={by}, locator={locator}")
        try:
            element = self.driver.find_element(by, locator)
            self._error_num = 0
            # 此处设置隐式等待是因为处理一次异常后，重新正常查找元素，重置隐式等待时间
            self.setup_implicitly_wait(10)
            return element
        except Exception as e:
            # 黑名单处理逻辑
            root_log.error("未找到指定元素", e)
            # 如果开始处理异常，则将隐式等待时间减少到2秒，快速处理
            self.setup_implicitly_wait(2)

            # 异常截图，并添加到测试报告中
            self.driver.get_screenshot_as_file("/results/error.png")
            allure.attach.file("/results/error.png", attachment_type=allure.attachment_type.PNG)

            # 如果最大尝试次数都没处理异常弹框，就自动抛出异常，将错误次数置为0，并将隐式等待时间重置
            if self._error_num > self._max_num:
                self._error_num = 0
                self.setup_implicitly_wait(10)
                raise e

            # 每次进入except处理一次异常(弹框)，_error_num都+1
            self._error_num += 1

            # 依次处理黑名单
            for ele in self._blacklist:
                # find_elements 会返回元素的列表，如果没有元素会返回一个空列表，参数为元组格式
                eles = self.driver.find_elements(*ele)
                # 如果存在黑名单中的异常弹框，则处理，处理完后再次查找指定元素
                if len(eles) > 0:
                    # 处理元素，此处为点击关闭弹框
                    eles[0].click()
                    # 此处return self.find表示处理异常后重新查找元素，
                    # 不能使用self.find_element()，因为self.find_element()只执行这一次，如果异常未处理掉，再次找不到，就不会再继续查找
                    return self.find(by, locator)

            # 如果黑名单都处理完了，仍没有找到想要的元素，则抛出异常
            raise e

    def finds(self, by, locator):
        """
        查找一组元素
        :param by: 点击方式，如id、xpath
        :param locator: 元素位置
        :return: 找到的一组元素，列表格式
        """
        root_log.info(f"finds: by={by}, locator={locator}")
        return self.driver.find_elements(by, locator)

    def finds_getnum(self, by, locator):
        """
        获取一组元素中包含的元素个数
        :param by: 点击方式，如id、xpath
        :param locator: 元素位置
        :return: 包含的元素个数
        """
        elements = self.finds(by, locator)
        return len(elements)

    def setup_implicitly_wait(self, timeout):
        """
        设置隐式等待时间
        :param timeout: 时间，单位秒
        :return:
        """
        self.driver.implicitly_wait(timeout)

    def find_click(self, by, locator):
        """
        找到元素并点击
        :param by: 点击方式，如id、xpath
        :param locator: 元素位置
        :return:
        """
        self.find(by, locator).click()

    def find_sendkeys(self, by, locator, text):
        """
        查找元素并输入值
        :param by: 点击方式，如id、xpath
        :param locator: 元素位置
        :param text: 输入的内容
        :return:
        """
        self.find(by, locator).send_keys(text)

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

    def wait(self, time, locator):
        """
        显示等待元素出现
        :param time: 等待时间
        :param locator: 定位元素
        :return:
        """
        loc = (MobileBy.XPATH, locator)
        WebDriverWait(self.driver, time).until(expected_conditions.element_to_be_clickable(loc))

    def parse_action(self, path, func_name):
        """
        读取配置文件，并根据配置文件中的定位查找元素
        :param path: 配置文件路径
        :param fun_name: 配置文件中的模块名，列表格式
        :return:
        """
        with open(path, "r", encoding="utf-8") as f:
            # 读取配置文件所有内容
            functions = yaml.safe_load(f)
            steps: List[Dict] = functions[func_name]

        # json 序列化与反序列化
        # json.dumps() 序列化 python对象转化成字符串
        # json.loads() 反序列化 字符串转化成python对象
        raw = json.dumps(steps)
        for key, value in self._params.items():
            # 将配置文件中参数化的部分替换为用例中传的值
            raw = raw.replace("${" + key + "}", value)
        steps = json.loads(raw)

        # 按模块名依次处理各部分
        for step in steps:
            if step["action"] == "find_click":
                self.find_click(step["by"], step["locator"])
            elif step["action"] == "find":
                self.find(step["by"], step["locator"])
            elif step["action"] == "find_sendkeys":
                self.find_sendkeys(step["by"], step["locator"], step["text"])
            elif step["action"] == "swip_click":
                self.swip_click(step["text"])
            elif step["action"] == "wait":
                self.wait(step["time"], step["locator"])
            elif step["action"] == "finds_getnum":
                return self.finds_getnum(step["by"], step["locator"])
