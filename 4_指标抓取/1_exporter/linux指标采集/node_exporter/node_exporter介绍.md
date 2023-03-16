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

# 指定抓取参数
可以通过配置 node_exporter 的命令行参数来控制它采集哪些指标。具体来说，可以使用 --collector.disable-defaults 参数来禁用默认采集器，并使用 --collector.<collector-name> 参数来启用或禁用特定的采集器。例如，以下命令将禁用所有默认采集器，只启用 cpu 和 diskstats 采集器：
node_exporter --collector.disable-defaults --collector.cpu --collector.diskstats

# 精确抓取某参数方法
如：只想抓取node_cpu_seconds_total
方案1：使用prometheus的metric_relabel_configs或者relabel_configs

# textfile使用
可以使用 --collector.textfile.directory 参数来指定一个目录，让 node_exporter **定期扫描该目录下的**.prom 文件，并将其中定义的指标暴露出去。
因此，可以编写一个脚本或者程序，定期将指定的指标输出到该目录下的 .prom 文件中，然后让 node_exporter 采集该目录下的指标即可。例如，以下命令将指定一个目录 /path/to/my/metrics，并将其中定义的指标暴露出去：
node_exporter --collector.textfile.directory /path/to/my/metrics
假如在该目录下放置一个meta.prom文件
meta.prom:
metadata{role="sj",datacenter="NJ"} 1
启动命令：
node_exporter --collector.textfile.directory /path/to/my/metrics
成功后可以在prometheus看到该数据
注意：**数据需要覆盖式写入**，即假如数据值变成2了
需要用echo metadata{role="sj",datacenter="NJ"} 2 > /path/to/my/metrics/meta.prom
