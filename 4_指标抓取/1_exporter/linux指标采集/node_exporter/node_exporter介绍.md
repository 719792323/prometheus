[node_exporter的github地址](https://github.com/prometheus/node_exporter)
# 下载
NodeExporter用于采集 Linux 系统的指标，如 CPU 使用率、内存使用率、磁盘空间使用率等。
```shell
# 下载
#set http_proxy=192.168.0.233:7890
#set https_proxy=192.168.0.233:7890
wget https://github.com/prometheus/node_exporter/releases/download/v1.5.0/node_exporter-1.5.0.linux-amd64.tar.gz
# 解压
tar -zxvf node_exporter-1.5.0.linux-amd64.tar.gz 
# 查看版本
cd node_exporter-1.5.0.linux-amd64/ && node_exporter --version
```
# 启动与参数
0. prometheus.yml中配置node_exporter
1. 启动
```shell
./node_exporter 
```
2. 一些可以指定的参数
--web.listen-address=":port" 指定运行端口，默认是9100
--web.telemetry-path="/xx" 指定提取数据路径，默认是/metrics
--collectors.enabled 指定node_exporter收集的功能模块
--no-collector 指定不需要的模块，如--no-collector.arp，不收集arp数据


