# Docker的安装与运行
## 安装Docker

环境
  - 管理工具：Docker Engine
  - runtime：runc
  - 操作系统：ubuntu16.04

Docker支持几乎所有的Linux发行版，也支持Mac和Windows。

各个操作系统的安装方法链接：https://docs.docker.com/engine/installation/

Docker分为开源免费的CE（Community Edition）版本和收费的EE（Enterprise Edition）版本，这里安装的是Docker CE版。

## 配置Docker的apt源
* 安装包，允许apt命令HTTPS访问Docker源。
```
  $ sudo apt-get install apt-transport-https ca-certificates curl software-properties-common
```
* 添加Docker官方的GPG
```
  $ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```
* 将Docker的源添加到/etc/apt/sources.list
```
  $ sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
```
* 安装Docker
```
  $ sudo apt-get update
  $ sudo apt-get install docker-ce
```

## 运行Docker
root下执行命令
```
  # docker run -d -p 80:80 httpd
```
过程描述：
- 从Docker Hub下载httpd镜像。镜像中已经安装好了Apache HTTP Server。
- 启动httpd容器，并将容器的80端口映射到host的80端口。

接下来可以通过浏览器验证容器是否正常工作，在浏览器中输入http://[your ubuntu host IP]，如果出现"it works"字样，则说明可以访问容器的http服务了，容器运行成功。

## 镜像下载加速
由于Docker Hub的服务器在国外，下载镜像会比较慢，DaoCloud提供了免费的国内镜像服务。

使用镜像服务：
- 在daocloud.io免费注册一个用户
- 登陆后，点击顶部菜单“加速器”
- 拷贝“加速器”命令并在host中执行
- 重启Docker deamon
  ```
    # systemctl restart docker.service
  ```
