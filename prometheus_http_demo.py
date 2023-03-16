import requests

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
