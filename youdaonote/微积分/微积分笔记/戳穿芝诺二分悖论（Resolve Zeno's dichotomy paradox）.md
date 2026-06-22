One versions of the [zeno dichotomy paradox](https://en.wikipedia.org/wiki/Zeno%27s_paradoxes#Dichotomy_paradox) says,  before Homer could reach the end of the path, he must reach half of the distance to it. Before reaching the last half, he must complete the next quarter of the distance. Reaching the next quarter, he must then cover the next eighth of the distance, then the next sixteenth, and so on. There are thus an infinite number of these segments that must first be accomplished before he could reach the end of the path.
![enter image description here](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Zeno_Dichotomy_Paradox.png/800px-Zeno_Dichotomy_Paradox.png)
This is of course not true, as evidenced by the convergence of the geometric series with ${\displaystyle r=1/2}$. The convergence of a geometric series reveals that a sum involving an infinite number of summands can indeed be finite, and so allows one to resolve Zeno's dichotomy paradox. Zeno's mistake is in the assumption that the sum of an infinite number of finite segments cannot be finite or one can never pass an infinite number of segments. 没那么简单，也要抽象成数学区间来讲
The essential point to resolve Zeno's dichotomy paradox is to understand why the sum of $\frac12+\frac14+\frac18+\frac{1}{16}+\cdots$ actually equal to 1，no less and no more. Except following the convergence of a geometric series, another way to understand the equality is using the nested intervals theorem. Choosing$$a_n=\frac12+\frac14+\frac18+\frac{1}{16}+\cdots+\frac{1}{2^{n-1}}+\frac{1}{2^n}$$ and $b_n=1$, then $$a_n<\frac12+\frac14+\frac18+\frac{1}{16}+\cdots+\frac{1}{2^{n-1}}+\frac{1}{2^n}+\cdots\leq b_n$$ holds for every nature number $n$ and $\lim _{n\rightarrow \infty }\left( b_{n}-a_{n}\right)=\lim _{n\rightarrow \infty }\frac{1}{2^n} =0$, according to the nested intervals theorem the intersection of all the $[a_n,b_n]$ contains exactly one real number, since 1 is an element of each of these intervals, $\frac12+\frac14+\frac18+\frac{1}{16}+\cdots+\frac{1}{2^{n-1}}+\frac{1}{2^n}+\cdots = 1$, this proved the sum of the series is 1.
Another thing to note is $\displaystyle\bigcup_{{n=1}}^{\infty}\left[ 0,a_n\right]=\left[ 0,1-\frac{1}{2^n}\right]=[0,1)$, one could prove it using --[[[[------------------.




----------

Quoted from :
https://en.wikipedia.org/wiki/Zeno%27s_paradoxes#Dichotomy_paradox
https://en.wikipedia.org/wiki/Geometric_series#Zeno.27s_paradoxes