sudo supervisord -c "/home/ubuntu/LYYDownloaderServer/LYYDownloaderServer_supervisord.conf"

sudo supervisorctl update all

sudo supervisorctl status all

---



supervisorctl stop all





pip3 install supervisor apscheduler  django-apscheduler



INSTALLED_APPS = (


    # ...


    "django_apscheduler",


)



sudo python3 manage.py migrate



copy FinancialChartsWebsite\FinancialCharts\management\commands  修改



sudo echo_supervisord_conf > supervisord.conf



edit the supervisord.conf

```javascript
[program:django_apscheduler]
command=sudo python3 /www/wwwroot/usdcc.net/FinancialChartsWebsite/manage.py runapscheduler

[supervisord]
user=root

[supervisorctl]

[inet_http_server]
port = 127.0.0.1:9001

[rpcinterface:supervisor]
supervisor.rpcinterface_factory = supervisor.rpcinterface:make_main_rpcinterface
```

sudo systemctl restart apache2



supervisord







supervisor.log



如果出现端口占用就看这里

https://stackoverflow.com/a/51970201







https://github.com/jcass77/django-apscheduler

http://supervisord.org/installing.html



