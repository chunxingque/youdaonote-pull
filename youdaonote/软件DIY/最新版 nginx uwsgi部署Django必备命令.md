 ​后期更改只要这些操作
<font color= "#0089FB">sudo chmod -R 777 /home/ubuntu/LYYDownloaderServer/; </font>
<font color= "#0089FB">**cd /home/ubuntu/LYYDownloaderServer/&&source SiteEnv/bin/activate**</font><font color= "#0089FB">; git fetch origin;git reset --hard origin/master;sudo systemctl daemon-reload;</font>sudo systemctl restart celery<font color= "#0089FB">;</font><font color= "#87C120">python manage.py makemigrations; python manage.py migrate; </font>python manage.py collectstatic --noinput; pkill -f uwsgi -9; uwsgi --ini uwsgi.ini; sudo systemctl restart nginx

---
~~mkdir /home/ubuntu/LYYDownloaderServer;cd /home/ubuntu/LYYDownloaderServer;sudo chmod -R 777 /home/ubuntu/LYYDownloaderServer/~~
<font color= "#F33232">不要以root登陆</font>
<font color= "#F33232">su - ubuntu</font>

C:\Users\22815\.ssh
upload the key to /home/ubuntu/.ssh/

chmod 600 ~/.ssh/id_rsa
chmod 700 ~/.ssh

如果还没有仓库： 
cd /home/ubuntu 
git clone git@github.com:redstoneleo/LYYDownloaderServer.git
如果已经有仓库： 
cd /home/ubuntu/LYYDownloaderServer
git fetch origin 
git reset --hard origin/master

开放所有端口
iptables -P INPUT ACCEPT;iptables -P FORWARD ACCEPT; iptables -P OUTPUT ACCEPT; iptables -F

cd /home/ubuntu/LYYDownloaderServer

sudo apt update && sudo apt upgrade;timedatectl set-timezone Asia/Shanghai

curl -LsSf [https://astral.sh/uv/install.sh](https://astral.sh/uv/install.sh) | sh


uv python install 3.12
uv python find 3.12
uv venv SiteEnv --python 3.12
sudo apt-get install rabbitmq-server  -y
sudo apt install ffmpeg -y


*~~改配置端口修改这个文件，如果改后连不上请确保端口打开和重启恢复~~*
*~~sudo chmod -R 777 /etc/ssh/~~*
*~~/etc/ssh/sshd_config 的 Port 22 为20022~~*

~~*sudo nano /etc/ssh/sshd_config*~~
~~*CTRL + O saves a Nano file*~~
~~*Enter一下*~~
~~*CTRL + X exits Nano*~~
~~*sudo systemctl restart ssh*~~


[https://github.com/mack-a/v2ray-agent](https://github.com/mack-a/v2ray-agent)
[https://github.com/233boy/v2ray/wiki/V2Ray%E4%B8%80%E9%94%AE%E5%AE%89%E8%A3%85%E8%84%9A%E6%9C%AC#](https://github.com/233boy/v2ray/wiki/V2Ray%E4%B8%80%E9%94%AE%E5%AE%89%E8%A3%85%E8%84%9A%E6%9C%AC#)~~<font color= "#F33232">安装</font>~~
~~<font color= "#F33232">v2ray add tcpd</font>~~

sudo apt install -y cron plocate


**<font color= "#FF0001">cd /home/ubuntu/LYYDownloaderServer/; source SiteEnv/bin/activate</font>**
<u>（前面不能有sudo,you should use the pip command (not pip3)）</u>:
uv pip install -U spylls azure-cognitiveservices-speech peewee google-genai pydub  azure-identity pydub edge_tts django-celery-results celery  uwsgi django markdown-it-py[plugins]   requests django_apscheduler m3u8 beautifulsoup4 djangorestframework google-genai peewee django-allauth[socialaccount] openai

mkdir -p /home/ubuntu/LYYDownloaderServer/{run,logs,media}

测试
~~sudo chmod -R 777 /home/ubuntu/LYYDownloaderServer/;~~ cd /home/ubuntu/LYYDownloaderServer/&&source SiteEnv/bin/activate; **python manage.py makemigrations; python manage.py migrate; python manage.py collectstatic --noinput;python manage.py runserver 0.0.0.0:8000**
~~sudo chmod -R 777 /home/ubuntu/LYYDownloaderServer/     （首次运行必须有）~~

sudo apt install nginx -y
sudo sed -i 's/^user.*/user ubuntu;/' /etc/nginx/nginx.conf; sudo systemctl restart nginx

sudo chmod -R 777 **/etc/nginx/conf.d/; **cd **/etc/nginx/conf.d/; **
**添加 /etc/nginx/conf.d/LYYDownloaderServer.conf**
sudo systemctl restart nginx

测试用：
cd /home/ubuntu/LYYDownloaderServer/&&source SiteEnv/bin/activate; uwsgi --http :8000 --chdir=/home/ubuntu/LYYDownloaderServer --module=LYYDownloaderServer.wsgi:application  --env DJANGO_SETTINGS_MODULE=LYYDownloaderServer.settings  --master --pidfile=/home/ubuntu/LYYDownloaderServer/LYYDownloaderServer.pid  --harakiri=20 --vacuum --processes=1 --max-requests=5000 --uid=505 --gid=505 --daemonize=/home/ubuntu/LYYDownloaderServer/LYYDownloaderServer_uwsgi.log


---
<font color= "#F33232">处理</font><font color= "#F33232">**ssl============**</font>
sudo apt install snapd
sudo apt-get remove certbot
sudo snap install --classic certbot
sudo certbot --nginx
sudo certbot renew --dry-run

卸载
sudo snap remove certbot

------**然后接着下面的（有问题就执行下面这一条）**

ipconfig/flushdns
**/etc/supervisor/conf.d/iMathSites.conf**
添加ipv4
wget -N [https://gitlab.com/fscarmen/warp/-/raw/main/menu.sh](https://gitlab.com/fscarmen/warp/-/raw/main/menu.sh) && bash menu.sh 4

<font color= "#333333">chrome://net-internals/#hsts 点击”Domain Security Policy” 页面拉直最底部,在”Delete domain security policies”部分中的”Domain”框中,输入想去掉”HTTPS”协议访问的网址</font>

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
sudo chmod -R 777  "/var/log/nginx/error.log"

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


