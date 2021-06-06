# 基础镜像使用centos7，本来可以直接使用Python镜像，但一直没装上git
FROM centos:7

# 添加启动脚本到root目录，设置工作目录后，可使用 COPY . . ，将当前目录所有文件拷贝到指定工作目录
ADD entrypoint.sh /root

# 设置工作目录为root
WORKDIR /root

# 设置用户为root
USER root

# 安装python相关环境
RUN yum install -y epel-release \
    && yum install -y python36 git python36-setuptools python36-devel.x86_64 \
    && easy_install-3.6 pip 

# 设置软链接将默认python环境指向python3
RUN ln -sf /usr/bin/python3.6 /usr/bin/python3

# 安装python3对应pip，用于安装项目里需要的依赖文件
RUN python3 -m pip install --upgrade pip

# 执行启动脚本
ENTRYPOINT ["/root/entrypoint.sh"]

