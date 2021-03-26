import allure
import requests


@allure.feature("企业微信通讯录相关测试")
class TestContact:
    @allure.story("创建成员")
    def test_create_member(self, get_assess_token, get_create_info):
        """
        创建成员
        :param get_assess_token: 企业微信assess_token
        :param get_create_info: 需创建成员的测试数据
        :return:
        """
        create_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={get_assess_token}'
        data = {
            "userid": get_create_info["userid"],
            "name": get_create_info["name"],
            "alias": get_create_info["alias"],
            "mobile": get_create_info["mobile"],
            "department": get_create_info["department"]
        }
        r = requests.post(url=create_member_url, json=data)
        print(r.json())
        assert 0 == r.json()["errcode"] and "created" == r.json()["errmsg"]

    @allure.story("读取成员")
    def test_get_member(self, get_assess_token, get_query_info):
        """
        读取成员
        :param get_assess_token: 企业微信assess_token
        :param get_query_info: 需读取成员的测试数据
        :return:
        """
        get_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={get_assess_token}&userid={get_query_info["userid"]}'
        r = requests.get(url=get_member_url)
        # print(r.json())
        assert "ok" == r.json()["errmsg"] and get_query_info["userid"] == r.json()["userid"]

    @allure.story("更新成员")
    def test_uptate_member(self, get_assess_token, get_update_info):
        """
        更新成员
        :param get_assess_token: 企业微信assess_token
        :param get_update_info: 需更新成员的测试数据
        :return:
        """
        update_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={get_assess_token}'
        data = {
            "userid": get_update_info["userid"],
            "name": get_update_info["name"],
            "alias": get_update_info["alias"]
        }
        r = requests.post(url=update_member_url, json=data)
        print(r.json())
        assert 0 == r.json()["errcode"] and "updated" == r.json()["errmsg"]

    @allure.story("删除成员")
    def test_delete_member(self, get_assess_token, get_delete_info):
        """
        删除成员
        :param get_assess_token: 企业微信assess_token
        :param get_delete_info: 需更新成员的测试数据
        :return:
        """
        delete_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={get_assess_token}&userid={get_delete_info["userid"]}'
        r = requests.get(url=delete_member_url)
        print(r.json())
        assert 0 == r.json()["errcode"] and "deleted" == r.json()["errmsg"]
