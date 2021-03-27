
import requests
import yaml


class Base:
    def __init__(self):
        # 定义一个session
        self.s = requests.Session()
        # 获取access_token
        self.token = self.get_access_token()
        # 将access_token写入session，后续不再利用token登录
        self.s.params = {"access_token": self.token}

    def get_access_token(self):
        """
        读取yaml文件中的公司信息，获取id和secret，
        :return: 用于后续操作的 access_token
        """
        with open('../datas/info.yml', 'r', encoding='utf-8') as f:
            f = yaml.safe_load(f)
        company_id = f["CompanyInfo"]["company_id"]
        company_secret = f["CompanyInfo"]["company_secret"]
        get_token_url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
        params = {
            "corpid": company_id,
            "corpsecret": company_secret
        }
        r = self.send("GET", url=get_token_url, params=params)
        return r.json()["access_token"]

    def send(self, *args, **kwargs):
        """
        封装发送请求的方法
        :param args:
        :param kwargs:
        :return:
        """
        return self.s.request(*args, **kwargs)
