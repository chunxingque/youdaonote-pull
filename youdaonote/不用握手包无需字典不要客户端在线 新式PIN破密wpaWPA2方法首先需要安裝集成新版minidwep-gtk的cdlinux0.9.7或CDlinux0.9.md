

|  |
| --- |
| 不用握手包无需字典不要客户端在线 新式PIN破密[wpa](http://www.kali.org.cn/forum-8-1.html)/WPA2方法首先需要安裝集成新版[minidwep](http://www.kali.org.cn/thread-10723-1-1.html)-gtk的[cdlinux](http://cdlinux.net/)0.9.7或CDlinux0.9.6.1。推荐硬盘安装CDlinux，可与XP形成双系统，又可保证得到CDlinux实模式，免去虚拟机模式经常无法识别[无线](http://www.kali.org.cn/forum-8-1.html)网卡的烦恼。新式PIN破解WPA WPA2方法：加密方式选择为WPA/WPA2方式时，扫描的信号发现大多最后都以wps结尾，这种信号开启了QSS加密，可以用最新式PIN码破解，破解成功率是百分百，只是时间长短的问题，1-12小时可以破解，须耐心和技巧。选择一个以wps结尾的信号，点击Reaver，注意，这里不是点击启动。之后会从12345670 开始 PIN 进度从0.04%开始破解进度是100%时可以出pin码跟密码。如果PIN的中途很慢或者重复的PIN一个数字，那就换一个时间段再PIN，正常是每隔2-4秒一个PIN码。此时记下最后一行PIN码，下次再破解这个信号的时候可以接着这个pin码继续PIN。如何接着上次记录的pin码继续PIN呢？在点Reaver的时候弹出的对话框中的数字-a -v -S -x 20 -r 100:10 -l 300 其中的S改为n,在300后面加空格，输入-加上次的pin码，比如-04740000，然后点OK继续上次的进度。共8位PIN码，当前四位PIN码正确后，会显示为90.00%，就只剩下后4位码了，这就证明快要得出密码了。直到PIN到100%之后出PIN码跟密码。记好SSID后面的信号名称，跟WPA PSK 后面的密码，然后关掉破解软件，到系统下找到这个信号，双击输入密码连接即大功告成。--------------------------------把CDlinux安装到硬盘 与XP形成双系统 附无线破解系统(基于CDlinux0.9.6.1及0.9.7)<http://www.kali.org.cn/thread-8943-1-1.html>附：无线破解系统(基于CDlinux0.9.6.1,CDlinux0.9.7)ISO镜像<http://kuai.xunlei.com/d/IZBYNGEUBZMX>       |

  
