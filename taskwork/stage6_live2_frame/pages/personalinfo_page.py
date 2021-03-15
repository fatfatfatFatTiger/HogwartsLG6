# -*- coding: utf-8 -*-
# @File : personalinfo_page.py
# @Author : Elf
# @Time : 2021/3/13 22:28


from HogwartsLG6.exercise.stage6_Appium.live2_frame.pages.base_page import BasePage
from HogwartsLG6.taskwork.stage6_live2_frame.conftest import root_log
from HogwartsLG6.taskwork.stage6_live2_frame.pages.personalinfosetup_page import PersonalInfoSetupPage


class PersonalInfoPage(BasePage):
    def click_setup(self):
        """
        个人信息页面点击页面右上角三个点，进入[个人信息-设置]页面
        :return:
        """
        self.parse_action('../datas/personalinfo_page.yaml', 'click_setup')
        root_log.info("【Step6: 个人信息页面点击页面右上角三个点，进入[个人信息-设置]页面】")
        return PersonalInfoSetupPage(self.driver)
