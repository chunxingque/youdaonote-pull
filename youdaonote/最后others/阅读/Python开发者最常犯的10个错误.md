Python是一门简单易学的编程语言，语法简洁而清晰，并且拥有丰富和强大的类库。与其它大多数程序设计语言使用大括号不一样 ，它使用缩进来定义语句块。

在平时的工作中，Python开发者很容易犯一些小错误，这些错误都很容易避免，本文总结了Python开发者最常犯的10个错误，一起来看下，不知你中枪了没有。

![](attachments/Python开发者最常犯的10个错误_image_0.jpeg)

 

1.滥用表达式作为函数参数默认值

Python允许开发者指定一个默认值给函数参数，虽然这是该语言的一个特征，但当参数可变时，很容易导致混乱，例如，下面这段函数定义：

>>> def foo(bar=[]):        # bar is optional and defaults to [] if not specified
...    bar.append("baz")    # but this line could be problematic, as we'll see...
...    return bar

在上面这段代码里，一旦重复调用foo()函数（没有指定一个bar参数），那么将一直返回'bar'，因为没有指定参数，那么foo()每次被调用的时候，都会赋予[]。下面来看看，这样做的结果：

>>> foo()
["baz"]
>>> foo()
["baz", "baz"]
>>> foo()
["baz", "baz", "baz"]

解决方案：

>>> def foo(bar=None):
...    if bar is None:		# or if not bar:
...        bar = []
...    bar.append("baz")
...    return bar
...
>>> foo()
["baz"]
>>> foo()
["baz"]
>>> foo()
["baz"]

2.错误地使用类变量

先看下面这个例子：

>>> class A(object):
...     x = 1
...
>>> class B(A):
...     pass
...
>>> class C(A):
...     pass
...
>>> print A.x, B.x, C.x
1 1 1

这样是有意义的：

>>> B.x = 2
>>> print A.x, B.x, C.x
1 2 1

再来一遍：

>>> A.x = 3
>>> print A.x, B.x, C.x
3 2 3

仅仅是改变了A.x，为什么C.x也跟着改变了。

在Python中，类变量都是作为字典进行内部处理的，并且遵循方法解析顺序（MRO）。在上面这段代码中，因为属性x没有在类C中发现，它会查找它的基类（在上面例子中只有A，尽管Python支持多继承）。换句话说，就是C自己没有x属性，独立于A，因此，引用 C.x其实就是引用A.x。

3.为异常指定不正确的参数

假设代码中有如下代码：

>>> try:
...     l = ["a", "b"]
...     int(l[2])
... except ValueError, IndexError:  # To catch both exceptions, right?
...     pass
...
Traceback (most recent call last):
  File "<stdin>", line 3, in <module>
IndexError: list index out of range

问题在这里，except语句并不需要这种方式来指定异常列表。然而，在Python 2.x中，except Exception,e通常是用来绑定异常里的 第二参数，好让其进行更进一步的检查。因此，在上面这段代码里，IndexError异常并没有被except语句捕获，异常最后被绑定 到了一个名叫IndexError的参数上。

在一个异常语句里捕获多个异常的正确方法是指定第一个参数作为一个元组，该元组包含所有被捕获的异常。与此同时，使用as关键字来保证最大的可移植性，Python 2和Python 3都支持该语法。

>>> try:
...     l = ["a", "b"]
...     int(l[2])
... except (ValueError, IndexError) as e:  
...     pass
...
>>>

4.误解Python规则范围

Python的作用域解析是基于LEGB规则，分别是Local、Enclosing、Global、Built-in。实际上，这种解析方法也有一些玄机，看下面这个例子： 

>>> x = 10
>>> def foo():
...     x += 1
...     print x
...
>>> foo()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in foo
UnboundLocalError: local variable 'x' referenced before assignment

许多人会感动惊讶，当他们在工作的函数体里添加一个参数语句，会在先前工作的代码里报UnboundLocalError错误（ 点击这里查看更详细描述）。 

在使用列表时，开发者是很容易犯这种错误的，看看下面这个例子：

>>> lst = [1, 2, 3]
>>> def foo1():
...     lst.append(5)   # This works ok...
...
>>> foo1()
>>> lst
[1, 2, 3, 5]

>>> lst = [1, 2, 3]
>>> def foo2():
...     lst += [5]      # ... but this bombs!
...
>>> foo2()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in foo
UnboundLocalError: local variable 'lst' referenced before assignment

为什么foo2失败而foo1运行正常？ 

答案与前面那个例子是一样的，但又有一些微妙之处。foo1没有赋值给lst，而foo2赋值了。lst += [5]实际上就是lst = lst + [5]，试图给lst赋值（因此，假设Python是在局部作用域里）。然而，我们正在寻找指定给lst的值是基于lst本身，其实尚未确定。

5.修改遍历列表

下面这段代码很明显是错误的：

>>> odd = lambda x : bool(x % 2)
>>> numbers = [n for n in range(10)]
>>> for i in range(len(numbers)):
...     if odd(numbers[i]):
...         del numbers[i]  # BAD: Deleting item from a list while iterating over it
...
Traceback (most recent call last):
  	  File "<stdin>", line 2, in <module>
IndexError: list index out of range

在遍历的时候，对列表进行删除操作，这是很低级的错误。稍微有点经验的人都不会犯。

对上面的代码进行修改，正确地执行：

>>> odd = lambda x : bool(x % 2)
>>> numbers = [n for n in range(10)]
>>> numbers[:] = [n for n in numbers if not odd(n)]  # ahh, the beauty of it all
>>> numbers
[0, 2, 4, 6, 8]

6.如何在闭包中绑定变量

看下面这个例子：

>>> def create_multipliers():
...     return [lambda x : i * x for i in range(5)]
>>> for multiplier in create_multipliers():
...     print multiplier(2)
...

你期望的结果是：

<code>0
2
4
6
8</code>

实际上：

<code>8
8
8
8
8</code>

是不是非常吃惊！出现这种情况主要是因为Python的后期绑定行为，该变量在闭包中使用的同时，内部函数又在调用它。

解决方案：

>>> def create_multipliers():
...     return [lambda x, i=i : i * x for i in range(5)]
...
>>> for multiplier in create_multipliers():
...     print multiplier(2)
...
0
2
4
6
8

7.创建循环模块依赖关系

假设有两个文件，a.py和b.py，然后各自导入，如下：

在a.py中：

import b

def f():
    return b.x
	
print f()

在b.py中：

import a

x = 1

def g():
    print a.f()

首先，让我们试着导入a.py：

<code>>>> import a
1</code>

可以很好地工作，也许你会感到惊讶。毕竟，我们确实在这里做了一个循环导入，难道不应该有点问题吗？

仅仅存在一个循环导入并不是Python本身问题，如果一个模块被导入，Python就不会试图重新导入。根据这一点，每个模块在试图访问函数或变量时，可能会在运行时遇到些问题。

当我们试图导入b.py会发生什么（先前没有导入a.py）：

>>> import b
Traceback (most recent call last):
  	  File "<stdin>", line 1, in <module>
  	  File "b.py", line 1, in <module>
    import a
  	  File "a.py", line 6, in <module>
	print f()
  	  File "a.py", line 4, in f
	return b.x
AttributeError: 'module' object has no attribute 'x'

出错了，这里的问题是，在导入b.py的过程中还要试图导入a.py，这样就要调用f()，并且试图访问b.x。但是b.x并未被定义。 

可以这样解决，仅仅修改b.py导入到a.py中的g()函数：

x = 1
def g():
    import a	# This will be evaluated only when g() is called
    print a.f()

无论何时导入，一切都可以正常运行：

>>> import b
>>> b.g()
1	# Printed a first time since module 'a' calls 'print f()' at the end
1	# Printed a second time, this one is our call to 'g'

8.与Python标准库模块名称冲突 

Python拥有非常丰富的模块库，并且支持“开箱即用”。因此，如果不刻意避免，很容易发生命名冲突事件。例如，在你的代码中可能有一个email.py的模块，由于名称一致，它很有可能与Python自带的标准库模块发生冲突。

9.未按规定处理Python2.x和Python3.x之间的区别

看一下foo.py：

import sys

def bar(i):
    if i == 1:
        raise KeyError(1)
    if i == 2:
        raise ValueError(2)

def bad():
    e = None
    try:
        bar(int(sys.argv[1]))
    except KeyError as e:
        print('key error')
    except ValueError as e:
        print('value error')
    print(e)

bad()

在Python 2里面可以很好地运行：

$ python foo.py 1
key error
1
$ python foo.py 2
value error
2

但是在Python 3里：

$ python3 foo.py 1
key error
Traceback (most recent call last):
  File "foo.py", line 19, in <module>
    bad()
  File "foo.py", line 17, in bad
    print(e)
UnboundLocalError: local variable 'e' referenced before assignment

解决方案：

import sys

def bar(i):
    if i == 1:
        raise KeyError(1)
    if i == 2:
        raise ValueError(2)

def good():
    exception = None
    try:
        bar(int(sys.argv[1]))
    except KeyError as e:
        exception = e
        print('key error')
    except ValueError as e:
        exception = e
        print('value error')
    print(exception)

good()

在Py3k中运行结果：

<code>$ python3 foo.py 1
key error
1
$ python3 foo.py 2
value error
2</code>

在 Python招聘指南里有许多关于Python 2与Python 3在移植代码时需要关注的注意事项与讨论，大家可以前往看看。

10.滥用__del__方法

比如这里有一个叫mod.py的文件：

import foo
class Bar(object):
   	    ...
    def __del__(self):
        foo.cleanup(self.myhandle)

下面，你在another_mod.py文件里执行如下操作：

import mod
mybar = mod.Bar()

你会获得一个AttributeError异常。

至于为什么会出现该异常，点击这里查看详情。当解释器关闭时，该模块的全局变量全部设置为None。因此，在上面这个例子里，当__del__被调用时，foo已经全部被设置为None。

一个很好的解决办法是使用atexit.register()代替。顺便说一句，当程序执行完成后，您注册的处理程序会在解释器关闭之前停止 工作。

修复上面问题的代码：

import foo
import atexit

def cleanup(handle):
    foo.cleanup(handle)


class Bar(object):
    def __init__(self):
        ...
        atexit.register(cleanup, self.myhandle)

在程序的正常终止的前提下，这个实现提供了一个整洁可靠的方式调用任何需要清理的功能。

总结

Python是一款强大而灵活的编程语言，并且带有许多机制和模式来大大提高工作效率。正如任何一门语言或软件工具一样，人们对其能力都会存在一个限制性地理解或欣赏，有些是弊大于利，有些时候反而会带来一些陷进。 体会一名语言的细微之处，理解一些常见的陷阱，有助于你在开发者的道路上走的更远。

来自： toptal



本文为CSDN编译整理，未经允许不得转载，如需转载请联系market#csdn.net(#换成@)

顶

16

 

踩

1

推荐阅读相关主题： 开发者 解决方案 全局变量 工作 语言 移植

- 相关文章

- 最新报道

- 一周消息树：微软半年内将终止对Win 7、Office 2010 SP1等产品的支持

- 深度神经网络DNN的多GPU数据并行框架 及其在语音识别的应用

- 兼容Windows工程：Cocos Studio for Mac 1.0 Beta版本发布

- Intel携手三星、博通等 建立物联网联盟OIC

- Microsoft、RedHat、IBM、Docker等公司加入Kubernetes社区

- 指尖上的阅读：MIT开发盲人专用设备FingerReader

已有50条评论

还可以再输入500个字

![](attachments/Python开发者最常犯的10个错误_image_1.gif)

redstoneleo欢迎您！

- 最新评论

- 最热评论

![](attachments/Python开发者最常犯的10个错误_image_2.jpeg)

xy_zhao 2014-05-13 23:11

第六点的那个i的变量搞得有点糊弄人，如下可能会更加容易理解一点~ >>> def create_multipliers(): ... return [lambda x, y=i : y * x for i in range(5)]

   回复

![](attachments/Python开发者最常犯的10个错误_image_3.gif)

laozi 2014-05-14 10:21

第6题我估计是为了说明问题，我认为真正的pythoner会这么解决： def my_multiplier( x ): return lambda i: i*x map( my_multiplier( 2 ), xrange( 5 ) )

   回复

![](attachments/Python开发者最常犯的10个错误_image_3.gif)

laozi 2014-05-14 10:56

回复@laozi:前面的代码犯了一个小错误，最好的做法是 map( my_multiplier( 2 ), range( 5 ) ) 因为对于map来说，执行可以并行的 而xrange是generator，每次调用才返回一个值，这种情况适合与在for循环里可能会提前终止循环，或是为了节省内存，因为range是直接生成一个列表 但是对于map来说，因为可以并行工作，所以用range直接产生list更好

   回复

![](attachments/Python开发者最常犯的10个错误_image_3.gif)

laozi 2014-05-13 17:19

还是要补一句，请先从c/c++入手，再进入python，这样你才能更深入理解The Zen of Python，同时你也有能力可以扩展python，切记，切记

1票，来自doglesss    回复

![](attachments/Python开发者最常犯的10个错误_image_3.gif)

laozi 2014-05-13 17:13

我以后一定要学会说话一次性说完，请在python的交互界面上输入import this，会有惊喜的，哈哈

   回复

![](attachments/Python开发者最常犯的10个错误_image_3.gif)

laozi 2014-05-13 17:01

顺便普及一下，Zen就是禅，想象一下禅，你就知道pythoner在追求什么了

   回复

![](attachments/Python开发者最常犯的10个错误_image_3.gif)

laozi 2014-05-13 16:55

顺便推广一下python的文化，特别是Tim Peters写的Python格言(The Zen of Python)，归纳一下就是简洁，优雅，可读性。这是真正的pythoner自然而然遵守的，记住我们就是程序界的雅皮士

   回复

![](attachments/Python开发者最常犯的10个错误_image_9.jpeg)

CyberLogic 2014-05-13 14:03

不错，收藏！

   回复

![](attachments/Python开发者最常犯的10个错误_image_10.jpeg)

FAIRose 2014-05-13 11:02

请问Python有哪些IDE啊？都是怎么用python做开发的？

   回复

![](attachments/Python开发者最常犯的10个错误_image_11.gif)

lnykfeng 2014-05-13 10:27

mark

   回复

![](attachments/Python开发者最常犯的10个错误_image_12.jpeg)

bearmingo 2014-05-13 09:04

学习了，

   回复

![](attachments/Python开发者最常犯的10个错误_image_13.gif)

coblan 2014-05-13 03:15

非常不错啊。很多问题我都遇到过。 实际上python的问题不仅仅如此，比如还有 * 相对导入，绝对导入。 * C和C++库抓来就可以用，但是可能存在c与C++对象提前析构 看似简单的python有时比C++还烦。包装了太多，你完全找不到错误所在。 用着python的迭代和生成器确实非常实用。python很灵活，但是在稍微大点的软件中设计模式还是需要的。 从这个文章中学到一招，atexit.register()，很不错。

   回复

![](attachments/Python开发者最常犯的10个错误_image_3.gif)

laozi 2014-05-13 10:47

atexit也是来自c/c++的，所以大家一定要清楚，原生态的python其实完全基于c/c++的，c和c++的库不是抓起来就能用的，需要一个包装接口的，提前析构的原因是python内部采用了智能指针来释放内存，而不是java的垃圾收集，包装接口写得不好，智能指针在该+1的时候没有+1，自然会提前析构

   回复

![](attachments/Python开发者最常犯的10个错误_image_13.gif)

coblan 2014-05-13 17:11

回复@laozi:C/C++库确实抓来就可以用，ctype直接就可以用。只不过c/c++对象需要你自己在c/c++侧暴露接口来自己管理而已，少量用些C/C++时根本就不需要用刻意包装好的python库。包装好的c/c++库(pyqt等等)只不过比你管理得更好而已。由于C/C++库设计的原因，某些C/C++对象析构问题，不管你怎么包装，python还是管理不了的。

   回复

![](attachments/Python开发者最常犯的10个错误_image_3.gif)

laozi 2014-05-14 10:02

回复@coblan:拜托，你那个ctypes就是直接调用动态库，这不是python的特性，这也不是pythoner该做的，你应该直接用c/c++写一个python扩展，在扩展代码里动态或编译调用so

   回复

![](attachments/Python开发者最常犯的10个错误_image_3.gif)

laozi 2014-05-14 10:29

回复@coblan:我再补充一句，设计模式的作用是什么？是为了快速适应需求变化，带来的问题是可读性的降低 请记住Special cases aren't special enough to break the rules. python就是为了快速开发而存在的，请拒绝设计模式，或是说你还没有真正成为一个pythoner，你只是一个python工程师

   回复

![](attachments/Python开发者最常犯的10个错误_image_18.jpeg)

奶白象 2014-05-13 00:07

路过。党争啊。。。

   回复

![](attachments/Python开发者最常犯的10个错误_image_19.gif)

zhu91aizhu 2014-05-12 20:07

请大神解释一下第一条。

   回复

![](attachments/Python开发者最常犯的10个错误_image_20.gif)

carr123 2014-05-12 19:26

啊哈，还漏了两条： 1. 有些人把python优美简洁的语法写成JAVA那么冗长垃圾 2. 有些人把python简洁的解决方案套上只有JAVA程序员才喜爱用的设计模式，使得代码可读性急剧下降。 还大言不惭“编程语言不重要，会了设计模式打遍天下”

   回复

![](attachments/Python开发者最常犯的10个错误_image_3.gif)

laozi 2014-05-13 11:13

你去看linux的内核代码，有多少是c++的，几乎都是c，你用c怎么玩设计模式啊。玩python+c/c++玩的是另一种设计模式，即谈判专家+特种部队模式，谈判专家玩的是业务逻辑，特种部队执行高负载工作，聪明的人一定明白我是怎么指代的

   回复

![](attachments/Python开发者最常犯的10个错误_image_3.gif)

laozi 2014-05-13 11:15

回复@laozi:港片看多了，还是完全按照港片的说法，谈判专家+飞虎队

   回复

![](attachments/Python开发者最常犯的10个错误_image_23.jpeg)

liqiao_2010 2014-05-13 16:01

回复@laozi:意思是逻辑用Python写，性能要求高的用c/c++?

   回复

![](attachments/Python开发者最常犯的10个错误_image_3.gif)

laozi 2014-05-13 16:09

回复@liqiao_2010:当然啊，不过这个c/c++不是纯的，是包装过的c/c++，你可以用c/c++写函数，写类，然后写个python扩展接口，这样python工程师一个import，就能像用原生态python类库一样使用这些c函数和c++类了（当然是通过接口），这就是python的开发模式

   回复

![](attachments/Python开发者最常犯的10个错误_image_25.gif)

qian_ice 2014-05-14 13:26

这狗币到处诋毁JAVA，还说JAVAer瞧不起别人，看看你自己说了JAVA多少坏话

   回复

![](attachments/Python开发者最常犯的10个错误_image_26.jpeg)

Linustd 2014-05-12 18:46

所有为了编程而编程的人，都是不要脸的人。 编程的目的是为了做出产品，完成功能。在任何编码之前，先应该想想需要怎么做，然后再去google一下python里这个功能是怎么写代码的就可以。 没有必要专门去学习编程，而是应该在需求中查资料，从而学会编程。 当然这需要一个前提，那就是你有基本的编程素养，而编程素养是不能通过学习一门语言而学会的，你需要的是比较深入的了解一个完整的系统的设计和编程方案。 比如，你在大学里就把《apue》这本书读了三遍，滚瓜烂熟，毕业后，公司招\聘问你会C++吗？ 你说不会，会PHP吗？你说不会，会PYTHON吗？你说还不会。 但是没问题， 给你C++的任务，给你PHP的任务，给你PYTHON的任务，你一边设计思路，一边google，照样能做出高质量的代码，而且比那些会c++, php, python的人，写的还健壮。

1票，来自haoyinpeng   1票  回复

![](attachments/Python开发者最常犯的10个错误_image_27.gif)

haoyinpeng 2014-05-12 22:13

同感！

   回复

![](attachments/Python开发者最常犯的10个错误_image_12.jpeg)

bearmingo 2014-05-13 09:42

一天到晚说要做产品的，也没看你们出什么好产品啊。。。。

   回复

![](attachments/Python开发者最常犯的10个错误_image_3.gif)

laozi 2014-05-13 10:50

我认识的写代码漂亮的，都不是计算机系毕业的，任何编程语言都是工具，关键是思想；如果采用同一个工具，比得就是思想；但是如果大家思路都很清晰，比得就是工具了。所以不用高看编程语言，同样也不要低看编程语言。

   回复

![](attachments/Python开发者最常犯的10个错误_image_30.jpeg)

ccnyou 2014-05-12 17:40

文章不错，翻译很烂，原文：http://www.toptal.com/python/top-10-mistakes-that-python-programmers-make

   回复

![](attachments/Python开发者最常犯的10个错误_image_31.jpeg)

比特C 2014-05-12 16:23

google了原文“Top 10 Mistakes that Python Programmers Make”，仅针对第一个例子，翻译的不够妥当，没有说清楚，另外oschina也有这篇文章的翻译，虽然不够通顺，但没有漏掉细节，重申一下，仅针对第一个例子，希望csdn越来越好。

   回复

![](attachments/Python开发者最常犯的10个错误_image_31.jpeg)

比特C 2014-05-12 16:02

我想问一下，第一个例子里，既然每次调用foo()都会给bar赋[]，那为什么每次调用的结果都是在列表后面追加？这样解释不通啊。顺带求原文链接。

   回复

![](attachments/Python开发者最常犯的10个错误_image_13.gif)

coblan 2014-05-13 03:01

我遇到过这个问题。实际上是在生成函数对象foo时，系统就绑定了一个空的list对象，作为bar的默认参数。所以每次调用函数的时候，默认参数都是指向的同一个list对象。

   回复

![](attachments/Python开发者最常犯的10个错误_image_34.jpeg)

小小的猛 2014-05-13 09:58

.apend() 函数作用就是添加附加上去 同一个bar自然追加 个人理解哈

  1票  回复

![](attachments/Python开发者最常犯的10个错误_image_3.gif)

laozi 2014-05-13 11:03

我前面不是说过的，原生态的python其实就是c/c++, 对于列表来说传的是引用，对于对象来说也是引用，但是python的变量在某些情况也是无需事先声明的，比如缺省参数，这时python解释器，就会自动分配一个“全局”变量，作用域仅限于函数内部，不但是[]，你用def foo( bar = [ 'first', ] )去试，结果是一样的

   回复

![](attachments/Python开发者最常犯的10个错误_image_3.gif)

laozi 2014-05-13 11:07

同样，python的的内置数据类型，字典{}，集合set([])做为参数都是传引用的，对这两种类型去设缺省值，然后在函数里去增加值，也是累加的。

   回复

![](attachments/Python开发者最常犯的10个错误_image_3.gif)

laozi 2014-05-13 11:09

其实利用这个特性，我们可以实现一个静态变量的功能，全局作用于函数，赋值一次，运算多次

   回复

![](attachments/Python开发者最常犯的10个错误_image_3.gif)

laozi 2014-05-13 11:22

回复@coblan:class StaticInt: def __init__( self, val ): self.val = val def foo( counter = StaticInt( 0 ) ): counter.val += 1 return counter 只是为了说明问题，细节就不多完善了

   回复

![](attachments/Python开发者最常犯的10个错误_image_39.jpeg)

candyguy242 2014-05-12 16:02

mark

   回复

![](attachments/Python开发者最常犯的10个错误_image_40.gif)

chg_lele 2014-05-12 14:48

很好的翻译文章，非常容易犯的错误！

   回复

![](attachments/Python开发者最常犯的10个错误_image_41.jpeg)

丨LYF丨 2014-05-12 14:33

mark

   回复

![](attachments/Python开发者最常犯的10个错误_image_42.gif)

supermig 2014-05-12 14:30

makr

   回复

![](attachments/Python开发者最常犯的10个错误_image_43.jpeg)

okgoood 2014-05-12 13:57

饿,受不了这种头可以缩进缩出的乌龟语言,还是只没有尾巴的乌龟

  2票  回复

![](attachments/Python开发者最常犯的10个错误_image_3.gif)

laozi 2014-05-12 14:54

也就是说你写的代码没有缩进，都是顶格写的，这算露隐癖吗？

1票，来自sylcc_    回复

![](attachments/Python开发者最常犯的10个错误_image_20.gif)

carr123 2014-05-12 19:23

JAVA的臃肿代码我都懒得写，哈哈

1票，来自my雯wife    回复

![](attachments/Python开发者最常犯的10个错误_image_46.jpeg)

haitianqingye 2014-05-12 12:35

提醒了我

   回复

![](attachments/Python开发者最常犯的10个错误_image_47.gif)

bbsdkjdx 2014-05-12 12:00

很好的文章，学习！

   回复

![](attachments/Python开发者最常犯的10个错误_image_48.gif)

磊娃 2014-05-12 11:58

mark

   回复

![](attachments/Python开发者最常犯的10个错误_image_49.jpeg)

Eliezer_洪康 2014-05-12 11:21

mark

   回复

![](attachments/Python开发者最常犯的10个错误_image_50.jpeg)

xiaoai 2014-05-12 11:18

短短的几句总结，就有N多错字，这也许是社会大环境造就的吧！

   回复

![](attachments/Python开发者最常犯的10个错误_image_3.gif)

laozi 2014-05-12 10:05

非常令人开心，本来以为进来又是什么tab和空格的说教，很专业，对编辑赞一下