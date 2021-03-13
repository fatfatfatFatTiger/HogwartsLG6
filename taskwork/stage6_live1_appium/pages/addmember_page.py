# -*- coding: utf-8 -*-
# @File : addmember_page.py
# @Author : Elf
# @Time : 2021/3/7 18:14

from HogwartsLG6.taskwork.stage6_live1_appium.pages.base_page import BasePage


class AddmemberPage(BasePage):
    def add_member_and_assert(self, key):
        # 初始化需要sendkeys的值
        self._member_info = {
            "name": key[0]["name"],
            "phone": key[0]["phone"]
        }

        configfile_path = '../datas/addmember_page.yaml'
        # 读取配置文件，完成添加成员操作
        self.parse_configfile(configfile_path, 'input_info')

        # 获取保存成功后的弱提示文字
        result = self.parse_configfile(configfile_path, 'assert_result')
        assert "添加成功" == result

