import pytest
import yaml

# 打开yaml文件，读取数据
with open('../datas/info.yml', 'r', encoding='utf-8') as f:
    f = yaml.safe_load(f)
    member_datas = f["MemberInfo"]["datas"]
    member_ids = f["MemberInfo"]["ids"]


# 获取用于创建成员的测试数据
@pytest.fixture(scope='class', params=member_datas, ids=member_ids)
def get_member_info(request):
    data = request.param
    print(f"测试数据为：{data}", type(data))
    yield data
