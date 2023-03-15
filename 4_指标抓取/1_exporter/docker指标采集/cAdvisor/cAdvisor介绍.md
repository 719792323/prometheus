# cAdvisor功能
cAdvisor（Container Advisor）是由 Google 开发的一个开源工具，用于监控和分析容器的资源使用情况和性能指标，如 CPU、内存、磁盘和网络等方面的数据。它支持 Docker 和 Kubernetes 等容器平台，可以提供精细的容器性能指标和资源利用率分析，帮助用户更好地理解和优化容器应用程序的性能。
cAdvisor支持以下功能：
* 监控容器的资源使用情况和性能指标，包括 CPU、内存、磁盘和网络等方面的数据。
* 提供容器的实时性能数据和历史数据，用户可以查看容器的 CPU 使用率、内存使用率、网络传输速率等数据。
* 支持容器的自动发现和监控，无需手动配置。
* 提供 REST API 和 Web UI 接口，方便用户查看容器的监控数据和分析结果。
* 支持与 Prometheus 等监控系统集成，用户可以将 cAdvisor 采集的数据导入到监控系统中进行分析和展示。
# 安装使用
1. prometheus.yml中配置cadvisor
2. 运行
```shell
docker run \
  --volume=/:/rootfs:ro \
  --volume=/var/run:/var/run:rw \
  --volume=/sys:/sys:ro \
  --volume=/var/lib/docker/:/var/lib/docker:ro \
  --volume=/dev/disk/:/dev/disk:ro \
  --publish=8080:8080 \
  --detach=true \
  --name=cadvisor \
  google/cadvisor:latest
```
3. 监控具体某容器
* 如查看容器名叫mysql的容器内存使用情况
promql=container_memory_usage_bytes{name="mysql"}
* cpu使用率
这个表达式会计算在过去 1 分钟内，容器的 CPU 使用率。rate() 函数会计算时间序列的变化率，因此我们需要将总的 CPU 使用时间除以时间范围，得到每秒的 CPU 使用时间，然后将结果乘以 100，将结果转换为百分比形式。
rate(container_cpu_usage_seconds_total{name="mysql"}[1m]) * 100