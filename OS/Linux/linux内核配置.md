## 步骤
- 下载内核：https://www.kernel.org/
- tar xvJf linux-4.16.11.tar.xz -C /usr/src/
- make menuconfig
- make
- make modules_install
- make install
- cat /boot/grub2/grub.cfg
- grub2-set-default 'CentOS Linux (4.16.11) 7 (Core)'
- grub2-editenv list

## 参考
[1] https://blog.csdn.net/mrzhouxiaofei/article/details/79140435
