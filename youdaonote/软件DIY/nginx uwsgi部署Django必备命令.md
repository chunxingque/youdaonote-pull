 ​后期更改只要这些操作
sudo su -
~~sudo chmod -R 777 /home/ubuntu/LYYDownloaderServer/; sudo chmod -R 777 /home/ubuntu/; sudo chmod -R 777 /home/;~~cd /home/ubuntu/LYYDownloaderServer/&&source SiteEnv/bin/activate; python manage.py makemigrations; python manage.py migrate; python manage.py collectstatic --noinput; pkill -f uwsgi -9; uwsgi --ini uwsgi.ini; sudo systemctl restart nginx

---
mkdir /home/ubuntu/LYYDownloaderServer;cd /home/ubuntu/LYYDownloaderServer;sudo chmod -R 777 /home/ubuntu/LYYDownloaderServer/
第一步上传代码

开放所有端口
iptables -P FORWARD ACCEPT; iptables -P OUTPUT ACCEPT; iptables -F

sudo apt-get update;timedatectl set-timezone Asia/Shanghai

*~~改配置端口修改这个文件，如果改后连不上请确保端口打开和重启恢复~~*
*~~sudo chmod -R 777 /etc/ssh/~~*
*~~/etc/ssh/sshd_config 的 Port 22 为20022~~*

~~*sudo nano /etc/ssh/sshd_config*~~
~~*CTRL + O saves a Nano file*~~
~~*Enter一下*~~
~~*CTRL + X exits Nano*~~
~~*sudo systemctl restart ssh*~~


[https://github.com/mack-a/v2ray-agent](https://github.com/mack-a/v2ray-agent)
[https://github.com/233boy/v2ray/wiki/V2Ray%E4%B8%80%E9%94%AE%E5%AE%89%E8%A3%85%E8%84%9A%E6%9C%AC#](https://github.com/233boy/v2ray/wiki/V2Ray%E4%B8%80%E9%94%AE%E5%AE%89%E8%A3%85%E8%84%9A%E6%9C%AC#)<font color= "#F33232">~~安装~~</font>
<font color= "#F33232">v2ray add tcpd</font>

sudo apt-get install -y mlocate python3-pip cron socat
sudo pip3 install virtualenv

cd /home/ubuntu/LYYDownloaderServer/; virtualenv SiteEnv; source SiteEnv/bin/activate
<u>（前面不能有sudo,you should use the pip command (not pip3)）</u>:
pip install -U  markdown-it-py[plugins] django uwsgi requests django_apscheduler m3u8 bs4

测试
~~sudo chmod -R 777 /home/ubuntu/LYYDownloaderServer/;~~ cd /home/ubuntu/LYYDownloaderServer/&&source SiteEnv/bin/activate; python manage.py makemigrations; python manage.py migrate; python manage.py collectstatic --noinput;python manage.py runserver 0.0.0.0:8000
~~sudo chmod -R 777 /home/ubuntu/LYYDownloaderServer/     （首次运行必须有）~~

pkill -f uwsgi -9; uwsgi --ini uwsgi.ini; 

sudo apt install nginx -y
sudo sed -i 's/^user.*/user ubuntu;/' /etc/nginx/nginx.conf; sudo systemctl restart nginx

sudo chmod -R 777 **/etc/nginx/conf.d/; **cd **/etc/nginx/conf.d/; **
**添加 /etc/nginx/conf.d/LYYDownloaderServer.conf**


~~测试用：~~
~~cd /home/ubuntu/LYYDownloaderServer/&&source SiteEnv/bin/activate; ~~

~~uwsgi --http :8000 --module LYYDownloaderServer.wsgi  --chdir=/home/ubuntu/LYYDownloaderServer --module=LYYDownloaderServer.wsgi:application  --env DJANGO_SETTINGS_MODULE=LYYDownloaderServer.settings  --master --pidfile=/home/ubuntu/LYYDownloaderServer/LYYDownloaderServer.pid  --http :8000 --harakiri=20 --vacuum --processes=1 --max-requests=5000 --uid=505 --gid=505 --daemonize=/home/ubuntu/LYYDownloaderServer/LYYDownloaderServer_uwsgi.log~~


openssl dhparam -out /home/ubuntu/LYYDownloaderServer/ssl/dhparam.pem 2048
wget -O -  [https://get.acme.sh](https://get.acme.sh) | sh -s email=redstone-cold@163.com
安装好后退出终端然后重新登陆
acme.sh --upgrade
ECC证书申请：
acme.sh --register-account -m redstone-cold@163.com
~~sudo systemctl stop nginx~~
仅更新的时候用acme.sh --renew -d mathjoy.qthome.org --force --ecc

~~export CF_Key="41b1cd6a3b55991a751de62483b6db4084cb4"; export CF_Email="redstone-cold@163.com"; acme.sh --issue --dns dns_cf -d mathjoy.qthome.org  --server letsencrypt~~
acme.sh --issue --standalone -d mathjoy.qthome.org

acme.sh --install-cert -d mathjoy.qthome.org --ecc --key-file       /home/ubuntu/LYYDownloaderServer/ssl/domain.key  --fullchain-file /home/ubuntu/LYYDownloaderServer/ssl/fullchain.cer --cert-file            /home/ubuntu/LYYDownloaderServer/ssl/ca.cer --reloadcmd     "service nginx force-reload"

------**然后接着下面的（有问题就执行下面这一条）**

~~sudo chmod -R 777 /home/ubuntu/LYYDownloaderServer/; sudo chmod -R 777 /home/ubuntu/; sudo chmod -R 777 /home/~~
cd /home/ubuntu/LYYDownloaderServer/&&source SiteEnv/bin/activate; python manage.py makemigrations; python manage.py migrate; python manage.py collectstatic --noinput; pkill -f uwsgi -9; uwsgi --ini uwsgi.ini; sudo systemctl restart nginx

ipconfig/flushdns
**/etc/supervisor/conf.d/iMathSites.conf**

---
解决端口占用
sudo fuser -k 443/tcp
```
```

卸载nginx
sudo apt-get remove nginx nginx-common
安装nginx
sudo apt install nginx -y
升级

nginx -t

sudo systemctl status nginx
sudo systemctl stop nginx
sudo systemctl start nginx
sudo systemctl restart nginx

error.log路径 /var/log/nginx/
uninstall-nginx What is the best way to uninstall nginx - Ask Ubuntu



**ssl**
DNS申请方式：（目前暂时不用到自己的网站）
acme.sh --issue --dns -d techjoy.tk  --yes-I-know-dns-manual-mode-enough-go-ahead-please
acme.sh --renew -d techjoy.tk  --yes-I-know-dns-manual-mode-enough-go-ahead-please
acme.sh --install-cert -d techjoy.tk \
--key-file       /home/ubuntu/LYYDownloaderServer/techjoy.tk.key  \
--fullchain-file /home/ubuntu/LYYDownloaderServer/fullchain.cer \
--ca-file        /home/ubuntu/LYYDownloaderServer/ca.cer \
--reloadcmd     "service nginx force-reload"

nginx配置推荐




free net与网站共存的方式
安装 选择3与网站共存

其次是



=====================
开机启动：
"/etc/systemd/system/LYYDownloaderServer.service"

sudo systemctl enable LYYDownloaderServer

sudo systemctl start LYYDownloaderServer & sudo systemctl status LYYDownloaderServer

sudo systemctl status LYYDownloaderServer





Gitea,可能还是要创建git用户





/var/snap/gitea/common/data/gitea-repositories/redstoneleo/

cd /var/snap/gitea/common/data/gitea-repositories/redstoneleo/lyydownloaderserver.git/hooks/


chmod +x "/var/snap/gitea/common/data/gitea-repositories/redstoneleo/lyydownloaderserver.git/hooks/post-receive.d/LYYDownloaderServer"


