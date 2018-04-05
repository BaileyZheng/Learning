# 安装Docker

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
