# -*- coding: utf-8 -*-

import allure
import pytest


@allure.feature("测试计算器")
class TestCalc:
    """
    优化点：
    1.把 setup 和 teardown 换成 fixture 方法 get_calc
    2.把 get_calc 方法放到 conftest 中
    3.把参数化换成了 fixture参数化方式
    4.测试用例中的数据需要通过 get_datas 获取
    get_datas 返回一个列表[0.1,0.2,0.3]，分别代表了a,b,expect
    """

    @allure.story("测试加法")
    @pytest.mark.run(order=1)
    def test_add(self, get_calc1, get_add_datas):
        with allure.step("计算两个数相加和"):
            result = get_calc1.add(get_add_datas[0], get_add_datas[1])
        if isinstance(result, float):
            result = round(result, 2)
        assert result == get_add_datas[2]

    @allure.story("测试除法")
    def test_div(self, get_calc1, get_div_datas):
        with allure.step("计算两个数相除商"):
            result = get_calc1.div(get_div_datas[0], get_div_datas[1])
        if isinstance(result, float):
            result = round(result, 2)
        assert result == get_div_datas[2]

    @allure.story("测试减法")
    @pytest.mark.second
    def test_sub(self, get_calc1, get_sub_datas):
        with allure.step("计算两个数相减差"):
            result = get_calc1.sub(get_sub_datas[0], get_sub_datas[1])
        if isinstance(result, float):
            result = round(result, 2)
        assert result == get_sub_datas[2]

    @allure.story("测试乘法")
    @pytest.mark.run(order=3)
    def test_mul(self, get_calc1, get_mul_datas):
        with allure.step("计算两个数相乘积"):
            result = get_calc1.mul(get_mul_datas[0], get_mul_datas[1])
        if isinstance(result, float):
            result = round(result, 2)
        assert result == get_mul_datas[2]
