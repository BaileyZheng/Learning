# install 错误

错误描述：
```
  E: Could not get lock /var/lib/dpkg/lock - open (11: Resource temporarily unavailable)
  E: Unable to lock the administration directory (/var/lib/dpkg/), is another process using it?
```

错误原因：

  此时apt还在运行


解决方案：

找到并杀死所有apt-get的apt进程
```
  ps -A | grep apt
  sudo kill -SIGKILL processnumber
```

参考链接：https://blog.csdn.net/u011596455/article/details/60322568
