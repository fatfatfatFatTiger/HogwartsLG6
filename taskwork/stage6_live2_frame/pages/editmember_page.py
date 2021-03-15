# -*- coding: utf-8 -*-
# @File : editmember_page.py
# @Author : Elf
# @Time : 2021/3/13 22:35

from HogwartsLG6.taskwork.stage6_live2_frame.pages.base_page import BasePage
from HogwartsLG6.taskwork.stage6_live2_frame.conftest import root_log


class EditMemeberPage(BasePage):
    def delete_member(self):
        """
        [编辑成员]页面点击删除成员按钮，二次弹框点击确认按钮
        :return:
        """
        self.parse_action('../datas/editmember_page.yaml', 'delete_member')
        root_log.info("【Step8: [编辑成员]页面点击删除成员按钮】")
        return self

    def get_after_del_results(self, search_keyword):
        """
        选择元素删除后，统计搜索结果剩余个数
        删除后直接返回搜索结果页面，刷新，此处有2个操作，先是显示等待搜索结果出来后，再统计当前关键词下搜索结果个数
        :param search_keyword: 搜索关键词
        :return:
        """
        self._params['search_keyword'] = search_keyword
        after_num = self.parse_action('../datas/editmember_page.yaml', 'get_after_del_results')
        root_log.info("【删除用户后获取搜索结果个数】")
        return after_num


