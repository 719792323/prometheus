[官网中文文档](https://chaosblade.io/)
# ChaosBlade功能
* 基础资源：比如 CPU、内存、网络、磁盘、进程等实验场景；
* Java 应用：比如数据库、缓存、消息、JVM 本身、微服务等，还可以指定任意类方法注入各种复杂的实验场景；
* C++ 应用：比如指定任意方法或某行代码注入延迟、变量和返回值篡改等实验场景；
* Docker 容器：比如杀容器、容器内 CPU、内存、网络、磁盘、进程等实验场景；
* 云原生平台：比如 Kubernetes 平台节点上 CPU、内存、网络、磁盘、进程实验场景，Pod 网络和 Pod 本身实验场景如杀 Pod，容器的实验场景如上述的 Docker 容器实验场景；

# ChaosBlade下载安装
```shell
wget https://github.com/chaosblade-io/chaosblade/releases/download/v1.7.1/chaosblade-1.7.1-linux-amd64.tar.gz
tar -zxvf chaosblade-1.7.1-linux-amd64.tar.gz
```

# linux负载
全局指标：
* --timeout
## cpu
* cpu-count：指定 CPU 负载的核数；int；仅当cpu-list为空时有效，取值范围为 0-cpu 逻辑核数，默认取值 cpu 逻辑核数
* cpu-list：指定 CPU 负载的具体核，核索引从 0 开始；string；0-3 或 0,3
* cpu-percent：指定 CPU 负载百分比；int；取值范围为0-100，默认为100
* climb-time：指定 CPU 负载爬坡时间，单位秒；int；取值范围为0-600，默认为0
注意：创建多个cpu负载示例，默认只生效cpu-percent最大的那一个。
### 二次函数CPU曲线思路
> ./blade create cpu load --cpu-percent 40 --climb-time 120 --timeout 120;./blade create cpu load --cpu-percent 20 --timeout 160;./blade create cpu load --cpu-percent 10  --timeout 200;
>> 下降曲线不光滑，可以将cpu负载的间隔缩小，相隔负载timeout阶段时间点缩小来解决
### 激凸增长型曲线思路
> ./blade create cpu load --cpu-percent 10 --timeout 10;
十秒后;
./blade create cpu load --cpu-percent 20 --timeout 10;
.... 
### 爬坡增值型曲线思路
> ./blade create cpu load --cpu-percent 10 --climb-time 10 --timeout 10;
十秒后;
./blade create cpu load --cpu-percent 10 --timeout 10;./blade create cpu load --cpu-percent 20 --climb-time 10 --timeout 10
...
## 内存

## 网络

## 文件IO
