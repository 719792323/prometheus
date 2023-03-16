# Grafana的使用
正确安装并启动Grafana后
打开浏览器，访问端口为3000，打开Grafana控制面板，初始默认账号和密码均为 admin，初次登录需要修改密码。

# Centos Grafana安装
1. 更新yum源
yum update
2. 配置grafana的yum源
vim /etc/yum.repos.d/grafana.repo
```properties
[grafana]
name=grafana
baseurl=https://mirrors.aliyun.com/grafana/yum/rpm
repo_gpgcheck=0
enabled=1
gpgcheck=0
```
yum makecache
yum repolist
3. 安装Grafana
yum install -y grafana
4. 查看安装的Grafana版本
rpm -qa | grep grafana
5. 启动Grafana
* systemctl daemon-reload
#启动
* systemctl start grafana-server
#查看Grafana状态
* systemctl status grafana-server
#设置开机启动，如果不需要可以不执行该命令
* systemctl enable grafana-server
#关闭Grafana
* systemctl stop grafana-server