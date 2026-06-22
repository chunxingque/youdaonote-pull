https://twitter.com/job_openings_ng/status/1732291345987813788

https://drive.google.com/file/d/14NgAvAMk2T-ed9NnA34PgilxC97lxGQW/view





IS TUPLE COMPREHENSION POSSIBLE? IF YES, HOW, AND IF NOT WHY?
Tuple comprehension is not possible in Python, unlike list comprehensions. It would result in a generator, not a tuple



WHAT ARE FUNCTION ANNOTATIONS IN PYTHON?
Function annotations add metadata to function parameters and return value. They are used to provide information about expected types or behavior.









口语

https://youteam.io/blog/senior-python-developer-interview-questions-and-answers/#6_Describe_a_situation_where_you_had_to_integrate_Python_with_a_non-Python_system_or_service_such_as_a_messaging_queue_or_a_RESTful_API



https://blog.imocha.io/python-interview-questions-and-answers



https://builtin.com/software-engineering-perspectives/python-interview-questions





可能有几个老旧的算法题

https://www.educative.io/blog/python-interview-questions

Question 38:开始



可以最后看

https://www.w3resource.com/python-interview/index.php

https://www.keka.com/python-coding-interview-questions





Sure, my name is Zhao. Thanks for offering me this opportunity to join
the interview. I have started developing websites and desktop software since
2012. Technologies I used include Python, Django, PyQt, HTML, CSS, JavaScript,
Git, and REST API. Among them I use Python and Django more often. Besides, I am familiar with user experience design, so I implement software features with
user experience in mind. Designing a simple user experience can make the software convenient to use. Furthermore, I like mathematics, so I'm conscientious in doing my job, and I have strong self-learning ability, if there are new technologies or
skills I have to learn, I am confident in mastering them quickly. OK, this is it.





I am a little of perfectionism, so sometimes I will try to improve the
old but not elegant code. Most of the time the old code works well, but once I
tried to make it elegant, it is highly possible that I will introduce new bugs
into the code, which results in a lot of unnecessary work to fix the code, but
it didn’t contribute much to the product, which led me to
think about the sense of code perfectionism, and whether my perfectionism will
essentially contribute to problems I am working on.





That's because I gradually realized my strength lies in logical
reasoning, although the strength is helpful for the designing work, I think the
strength will contribute more in programming work. So I changed my job as a
software developer.





Of course, I am worried that I will take over my job. I heard from an expert who predicted that ai will be capable of doing some basic entry level programming work within 10 years. I had thought about the crisis for a while and finally I concluded that I have to upgrade myskills into new level. In order to survive uh keep learning and keep evolving is my reaction to the AI crisis





For example，in some registration forms和which require you to select the country your currently living。Uh some forms are well left that field blank, A good user experience in this case are can automatically select thecountry the user is currently aliving according to his IP location, Although it is are not uh absolutely answer, but uh it would be are correct in most of the cases. So the automatic selection based on the application is a great experience that can help the registration process simple





The Global Interpreter Lock (GIL) is a mechanism in CPython (the reference implementation of Python) that ensures only one thread executes Python bytecode at a time. Here are some key points about the Python GIL:

1. GIL and multi-threading: The GIL prevents multiple native threads from executing Python bytecodes simultaneously. This means that even if you have multiple threads in your Python program, only one thread can execute Python code at a time. As a result, the GIL can limit the potential performance gains from multi-threading in CPU-bound tasks.

2. GIL and I/O-bound tasks: The GIL does not significantly impact I/O-bound tasks, such as network requests or file operations, as these tasks often involve waiting for external resources. In such cases, the GIL can be released, allowing other threads to execute Python code concurrently.

3. GIL and CPU-bound tasks: The GIL can be a bottleneck for CPU-bound tasks, where the majority of the work is done in Python code. Since only one thread can execute Python bytecodes at a time, multi-threading may not provide significant performance improvements for CPU-bound tasks. However, multi-threading can still be useful in scenarios involving I/O operations within CPU-bound tasks.

4. GIL and multi-processing: Python's `multiprocessing` module allows for true parallelism by creating separate processes, each with its own Python interpreter and GIL. Each process can utilize multiple cores and execute Python code concurrently, bypassing the limitations imposed by the GIL. This makes multi-processing a viable option for CPU-bound tasks.

5. GIL and C extensions: C extensions, which are written in languages like C or C++, can release the GIL during their execution, allowing multiple threads to run concurrently. This can be beneficial for performance-critical sections of code that are implemented as C extensions.

6. GIL and alternative implementations: It's important to note that the GIL is specific to CPython. Other implementations of Python, such as Jython or IronPython, may not have a GIL or may have different threading models that allow for true parallelism.

7. GIL and thread safety: The GIL ensures thread safety within the CPython interpreter by preventing multiple threads from accessing and modifying Python objects simultaneously. This simplifies the implementation of CPython and helps avoid race conditions.

It's worth mentioning that there have been ongoing discussions and efforts to address the limitations of the GIL in CPython. However, as of my knowledge cutoff in September 2021, the GIL remains a characteristic of CPython.



Well, different projects have different difficulties, but one critical problem among the different projectsis to collaborate with your customers to figure out the right solution to the problems. Sometimes when you ask your customers or they just are present you the sofa design the hota planned， But the the software port type are may be a efficient way to solve the needs. So you shouldn't swallow to their software design without question and to go to the development of the software. Instead you should ask or why the shoes why the software should work that way. Then your customer might tell you that that's because uh we want to solve what kind of problem. And you can even ask what you want to solve their problem. Then your customer might tell you the reason I finished you can even eat rating the process of a few times until you both of figure out the true needs，Then because you as a experienced programmer have the software engineer background. You caneven uh propose or if more efficient solution to the needs of which can even also help save you a lot ofa development are efforts。Otherwise your team might spend a lot of time energy in a workinga software that might not are fully solve your customers problems。











多线程的问题 deadlock

2. 说说同步，阻塞 ，异步， 非阻塞吧。

3. 说说操作系统进程通信方法，线程同步，通信方法。

4. 问你了解tcp么，说说为什么多线程下载快把。

5. 谈谈cookies和seeions吧

说说TCP和UDP的区别吧。

---

缓存

碰到的问题

正则表达式

算法 数据结构

数据库

Linux

团队合作



候选人应该做好哪些技术准备呢?

网上可以搜到一些面试题, 找了一些还不错的链接列出来

http://programmers.stackexchange.com/questions/21917/python-interview-questions
https://github.com/sigmavirus24/python-interview-questions
https://gist.github.com/xiangzhuyuan/7454001522d275021b2d
https://github.com/ContinuumIO/interview-questions
https://github.com/Flowerowl/python_articles
http://marselester.com/preparation-to-python-interview.html
https://github.com/zachwill/cracking-the-coding-interview
http://www.bogotobogo.com/python/python_interview_questions.php
https://www.quora.com/What-are-good-Python-interview-questions
https://www.reddit.com/r/Python/comments/1knw7z/python_interview_questions
https://github.com/1st/interview/blob/master/python.md

还有2个中文:

https://github.com/taizilongxu/interview_python
https://gist.github.com/prim/3e7f814187c715541ef2


毕竟我也是面试官, 就不划定那些是常见问题了. 防止我的主观意见对于未来影响面试者的评价公正性. 而且我也要说一点, 我也不评论上述文章中的答案的正确性了. 大家还是需要在面试前先做些查询和研究了

用心

1. 去某公司面试前, 或者立志要去该公司. 最好先了解公司用到的python相关的技术栈, 这样可以有针对的准备相关内容

1. 针对性的准备想要做的职位的python技能需求. 比如面试运维开发, 多准备系统, 数据库, 配置管理相关的知识, 比如web框架(除非了解到该职位需要)

1. 及时关注python技能最新用法, 或者推荐用法. 多了解python3的趋势, 有可能会被面试官问到.

1. 有个github账号. 能把自己的想法实践出来的python项目, 这样就多了了解你的机会. 可能在面试中就会少问你对应的技术点





Web conferencing details provided upon confirmation.

Kindly prepare yourself for a 30-second (elevator pitch) - a quick self-presentation and get ready to present your recent projects and your skills.

 

How to do well in this interview?

 

1. Be on time! It is very unprofessional to be late even by 5 min and will decrease your chance of passing the interview.

 

2. Prepare yourself, this interview will be extremally technical and you will be facing a senior developer who will ask you many questions regarding your stack. Make it count!

 

3. Show us you are interesting, make a 30-second self-presentation pitch to show us who you really are, tell us something unusual about you and stand out.

 

4. Be presentable, make sure your camera and microphone work perfectly

 

5. Lastly, it is highly recommended to prepare a project you have worked on and present it in the interview. Show us your best work and show us you are passionate about it.



 





