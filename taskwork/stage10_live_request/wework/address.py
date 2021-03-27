
from HogwartsLG6.taskwork.stage10_live_request.wework.base import Base


class Address(Base):
    def create_member(self, member_info):
        """
        创建成员
        :param member_info: yaml文件中的用户信息
        :return:
        """
        create_member_url = 'https://qyapi.weixin.qq.com/cgi-bin/user/create'
        data = {
            "userid": member_info["userid"],
            "name": member_info["name"],
            "alias": member_info["alias"],
            "mobile": member_info["mobile"],
            "department": member_info["department"]
        }
        r = self.send("POST", url=create_member_url, json=data)
        return r.json()

    def get_member(self, member_info):
        """
        获取成员
        :param member_info: yaml文件中的用户信息
        :return:
        """
        get_member_url = 'https://qyapi.weixin.qq.com/cgi-bin/user/get'
        params = {
            "userid": member_info["userid"]
        }
        r = self.send("GET", get_member_url, params=params)
        return r.json()

    def update_member(self, member_info, new_name):
        """
        更新成员
        :param member_info: yaml文件中的用户信息
        :param new_name: 更新后的成员姓名
        :return:
        """
        update_member_url = 'https://qyapi.weixin.qq.com/cgi-bin/user/update'
        data = {
            "userid": member_info["userid"],
            "name": new_name,
            "mobile": member_info["mobile"]
        }
        r = self.send("POST", url=update_member_url, json=data)
        return r.json()

    def delete_member(self, member_info):
        """
        删除成员
        :param member_info: yaml文件中的用户信息
        :return:
        """
        delete_member_url = 'https://qyapi.weixin.qq.com/cgi-bin/user/delete'
        params = {
            "userid": member_info["userid"]
        }
        r = self.send("GET", url=delete_member_url, params=params)
        return r.json()

