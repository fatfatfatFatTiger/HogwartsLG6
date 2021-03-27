
import allure
from HogwartsLG6.taskwork.stage10_live_request.wework.address import Address


@allure.feature("企业微信通讯录相关测试")
class TestContact:
    def setup(self):
        self.address = Address()

    @allure.story("创建成员")
    def test_create_member(self, get_member_info):
        # step1.创建前先判断成员是否存在，如果存在就先删除该成员
        self.address.delete_member(get_member_info)     # 利用删除接口进行数据清理，如果用户不存在时仍删除，不会报错，因为报错信息藏在字典中，但此处未进行断言
        # step2.创建成员
        r = self.address.create_member(get_member_info)
        assert r.get("errmsg", "network error") == "created"    # 根据key从字典中取value，如果没有这个key，则给出提示
        # step3.获取成员信息，判断是否创建成功
        r = self.address.get_member(get_member_info)
        # step4.删除无用数据，保证不遗留测试脏数据
        self.address.delete_member(get_member_info)     # 不能放断言后删除，假如断言失败，则不会执行删除操作，会遗留脏数据
        assert r.get("name") == get_member_info["name"]

    @allure.story("读取成员")
    def test_get_member(self, get_member_info):
        # step1.以防要获取成员不存在，需要先创建一个成员
        self.address.create_member(get_member_info)
        # step2.获取成员信息
        r = self.address.get_member(get_member_info)
        assert r.get("errmsg") == "ok"
        assert r.get("name") == get_member_info["name"]

    @allure.story("更新成员")
    def test_update_member(self, get_member_info):
        # step1.先删除脏数据
        self.address.delete_member(get_member_info)
        # step2.新创建一个成员
        self.address.create_member(get_member_info)
        new_name = get_member_info["name"] + "tmp"
        # step3.在新创建的成员基础上修改姓名
        r = self.address.update_member(get_member_info, new_name)
        assert r.get("errmsg") == "updated"
        # step4.获取成员信息，验证姓名是否更新成功
        r = self.address.get_member(get_member_info)
        assert r.get("name") == new_name

    @allure.story("删除成员")
    def test_delete_member(self, get_member_info):
        # step1.以防要获取成员不存在，需要先创建一个成员
        self.address.create_member(get_member_info)
        # step2.删除成员
        r = self.address.delete_member(get_member_info)
        assert r.get("errmsg") == "deleted"
        # step3.再次获取成员信息，验证是否删除成功
        r = self.address.get_member(get_member_info)
        assert r.get("errcode") == 60111


