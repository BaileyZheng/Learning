
## 步骤
```
# rpm -import https://www.elrepo.org/RPM-GPG-KEY-elrepo.org
# rpm -Uvh http://www.elrepo.org/elrepo-release-7.0-2.el7.elrepo.noarch.rpm
# yum --disablerepo="*" --enablerepo="elrepo-kernel" list available
# yum -y --enablerepo=elrepo-kernel install kernel-ml.x86_64 kernel-ml-devel.x86_64 
cat /boot/grub2/grub.cfg
grub2-set-default 'CentOS Linux (4.16.9-1.el7.elrepo.x86_64) 7 (Core)'
grub2-editenv list
reboot
```
## 参考
[1] https://www.centos.bz/2017/08/upgrade-centos-7-6-kernel-to-4-12-4/
[2] https://www.htcp.net/3425.html
