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
import select_money
import send_money

if __name__ == "__main__":
    old_money = money.saved_money
    print(f"原有存款为 {old_money} 元")

    monthly_salary = select_money.query_salary(1000)
    print(f"当月发工资 {monthly_salary} 元")

    new_money = send_money.add_money(monthly_salary)
    print(f"发工资后存款为 {new_money} 元")
