  
CDlinux 0.9.7.1  
基于CDlinux 0.9.7.1打包，使用minileaf的spring包无线模块，加入minidwep-gtk，feedingbottle，inflator等无线工具，加入超级权限，将启动调为默认中文  
  
精简保留minidwep-gtk和feedingbottle这两个高质量破解软件，更新feedingbottle到3.1，minidwep-gtk-30131。除原版的600万密码字典外，再在cdlinux\tce\目录下增加千万密码字典。  
**这是一个系统，请用虚拟机运行或刻盘Bios设置光盘启动或U盘启动等**  
  
wep破解我不说了下面我来说如何破解wpa2.我先说下，这是利用WPS(WIFI Protect Setup）的pin码，通过猜pin码连接路由，因为pin码纯数字，所以这样破解的成功率高达90%，只是时间性问题。如果漏码只能说你人品差。。。破了之后无线配置工具一般都有wps功能的。  
  
方法一：使用minidwep-gtk,打开后选加密方式wap/wap2,点扫描，看路由名称、信道后面有没有wps,有的话，点reaver，点ok。之后就是漫长的破解。  
  
方法二：使用inflator1.0，选yes,之后选网卡，再选next，之后选Scan for~~~,选路由，点next，然后勾第一个。点run  
  
由于破解漫长，需要保存进度，文件在/usr/local/etc/reaver/MAC地址.wpc拷贝下来，下次启动替换。  
或创建虚拟机快照，我觉得这个保险

### 破解WEP/WPA/WPA2攻略:

1、用光盘启动Lunux系统在桌面上会有一个 minidwe-gtk 快捷方式。

![](attachments/CDlinux%200.9.7.1基于CDlinux%200.9.7.1打包，使用minileaf的spring包无线模块，加入minidwep-gtk，feeding_image_0.png)

2、启动软件后在加密方式那里选择 wpa/apa2 再接 扫描就可以了。

3、找到无线网络后再点右边的第四个图标“reaver” 启动破解接着会有个对话框，按OK就可以了。

4、接着会出理一个窗口 This window wii appear 就等丰他破解吧，运气好的话数十分钟就可以破解了  
  
 

最好是用虚拟机( <http://www.sd173.com/html/122.html>)来加载 iso运行。要不然就要把iso刻成光盘来启动。  
  
魔方也不错<http://www.sd173.com/html/224.html>  
包含无线工具  
·aircrack-ng  
·minidwep-gtk  
·feedingbottle  
·inflator  
·mdk3-v6（打开终端输入 “sudo mdk3”）  
2013.8.12，特地制作了一个经典稳定版本，minidwep-gtk-30513修改了参数，防止漏码，特供新手使用！  
<http://pan.baidu.com/s/1c06EIY0>  
2014.1.23更新经典稳定版，更改背景图，minidwep-gtk-30513优化参数，字典替换成5M纯数字弱密，更加适合跑包使用！  
<http://pan.baidu.com/s/1qWPmEZE>  
------------------------------------------------------------以下为普通版--------------------------------------------------------------------------2012.8.25更新，删除wpscrackgui，调整minidwep-gtk为fine版本，体积被缩小到了138MB  
<http://pan.baidu.com/share/link?shareid=5385&uk=4178331956>  
2013.1.28更新，升级Minidwep-gtk到31214  
<http://pan.baidu.com/share/link?shareid=225365&uk=4178331956>  
2013.1.31更新，升级无线包模块  
<http://pan.baidu.com/share/link?shareid=236835&uk=4178331956>  
2013.3.30更新，更新minidwep-gtk（minidwep-gtk-40325）  
<http://pan.baidu.com/s/1eQtJ0ga>  
2013.4.29更新，更新minidwep-gtk（minidwep-gtk-40420）  
<http://pan.baidu.com/s/1bn6GK5T>  
2013.8.12更新，修正inflator不能扫描的问题，进一步减小体积  
<http://pan.baidu.com/s/1bntj6qV>  
2014.1.23更新，修改开机背景图与桌面背景，更加美观，增加webQQ（原来的linux QQ已无法使用），将reaver原默认参数“-a -v -S -x 20 -r 100:10 -l 2”改为“-a -v -n -x 20 -r 100:10 -l 60 -d 0” 防止漏码，还原伪防pin路由真实等待速度，加快pin的速度。  
<http://pan.baidu.com/s/1gdBsrVP>  
2014.8.19更新，修复20140125版的严重问题，增加屏幕常亮脚本，握手包管理文件。因为是修复上一版的bug，所以取版本号为20140125\_Fixed。从这一版开始，开机第一件事情就是执行“开机必须第一个执行（双击）！-屏幕常亮脚本”。可以双击或者右键-执行，执行过程中不会有任何窗口弹出。执行这个脚本的目的就是为了去掉cdlinux的自动黑屏（屏保），防止破解过程中的损失。  
<http://pan.baidu.com/s/1ntibbjr>  
  
2014.8.21更新，全新aircrack-ng 1.2，reaver1.5，大量网卡驱动。其实这次更新并没有我的什么功劳，因为模块是拿了CDlinux-EX的，我只是根据我的喜好调整了一些桌面启动器和字典文件，为了表示对原作者的尊重与感谢，此版本以EX命名  
<http://pan.baidu.com/s/1i3mmWTn>  
  
2014.9.14更新，用回spring包，加入“30s后启动屏保”脚本。  
<http://pan.baidu.com/s/1qWltnsg>  
2015.5.24更新，加入pixiewps（wps新漏洞工具，可秒破，但是仅适用于雷凌、部分博通芯片的路由，常见的atheros芯片无法破解，所以其实是比较鸡肋的） （启动pixiewps仅需在reaver参数后加“-K 1"即可）更新reaver 1.5.2（非官方版本）【本次更新在晚上，比较仓促，未进行测试，有兴趣的朋友可以测试一下，下周我再找时间测试】  
<http://pan.baidu.com/s/1ntrCGjB>  
另外请注意经典版与普通版的区别！不要下载错了！（建议新手使用经典版）经典版使用30513版本，更加稳定，普通版使用最新版的minidwep-gtk，功能更多（支持乱序pin，另类排序，自动pin功能），但不支持自动保存进度，其他地方普通版和经典版是完全一样的！  
CDlinux 0.9.6.1  
基于CDlinux 0.9.6.1制作，使用minileaf的spring包无线模块，加入Minidwep-gtk、feedingbottle、inflator和超级权限，启动默认中文  
  
包含无线工具  
·aircrack-ng  
·minidwep-gtk  
·feedingbottle  
·inflator  
·mdk3-v6  
2013.2.1更新，升级feedingbottle到3.2.3 minidwep-gtk到31214  
下载地址：<http://pan.baidu.com/share/link?shareid=238557&uk=4178331956>  
2013.3.31更新，更新minidwep-gtk（minidwep-gtk-40325）  
<http://pan.baidu.com/share/link?shareid=446261&uk=4178331956>  
2013.6.15更新，更新minidwep-gtk（minidwep-gtk-40420）  
<http://pan.baidu.com/share/link?shareid=2559072361&uk=4178331956>  
注：因为Minidwep版本与0.9.7.1中的版本相同，故取版本0429   
2014.1.23更新，修改桌面背景，更加美观，增加webQQ，将reaver原默认参数“-a -v -S -x 20 -r 100:10 -l 2”改为“-a -v -n -x 20 -r 100:10 -l 60 -d 0” 防止漏码，还原伪防pin路由真实等待速度，加快pin的速度。  
<http://pan.baidu.com/s/1sjsBXil>  
  
基于CDlinux 0.9.7.1打包，使用landao\_gd的无线模块，加入inflator、超级权限，此版本为精简版，仅104MB，无线工具较新，可能不稳定，无线网卡驱动较少。  
集成Minidwep-gtk-31214、inflator1.0、feedingbottle3.2.3  
据网友反映 抓包有问题  
2013.1.28制作   
下载地址：<http://pan.baidu.com/share/link?shareid=223190&uk=4178331956>  
喜欢Beini的朋友可以到这里：<http://www.sd173.com/html/180.html>  
  
  
  
这是一个系统，请用虚拟机运行或刻盘Bios设置光盘启动或U盘启动等(本本内置网卡不支持虚拟机）但U启有一定难度，我没有试过，但许多网友反映U启成功，可以参考：[http://kingofclever.blog.163.com ... 675120136153742801/](http://kingofclever.blog.163.com/blog/static/12684675120136153742801/)  
wep破解我就不说了，下面我来说如何破解wpa2。我先说下，这是利用wps(WIFI Protect Setup）的pin码，通过猜pin码连接路由，因为pin码纯数字，所以这样破解的成功率高达90%，只是时间性问题。  
现在帖子发布有一年了 现在破解已经没有以前那么容易了 越来越多路由开始防pin了。   
  
方法1：使用minidwep-gtk,打开后选加密方式wap/wap2,点扫描，看路由名称、信道后面有没有wps,有的话(minidwep-gtk显示wps有点问题，有时候不带wps也是可以的，你可以先试一试看看能不能pin），点reaver，之后弹出的参数，将S改成n（注意是n不是N,这是为了防止漏码。），另外将-l后面的"300“改成”60“,之后点ok即可。  
方法2：使用inflator1.0，选yes,之后选网卡，再选next，之后选Scan for~~~,选路由，点next，然后勾第一个。点run  
  
由于破解漫长，需要保存进度，创建虚拟机快照，到时恢复  
  
这种方法破解要很久，要有很大的耐心，破不了别喷我。特别注意：很多路由器都会自锁，会出现pin死现象（就是总是重复一个码），这时需要暂停，创建虚拟机快照，到时恢复。  
软件破解成功后会弹出“PIn:XXX WPA PSK:XXX"  
注意：有可能会出很长一串的随机密码，这是需要再点Reaver,在后面加上命令-p XXXXXXXX（你破解的pin码）