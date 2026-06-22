

Dedekind cuts are named after the German mathematician Richard Dedekind (1831-1916).



Dedekind Cuts: Real Numbers as Partitions

of the Ordered Field of Rational Numbers

Dedekind cuts of rational numbers.

construct the number continuum from the rationals using Dedekind 



construction of real numbers using Dedekind 

What is the continuum? On the face of it, there are several distinct forms of the continuum as a mathematical concept: in geometry, as a straight line, in analysis as the real number system (characterized in one of several ways), and in set theory as the power set of the natural numbers and, alternatively, as the set of all infinite sequences of zeros and ones.

http://www.themathpage.com/acalc/continuous.htm#def-cont





![](attachments/(冲突)连续统和%20Dedekind%20cut_image_0.png)



![](attachments/(冲突)连续统和%20Dedekind%20cut_image_1.png)



![](attachments/(冲突)连续统和%20Dedekind%20cut_image_2.png)



![](attachments/(冲突)连续统和%20Dedekind%20cut_image_3.png)



![](attachments/(冲突)连续统和%20Dedekind%20cut_image_4.png)



![](attachments/(冲突)连续统和%20Dedekind%20cut_image_5.png)









This postulate makes the domain

of real numbers continuous, in the sense that the straight line has this

property. 



I don't have time to write a full answer right now, but this may help. When you construct the real numbers you need to construct them out of things you have at hand. If you are constructing the reals, presumably you don't yet have real numbers to work with (why construct them if you did?), so you must use Q. Dedekind cuts are simply a way to represent real numbers in terms of rational numbers.



![](attachments/(冲突)连续统和%20Dedekind%20cut_image_6.png)



The

equation x 2 − 2 = 0 must have a root, it was argued, because, as x grows from

0 to 2, x 2 − 2 increases, and is first negative and then positive; if x changes

continuously, so does x − 2; hence x 2 − 2 must assume the value 0 in passing

from negative to positive.

好奇心驱使我们寻找连续，后面应该是so does x^2 − 2

罗素282

假设if x changes continuously，在只知道有理数的情况下要探讨x^2 − 2是否会等于0的问题就需要连续统

![](attachments/(冲突)连续统和%20Dedekind%20cut_image_7.png)

no, but yearling for the number continuum 

需要证明的是当分割点是无理数的时候要证明两个有理数cut之间只能有一个无理数不可能存在多个

yet there are many ways of dividing all rational numbers into

two classes, such that all numbers of one class come after all numbers of the

other class, and no rational number lies between the two classes, 





The Concept of Number - B. Artmann (Ellis Horwood, 1988),  P46,

CONSTRUCTION OF R

If we compare the Dedekind process with the path we took through decimal

sequences, or with the Cantor process (to be dealt with below) and work

through each process in all details, there is no doubt that the Dedekind

process is by far the simplest. That is to say, if one puts value on every

detail of the proof and its understanding, then with Dedekind we have the

least trouble. 



"a real number is a Dedekind cut"

then, we have to do with a cut produced by no rational number, we create a new irrational number, 

应该说是reveal



概念介绍

A set partition of the rational numbers into two nonempty subsets 

![S_1](attachments/(冲突)连续统和%20Dedekind%20cut_image_8.gif)

 and 

![S_2](attachments/(冲突)连续统和%20Dedekind%20cut_image_9.gif)

 such that all members of 

![S_1](attachments/(冲突)连续统和%20Dedekind%20cut_image_10.gif)

 are less than those of 

![S_2](attachments/(冲突)连续统和%20Dedekind%20cut_image_11.gif)

 and such that 

![S_1](attachments/(冲突)连续统和%20Dedekind%20cut_image_12.gif)

 has no greatest member.

a Dedekind cut, named after Richard Dedekind, is a partition of the rational numbers into two non-empty sets A and B, such that all elements of A are less than all elements of B, and A contains no greatest element. Dedekind cuts are one method of construction of the real numbers.

The set B may or may not have a smallest element among the rationals. If B has a smallest element among the rationals, the cut corresponds to that rational. Otherwise, that cut defines a unique irrational number which, loosely speaking, fills the "gap" between A and B. In other words, A contains every rational number less than the cut, and B contains every rational number greater than or equal to the cut. An irrational cut is equated to an irrational number which is in neither set. Every real number, rational or not, is equated to one and only one cut of rationals.





It is more symmetrical to use the (A,B) notation for Dedekind cuts, but each of A and B does determine the other. It can be a simplification, in terms of notation if nothing more, to concentrate on one "half" — say, the lower one — and call any downward closed set A without greatest element a "Dedekind cut".

Every rational number determines two cuts; one where x is the largest element in L, and one where it is the smallest element in R. To avoid double representations, an arbitrary choice must be made: requiring L does not have a largest element (or, essentially equivalently, that R does have have a smallest element). The set of real numbers is then the set of all Dedekind cuts.

Dedekind constructed the number continuum by filling those gaps







Ordering of cuts

Regard one Dedekind cut (A, B) as less than another Dedekind cut (C, D) (of the same superset) if A is a proper subset of C. Equivalently, if D is a proper subset of B, the cut (A, B) is again less than (C, D). In this way, set inclusion can be used to represent the ordering of numbers, and all other relations (greater than, less than or equal to, equal to, and so on) can be similarly created from set relations.

还有数量关系 加减乘除运算

![](attachments/(冲突)连续统和%20Dedekind%20cut_image_13.png)

Dedekind的加减乘除运算

https://www.math.brown.edu/~res/INF/handout3.pdf

![](attachments/(冲突)连续统和%20Dedekind%20cut_image_14.png)



https://books.google.com.hk/books?id=AORWT3SsKOoC&pg=PA68&dq=dedekind+cut&hl=zh-CN&sa=X&redir_esc=y&sourceid=cndr#v=onepage&q=dedekind%20cut&f=true



I like the modern view that a real number is a Dedekind cut rather that "a Dedekind cut is produced by a real number". The second form in quotes seems to imply that real numbers exist already and they produce the cut. The former statement on the hand means that the cut itself is called a real number. 



When the real numbers are defined this way, they satisfy the intermediate value theorem. If f(x) is a continuous function that has 

![{\displaystyle f(a)<Q}](attachments/(冲突)连续统和%20Dedekind%20cut_image_15.png)

 and 

![{\displaystyle f(b)>Q}](attachments/(冲突)连续统和%20Dedekind%20cut_image_16.png)

, there is a number x between a and b with 

![{\displaystyle f(x)=Q}](attachments/(冲突)连续统和%20Dedekind%20cut_image_17.png)

. Simply make the cut of those numbers with function value less than Q. That cut is the required number.





 constructing the real numbers from

the rational numbers





 the set of rational numbers is riddled

with “holes” where there ought to be numbers. Here we will try to make this

statement more precise and then indicate how these holes can be “filled” result-

ing in the number continuum.

 In fact,

there are a lot more cuts than there are rational cut numbers. However, we can

fix this by enlarging the number system so that there is a cut number for every

Dedekind cut. The way this is usually done is to define the new number system

to actually be the set of all Dedekind cuts of the rationals.

![](attachments/(冲突)连续统和%20Dedekind%20cut_image_18.png)

We will think of a Dedekind cut L as specifying a certain location (the

location between L and its complement R) along the rational number line. We

will think of the real number system R as being the set of all such locations.

Then each real number x corresponds to a Dedekind cut L x , which is to be

thought of as the set of all rational numbers to the left of the location x. 



The basic notions of Calculus are derivative and integral: the

derivative is a measure for the rate of change, the integral a measure

for the total effect of a process of continuous change. A precise under-

standing of these concepts and their overwhelming fruitfulness rests

upon the concepts of limit and of function which in turn depend upon

an understanding of the continuum of numbers.



构造出连续体之后可以趁机说明连续体（实数系）不包含无穷小量

Unlike the Greek’s “numbers,” which moved discretely from one value to the next, the magnitudes (time, for example) varied continuously.



Dedekind uses intuitive ideas from geometry to provide motivation for his development and thus there are similarities to Euxodus’ treatment of the real numbers. However, Dedekind avoided the cumbersome nature of the Greek’s definitions. Furthermore, Bottazzini [1, p. 269] states that unlike the Greek treatment of incommensurable magnitudes, Dedekind’s theory clearly indicates a notion of the continuum, whose “essence is precisely given by the axiom of continuity.”

 while Dedekind’s cuts have a geometric feel, his theory is soundly established in an arithmetic manner. 



provide a sound proof of the intermediate value theorem



