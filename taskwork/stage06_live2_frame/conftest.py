# -*- coding: utf-8 -*-
# @File : conftest.py
# @Author : Elf
# @Time : 2021/3/14 9:41


import logging

root_log = logging.getLogger(__name__)

logging.basicConfig(level=logging.INFO,
                    # 日志格式
                    # 时间、代码所在文件名、代码行号、日志级别名字、日志信息
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    # 打印日志的时间
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    # 日志文件存放的目录（目录必须存在）及日志文件名
                    filename='../logs/run_testcase.log',
                    # 打开日志文件的方式，a表示追加，+表示可读
                    filemode='a+'
                    )
