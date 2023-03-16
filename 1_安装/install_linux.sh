#!/bin/bash
# 以下载安装2.3.2版本为例
# 设置IP代理（可选）
ip=xxx
set http_proxy=$ip
set https_proxy=$ip

# 同步时间
timedatectl set-timezone Asia/Shanghai

# 下载
wget https://github.com/prometheus/prometheus/releases/download/v2.3.2/prometheus-2.3.2.linux-amd64.tar.gz

# 解压
tar -zxvf prometheus-2.3.2.linux-amd64.tar.gz

# 移动文件到/usr/local
cp prometheus-2.3.2.linux-amd64/prometheus /usr/local/bin/
cp prometheus-2.3.2.linux-amd64/promtool /usr/local/bin/

# 输出版本信息
prometheus --version
