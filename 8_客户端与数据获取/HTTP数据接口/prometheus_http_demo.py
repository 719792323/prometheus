import requests
# 可以向prometheus的apiserver拉取数据，url地址是http://prometheus服务地址/api/v1/query?query=promql
# 查询结果将以json数据的格式返回，其中value有两个值，第一个值是时间戳，第二个值是具体值
# "value": [ 1678956118.381,"8182.93"]
# 如下使用requests向prometheus获取node_cpu_seconds_total的代码
if __name__ == '__main__':
    # 设置Prometheus的URL
    prometheus_url = 'http://192.168.56.128:9090'

    # 设置Prometheus查询语句
    prometheus_query = 'node_cpu_seconds_total'

    # 发送GET请求到Prometheus，并获取响应
    response = requests.get(prometheus_url + '/api/v1/query', params={'query': prometheus_query})

    # 检查HTTP状态码是否为200
    if response.status_code == 200:
        # 提取响应中的JSON数据
        json_data = response.json()
        print(json_data)
    else:
        print('Error:', response.status_code)
