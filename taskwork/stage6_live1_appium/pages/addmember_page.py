# -*- coding: utf-8 -*-
# @File : addmember_page.py
# @Author : Elf
# @Time : 2021/3/7 18:14

from HogwartsLG6.taskwork.stage6_live1_appium.pages.base_page import BasePage


class AddmemberPage(BasePage):
    def add_member_and_assert(self):
        """
        录入信息，保存联系人，并断言是否添加成功
        :return:
        """
        configfile_path = '../datas/addmember_page.yaml'

        # 当前类继承BasePage类，可直接调用基类中解析配置文件方法
        # 依次输入姓名、选择性别、输入手机号、点击保存按钮
        self.parse_configfile(configfile_path, 'input_info')

        # 获取保存成功后的弱提示文字
        result = self.parse_configfile(configfile_path, 'assert_result')
        assert "添加成功" == result

