import requests
from HogwartsLG6.taskwork.stage17_platform.backend.backend import db, Suite, Case


def test_db_init():
    # 数据库创建表
    db.create_all()

    # 添加测试套件数据
    suite_login = Suite(suite_name='测试套件_登录', suite_desc='该测试套件的用例用于验证登录功能')
    suite_search = Suite(suite_name='测试套件_搜索', suite_desc='该测试套件的用例用于验证搜索功能')
    db.session.add(suite_login)
    db.session.add(suite_search)
    db.session.commit()

    # 添加测试用例数据
    case_login_success = Case(case_name='登录成功', case_desc='验证登录成功', case_steps='步骤1.步骤2.步骤3', suite_id=1)
    case_login_fail = Case(case_name='登录失败', case_desc='验证登录失败', case_steps='步骤1.步骤2.步骤3', suite_id=1)
    case_search_success = Case(case_name='模糊查询', case_desc='验证模糊查询', case_steps='步骤1.步骤2.步骤3', suite_id=2)
    db.session.add(case_login_success)
    db.session.add(case_login_fail)
    db.session.add(case_search_success)
    db.session.commit()


def test_cases_get():
    r = requests.get('http://127.0.0.1:5000/testcase')
    size_origin = len(r.json())
    print(f'初始用例数size_origin：{size_origin}')
    print(repr(r.json()))   # 此处不加repr输出结果也一样


def test_cases_post():
    r = requests.get('http://127.0.0.1:5000/testcase')
    size_origin = len(r.json())
    print(f'初始用例数size_origin：{size_origin}')
    r = requests.post(
        'http://127.0.0.1:5000/testcase',
        json={
            'case_name': '按用例名查询',
            'case_desc': '验证按用例名查询',
            'case_steps': '步骤1.步骤2.步骤3',
            'suite_id': 2,
            'case_remark': '新增用例'
        }
    )
    assert r.status_code == 200

    r = requests.get('http://127.0.0.1:5000/testcase')
    size_add = len(r.json())
    print(f'新增用例后用例数size_add：{size_add}')
    assert size_add == size_origin + 1


def test_testcase_update():
    r = requests.get('http://127.0.0.1:5000/testcase')
    size_origin = len(r.json())
    print(f'初始用例数size_origin：{size_origin}')
    r = requests.put(
        'http://127.0.0.1:5000/testcase',
        params={'case_name': '按用例名查询'},
        json={
            'case_name': '按用例名查询',
            'case_desc': '验证按用例名查询',
            'case_steps': '步骤1.步骤2.步骤3',
            'suite_id': 2,
            'case_remark': '修改用例eweqwe'
        }
    )
    assert r.status_code == 200

    r = requests.get('http://127.0.0.1:5000/testcase')
    size_new = len(r.json())
    assert size_new == size_origin


def test_cases_delete():
    r = requests.get('http://127.0.0.1:5000/testcase')
    size_origin = len(r.json())
    print(f'初始用例数size_origin：{size_origin}')
    requests.delete('http://127.0.0.1:5000/testcase', params={'case_name': '按用例名查询'})
    r = requests.get('http://127.0.0.1:5000/testcase')
    size_del = len(r.json())
    print(f'删除用例后用例数size_del：{size_del}')
    assert size_del == size_origin - 1


def test_relationship_cases():
    cst = Suite(suite_name='测试套件_提交', suite_desc='该测试套件的用例用于验证提交功能')

    # 关联方式A新增用例
    Case(case_name='提交失败_用户名错误', case_desc='关联测试套用例_方式A', suite=cst)
    Case(case_name='提交失败_密码错误', case_desc='关联测试套用例_方式A', suite=cst)

    # 关联方式B新增用例
    yl1 = Case(case_name='提交成功', case_desc='关联测试套件用例_方式B')
    cst.case.append(yl1)

    db.session.add(cst)
    db.session.commit()
