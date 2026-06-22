The axiom of continuity of a line

![](attachments/Dedekind%20cut争论_image_0.png)



N.B. There is one and only one point which produces the division, "one and only one" requires establishing both existence and uniqueness. here is a good explanation on the meaning of “one and only one” (see the answer and the comments).

Dedekind's aim was to form the number continuum by making an analogy with the axiom of continuity of a line. He stated(in Chapter V) that if the domain R possesses also continuity, then the following theorem is true:

![](attachments/Dedekind%20cut争论_image_1.png)



![](attachments/Dedekind%20cut争论_image_2.png)

He then showed that there exist infinitely many cuts not produced by rational numbers using the following Dedekind cut

![](attachments/Dedekind%20cut争论_image_3.png)

He continued that 

But this cut is produced by no rational number. To demonstrate this it must be shown first of all that there exists no rational number whose square = D.

So why he show there exists no rational number whose square = D first of all ? As far As I know, he just simplified the cut from  

Dedekind cut of the rational numbers is given by

![A=\{a\in {\mathbb  {Q}}:a^{2}<2{\text{ or }}a<0\},](attachments/Dedekind%20cut争论_image_4.png)

![B=\{b\in {\mathbb  {Q}}:b^{2}>2{\text{ and }}b>0\}.](attachments/Dedekind%20cut争论_image_5.png)

Th

[Dedekind's aim.docx](attachments/Dedekind's aim.docx)



证明没有有理数的平方是2的用意何在？并不足以证明这个cut有间隙

什么样的缺失数系可以作为Dedekind cut构建的基础？一个条件就是间隙为零，因为Dedekind cut要以间隙定义一个数，如果间隙不为0，那么就会得出矛盾——比如否定只有一个点产生Dedekind cut的连续公理，否定区间套定理，





Foundations and Fundamental Concepts of Mathematics, Howard Eves, 3rd ed

Dedekind was led to his procedure for introducing the real

numbers when he found it difficult in his lectures to give a clear deﬁnition of

continuity, a property that is possessed by the ordered set of real numbers

but that is not possessed by the ordered set of rational numbers. After con-

siderable cogitation on the diﬂiculty, Dedekind perceived that the essence

of the continuity of a straight line lies in the property that if all the points

of the line are divided into two classes, such that every point in the ﬁrst

class lies to the left of every point in the second class, then there exists

one and only one point of the line that produces this severance of the line into

the two classes.

如果考虑两条射线末端是否存在端点的问题便会引出更多



A Dedekind cut (A | B) in the set of rational numbers is a

partition, or separation, of these numbers into two classes



Types of Dedekind Cut There are three possible types of Dedekind cuts

(A I B) in the set of rational numbers, for we may have the situations where

(a) A has a largest element a and B has no smallest element, (b) A has no

largest element and B has a smallest element b, (c) A has no largest element

and B has no smallest element.

A seeming fourth possibility, where A has a largest element a and B has

a smallest element b, cannot occur, for between any two distinct rational

numbers a and b there is always a rational number c, and this number c could

not lie in either A or B, which contradicts the formation of the sets A and B.



An example of a Dedekind cut of type (a) is the cut (AIB) in which A

consists of all the rational numbers less than or equal to 2, while B contains

all the remaining rational numbers. Here A has a largest element—namely,

2—and B has no smallest element.

An example of a Dedekind cut of type (b) is the cut (AIB) in which A

consists of all the rational numbers less than 2, while B contains all the

remaining rational numbers. Here A has no largest element, but B has s

smallest element, namely 2.

An example of a Dedekind cut of type (c) is the cut (AIB) in which A

consists of all the non-positive rational numbers and those positive rational

numbers whose squares are less than 2, while B contains all the remaining

rational numbers. Here A has no largest element and B has no smallest

element.(need to prove)

A Dedekind cut of the rational numbers that is of type (a) or

type (b) is called a rational cut. To each rational number r there correspond

two cuts, one of type (a) and one of type (b). In order to have a one-to-one

correspondence between the rational cuts and the rational numbers, we shall

consider only rational cuts of type (b).





什么性质的数系可在Dedekind cut的加持下构建出连续体？ dense - zero gap

无有理数之平方=2是为了做什么？

怎么显现出有理数有gap -无最大最小数







I like the modern view that a real number is a Dedekind cut rather that "a Dedekind cut is produced by a real number". The second form in quotes seems to imply that real numbers exist already and they produce the cut. The former statement on the hand means that the cut itself is called a real number. Then we don't have that question of uniqueness which you are asking.



For a Dedekind cut which is not produced by a rational number, 

don't correspond to rational, 

  You want to say this represents a gap in the rationals and it is filled by exactly one real number (and according to you Dedekind did not prove this). 



the cut (A, B) is greater than all the members of A and less than all the members of B. Further any real number with this property has to be this cut (A, B) only. If the cut is unique so is the thing defined via the cut. 

Sincerely ,

Zhao





Difference cut and number no harm

Dedekind revealed a "gap" in the rational numbers by using the cut produced by no rational number and the line continuity axiom, but he didn't prove why only one number(defined by the cut)   is enough to fill the gap so that led the enlarged number system the number continuum. 

This is a crucial question I think Dedekind had to answer but he did not. 





During the past mails, my focus is not on the uniqueness of the number,  but on involving you my opinion that Dedekind  prove why only one number(defined by the cut) is enough to fill the gap. 















this is the flaw Dedekind did not h



the gap could be filled by one and only one number 



using only one number







Dedekind did not prove a cut produced by no rational number was produced by only one irrational number in his book, what he actual showed was there did exist at least one irrational number producing the cut. I think we can prove the uniqueness of the number using the density property of rationals, or prove  by contradiction that If the cut was produced by more than one irrational number, then there is a rational number between any two irrationals.

如果gap长度不为0会导致什么矛盾





this is what I mean that he did not prove the uniqueness of the number(sorry for my poor description of this opinion last time).



Dedekind revealed a "gap" in the rational numbers by using the cut produced by no rational number and the line continuity axiom,but he didn't prove why the gap could be filled by







命我们有数的连续体，与    为什么要从有理数开始构建数的连续体？





也许是trival，当考虑可以用dedekind cut加持的数系构造连续体的时候，数系必须0 gap，0 gap和dense等价吗？也就是dense必须吗 ？数系必须dense吗？

0 gap的长度定义的前提是确定了gap的存在，否则对实数分割也可以的到0gap，没意义

也许没有明确说明，但是我看到了他后面的证明