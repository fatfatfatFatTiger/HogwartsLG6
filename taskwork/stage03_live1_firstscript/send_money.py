"""
课后作业
原有存款 1000元， 发工资之后存款变为2000元
定义模块
1、money.py saved_money = 1000
2、定义发工资模块 send_money，用来增加收入计算
3、定义工资查询模块 select_money，用来展示工资数额
4、定义一个start.py ，启动文件展示最终存款金额
"""

import money


def add_money(salary):
    money.saved_money += salary
    return money.saved_money


if __name__ == "__main__":
    monthly_salary = 1000
    print(f"当月发工资 {monthly_salary} 元")
    now_money = add_money(monthly_salary)
    print(f"发工资后存款为 {now_money} 元")


