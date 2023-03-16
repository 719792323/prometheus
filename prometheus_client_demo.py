# pip install prometheus_client
# 如下定义了一个 Summary 类型的指标
# request_processing_seconds，用于记录请求处理时间。
# 然后使用 start_http_server 函数启动了一个 HTTP 服务器，监听 8000 端口。
# 最后在 while 循环中模拟请求处理，调用 process_request 函数并记录指标数据。
# 在浏览器中访问 http://localhost:8000/metrics 即可查看导出的指标数据。可以看到类似如下的指标数据：
# request_processing_seconds_count 223
# request_processing_seconds_sum 123.456

from prometheus_client import start_http_server, Summary,Gauge
import random
import time

# 定义一个 Summary 类型的指标，用于记录请求处理时间
# REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')
REQUEST_TIME = Gauge('request_processing_seconds', 'Time spent processing request')

# 模拟请求处理
@REQUEST_TIME.time()
def process_request(t):
    time.sleep(t)


if __name__ == '__main__':
    # 启动 HTTP 服务器，监听 8000 端口
    start_http_server(8000)

    # 模拟请求处理，记录指标数据
    while True:
        process_request(random.random())

