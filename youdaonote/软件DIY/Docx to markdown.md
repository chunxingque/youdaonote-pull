转成HTML也是不错的解决方法

J:\自动备份盘\软件\pandoc-2.13\pandoc.exe -s 

1.docx 

--self-contained -o example35.html



额外处理：

1    去除body及其之外的东西、第一段、

2    <br />  →  空

3

$${\Downarrow 

}                                                →                $${\Downarrow}$$$$



4   bullet→cdot

5    ⇓              →         $${\Downarrow}$$

\# \\

\end{matrix}\left( 3 \right)        →      删除红的，后面一个替换为\tag{3}  ，搜索黑体看有无



正则表达式情况下（处理img tag的尺寸问题）：    

- style=.+?in"   替换成 空

- \\#\\left\( 1 \\right\) \\\\      替换成 \\tag\{1\}     注意里面的数字（1）换一下



---

E:\自动备份盘\软件\pandoc-2.7-windows-i386\pandoc.exe -s 

2.docx 

-t markdown-smart --wrap=none -o example35.md



---





Markdown to Docx

F:\自动备份盘\软件\pandoc-2.7-windows-i386\pandoc.exe  -s  F:\自动备份盘\软件\pandoc-2.7-windows-i386\example35.md -o example35.docx







下载选择 windows-i386.zip

https://github.com/jgm/pandoc/releases/tag/2.3.1



wrap lines的问题

https://github.com/jgm/pandoc/issues/4267