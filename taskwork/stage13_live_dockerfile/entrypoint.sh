#!/bin/sh

# 设置一个目录保存项目文件
mkdir /opt/project
cd /opt/project
# 进入指定目录后，从github克隆项目
git clone git://github.com/ycwdaaaa/holmes.git
cd holmes
# 进入项目文件目录后，安装相关依赖
pip install -r requirement.txt

# 之前设置了软链接将默认python环境指向python3，此处可以直接使用python3来执行python文件
python3 app.py

