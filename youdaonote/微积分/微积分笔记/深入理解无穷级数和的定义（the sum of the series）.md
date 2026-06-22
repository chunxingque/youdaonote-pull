2+2=4 有限个的运算，穷举、数数就可以核实准确性，信心满满

无穷级数和，无穷无尽的加数，数不过来，不好核实准确性，让人怀疑——从极限逼近的角度认识它的正确性

numerical

equality. 

Given an infinite sequence (a1, a2, a3, ...), a series is informally the form of adding all those terms together: a1 + a2 + a3 + ···. To emphasize that there are an infinite number of terms, a series is often called an infinite series. 

![](attachments/深入理解无穷级数和的定义（the%20sum%20of%20the%20series）_image_0.png)

值得注意的是等式右边并不是左边的和，只是左边的缩写形式。

![](attachments/深入理解无穷级数和的定义（the%20sum%20of%20the%20series）_image_1.png)

because when you start from adding up the first two terms of the infinite sequence, and then add the third term, the 4-th term, ..., no matter how much time you spend on adding these terms, you always end up adding up only a finite number of terms , thus you couldn't add up an infinite number of terms, so cannot compute their sum by adding one term after another.  

An easy way that an infinite series has a sum is if all the $a_n$ are zero for n sufficiently large. Such a series can be identified with a finite sum, so it is only infinite in a trivial sense.

Working out the properties of the series that has a sum even if infinitely many terms are non-zero is the essence of the study of series. Consider the example

![](attachments/深入理解无穷级数和的定义（the%20sum%20of%20the%20series）_image_2.jpeg)

It is possible to "visualize" it has sum on the real number line: we can imagine a line of length 2, with successive segments marked off of lengths 1, ½, ¼, etc. There is always room to mark the next segment, because the amount of line remaining is always the same as the last segment marked: when we have marked off ½, we still have a piece of length ½ unmarked, so we can certainly mark the next ¼. This argument does not prove that the sum is equal to 2 (although it is), but it does prove that it is at most 2. In other words, the series has an upper bound. As for proving the series is equal to 2, we choose $$a_n=1+\frac12+\frac14+\frac18+\frac{1}{16}+\cdots+\frac{1}{2^{n-1}}+\frac{1}{2^n}$$ and $b_n=2$, then $$a_n<1+\frac12+\frac14+\frac18+\frac{1}{16}+\cdots+\frac{1}{2^{n-1}}+\frac{1}{2^n}+\cdots\leq b_n$$ holds for every nature number $n$  and $\lim _{n\rightarrow \infty }\left( b_{n}-a_{n}\right) =\lim _{n\rightarrow \infty }\frac{1}{2^n}=0$ , according to the nested intervals theorem the intersection of all the $[a_n,b_n]$ contains exactly one real number, since 2 is an element of each of these intervals, $1+\frac12+\frac14+\frac18+\frac{1}{16}+\cdots+\frac{1}{2^{n-1}}+\frac{1}{2^n}+\cdots = 2$, this proved the sum of the series is 2.

It is also possible to prove 
$$1 - {1 \over 2} + {1 \over 3} - {1 \over 4} + {1 \over 5} - \cdots =\sum_{n=1}^\infty {\left(-1\right)^{n-1} \over n}=\ln(2)$$
using the nested intervals theorem by choosing $a_k=\sum_{n=1}^{2k} {\left(-1\right)^{n-1} \over n}$ and $b_k=\sum_{n=1}^{2k+1} {\left(-1\right)^{n-1} \over n}$ for all natural numbers $k$.

While a more general method to get the sum of a series is by taking limit. 

![](attachments/深入理解无穷级数和的定义（the%20sum%20of%20the%20series）_image_3.png)

As you see, we defined the sum of a infinite series, this result seems not like that naturally as 2 + 2 is computed out equal to 4，so is the definition give us the true sum of the infinite series?  $\lim _{n\rightarrow \infty }S_{n}$ has a meaning that the number of the first n terms added up increases indefinitely, this is equivalent to $$a_{1}+a_{2}+a_{3}+\cdots $$, thus defining the sum of a series as the limit of the sequence of its partial sums is intuitively plausible.

Given the definition gives the true sum of the infinite series, the statement that 0.999… = 1 can itself be interpreted and proven as:

${\displaystyle 0.999\ldots =\lim _{n\to \infty }0.\underbrace {99\ldots 9} _{n}=\lim _{n\to \infty }\sum _{k=1}^{n}{\frac {9}{10^{k}}}=\lim _{n\to \infty }\left(1-{\frac {1}{10^{n}}}\right)=1-\lim _{n\to \infty }{\frac {1}{10^{n}}}=1\,-\,0=1.\,}$





批注：一开始convergent和divergent是对一个sequence来说的，定义如下

![](attachments/深入理解无穷级数和的定义（the%20sum%20of%20the%20series）_image_4.png)

但怎么能说级数convergent和divergent了呢？级数，根据上面的定义不就是一个数列的无穷多项依次加起来的一个和式吗？对于一个和式能说convergent和divergent吗？我看不如说一个级数has a sum or not，然后说其部分和组成的数列convergent和divergent似乎比较合适！说一个series converges to a limit L不如说这个series =L。

![](attachments/深入理解无穷级数和的定义（the%20sum%20of%20the%20series）_image_5.png)

quoted from http://www.mathcentre.ac.uk/resources/uploaded/mc-ty-convergence-2009-1.pdf





























到后面讲完有和的一般条件后再说



考虑到级数的部分和收敛那么该级数就一定有sum

Given that the series converges, proving that it is equal to 2 requires only elementary algebra. If the series is denoted S, it can be seen that

![](attachments/深入理解无穷级数和的定义（the%20sum%20of%20the%20series）_image_6.jpeg)

Therefore,

![](attachments/深入理解无穷级数和的定义（the%20sum%20of%20the%20series）_image_7.jpeg)





![](attachments/深入理解无穷级数和的定义（the%20sum%20of%20the%20series）_image_8.png)



![](attachments/深入理解无穷级数和的定义（the%20sum%20of%20the%20series）_image_9.png)



![](attachments/深入理解无穷级数和的定义（the%20sum%20of%20the%20series）_image_10.png)



我们没办法做到把级数的无穷多项加起来求个和，于是我们便采用极限的方法来逼近级数的和，逼近的过程中排除了很多似是而非的“和”，最终大浪淘沙出真金得到了真正的“和”。

→无穷大包含着逼近和排出的思想，是要好好深入了解才行的



之前我一直在思考这个问题：

1/2 + 1/4 + 1/8 + 1/16 + …=1，这个级数的和是真等于1呢还是就只是个极限逼近的另类写法？是像2+2=4那样确确实实真等还是有点什么差距取不到？

现在问题想清楚了，答案是真等于啊！为此写了篇博文《深入理解无穷级数和的定义（the sum of the series）》http://www.cnblogs.com/iMath/p/6368611.html

大家有兴趣可以看看，文中也再次说明了0.999… 是真真正正等于1的，不用再怀疑~~~ 



说部分和数列convergent和divergent没问题，要说series也这样就憋扭了，毕竟级数和部分和数列是不同的东西

把级数认为是数列的所有项按照次序全部相加的结果比用极限定义的方式更容易理解； 2“一项项加下去，有限逐步变为无限”，一项项加下去，无论进行到什么时候得到的终归是有限项相加的结果，要到达无限只能是极限后的最终状态了，我以前就思考过从有限过渡到无限的问题，结论就是：除了取极限，否则的话不可能。请多多指教！



![](attachments/深入理解无穷级数和的定义（the%20sum%20of%20the%20series）_image_11.png)

把余下的路程无限二分下去，最终会仍然可二分呢还是不可分？如果不可分，那么最终是一种什么状态呢？



是的，先看大概，再究细节，我发现用这个方法学习微积分很受用



无限个数的和的定义不依赖于无穷级数和的定义，依赖于自然数的无限个数，无穷级数和的定义只是提供了计算方法（极限逼近）

