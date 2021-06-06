# -*- coding: utf-8 -*-
# @File : test_calc.py
# @Author : Elf
# @Time : 2021/2/3 23:24


from HogwartsLG6.taskwork.stage4_record_pytest.common.calc import Calculator
import pytest
import yaml

with open("./datas/calc.yml", encoding='utf-8') as f:
    f = yaml.safe_load(f)

    add = f["add"]
    add_datas = add["datas"]
    add_myid = add["myid"]

    div = f["div"]
    div_datas = div["datas"]
    div_myid = div["myid"]


class TestCalc:
    def setup_class(self):
        print("【开始计算加法和除法】")
        self.calc = Calculator()

    def teardown_class(self):
        print("【加法和除法计算结束】")

    def setup(self):
        print("用例执行开始...")

    def teardown(self):
        print("用例执行结束...")

    @pytest.mark.parametrize(
        'a, b, expect',
        add_datas,
        ids=add_myid
    )
    def test_add(self, a, b, expect):
        result = self.calc.add(a, b)
        if isinstance(result, float):
            result = round(result, 2)
        assert result == expect

    @pytest.mark.parametrize(
        'a, b, expect',
        div_datas,
        ids=div_myid
    )
    def test_div(self, a, b, expect):
        result = self.calc.div(a, b)
        if isinstance(result, float):
            result = round(result, 2)
        assert result == expect


if __name__ == "__main__":
    pass
