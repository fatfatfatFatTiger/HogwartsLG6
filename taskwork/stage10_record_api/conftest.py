import allure
import pytest
import requests
import yaml

# 打开yaml文件，读取数据
with open('../datas/info.yml', 'r', encoding='utf-8') as f:
    f = yaml.safe_load(f)
    company_id = f["CompanyInfo"]["company_id"]
    company_secret = f["CompanyInfo"]["company_secret"]
    create_datas = f["CreateMemberInfo"]["datas"]
    create_ids = f["CreateMemberInfo"]["ids"]
    get_datas = f["GetMemberInfo"]["datas"]
    get_ids = f["GetMemberInfo"]["ids"]
    update_datas = f["UpdateMemeberInfo"]["datas"]
    update_ids = f["UpdateMemeberInfo"]["ids"]
    delete_datas = f["DeleteMemeberInfo"]["datas"]
    delete_ids = f["DeleteMemeberInfo"]["ids"]


# 获取企业微信的access_token
@pytest.fixture(scope='class')
def get_assess_token():
    get_token_url = f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={company_id}&corpsecret={company_secret}'
    r = requests.get(url=get_token_url)
    return r.json()["access_token"]


# 获取用于创建成员的测试数据
@pytest.fixture(scope='class', params=create_datas, ids=create_ids)
def get_create_info(request):
    data = request.param
    print(f"测试数据为：{data}")
    yield data


# 获取用于读取成员的测试数据
@pytest.fixture(scope='class', params=get_datas, ids=get_ids)
def get_query_info(request):
    data = request.param
    print(f"测试数据为：{data}")
    yield data


# 获取用于更新成员的测试数据
@pytest.fixture(scope='class', params=update_datas, ids=update_ids)
def get_update_info(request):
    data = request.param
    print(f"测试数据为：{data}")
    yield data


# 获取用于删除成员的测试数据
@pytest.fixture(scope='class', params=delete_datas, ids=delete_ids)
def get_delete_info(request):
    data = request.param
    print(f"测试数据为：{data}")
    yield data
