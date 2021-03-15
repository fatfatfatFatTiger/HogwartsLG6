# -*- coding: utf-8 -*-
# @File : personalinfosetup_page.py
# @Author : Elf
# @Time : 2021/3/13 22:32


from HogwartsLG6.taskwork.stage6_live2_frame.pages.base_page import BasePage
from HogwartsLG6.taskwork.stage6_live2_frame.conftest import root_log
from HogwartsLG6.taskwork.stage6_live2_frame.pages.editmember_page import EditMemeberPage


class PersonalInfoSetupPage(BasePage):
    def click_edit(self):
        """
        [个人信息-设置]页面点击编辑成员，进入[编辑成员]页面
        :return:
        """
        self.parse_action('../datas/personalinfosetup_page.yaml', 'click_edit')
        root_log.info("【Step7: [个人信息-设置]页面点击编辑成员，进入[编辑成员]页面】")
        return EditMemeberPage(self.driver)
