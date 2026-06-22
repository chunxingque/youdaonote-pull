
```bash
apt-get update -y
apt-get upgrade
sudo apt install xfce4
sudo apt install xrdp
sudo systemctl enable xrdp.service
sudo adduser xrdp ssl-cert
sudo ufw allow 3389
echo "startxfce4" > ~/.xsession
chmod +x ~/.xsession
systemctl restart xrdp.service
passwd ubuntu #为ubuntu这个账户设置好密码
sudo update-alternatives --config x-session-manager  #选择startxfce4
sudo reboot
sudo apt install chromium-browser
```


下面的都不行
---
谷歌搜索 xrdp kde ubuntu


KDE安装



sudo useradd redstoneleo
sudo passwd redstoneleo
=redstone<>?



sudo chmod -R 777 "/etc/xrdp/xrdp.ini"

