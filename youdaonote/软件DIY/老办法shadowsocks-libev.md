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



上面搞完不行的话就用下面的重启一下；换成444端口后正常了

sudo systemctl restart shadowsocks-libev.service



客户端连接改一下server_port 端口号、密码



sudo systemctl stop shadowsocks-libev.service











===========BBR加速

sudo wget –no-check-certificate https://github.com/teddysun/across/raw/master/bbr.sh

sudo  chmod +x bbr.sh

sudo  ./bbr.sh



验证当前TCP控制算法的命令：

sysctl net.ipv4.tcp_available_congestion_control 



返回值含有bbr就ok



验证BBR是否已经启动。

sysctl net.ipv4.tcp_congestion_control 



返回值一般为：

net.ipv4.tcp_congestion_control = bbr





