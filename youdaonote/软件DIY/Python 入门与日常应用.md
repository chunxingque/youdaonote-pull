Python 入门与日常应用

2012年08月20日 ⁄ 学习笔记 ⁄ 共 15764字 ⁄ 评论数 8 ⁄ 被围观 318 views+

Python 介绍¶

- Python 应用领域

- Web 与 Internet 编程

- 简单的 CGI 编程

- Web 框架：Django、TurboGears……

- 高端解决方案：Zope……

- 高级内容管理系统：Plone……

- HTML 和 XML 解析

- 收发电邮

- RSS 聚合阅读

- 其他 Internet 协议：xmlrpc ……

- 数据库访问

- Sqlite，MySQL, Oracle, MS SQL Server, PostgreSQL, SybODBC……

- 对象数据库：ZODB、 Durus……

- GUI 编程

- Tk

- wxWidgets

- GTK+

- Qt

- MFC

- Delphi

- 科学计算

- 生物信息学

- 物理学

- 教育

- 网络编程

- socket

- 异步网络编程框架：Twisted

- 软件开发

- 构建控制：SCons

- 持续编译与集成：Buildbot 与 Apache Gump

- Bug 列表与项目管理：Roundup 与 Trac

- Python IDE

- 游戏与 3D 图形编程

- 游戏编程库与游戏下载

- 游戏框架：pygame 和 PyKyra

Python 入门与日常应用¶

- 可以使用 Python 编程的设备

- PC（Windows、Linux、Mac等）

- 诺基亚S60智能机

- WinCE 及 PPC 设备

- 嵌入式 Linux 设备

- 2.x 与 3.x 的版本选择

这次以 Windows 平台为例进行说明。

目前 Python 正在从 2.x 系列转向 3.x 系列，2.7 是 Python 2.x 系列的最后一个版本，也就是说，今后不会有 2.8 的出现。

但是这也面临一个问题，2.x 系列具有丰富和稳定的第三方库可以使用，但是语法不及 3.x 的先进；3.x 的语法先进，但是第三方库还是非常有限的。

那对于初学者应该选择哪个版本呢？

- Python 官网上对于这个问题也有专门的讨论，详情请见：Python 2 or 3

- 个人建议使用 2.x 系列并且使用 Python2.5 或 2.6 或 2.7，原因如下：

- 我们使用 Python 是为了方便日常应用，2.5 以后的系列具有非常丰富的库，而且在 Windows 上的兼容性也是比较好的，可以方便日常应用

- 3.0 之后在语法有所改进，使其更加 Pythonic，但是很多改进对于初学者来说是很难遇到的

- 安装包的选择

- 手动编译

可以从 Python 官网上下载源代码，自行手动编译。

这样做的好处是你可以自己进行一些定制；不好的是，可能会与别人的解析器稍有不同，兼容性不够好。

这种方式更加适用于想深入 Python 内部实现的人，初学者不建议采用。

- Python 官网下载

官网的下载链接可能被封，原因不明，请使用以下链接：

http://www.python.org/ftp/python/

从官网下载源代码是一个不错的选择，但是要说发行版还是 ActiveState 的好用

- ActiveState 发行版（推荐下载）

ActiveState 是专注于动态语言开发的一个公司，大家可以多关注下。

ActiveState 的 Python 发行版具有如下优点：

- 发行版附带的文档比官网的文档更加丰富

- ActiveState 对它做过优化，使其更加稳定，兼容性更好

- http://www.activestate.com/activepython/downloads

- 安装

- 安装路径

安装的路径最好是在分区的根目录下，如 D:\Python2x。

不要放在 Programer Files 目录下，因为这个路径有空格，可能在使用过程中引入不必要的麻烦。

- 安装验证

验证安装是否成功：

打开 cmd，输入 python，看下是否进入 python 交互界面。

如果没有的话，请确保将 Python 的安装路径加入到系统的环境变量中。

- 多版本共存

不建议初学者在一台计算机上安装多个 Python 版本，因为这会带来使用上的不便。

- Python 目录解析

- 开发工具的使用

- 最轻量级的开发工具：python 交互界面

打开 cmd，输入 python 即可。

可以尝试一些新的想法，体验即时编程与动态编程！

但是单纯地使用 cmd 界面可能不太友好，因为它的补全功能不足。

这里有两个选择：

- 一个是按照 ipython，它可以在 cmd 窗口的 python 交互界面中添加 TAB 键补全功能，但是配置和安装比较麻烦。

- 另一个就是使用第三方的交互工具，比如 Dreampie （ 使用的时候注意先设置下字体，否则中文显示不正常 ）,它具有如下优点:

- GUI

- 带有自动补全功能

- 可以一次执行一个代码段

- 执行结果和输出结果可以导入导出

- 开源

- 普通文本编辑器（记事本、Emacs 等）

一般我们会把代码保存成一个文件，方便多次调用执行。

可以使用任意一款文本编辑器来进行 python 编程，最后保存成 *.py 就可以了，够轻量的吧！

如果你会 Emacs，那当然最好咯，因为 Emacs 中可以专门开一个 buffer 作为 python 交互环境，而且还可以方便调出你以前的代码片段，还可以设置 python 的调试环境。

要运行一个 *.py 文件，只要在 cmd 窗口中输入：

python a.py

- 重型工具：Eclipse + PyIDE

如果你想用 Python 开发一个正规一点的项目，Eclipse + PyIDE 是一个不错的选择。

Eclipse 中集成了 svn，PyIDE 可以很好地支持源码编辑、单元测试编写、程序保存时自动运行测试用例（需配置）、持续集成与构建等。

具体如何使用 Eclipse + PyIDE 等进行敏捷开发实践，请阅读： Apress.Foundations.of.Agile.Python.Development.Jun.2008.eBook-BBL.pdf （下载地址见参考资料）

- 其他可选IDE

- Python 之禅

Python 之禅代表了 Python 编程的一种理念，大家可在日常编程中领悟其中的奥妙。

在交互式界面中输入：

查看源代码 打印帮助

|   |   |
| - | - |
| 1 | &gt;&gt;&gt; import this |


|   |   |
| - | - |
| 2 | The Zen of Python, by Tim Peters |


|   |   |
| - | - |
| 3 |    |


|   |   |
| - | - |
| 4 | Beautiful is better than ugly. |


|   |   |
| - | - |
| 5 | Explicit is better than implicit. |


|   |   |
| - | - |
| 6 | Simple is better than complex. |


|   |   |
| - | - |
| 7 | Complex is better than complicated. |


|   |   |
| - | - |
| 8 | Flat is better than nested. |


|   |   |
| - | - |
| 9 | Sparse is better than dense. |


|   |   |
| - | - |
| 10 | Readability counts. |


|   |   |
| - | - |
| 11 | Special cases aren't special enough to break the rules. |


|   |   |
| - | - |
| 12 | Although practicality beats purity. |


|   |   |
| - | - |
| 13 | Errors should never pass silently. |


|   |   |
| - | - |
| 14 | Unless explicitly silenced. |


|   |   |
| - | - |
| 15 | In the face of ambiguity, refuse the temptation to guess. |


|   |   |
| - | - |
| 16 | There should be one-- and preferably only one --obvious way to do it. |


|   |   |
| - | - |
| 17 | Although that way may not be obvious at first unless you're Dutch. |


|   |   |
| - | - |
| 18 | Now is better than never. |


|   |   |
| - | - |
| 19 | Although never is often better than \*right\* now. |


|   |   |
| - | - |
| 20 | If the implementation is hard to explain, it's a bad idea. |


|   |   |
| - | - |
| 21 | If the implementation is easy to explain, it may be a good idea. |


|   |   |
| - | - |
| 22 | Namespaces are one honking great idea -- let's do more of those! |


- 内置对象

Python 中一切都是对象，容器存放对象，所以也就是无所不包。

- 数字 number

- int

查看源代码 打印帮助

|   |   |
| - | - |
| 1 | num\_int = 123 |


|   |   |
| - | - |
| 2 | type(num\_int) |


- long

查看源代码 打印帮助

|   |   |
| - | - |
| 1 | num\_long = 123L |


|   |   |
| - | - |
| 2 | type(num\_long) |


- float

查看源代码 打印帮助

|   |   |
| - | - |
| 1 | num\_float = 12.3 |


|   |   |
| - | - |
| 2 | type(num\_float) |


- complex

查看源代码 打印帮助

|   |   |
| - | - |
| 1 | num\_complex = 1.0e0j |


|   |   |
| - | - |
| 2 | type(num\_complex) |


|   |   |
| - | - |
| 3 | num\_complex.real |


|   |   |
| - | - |
| 4 | num\_complex.imag |


- 字符串 string

查看源代码 打印帮助

|   |   |
| - | - |
| 1 | norm\_str = "hello world" |


|   |   |
| - | - |
| 2 | type(norm\_str) |


|   |   |
| - | - |
| 3 | print norm\_str |


|   |   |
| - | - |
| 4 | unicode\_str = u"this is unicode string" |


|   |   |
| - | - |
| 5 | type(unicode\_str) |


|   |   |
| - | - |
| 6 | print unicode\_str |


|   |   |
| - | - |
| 7 | raw\_str = r"this is raw string\\n" |


|   |   |
| - | - |
| 8 | type(raw\_str) \# 其实是一个 normal string，只不过不转义 |


|   |   |
| - | - |
| 9 | print raw\_str |


|   |   |
| - | - |
| 10 | raw\_unicode\_str = ur"raw unicode \\n" \# u 与 r 顺序不能反了 |


|   |   |
| - | - |
| 11 | type(raw\_unicode\_str) |


|   |   |
| - | - |
| 12 | print raw\_unicode\_str |


|   |   |
| - | - |
| 13 | multi\_line\_str\_1 = "first line\\ |


|   |   |
| - | - |
| 14 | second line" |


|   |   |
| - | - |
| 15 | print multi\_line\_str\_1 \# 不会自动换行 |


|   |   |
| - | - |
| 16 | multi\_line\_str\_2 = '''first line |


|   |   |
| - | - |
| 17 | second line''' |


|   |   |
| - | - |
| 18 | print multi\_line\_str\_2 |


|   |   |
| - | - |
| 19 | multi\_line\_str\_3 = """first line |


|   |   |
| - | - |
| 20 | second line""" |


|   |   |
| - | - |
| 21 | print multi\_line\_str\_3 |


- 元组 tuple

查看源代码 打印帮助

|   |   |
| - | - |
| 1 | num\_tuple = (1, 2, 3) |


|   |   |
| - | - |
| 2 | char\_tuple = tuple("hello") \# tuple 是一个内置函数 |


|   |   |
| - | - |
| 3 | print num\_tuple[0] |


|   |   |
| - | - |
| 4 | num\_tuple[0] = 2 \# tuple 的值不可修改 |


|   |   |
| - | - |
| 5 | emb\_tuple = (1, 2, char\_tuple) \# 嵌套 tuple |


|   |   |
| - | - |
| 6 | emb\_tuple += (tuple, ) \# tuple 可以包含函数，这里注意 tuple 添加元素的方法 |


|   |   |
| - | - |
| 7 | emb\_tuple[3]("good") |


- 列表 list

- 基本操作

查看源代码 打印帮助

|   |   |
| - | - |
| 1 | num\_list = [1, 2, 3] |


|   |   |
| - | - |
| 2 | num\_list[0] = 4 \# list 与 tuple 类似，不过 list 可以修改元素 |


|   |   |
| - | - |
| 3 | num\_list.pop() |


|   |   |
| - | - |
| 4 | num\_list.append(5) |


|   |   |
| - | - |
| 5 | num\_list.extend([6, 7, 8]) |


|   |   |
| - | - |
| 6 | num\_list.reverse() |


|   |   |
| - | - |
| 7 | num\_list.reverse() |


- 列表内移动元素

查看源代码 打印帮助

|   |   |
| - | - |
| 1 | num\_list.insert(2, num\_list.pop(4)) |


- slice 切片操作

查看源代码 打印帮助

|   |   |
| - | - |
| 1 | num\_list[2: 5: 2] |


|   |   |
| - | - |
| 2 | num\_list[: 2] |


|   |   |
| - | - |
| 3 | num\_list[2: ] |


- list rotation

查看源代码 打印帮助

|   |   |
| - | - |
| 1 | num\_list = num\_list[2:] + num\_list[:2] |


- list comprehensions 列表推导:

- 对每个元素执行一个操作，并组成一个新的列表

查看源代码 打印帮助

|   |   |
| - | - |
| 1 | new\_list\_1 = [ x \*\* 2 for x in num\_list] |


|   |   |
| - | - |
| 2 | new\_list\_2 = map(lambda x: x \*\* 2, num\_list) |


- 取出列表中的偶数，组成一个新的列表

查看源代码 打印帮助

|   |   |
| - | - |
| 1 | new\_list\_3 = [x for x in num\_list if (x % 2) == 0] |


|   |   |
| - | - |
| 2 | new\_list\_4 = filter(lambda x: (x % 2) == 0, num\_list) |


- enumerate

查看源代码 打印帮助

|   |   |
| - | - |
| 1 | for idx, elem in enumerate(num\_list): |


|   |   |
| - | - |
| 2 |     print "index: %d, value: %d" % (idx, elem) |


- 清空列表

del num_list[:]

- 集合 set

查看源代码 打印帮助

|   |   |
| - | - |
| 1 | set\_a = set([1, 2, 3]) |


|   |   |
| - | - |
| 2 | set\_b = set([3, 4, 5]) |


|   |   |
| - | - |
| 3 | set\_a.union(set\_b) |


|   |   |
| - | - |
| 4 | set\_a.intersection(set\_b) |


|   |   |
| - | - |
| 5 | set\_a.difference(set\_b) |


|   |   |
| - | - |
| 6 | set\_a.symmetric\_difference(set\_b) |


|   |   |
| - | - |
| 7 | set\_a.issubset(set\_b) |


|   |   |
| - | - |
| 8 | set\_a.issuperset(set\_a.union(set\_b)) |


|   |   |
| - | - |
| 9 | set\_a.issuperset(set([3])) |


- 字典 dictionary

查看源代码 打印帮助

|   |   |
| - | - |
| 1 | dict\_joe = {"name":"Joe", "age":34, "skill":u"降龙十八掌"} |


|   |   |
| - | - |
| 2 | print dict\_joe["skill"] |


|   |   |
| - | - |
| 3 | dict\_joe["height"] = 1.85 |


|   |   |
| - | - |
| 4 | del dict\_joe["age"] |


|   |   |
| - | - |
| 5 | dict\_joe |


- None

- 逻辑

True False

- 可调用对象

callable

- 类型

查看源代码 打印帮助

|   |   |
| - | - |
| 1 | num = int(123) |


- 生成器

查看源代码 打印帮助

|   |   |
| - | - |
| 1 | def fibonacci(): |


|   |   |
| - | - |
| 2 |     a, b = 0, 1 |


|   |   |
| - | - |
| 3 |     while True: |


|   |   |
| - | - |
| 4 |           yield b |


|   |   |
| - | - |
| 5 |           a, b = b, a + b |


|   |   |
| - | - |
| 6 | fib = fibonacci() \# fib 是一个 iterator |


|   |   |
| - | - |
| 7 | fib.next() |


|   |   |
| - | - |
| 8 | [fib.next() for i in range(10)] |


|   |   |
| - | - |
| 9 | [fib.next() for i in range(10)] |


- 函数

常用的内置函数：

map

filter

enumerate

- 方法

- 基本表达式

- 函数定义

- 普通函数

查看源代码 打印帮助

|   |   |
| - | - |
| 1 | def func\_1(a, b): |


|   |   |
| - | - |
| 2 |     return a + b |


|   |   |
| - | - |
| 3 |    |


|   |   |
| - | - |
| 4 | func\_1(1, 2) |


- 多个返回值的函数

查看源代码 打印帮助

|   |   |
| - | - |
| 1 | def func\_2(a, b): |


|   |   |
| - | - |
| 2 |     return b, a |


|   |   |
| - | - |
| 3 |    |


|   |   |
| - | - |
| 4 | func\_2(1, 2) |


- positional arguments

查看源代码 打印帮助

|   |   |
| - | - |
| 1 | def func\_3(a, b, \*numbers): |


|   |   |
| - | - |
| 2 |     return a + b, sum(numbers) |


|   |   |
| - | - |
| 3 |    |


|   |   |
| - | - |
| 4 | func\_3(1, 2, 3, 4, 5, 6) |


- named arguments

查看源代码 打印帮助

|   |   |
| - | - |
| 1 | def func\_5(first=1, second=2): |


|   |   |
| - | - |
| 2 |     return first + second |


|   |   |
| - | - |
| 3 |    |


|   |   |
| - | - |
| 4 | func\_5() |


|   |   |
| - | - |
| 5 | func\_5(first=3) |


- positional and named arguments

查看源代码 打印帮助

|   |   |
| - | - |
| 1 | def func\_6(\*args, \*\*kw): |


|   |   |
| - | - |
| 2 |     print args |


|   |   |
| - | - |
| 3 |     print kw |


|   |   |
| - | - |
| 4 |    |


|   |   |
| - | - |
| 5 | func\_6(1,2, 3, 4, first=2, second=3) |


- 函数属性

查看源代码 打印帮助

|   |   |
| - | - |
| 1 | def func\_4(): |


|   |   |
| - | - |
| 2 |     func\_4.count += 1 |


|   |   |
| - | - |
| 3 |     return func\_4.count |


|   |   |
| - | - |
| 4 |    |


|   |   |
| - | - |
| 5 | func\_4.count = 0 |


|   |   |
| - | - |
| 6 | func\_4() |


|   |   |
| - | - |
| 7 | func\_4() |


|   |   |
| - | - |
| 8 | func\_4() |


- 命名空间与作用域

查看源代码 打印帮助

|   |   |
| - | - |
| 1 | def func\_7(): |


|   |   |
| - | - |
| 2 |     count += 1 |


|   |   |
| - | - |
| 3 |     print count |


|   |   |
| - | - |
| 4 |    |


|   |   |
| - | - |
| 5 | count = 1 |


|   |   |
| - | - |
| 6 | func\_7() |


|   |   |
| - | - |
| 7 |    |


|   |   |
| - | - |
| 8 | def func\_7(): |


|   |   |
| - | - |
| 9 |     global count |


|   |   |
| - | - |
| 10 |     count += 1 |


|   |   |
| - | - |
| 11 |     print count |


|   |   |
| - | - |
| 12 |    |


|   |   |
| - | - |
| 13 | func\_7() |


- 匿名函数 lambda

- 生成器

generator

- 流程控制

- if

查看源代码 打印帮助

|   |   |
| - | - |
| 1 | def flow\_if(x): |


|   |   |
| - | - |
| 2 |     if x &lt; 2: |


|   |   |
| - | - |
| 3 |         print "x less than 2" |


|   |   |
| - | - |
| 4 |     elif x == 2: |


|   |   |
| - | - |
| 5 |         print "x equal 2" |


|   |   |
| - | - |
| 6 |     else: |


|   |   |
| - | - |
| 7 |         print "x greater than 2" |


|   |   |
| - | - |
| 8 |    |


|   |   |
| - | - |
| 9 | flow\_if(2) |


|   |   |
| - | - |
| 10 |    |


|   |   |
| - | - |
| 11 | flow\_if(1) |


|   |   |
| - | - |
| 12 |    |


|   |   |
| - | - |
| 13 | flow\_if(3) |


- while

查看源代码 打印帮助

|   |   |
| - | - |
| 1 | def flow\_while(x): |


|   |   |
| - | - |
| 2 |     while True: |


|   |   |
| - | - |
| 3 |         x -= 1 |


|   |   |
| - | - |
| 4 |         print x |


|   |   |
| - | - |
| 5 |         if x &lt; 0: |


|   |   |
| - | - |
| 6 |             break |


|   |   |
| - | - |
| 7 |    |


|   |   |
| - | - |
| 8 | flow\_while(10) |


- for

查看源代码 打印帮助

|   |   |
| - | - |
| 1 | def flow\_for(x): |


|   |   |
| - | - |
| 2 |     for i in range(x): |


|   |   |
| - | - |
| 3 |         print i |


|   |   |
| - | - |
| 4 |    |


|   |   |
| - | - |
| 5 | flow\_for(10) |


- OOP

查看源代码 打印帮助

|   |   |
| - | - |
| 1 | class DemoClass(object): |


|   |   |
| - | - |
| 2 |     demo\_count = 0 |


|   |   |
| - | - |
| 3 |    |


|   |   |
| - | - |
| 4 |     def \_\_init\_\_(self): |


|   |   |
| - | - |
| 5 |         self.\_\_age = 1 |


|   |   |
| - | - |
| 6 |    |


|   |   |
| - | - |
| 7 |     def show\_demo(self): |


|   |   |
| - | - |
| 8 |         print "hello world!" |


|   |   |
| - | - |
| 9 |    |


|   |   |
| - | - |
| 10 |     @staticmethod |


|   |   |
| - | - |
| 11 |     def static\_show(): |


|   |   |
| - | - |
| 12 |         print "static function!" |


|   |   |
| - | - |
| 13 |    |


|   |   |
| - | - |
| 14 |     @classmethod |


|   |   |
| - | - |
| 15 |     def class\_show(cls): |


|   |   |
| - | - |
| 16 |         print "class function!" |


|   |   |
| - | - |
| 17 |    |


|   |   |
| - | - |
| 18 | dc = DemoClass() |


|   |   |
| - | - |
| 19 | dc.demo\_count |


|   |   |
| - | - |
| 20 | dc.\_\_age |


|   |   |
| - | - |
| 21 | dc.show\_demo() |


|   |   |
| - | - |
| 22 | dc.static\_show() |


|   |   |
| - | - |
| 23 | dc.class\_show() |


|   |   |
| - | - |
| 24 | DemoClass.static\_show() |


|   |   |
| - | - |
| 25 | DemoClass.class\_show() |


|   |   |
| - | - |
| 26 | DemoClass.show\_demo() |


|   |   |
| - | - |
| 27 | DemoClass.demo\_count |


- 库的使用

- 内置库与标准库

- winsound

查看源代码 打印帮助

|   |   |
| - | - |
| 1 | import winsound |


|   |   |
| - | - |
| 2 |    |


|   |   |
| - | - |
| 3 | def beeps(duration): |


|   |   |
| - | - |
| 4 |     freq = 100 |


|   |   |
| - | - |
| 5 |     while freq &lt; 3000: |


|   |   |
| - | - |
| 6 |         winsound.Beep(freq, dura) |


|   |   |
| - | - |
| 7 |     freq += 100 |


|   |   |
| - | - |
| 8 |    |


|   |   |
| - | - |
| 9 | beeps(100) |


|   |   |
| - | - |
| 10 |    |


|   |   |
| - | - |
| 11 | winsound.PlaySound("f:/python\_tech/start.wav", winsound.SND\_ASYNC) |


- reduce

查看源代码 打印帮助

|   |   |
| - | - |
| 1 | from operator import mul |


|   |   |
| - | - |
| 2 | n=10 |


|   |   |
| - | - |
| 3 | print reduce(mul, range(1,n+1)) |


或者

查看源代码 打印帮助

|   |   |
| - | - |
| 1 | n=10 |


|   |   |
| - | - |
| 2 | print reduce(lambda x,y:x\*y, range(1,n+1)) |


- time

查看源代码 打印帮助

|   |   |
| - | - |
| 1 | import time |


|   |   |
| - | - |
| 2 |    |


|   |   |
| - | - |
| 3 | dir(time) |


|   |   |
| - | - |
| 4 | time.asctime() |


|   |   |
| - | - |
| 5 | time.time() |


|   |   |
| - | - |
| 6 | time.clock() |


|   |   |
| - | - |
| 7 | time.sleep(3) |


- datetime

查看源代码 打印帮助

|   |   |
| - | - |
| 1 | import datetime |


|   |   |
| - | - |
| 2 | datetime.datetime.now() |


|   |   |
| - | - |
| 3 | datetime.datetime(2010, 12, 14, 16, 22, 22, 640000) |


|   |   |
| - | - |
| 4 | t1 = datetime.datetime.now() |


|   |   |
| - | - |
| 5 | datetime.datetime.now() - t1 |


- socket

- tcp server

查看源代码 打印帮助

|   |   |
| - | - |
| 1 | import socket |


|   |   |
| - | - |
| 2 | sock = socket.socket(socket.AF\_INET, socket.SOCK\_STREAM) |


|   |   |
| - | - |
| 3 | sock.bind(('', 8881)) |


|   |   |
| - | - |
| 4 | sock.listen(1) |


|   |   |
| - | - |
| 5 |    |


|   |   |
| - | - |
| 6 | while True: |


|   |   |
| - | - |
| 7 |     newSocket, address = sock.accept() |


|   |   |
| - | - |
| 8 |     print "Connected from", address |


|   |   |
| - | - |
| 9 |     while True: |


|   |   |
| - | - |
| 10 |         receivedData = newSocket.recv(8192) |


|   |   |
| - | - |
| 11 |         if not receivedData: |


|   |   |
| - | - |
| 12 |         break |


|   |   |
| - | - |
| 13 |         newSocket.sendall(receivedData) |


|   |   |
| - | - |
| 14 |     newSocket.close() |


|   |   |
| - | - |
| 15 |     print "Disconnected from", address |


|   |   |
| - | - |
| 16 | sock.close() |


- tcp client

查看源代码 打印帮助

|   |   |
| - | - |
| 1 | import socket |


|   |   |
| - | - |
| 2 |    |


|   |   |
| - | - |
| 3 | sock = socket.socket(socket.AF\_INET, socket.SOCK\_STREAM) |


|   |   |
| - | - |
| 4 | sock.connect(('localhost', 8881)) |


|   |   |
| - | - |
| 5 | print "Connected to server" |


|   |   |
| - | - |
| 6 | sock.send("hello") |


|   |   |
| - | - |
| 7 | response = sock.recv(8192) |


|   |   |
| - | - |
| 8 | print response |


|   |   |
| - | - |
| 9 | sock.close() |


- udp connection

查看源代码 打印帮助

|   |   |
| - | - |
| 1 | s = socket.socket(socket.AF\_INET, socket.SOCK\_DGRAM) |


|   |   |
| - | - |
| 2 | s.bind(('', 8000)) |


|   |   |
| - | - |
| 3 | s.sendto("hello", ("192.168.27.73", 4001))    \# data, address |


|   |   |
| - | - |
| 4 | s.recvfrom(1000) \# buffer size |


- struct

查看源代码 打印帮助

|   |   |
| - | - |
| 1 | import struct |


|   |   |
| - | - |
| 2 |    |


|   |   |
| - | - |
| 3 | a = 1.3 |


|   |   |
| - | - |
| 4 | s = struct.pack('f', a) |


|   |   |
| - | - |
| 5 |    |


|   |   |
| - | - |
| 6 | for i in s: |


|   |   |
| - | - |
| 7 |     print '%x' % ord(i) |


|   |   |
| - | - |
| 8 |    |


|   |   |
| - | - |
| 9 | a = struct.unpack('f', s) |


- sqlite3

查看源代码 打印帮助

|   |   |
| - | - |
| 1 | DB\_FILE = "f:\\\\python\_tech\\\\eg.db" |


|   |   |
| - | - |
| 2 |    |


|   |   |
| - | - |
| 3 | import sqlite3 |


|   |   |
| - | - |
| 4 |    |


|   |   |
| - | - |
| 5 | conn1 = sqlite3.connect(DB\_FILE) |


|   |   |
| - | - |
| 6 | c = conn1.cursor() |


|   |   |
| - | - |
| 7 | c.execute('''create table stocks |


|   |   |
| - | - |
| 8 | (date text, trans text, symbol text, |


|   |   |
| - | - |
| 9 | qty real, price real)''') |


|   |   |
| - | - |
| 10 | c.execute("""insert into stocks values ('2006-01-05','BUY','RHAT',100,35.14)""") |


|   |   |
| - | - |
| 11 | conn1.commit() |


|   |   |
| - | - |
| 12 |    |


|   |   |
| - | - |
| 13 | conn2 = sqlite3.connect(DB\_FILE) |


|   |   |
| - | - |
| 14 | c2 = conn2.cursor() |


|   |   |
| - | - |
| 15 | c2.execute('select \* from stocks') |


|   |   |
| - | - |
| 16 | c2.fetchall() |


- SimpleHTTPServer

查看源代码 打印帮助

|   |   |
| - | - |
| 1 | python -m SimpleHTTPServer.py |


- SimpleXMLRPCServer

- server

查看源代码 打印帮助

|   |   |
| - | - |
| 1 | from SimpleXMLRPCServer import SimpleXMLRPCServer |


|   |   |
| - | - |
| 2 |    |


|   |   |
| - | - |
| 3 | server = SimpleXMLRPCServer(("192.168.27.73", 8000)) |


|   |   |
| - | - |
| 4 | server.register\_introspection\_functions() |


|   |   |
| - | - |
| 5 |    |


|   |   |
| - | - |
| 6 | server.register\_function(pow) |


|   |   |
| - | - |
| 7 |    |


|   |   |
| - | - |
| 8 | def adder\_function(x,y): |


|   |   |
| - | - |
| 9 |     return x + y |


|   |   |
| - | - |
| 10 | server.register\_function(adder\_function, 'add') |


|   |   |
| - | - |
| 11 |    |


|   |   |
| - | - |
| 12 | print "start rpc server" |


|   |   |
| - | - |
| 13 | server.serve\_forever() |


- client

查看源代码 打印帮助

|   |   |
| - | - |
| 1 | import xmlrpclib |


|   |   |
| - | - |
| 2 |    |


|   |   |
| - | - |
| 3 | s = xmlrpclib.Server('http://localhost:8000') |


|   |   |
| - | - |
| 4 | print s.pow(2,3)  \# Returns 2\*\*3 = 8 |


|   |   |
| - | - |
| 5 | print s.add(2,3)  \# Returns 5 |


|   |   |
| - | - |
| 6 | print s.div(5,2)  \# Returns 5//2 = 2 |


|   |   |
| - | - |
| 7 |    |


|   |   |
| - | - |
| 8 | print s.system.listMethods() |


- ctypes 用于与 C 语言的交互

- windll

查看源代码 打印帮助

|   |   |
| - | - |
| 1 | from ctypes import \* |


|   |   |
| - | - |
| 2 | import os,time |


|   |   |
| - | - |
| 3 |    |


|   |   |
| - | - |
| 4 | class MEMORYSTATUS (Structure): |


|   |   |
| - | - |
| 5 |     \_fields\_ = [('dwLength', c\_ulong),\#sizeof(MEMORYSTATUS) |


|   |   |
| - | - |
| 6 |                 ('dwMemoryLoad',c\_ulong), \# percent of memory in use |


|   |   |
| - | - |
| 7 |                 ('dwTotalPhys', c\_ulong),\#;     // bytes of physical memory |


|   |   |
| - | - |
| 8 |                 ('dwAvailPhys', c\_ulong),\#;     // free physical memory bytes |


|   |   |
| - | - |
| 9 |                 ('dwTotalPageFile',c\_ulong),\#; // bytes of paging file |


|   |   |
| - | - |
| 10 |                 ('dwAvailPageFile', c\_ulong),\#; // free bytes of paging file |


|   |   |
| - | - |
| 11 |                 ('dwTotalVirtual', c\_ulong),\#;  // user bytes of address space |


|   |   |
| - | - |
| 12 |                 ('dwAvailVirtual',c\_ulong),\#;  // free user bytes |


|   |   |
| - | - |
| 13 |     ] |


|   |   |
| - | - |
| 14 |    |


|   |   |
| - | - |
| 15 | if os.name == 'nt': |


|   |   |
| - | - |
| 16 |     mem = MEMORYSTATUS() |


|   |   |
| - | - |
| 17 |     memptr = pointer(mem) |


|   |   |
| - | - |
| 18 |     windll.kernel32.GlobalMemoryStatus(memptr) |


|   |   |
| - | - |
| 19 |    |


|   |   |
| - | - |
| 20 |     print "mem used",mem.dwMemoryLoad,"%" |


|   |   |
| - | - |
| 21 |     print "mem",mem.dwTotalPhys |


- msvcrt

查看源代码 打印帮助

|   |   |
| - | - |
| 1 | from ctypes import \* |


|   |   |
| - | - |
| 2 | msvcrt = cdll.msvcrt |


|   |   |
| - | - |
| 3 | message\_string = "Hello world!\\n" |


|   |   |
| - | - |
| 4 | msvcrt.printf("Testing: %s", message\_string) |


- os

- 调用外部程序

查看源代码 打印帮助

|   |   |
| - | - |
| 1 | import os |


|   |   |
| - | - |
| 2 | os.system("calc") |


|   |   |
| - | - |
| 3 |    |


|   |   |
| - | - |
| 4 | import os |


|   |   |
| - | - |
| 5 | cmd = "date" |


|   |   |
| - | - |
| 6 | s = os.popen(cmd).readline() |


- 文件管理

# 创建目录


查看源代码

打印帮助

|   |   |
| - | - |
| 1 | os.mkdir("file") |





# 创建文件




查看源代码

打印帮助

|   |   |
| - | - |
| 1 | os.mknod("test.txt") |


|   |   |
| - | - |
| 2 | open("test.txt",w) |





# 复制文件




查看源代码

打印帮助

|   |   |
| - | - |
| 1 | shutil.copyfile("old\_file","new\_file") |


|   |   |
| - | - |
| 2 | shutil.copy("old\_file","new\_file\_or\_dir") |





# 复制文件树：




查看源代码

打印帮助

|   |   |
| - | - |
| 1 | shutil.copytree("old\_dir","new\_dir") |





# 重命名文件或目录




查看源代码

打印帮助

|   |   |
| - | - |
| 1 | os.rename("old\_name","new\_name") |





# 移动文件




查看源代码

打印帮助

|   |   |
| - | - |
| 1 | shutil.move("old\_pos","new\_pos") |





# 删除文件




查看源代码

打印帮助

|   |   |
| - | - |
| 1 | os.remove("file") |





# 删除空目录




查看源代码

打印帮助

|   |   |
| - | - |
| 1 | os.rmdir("dir") |





# 删除目录树




查看源代码

打印帮助

|   |   |
| - | - |
| 1 | shutil.rmtree("dir") |





# 判断文件或目录是否存在




os.path.exists("goal")




# 判断是否为目录




查看源代码

打印帮助

|   |   |
| - | - |
| 1 | os.path.isdir("goal") |





# 判断是否为文件




查看源代码

打印帮助

|   |   |
| - | - |
| 1 | os.path.isfile("goal") |





# 当前目录




查看源代码

打印帮助

|   |   |
| - | - |
| 1 | os.path.abspath(os.curdir) |





# 跳转目录




查看源代码

打印帮助

|   |   |
| - | - |
| 1 | os.chdir("path") |





# 获取用户根目录




查看源代码

打印帮助

|   |   |
| - | - |
| 1 | os.path.expanduser("~") |





# 分割路径与文件名




查看源代码

打印帮助

|   |   |
| - | - |
| 1 | os.path.split("c:\\\\music\\\\ap\\\\mahadeva.mp3") |





# 分割文件名与扩展名




查看源代码

打印帮助

|   |   |
| - | - |
| 1 | os.path.splitext(filename) |





# 列举指定扩展名的文件




查看源代码

打印帮助

|   |   |
| - | - |
| 1 | lst = ['.bmp', '.jpg', '.gif'] |


|   |   |
| - | - |
| 2 | filter(lambda x: x[-4:] in lst, os.listdir("e://pictures/")) |





- bisect

查看源代码 打印帮助

|   |   |
| - | - |
| 1 | grades = "FEDCBA" |


|   |   |
| - | - |
| 2 | breakpoints = [30, 44, 66, 75, 85] |


|   |   |
| - | - |
| 3 |    |


|   |   |
| - | - |
| 4 | from bisect import bisect |


|   |   |
| - | - |
| 5 |    |


|   |   |
| - | - |
| 6 | def grade(total): |


|   |   |
| - | - |
| 7 |           return grades[bisect(breakpoints, total)] |


|   |   |
| - | - |
| 8 |    |


|   |   |
| - | - |
| 9 | grade(66) |


|   |   |
| - | - |
| 10 |    |


|   |   |
| - | - |
| 11 | map(grade, [33, 99, 77, 44, 12, 88]) |


- re

查看源代码 打印帮助

|   |   |
| - | - |
| 1 | import urllib |


|   |   |
| - | - |
| 2 |    |


|   |   |
| - | - |
| 3 | sock = urllib.open('url') |


|   |   |
| - | - |
| 4 | source = sock.read() |


|   |   |
| - | - |
| 5 | sock.close() |


|   |   |
| - | - |
| 6 |    |


|   |   |
| - | - |
| 7 | import re |


|   |   |
| - | - |
| 8 | comment\_str = """ |


|   |   |
| - | - |
| 9 | &lt;!--addfa--&gt; |


|   |   |
| - | - |
| 10 | """ |


|   |   |
| - | - |
| 11 | re.findall(r'&lt;!--(.+?)--&gt;', source, re.S) |


- xml.etree.ElementTree

查看源代码 打印帮助

|   |   |
| - | - |
| 1 | from xml.etree.ElementTree import \* |


|   |   |
| - | - |
| 2 |    |


|   |   |
| - | - |
| 3 | book = ElementTree() |


|   |   |
| - | - |
| 4 | purchaseorder = Element('PurchaseOrder') |


|   |   |
| - | - |
| 5 | book.\_setroot(purchaseorder) |


|   |   |
| - | - |
| 6 | SubElement(purchaseorder,  'account', {'refnum' : "2390094"}) |


|   |   |
| - | - |
| 7 | item = Element("item", {'sku' : '33-993933', 'qty' : '4'}) |


|   |   |
| - | - |
| 8 | purchaseorder.append(item) |


|   |   |
| - | - |
| 9 | SubElement(item, 'name').text = "Potato Smasher" |


|   |   |
| - | - |
| 10 | SubElement(item, 'description').text = "Smash Potatoes like never before." |


|   |   |
| - | - |
| 11 | book.write("f:/python\_tech/book.xml") |


- sgmllib

查看源代码 打印帮助

|   |   |
| - | - |
| 1 | from sgmllib import SGMLParser |


|   |   |
| - | - |
| 2 | import urllib |


|   |   |
| - | - |
| 3 |    |


|   |   |
| - | - |
| 4 | class URLLister(SGMLParser): |


|   |   |
| - | - |
| 5 |     def reset(self): |


|   |   |
| - | - |
| 6 |         SGMLParser.reset(self) |


|   |   |
| - | - |
| 7 |         self.urls = [] |


|   |   |
| - | - |
| 8 |     def start\_a(self, attrs): |


|   |   |
| - | - |
| 9 |         href = [v for k, v in attrs if k=='href'] |


|   |   |
| - | - |
| 10 |         if href: |


|   |   |
| - | - |
| 11 |             self.urls.extend(href) |


|   |   |
| - | - |
| 12 |    |


|   |   |
| - | - |
| 13 | usock = urllib.urlopen("http://diveintopython.org/") |


|   |   |
| - | - |
| 14 | parser = URLLister() |


|   |   |
| - | - |
| 15 | parser.feed(usock.read()) |


|   |   |
| - | - |
| 16 | usock.close() |


|   |   |
| - | - |
| 17 | parser.close() |


|   |   |
| - | - |
| 18 | for url in parser.urls: |


|   |   |
| - | - |
| 19 |     print url |


|   |   |
| - | - |
| 20 | parser.output() |


- threading

查看源代码 打印帮助

|   |   |
| - | - |
| 1 | import threading |


|   |   |
| - | - |
| 2 | import time |


|   |   |
| - | - |
| 3 |    |


|   |   |
| - | - |
| 4 | tha\_running = True |


|   |   |
| - | - |
| 5 |    |


|   |   |
| - | - |
| 6 | def thread\_a(): |


|   |   |
| - | - |
| 7 |     while tha\_running: |


|   |   |
| - | - |
| 8 |         time.sleep(1) |


|   |   |
| - | - |
| 9 |         print "a" |


|   |   |
| - | - |
| 10 |    |


|   |   |
| - | - |
| 11 | thb\_running = True |


|   |   |
| - | - |
| 12 |    |


|   |   |
| - | - |
| 13 | def thread\_b(): |


|   |   |
| - | - |
| 14 |     while thb\_running: |


|   |   |
| - | - |
| 15 |         time.sleep(1) |


|   |   |
| - | - |
| 16 |         print "b" |


|   |   |
| - | - |
| 17 |    |


|   |   |
| - | - |
| 18 | tha = threading.Thread(target=thread\_a, args=()) |


|   |   |
| - | - |
| 19 | thb = threading.Thread(target=thread\_b, args=()) |


|   |   |
| - | - |
| 20 |    |


|   |   |
| - | - |
| 21 | tha.start() |


|   |   |
| - | - |
| 22 | thb.start() |


- 第三方库

- 第三方库的寻找与安装

- pyttsx

查看源代码 打印帮助

|   |   |
| - | - |
| 1 | import pyttsx |


|   |   |
| - | - |
| 2 | engine = pyttsx.init() |


|   |   |
| - | - |
| 3 | engine.say('The quick brown fox jumped over the lazy dog.') |


|   |   |
| - | - |
| 4 | engine.runAndWait() |


- pyserial

查看源代码 打印帮助

|   |   |
| - | - |
| 1 | import serial |


|   |   |
| - | - |
| 2 |    |


|   |   |
| - | - |
| 3 | s = serial.Serial('COM1', 115200) |


|   |   |
| - | - |
| 4 | \# do not call s.open() here |


|   |   |
| - | - |
| 5 | s.write('hello') |


|   |   |
| - | - |
| 6 | s.read()    \# 读取一个字符 |


|   |   |
| - | - |
| 7 | s.readline(eol='\\n')    \# 读取一行 |


|   |   |
| - | - |
| 8 | s.close() |


- PIL

- 基本操作

查看源代码 打印帮助

|   |   |
| - | - |
| 1 | import Image&lt;/pre&gt; |


|   |   |
| - | - |
| 2 | \# 打开图像： |


|   |   |
| - | - |
| 3 |  im = Image.open("f:/python\_tech//cats.jpg") |


|   |   |
| - | - |
| 4 |    |


|   |   |
| - | - |
| 5 | \# 显示图片： |


|   |   |
| - | - |
| 6 |  im.show() |


|   |   |
| - | - |
| 7 |    |


|   |   |
| - | - |
| 8 | \# 显示图片的格式、尺寸和模式： |


|   |   |
| - | - |
| 9 |  print im.format, im.size, im.mode |


|   |   |
| - | - |
| 10 |    |


|   |   |
| - | - |
| 11 | \# 保存图片： |


|   |   |
| - | - |
| 12 |  im.save("f:/python\_tech//test.jpg") |


|   |   |
| - | - |
| 13 |    |


|   |   |
| - | - |
| 14 | \# 格式转换： |


|   |   |
| - | - |
| 15 |  im.save("f:/python\_tech//test.bmp") |


|   |   |
| - | - |
| 16 |    |


|   |   |
| - | - |
| 17 | \# 缩放（只能缩小）： |


|   |   |
| - | - |
| 18 |  im.thumbnail((100, 100)) |


|   |   |
| - | - |
| 19 |    |


|   |   |
| - | - |
| 20 | \# 改变尺寸： |


|   |   |
| - | - |
| 21 |  out = im.resize((400, 400)) |


|   |   |
| - | - |
| 22 |    |


|   |   |
| - | - |
| 23 | \# 剪切： |


|   |   |
| - | - |
| 24 |  box = (100, 100, 200, 200) |


|   |   |
| - | - |
| 25 |  region = im.crop(box) |


|   |   |
| - | - |
| 26 |  region.show() |


|   |   |
| - | - |
| 27 |    |


|   |   |
| - | - |
| 28 | \# 旋转： |


|   |   |
| - | - |
| 29 |  region = region.transpose(Image.ROTATE\_180) |


|   |   |
| - | - |
| 30 |  out = im.rotate(30) |


|   |   |
| - | - |
| 31 |    |


|   |   |
| - | - |
| 32 | \# 镜像： |


|   |   |
| - | - |
| 33 |  out = im.transpose(Image.FLIP\_LEFT\_RIGHT) |


|   |   |
| - | - |
| 34 |    |


|   |   |
| - | - |
| 35 | \# 贴图： |


|   |   |
| - | - |
| 36 |  im.paste(region, box) \# region 的实际尺寸必须与box相符 |


|   |   |
| - | - |
| 37 |    |


|   |   |
| - | - |
| 38 | \# RGB 转换： |


|   |   |
| - | - |
| 39 |  r, g, b = im.split() |


|   |   |
| - | - |
| 40 |  im = Image.merge("RGB", (b, g, r)) |


|   |   |
| - | - |
| 41 |    |


|   |   |
| - | - |
| 42 | \# 颜色转换： |


|   |   |
| - | - |
| 43 |  out = im.convert("L") |


|   |   |
| - | - |
| 44 |    |


|   |   |
| - | - |
| 45 | \# 图像增强-滤镜： |


|   |   |
| - | - |
| 46 |  import ImageFilter |


|   |   |
| - | - |
| 47 |  out = im.filter(ImageFilter.DETAIL) |


|   |   |
| - | - |
| 48 |  \# 像素操作： |


|   |   |
| - | - |
| 49 |  out = im.point(lambda i: i \* 1.2) |


|   |   |
| - | - |
| 50 |    |


|   |   |
| - | - |
| 51 | \# 处理示例： |


|   |   |
| - | - |
| 52 |  \# split the image into individual bands |


|   |   |
| - | - |
| 53 |  source = im.split() |


|   |   |
| - | - |
| 54 |    |


|   |   |
| - | - |
| 55 | R, G, B = 0, 1, 2 |


|   |   |
| - | - |
| 56 |    |


|   |   |
| - | - |
| 57 | \# select regions where red is less than 100 |


|   |   |
| - | - |
| 58 |  mask = source[R].point(lambda i: i &lt; 100 and 255) |


|   |   |
| - | - |
| 59 |    |


|   |   |
| - | - |
| 60 | \# process the green band |


|   |   |
| - | - |
| 61 |  out = source[G].point(lambda i: i \* 0.7) |


|   |   |
| - | - |
| 62 |    |


|   |   |
| - | - |
| 63 | \# paste the processed band back, but only where red was &lt; 100 |


|   |   |
| - | - |
| 64 |  source[G].paste(out, None, mask) |


|   |   |
| - | - |
| 65 |    |


|   |   |
| - | - |
| 66 | \# build a new multiband image |


|   |   |
| - | - |
| 67 |  im = Image.merge(im.mode, source) |


|   |   |
| - | - |
| 68 |    |


|   |   |
| - | - |
| 69 | \# 调整对比度、亮度、色彩平衡和柔和度： |


|   |   |
| - | - |
| 70 |  import ImageEnhance |


|   |   |
| - | - |
| 71 |    |


|   |   |
| - | - |
| 72 | enh = ImageEnhance.Contrast(im) |


|   |   |
| - | - |
| 73 |  enh.enhance(1.3).show("30% more contrast") |


# 处理动画图片序列：

查看源代码 打印帮助

|   |   |
| - | - |
| 1 | im = Image.open("f:/python\_tech//tu\_2.gif") |


|   |   |
| - | - |
| 2 | im.tell() |


|   |   |
| - | - |
| 3 | im.seek(1) |


# 截屏

查看源代码 打印帮助

|   |   |
| - | - |
| 1 | from PIL import ImageGrab |


|   |   |
| - | - |
| 2 | scr = ImageGrab.grab() |


|   |   |
| - | - |
| 3 | scr.show() |


- 批量缩放照片

查看源代码 打印帮助

|   |   |
| - | - |
| 1 | import os |


|   |   |
| - | - |
| 2 | import shutil |


|   |   |
| - | - |
| 3 | import Image |


|   |   |
| - | - |
| 4 | DIR = "F:\\pictures" |


|   |   |
| - | - |
| 5 | for root, dirs, files in os.walk(DIR): |


|   |   |
| - | - |
| 6 |     for name in files: |


|   |   |
| - | - |
| 7 |         print name |


|   |   |
| - | - |
| 8 |         im = Image.open(os.path.join(root, name)) |


|   |   |
| - | - |
| 9 |         im.thumbnail((3200, 2400)) |


|   |   |
| - | - |
| 10 |         im.save(os.path.join(root + "\\\\thumb", name)) |


- pyexcelerator

查看源代码 打印帮助

|   |   |
| - | - |
| 1 | import pyExcelerator as excel |


|   |   |
| - | - |
| 2 |    |


|   |   |
| - | - |
| 3 | wb = excel.Workbook() |


|   |   |
| - | - |
| 4 | ws = wb.add\_sheet('Scores') |


|   |   |
| - | - |
| 5 | content = [ |


|   |   |
| - | - |
| 6 | [1, 2, 3, 4, 5], |


|   |   |
| - | - |
| 7 | [6, 7, 8, 9, 10] |


|   |   |
| - | - |
| 8 | ] |


|   |   |
| - | - |
| 9 | for idx\_r, row in enumerate(content): |


|   |   |
| - | - |
| 10 |     for idx\_c, col in enumerate(row): |


|   |   |
| - | - |
| 11 |         ws.write(idx\_r, idx\_c, col) |


|   |   |
| - | - |
| 12 |    |


|   |   |
| - | - |
| 13 | wb.save("f:/python\_tech//table.xls") |


- win32com

查看源代码 打印帮助

|   |   |
| - | - |
| 1 | \# 调用迅雷 COM 接口 |


|   |   |
| - | - |
| 2 | import win32com.client |


|   |   |
| - | - |
| 3 |    |


|   |   |
| - | - |
| 4 | a=win32com.client.Dispatch('ThunderAgent.Agent.1') |


|   |   |
| - | - |
| 5 | a.AddTask('http://www.baidu.com/index.htm/') |


|   |   |
| - | - |
| 6 | a.CommitTasks() |


- 参考资料与网站

- Python in a nutshell

- ActivePython Documentation

- Python 核心编程

- 局域网电子书共享：ftp://192.168.0.201/共享上传区/Python

进阶¶

- 调试：log、windbg、pdb、pydev...

- 优化与加速：profile、pyrex...

- py2exe

- functional programming：http://docs.python.org/howto/functional.html

- 扩展模块的编写与发布

- 嵌入 Python 到 C/C++、Java、

- GUI 编程

- Web 编程

- 你可以从 Python 学到的

- Python 各领域的高级编程技术

- 各种专业库的源码实现

- Python 编译器的实现

- Python 虚拟机的实现

- Python 内存管理的实现

- 通过 jython 进入 Java 世界

- 通过 IronPython 进入 .Net 世界

- ...