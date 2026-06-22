文章目录

1. 1. 显示有限的接口到外部

1. 2. with的魔力

1. 3. filter的用法

1. 4. 一行作判断

1. 5. 装饰器之单例

1. 6. staticmethod装饰器

1. 7. property装饰器

1. 8. iter魔法

1. 9. 神奇partial

1. 10. 神秘eval

1. 11. exec

1. 12. getattr

1. 13. 命令行处理

1. 14. 读写csv文件

1. 15. 各种时间形式转换

1. 16. 字符串格式化

1. 17. 参考链接

本博客采用创作共用版权协议, 要求署名、非商业用途和保持一致. 转载本博客文章必须也遵循署名-非商业用途-保持一致的创作共用协议.

显示有限的接口到外部

当发布python第三方package时, 并不希望代码中所有的函数或者class可以被外部import, 在__init__.py中添加__all__属性,

该list中填写可以import的类或者函数名, 可以起到限制的import的作用, 防止外部import其他函数或者类

|   |   |
| - | - |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14 | \#!/usr/bin/env python<br>\# -\*- coding: utf-8 -\*-<br>from base import APIBase<br>from client import Client<br>from decorator import interface, export, stream<br>from server import Server<br>from storage import Storage<br>from util import (LogFormatter, disable\_logging\_to\_stderr,<br>                       enable\_logging\_to\_kids, info)<br>\_\_all\_\_ = ['APIBase', 'Client', 'LogFormatter', 'Server',<br>           'Storage', 'disable\_logging\_to\_stderr', 'enable\_logging\_to\_kids',<br>           'export', 'info', 'interface', 'stream'] |


with的魔力

with语句需要支持上下文管理协议的对象, 上下文管理协议包含__enter__和__exit__两个方法. with语句建立运行时上下文需要通过这两个方法执行进入和退出操作.

其中上下文表达式是跟在with之后的表达式, 该表示大返回一个上下文管理对象

|   |   |
| - | - |
| 1<br>2<br>3<br>4 | \# 常见with使用场景<br>with open("test.txt", "r") as my\_file:  \# 注意, 是\_\_enter\_\_()方法的返回值赋值给了my\_file,<br>    for line in my\_file:<br>        print line |


详细原理可以查看这篇文章, 浅谈 Python 的 with 语句

知道具体原理, 我们可以自定义支持上下文管理协议的类, 类中实现__enter__和__exit__方法

|   |   |
| - | - |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>23<br>24<br>25<br>26<br>27<br>28<br>29<br>30<br>31<br>32<br>33 | \#!/usr/bin/env python<br>\# -\*- coding: utf-8 -\*-<br>class MyWith(object):<br>    def \_\_init\_\_(self):<br>        print "\_\_init\_\_ method"<br>    def \_\_enter\_\_(self):<br>        print "\_\_enter\_\_ method"<br>        return self  \# 返回对象给as后的变量<br>    def \_\_exit\_\_(self, exc\_type, exc\_value, exc\_traceback):<br>        print "\_\_exit\_\_ method"<br>        if exc\_traceback is None:<br>            print "Exited without Exception"<br>            return True<br>        else:<br>            print "Exited with Exception"<br>            return False<br>def test\_with():<br>    with MyWith() as my\_with:<br>        print "running my\_with"<br>    print "------分割线-----"<br>    with MyWith() as my\_with:<br>        print "running before Exception"<br>        raise Exception<br>        print "running after Exception"<br>if \_\_name\_\_ == '\_\_main\_\_':<br>    test\_with() |


执行结果如下:

|   |   |
| - | - |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19 | \_\_init\_\_ method<br>\_\_enter\_\_ method<br>running my\_with<br>\_\_exit\_\_ method<br>Exited without Exception<br>------分割线-----<br>\_\_init\_\_ method<br>\_\_enter\_\_ method<br>running before Exception<br>\_\_exit\_\_ method<br>Exited with Exception<br>Traceback (most recent call last):<br>  File "bin/python", line 34, in &lt;module&gt;<br>    exec(compile(\_\_file\_\_f.read(), \_\_file\_\_, "exec"))<br>  File "test\_with.py", line 33, in &lt;module&gt;<br>    test\_with()<br>  File "test\_with.py", line 28, in test\_with<br>    raise Exception<br>Exception |


证明了会先执行__enter__方法, 然后调用with内的逻辑, 最后执行__exit__做退出处理, 并且, 即使出现异常也能正常退出

filter的用法

相对filter而言, map和reduce使用的会更频繁一些, filter正如其名字, 按照某种规则过滤掉一些元素

|   |   |
| - | - |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9 | \#!/usr/bin/env python<br>\# -\*- coding: utf-8 -\*-<br>lst = [1, 2, 3, 4, 5, 6]<br>\# 所有奇数都会返回True, 偶数会返回False被过滤掉<br>print filter(lambda x: x % 2 != 0, lst)<br>\#输出结果<br>[1, 3, 5] |


一行作判断

当条件满足时, 返回的为等号后面的变量, 否则返回else后语句

|   |   |
| - | - |
| 1<br>2<br>3<br>4<br>5<br>6 | lst = [1, 2, 3]<br>new\_lst = lst[0] if lst is not None else None<br>print new\_lst<br>\# 打印结果<br>1 |


装饰器之单例

使用装饰器实现简单的单例模式

|   |   |
| - | - |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18 | \# 单例装饰器<br>def singleton(cls):<br>    instances = dict()  \# 初始为空<br>    def \_singleton(\*args, \*\*kwargs):<br>        if cls not in instances:  \#如果不存在, 则创建并放入字典<br>            instances[cls] = cls(\*args, \*\*kwargs)<br>        return instances[cls]<br>    return \_singleton<br>@singleton<br>class Test(object):<br>    pass<br>if \_\_name\_\_ == '\_\_main\_\_':<br>    t1 = Test()<br>    t2 = Test()<br>    \# 两者具有相同的地址<br>    print t1, t2 |


staticmethod装饰器

类中两种常用的装饰, 首先区分一下他们

- 普通成员函数, 其中第一个隐式参数为对象

- classmethod装饰器, 类方法(给人感觉非常类似于OC中的类方法), 其中第一个隐式参数为类

- staticmethod装饰器, 没有任何隐式参数. python中的静态方法类似与C++中的静态方法

|   |   |
| - | - |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>23<br>24<br>25<br>26<br>27<br>28<br>29<br>30<br>31<br>32<br>33<br>34<br>35 | \#!/usr/bin/env python<br>\# -\*- coding: utf-8 -\*-<br>class A(object):<br>    \# 普通成员函数<br>    def foo(self, x):<br>        print "executing foo(%s, %s)" % (self, x)<br>    @classmethod   \# 使用classmethod进行装饰<br>    def class\_foo(cls, x):<br>        print "executing class\_foo(%s, %s)" % (cls, x)<br>    @staticmethod  \# 使用staticmethod进行装饰<br>    def static\_foo(x):<br>        print "executing static\_foo(%s)" % x<br>def test\_three\_method():<br>    obj = A()<br>    \# 直接调用噗通的成员方法<br>    obj.foo("para")  \# 此处obj对象作为成员函数的隐式参数, 就是self<br>    obj.class\_foo("para")  \# 此处类作为隐式参数被传入, 就是cls<br>    A.class\_foo("para")  \#更直接的类方法调用<br>    obj.static\_foo("para")  \# 静态方法并没有任何隐式参数, 但是要通过对象或者类进行调用<br>    A.static\_foo("para")<br>if \_\_name\_\_ == '\_\_main\_\_':<br>    test\_three\_method()<br>    <br>\# 函数输出<br>executing foo(&lt;\_\_main\_\_.A object at 0x100ba4e10&gt;, para)<br>executing class\_foo(&lt;class '\_\_main\_\_.A'&gt;, para)<br>executing class\_foo(&lt;class '\_\_main\_\_.A'&gt;, para)<br>executing static\_foo(para)<br>executing static\_foo(para) |


property装饰器

- 定义私有类属性

将property与装饰器结合实现属性私有化(更简单安全的实现get和set方法)

|   |   |
| - | - |
| 1<br>2 | \#python内建函数<br>property(fget=None, fset=None, fdel=None, doc=None) |


fget是获取属性的值的函数,fset是设置属性值的函数,fdel是删除属性的函数,doc是一个字符串(like a comment).从实现来看，这些参数都是可选的

property有三个方法getter(), setter()和delete() 来指定fget, fset和fdel。 这表示以下这行

|   |   |
| - | - |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13 | class Student(object):<br>    @property  \#相当于property.getter(score) 或者property(score)<br>    def score(self):<br>        return self.\_score<br>    @score.setter \#相当于score = property.setter(score)<br>    def score(self, value):<br>        if not isinstance(value, int):<br>            raise ValueError('score must be an integer!')<br>        if value &lt; 0 or value &gt; 100:<br>            raise ValueError('score must between 0 ~ 100!')<br>        self.\_score = value |


iter魔法

- 通过yield和__iter__的结合, 我们可以把一个对象变成可迭代的

- 通过__str__的重写, 可以直接通过想要的形式打印对象

|   |   |
| - | - |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>23<br>24<br>25<br>26<br>27<br>28 | \#!/usr/bin/env python<br>\# -\*- coding: utf-8 -\*-<br>class TestIter(object):<br>    def \_\_init\_\_(self):<br>        self.lst = [1, 2, 3, 4, 5]<br>    def read(self):<br>        for ele in xrange(len(self.lst)):<br>            yield ele<br>    def \_\_iter\_\_(self):<br>        return self.read()<br>    def \_\_str\_\_(self):<br>        return ','.join(map(str, self.lst))<br>    <br>    \_\_repr\_\_ = \_\_str\_\_<br>def test\_iter():<br>    obj = TestIter()<br>    for num in obj:<br>        print num<br>    print obj<br>if \_\_name\_\_ == '\_\_main\_\_':<br>    test\_iter() |


神奇partial

partial使用上很像C++中仿函数(函数对象).

在stackoverflow给出了类似与partial的运行方式

|   |   |
| - | - |
| 1<br>2<br>3<br>4<br>5<br>6<br>7 | def partial(func, \*part\_args):<br>    def wrapper(\*extra\_args):<br>        args = list(part\_args)<br>        args.extend(extra\_args)<br>        return func(\*args)<br>    return wrapper |


利用用闭包的特性绑定预先绑定一些函数参数, 返回一个可调用的变量, 直到真正的调用执行

|   |   |
| - | - |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17 | \#!/usr/bin/env python<br>\# -\*- coding: utf-8 -\*-<br>from functools import partial<br>def sum(a, b):<br>    return a + b<br>def test\_partial():<br>    fun = partial(sum, 2)   \# 事先绑定一个参数, fun成为一个只需要一个参数的可调用变量<br>    print fun(3)  \# 实现执行的即是sum(2, 3)<br>if \_\_name\_\_ == '\_\_main\_\_':<br>    test\_partial()<br>    <br>\# 执行结果<br>5 |


神秘eval

eval我理解为一种内嵌的python解释器(这种解释可能会有偏差), 会解释字符串为对应的代码并执行, 并且将执行结果返回

看一下下面这个例子

|   |   |
| - | - |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21 | \#!/usr/bin/env python<br>\# -\*- coding: utf-8 -\*-<br>def test\_first():<br>    return 3<br>def test\_second(num):<br>    return num<br>action = {  \# 可以看做是一个sandbox<br>        "para": 5,<br>        "test\_first" : test\_first,<br>        "test\_second": test\_second<br>        }<br>def test\_eavl():  <br>    condition = "para == 5 and test\_second(test\_first) &gt; 5"<br>    res = eval(condition, action)  \# 解释condition并根据action对应的动作执行<br>    print res<br>if \_\_name\_\_ == '\_ |


exec

- exec在Python中会忽略返回值, 总是返回None, eval会返回执行代码或语句的返回值

- exec和eval在执行代码时, 除了返回值其他行为都相同

- 在传入字符串时, 会使用compile(source, '<string>', mode)编译字节码. mode的取值为exec和eval

|   |   |
| - | - |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>23 | \#!/usr/bin/env python<br>\# -\*- coding: utf-8 -\*-<br>def test\_first():<br>    print "hello"<br>def test\_second():<br>    test\_first()<br>    print "second"<br>def test\_third():<br>    print "third"<br>action = {<br>        "test\_second": test\_second,<br>        "test\_third": test\_third<br>        }<br>def test\_exec():<br>    exec "test\_second" in action<br>if \_\_name\_\_ == '\_\_main\_\_':<br>    test\_exec()  \# 无法看到执行结果 |


getattr

getattr(object, name[, default])Return the value of the named attribute of object. name must be a string. If the string is the name of one of the object’s attributes, the result is the value of that attribute. For example, getattr(x, ‘foobar’) is equivalent to x.foobar. If the named attribute does not exist, default is returned if provided, otherwise AttributeError is raised.

通过string类型的name, 返回对象的name属性(方法)对应的值, 如果属性不存在, 则返回默认值, 相当于object.name

|   |   |
| - | - |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>23<br>24<br>25 | \# 使用范例<br>class TestGetAttr(object):<br>    test = "test attribute"<br>    def say(self):<br>        print "test method"<br>def test\_getattr():<br>    my\_test = TestGetAttr()<br>    try:<br>        print getattr(my\_test, "test")<br>    except AttributeError:<br>        print "Attribute Error!"<br>    try:<br>        getattr(my\_test, "say")()<br>    except AttributeError: \# 没有该属性, 且没有指定返回值的情况下<br>        print "Method Error!"<br>if \_\_name\_\_ == '\_\_main\_\_':<br>    test\_getattr()<br>    <br>\# 输出结果<br>test attribute<br>test method |


命令行处理

|   |   |
| - | - |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>23<br>24<br>25<br>26<br>27<br>28<br>29<br>30<br>31<br>32<br>33<br>34<br>35<br>36<br>37<br>38 | def process\_command\_line(argv):<br>    """<br>    Return a 2-tuple: (settings object, args list).<br>    `argv` is a list of arguments, or `None` for ``sys.argv[1:]``.<br>    """<br>    if argv is None:<br>        argv = sys.argv[1:]<br>    \# initialize the parser object:<br>    parser = optparse.OptionParser(<br>        formatter=optparse.TitledHelpFormatter(width=78),<br>        add\_help\_option=None)<br>    \# define options here:<br>    parser.add\_option(      \# customized description; put --help last<br>        '-h', '--help', action='help',<br>        help='Show this help message and exit.')<br>    settings, args = parser.parse\_args(argv)<br>    \# check number of arguments, verify values, etc.:<br>    if args:<br>        parser.error('program takes no command-line arguments; '<br>                     '"%s" ignored.' % (args,))<br>    \# further process settings &amp; args if necessary<br>    return settings, args<br>def main(argv=None):<br>    settings, args = process\_command\_line(argv)<br>    \# application code here, like:<br>    \# run(settings, args)<br>    return 0        \# success<br>if \_\_name\_\_ == '\_\_main\_\_':<br>    status = main()<br>    sys.exit(status) |


读写csv文件

|   |   |
| - | - |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15 | \# 从csv中读取文件, 基本和传统文件读取类似<br>import csv<br>with open('data.csv', 'rb') as f:<br>    reader = csv.reader(f)<br>    for row in reader:<br>        print row<br>\# 向csv文件写入<br>import csv<br>with open( 'data.csv', 'wb') as f:<br>    writer = csv.writer(f)<br>    writer.writerow(['name', 'address', 'age'])  \# 单行写入<br>    data = [<br>            ( 'xiaoming ','china','10'),<br>            ( 'Lily', 'USA', '12')]<br>    writer.writerows(data)  \# 多行写入 |


各种时间形式转换

只发一张网上的图, 然后差文档就好了, 这个是记不住的

![](attachments/Python奇技淫巧%20%20Snow%20Memory_image_0.jpeg)

字符串格式化

一个非常好用, 很多人又不知道的功能

|   |   |
| - | - |
| 1<br>2<br>3 | &gt;&gt;&gt; name = "andrew"<br>&gt;&gt;&gt; "my name is {name}".format(name=name)<br>'my name is andrew' |


参考链接