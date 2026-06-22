

heroku login

13529123633@139.com

heroku run bash



heroku run python manage.py shell

heroku ps:scale

heroku apps



find / -name "django-server.log"

find / -name "httpd.conf"



you-get -d -u http://tv.sohu.com/20170222/n481440014.shtml



you-get   -d -u "http://v.youku.com/v_show/id_XMTc3MTE4ODM0OA==.html?from=s1.8-1-1.1&spm=a2h0k.8191407.0.0"



ykdl.py -i http://tv.sohu.com/20170222/n481440014.shtml

ykdl.py -i "http://v.youku.com/v_show/id_XMTc3MTE4ODM0OA==.html?from=s1.8-1-1.1&spm=a2h0k.8191407.0.0"



https://www.proxynova.com/proxy-server-list/country-cn/









管理终端连接密码： 254985





requirements.txt 

whitenoise==2.0.6

-e git+https://github.com/redstoneleo/you-get.git#egg=you-get















http://www.iqiyi.com/v_19rro7upa0.html?vfm=2008_aldbd&fc=828fb30b722f3164&fv=p_02_01

you-get下 Qprocess解析不出来，但是subprocess却可以

安装的时候释放you-get，卸载软件的时候清理you-get



加log 统计encoding情况

try:

                parseResult = str(process.readAllStandardOutput(), 'gbk')

            except:

                parseResult = str(process.readAllStandardOutput(), 'utf8')



ykdl#这些站you-get已坏，因为默认优先ykdl解析，所以不不必加

v.pptv.com

tv.cctv.com   

www.iqiyi.com







 'onlineParseSites': ['tv.cctv.com',#本地解析出问题，搞不好只能放在线上 http://tv.cctv.com/2017/02/22/VIDEgReDx3VGvIOZN6sozq3q170222.shtml

 'm.lswuyou.com',#目前仍然是线上解析

], 'vipSites': ['www.iqiyi.com', 'm.lswuyou.com'],





 'youGetParseSites': ['www.tudou.com',#ykdl会出现土豆文件名问题+自动分配

'my.tv.sohu.com'  tv.sohu.com]}#ykdl有解析结果，但是不能下载，http://my.tv.sohu.com/pl/9042850/81274187.shtml

v.qq.com#youget解除了限速，随时检查https://github.com/zhangn1985/ykdl/blob/master/ykdl/extractors/qq/video.py

v.youku.com 自动分配



I parse site



测试bug

Invalid HTTP_HOST header: 'www.sbjudge2.com'. You may need to add 'www.sbjudge2.com' to ALLOWED_HOSTS.



lYYDownloaderClientLog(request):

    print('----666666666666---', request.GET)

http://v.ifeng.com/program/mrmdm/#016bd663-bc8f-4382-8fe7-15c9cf1c75b3





安装Python

https://my.oschina.net/deepblue/blog/550452



wget https://www.python.org/ftp/python/3.6.0/Python-3.6.0.tar.xz

tar Jxvf  Python-3.6.0.tar.xz

cd Python-3.6.0

./configure --enable-shared \
            --prefix=/usr/local \
            LDFLAGS="-Wl,--rpath=/usr/local/lib"\

   --enable-loadable-sqlite-extensions&&make&&make install 



防错

 yum install sqlite* 

yum install sqlite-devel

http://stackoverflow.com/a/24449632/1485853



yum install mod_wsgi

Start up Apache, so that the httpd service will start automatically on a reboot:

sudo service httpd start





LD_LIBRARY_PATH=/usr/local/lib /usr/local/bin/python

/root/Python-3.6.0







scp，sftp，git Samba





返回值建议

update([other]) dict 

>>> parseTools=['ykdl','you-get']

>>> parseTools.remove('ykdl')

>>> parseTools

['you-get']

>>> parseTools.append('ykdl')

>>> parseTools

['you-get', 'ykdl']

>>> 

>>> parseTools.extend('23')

>>> parseTools

['you-get', 'ykdl', '2', '3']

>>> 





>>> from collections import deque



>>> d = deque('ghi')

>>> d[:20]

Traceback (most recent call last):

  File "<pyshell#5>", line 1, in <module>

    d[:20]

TypeError: sequence index must be integer, not 'slice'

























kill pid

http://blog.csdn.net/crazw/article/details/8266751



Add a User to a Group (or Second Group) on Linux

https://www.howtogeek.com/50787/add-a-user-to-a-group-or-second-group-on-linux/





mod_wsgi-express start-server --user imath --group www-data /root/LYYDownloaderServer/LYYDownloaderServer/wsgi.py



mod_wsgi-express start-server --application-type module LYYDownloaderServer.wsgi  --user imath --group www-data --port=80



gunicorn --bind 0.0.0.0:8000 LYYDownloaderServer.wsgi:application



mod_wsgi-express start-server --port 8000 project/wsgi.py





WSGIPythonPath  /root/LYYDownloaderServer

gunicorn  LYYDownloaderServer.wsgi









<VirtualHost *:80> 

ServerName 112.74.98.187

DocumentRoot /root/LYYDownloaderServer

WSGIScriptAlias / /root/LYYDownloaderServer/LYYDownloaderServer/wsgi.py

WSGIDaemonProcess LYYDownloaderServer python-path=/root/LYYDownloaderServer

WSGIProcessGroup LYYDownloaderServer

<Directory /root/LYYDownloaderServer/LYYDownloaderServer>

<Files wsgi.py>

Order deny,allow

Allow from all

</Files>

</Directory>

</VirtualHost> 



re.findall(r'''\s*#匹配换行和空格

[\[']*#匹配you-get解析爱课程、爱奇艺的字符化列表左边['，用括号（['）*的话findall会得出不相干的结果，故而不用

(?P<videoUrls>https?://\S*)#https也可以匹配，加上://是为了尽可能地让匹配到的结果是url（关键是为了排除标题里有http字样的万一情况，所以这里可能出现万一bug），\S match 非空字符

['\]]*''',#匹配you-get解析爱课程、爱奇艺的字符化列表右边']

 parseResult)







        









