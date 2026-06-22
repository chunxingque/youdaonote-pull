http://www.bioinfo-scrounger.com/archives/490



上次参照的是

https://woobeta.blogspot.com/2018/03/Amazon-aws-shadowsocks.html





---

2019年10月24日

sudo snap install shadowsocks-libev









---





stop实例后下次启动需要设置winscp的主机名称，然后putty里运行

sudo ssserver -c /etc/shadowsocks/config.json -d start



sudo ssserver -c /etc/shadowsocks/config.json -d stop



再重新设置客户端ip，





我填的是443



开启AWS入站端口：在启动实例后，把滚动条滚到最右边，点击安全组下的launch-wizard-1。

![](http://www.uml.org.cn/yunjisuan/images/2018062543.png)

点击操作，编辑入站规则。

![](http://www.uml.org.cn/yunjisuan/images/2018062544.png)



![](attachments/Shadowsocks-libev%20%20AWS搭建_image_0.png)

anywhere





客户端连接改一下server_port 端口号、密码



---



winscp登录界面那里注意看“保存密码”

设置里

![](attachments/Shadowsocks-libev%20%20AWS搭建_image_1.png)











https://www.linuxbabe.com/ubuntu/shadowsocks-libev-proxy-server-ubuntu-16-04-17-10





sudo apt update
sudo apt install -y shadowsocks-libev



/etc/shadowsocks-libev/config.json

服务端一般改下面的

{

    "server":["[::]","0.0.0.0"],

    "server_port":443,

    "local_port":1080,

    "password":"redstone123",

    "timeout":600,

    "method":"chacha20-ietf-poly1305"

}



sudo systemctl start shadowsocks-libev.service

sudo systemctl enable shadowsocks-libev.service

systemctl status shadowsocks-libev.service



换成444端口后正常了

sudo systemctl restart shadowsocks-libev.service



客户端连接改一下server_port 端口号、密码



sudo systemctl stop shadowsocks-libev.service



bbr

https://teddysun.com/489.html



https://github.com/xratzh/CBBR







