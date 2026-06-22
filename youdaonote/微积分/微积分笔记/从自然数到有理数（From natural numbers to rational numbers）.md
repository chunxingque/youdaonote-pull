看完本文后你至少会明白：

1. 自然数是否包括0

2. 有理数为什么可以用$\dfrac {p} {q}$这种形式唯一表示

3. 如何从自然数很自然地过渡到有理数

4. 如何证明$\sqrt {2}$不是有理数 



简单地来讲，自然数就是0,1,2,3, ...这些用来“数个数”的数，我们可以很直观地接受它们的存在。0是否包含在自然数里只是一个约定上的分歧[^1]，本文约定自然数包括0，后面我们会看到这种规定的优势。在自然数里进行“加”或“乘”运算产生的仍然是自然数，进行减法运算会出现“不够减”的情况，比如： $$1-2=?$$ 在自然数里这个式子没结果，为了解除这种限制，我们引入了负数， $$-1, -2, -3, ...$$ 自然数和负数统称为整数。正整数是1, 2, 3, 4, ...这些，它与自然数的区别在于是否包含0，这种区别正好可以让这两个概念各尽其用，要是规定自然数不包括0，那么这两个数的概念将会等同起来，最终就会不得不产生“自然数和0”、“正整数和0”、“非负整数”这些相对较为啰唆的表述，这就是规定自然数包括0的优势啦（此规定下“非负整数”就可以用“自然数”取而代之）。另外，把0包含在自然数集内对于集合论也是有着重要意义[^5]。



在整数里进行除法有时候也会产生无解的情况，比如$4\div 3$的结果就不是整数，为此我们引入有理数这个概念。有理数就是可以写成$\dfrac {p} {q}$这种形式的数，这里${p}$和${q}$都是整数并且${q≠0}$。整数也可以写成$\dfrac {p} {q}$这种形式，比如$2=\dfrac {2} {1}=\dfrac {-4} {-2}$，所以整数也是有理数。但是每个有理数的$\dfrac {p} {q}$表示形式并不是唯一的，比如$\dfrac {2} {4}$、$\dfrac {1} {2}$、$\dfrac {-2} {-4}$这三个都表示同一个数，为了让有理数的$\dfrac {p} {q}$表示形式唯一，我们可以规定${p}$是正整数，并且${p}$和${q}$没有比1大的公因子[^2]，那么不能用$\dfrac {p} {q}$这种形式唯一表示的就不是有理数了，我们可以据此来证明$\sqrt {2}$不是有理数（后续我会讲到如何从有理数过渡到无理数，此处先提到$\sqrt {2}$这个无理数并无大碍，毕竟各位之前都有所了解）。

我们首先假设$\sqrt {2}$是有理数，那么$\sqrt {2}$就可以用$\dfrac {p} {q}$这种形式唯一表示，即$$\sqrt {2}=\dfrac {p} {q}$$，按规定${p}$和${q}$没有比1大的公因子，接下来我们将导出与这个观点相悖的结论出来。对这个等式两边平方并稍作变换得到$$p^{2}=2q^{2}$$，那么$p^{2}$就是偶数了，显然$p$也必须是偶数，便有$p=2p_{0}$，$p_{0}$是整数，把前面等式的$p$换作$2p_{0}$后有$4p_{0}^{2}=2q^{2}$，即$2p_{0}^{2}=q^{2}$，这说明$q^{2}$是偶数，显然$q$也必须是偶数，这就证明了${p}$和${q}$有公因子2，这与前面的“${p}$和${q}$没有比1大的公因子”这个规定矛盾，而造成这种矛盾的起因就是我们一开始假设$\sqrt {2}$是有理数，这就证明了$\sqrt {2}$不是有理数[^3]。

References :



[^1]: Terence Tao, Analysis I, third edition, P15



[^2]: Richard Courant, Fritz John, Introduction to Calculus and Analysis Volume I, Reprint of the 1989 edition, P2



[^3]: Richard Courant, Fritz John, Introduction to Calculus and Analysis Volume I, Reprint of the 1989 edition, P5



[^5]: D.C. Goldrei, Classic Set Theory: For Guided Independent Study, P32





English Version: 

From natural numbers to rational numbers

The natural numbers 0,1,2,3, ... are for indicating "how many" objects there are in a collection or set of discrete elements, they are considered as given to us, together with the two fundamental operations, addition and multiplication, by which they may be combined. Whether 0 is included or not in the natural numbers is just a matter of notational convention more than anything else [^1]. Logicians include 0 in the set, mainly because of the importance of 0 in defining arithmetic within set theory[^5].

The inverse operations, subtraction and division, are not always possible within the set of natural numbers; we cannot subtract 2 from 1 or divide 1 by 2 and stay within that set. To make these operations possible without restriction we are forced to extend the concept of number by inventing the "negative" integers, and the fractions. The totality of all these numbers is called the class or set of rational numbers; they are all obtained from unity by using the "rational operations" of calculation, namely, addition, subtraction, multiplication, and division.

A rational number can always be written in the form p/q, where p and q are integers and q≠0. We can make this representation unique by requiring that q is positive and that p and q have no common factor larger than 1 [^2]. The unique representation requirement could be used to prove $\sqrt {2}$ is not a rational number.

![](attachments/从自然数到有理数（From%20natural%20numbers%20to%20rational%20numbers）_image_0.png)

![](attachments/从自然数到有理数（From%20natural%20numbers%20to%20rational%20numbers）_image_1.png)

[^3]

Last but not least，I advocate including 0 as the first natural number in order to make a difference between positive integers and natural numbers, so that we can avoid somewhat redundant expressions like "non-negative integers", "positive integers and 0", "natural numbers and 0".

 

References :

[^1]: Terence Tao, Analysis I, third edition, P15



[^2]: Richard Courant, Fritz John, Introduction to Calculus and Analysis Volume I, Reprint of the 1989 edition, P2



[^3]: Richard Courant, Fritz John, Introduction to Calculus and Analysis Volume I, Reprint of the 1989 edition, P5



[^5]: D.C. Goldrei, Classic Set Theory: For Guided Independent Study, P32







---

The mathematical theory of the natural numbers or positive integers is known as arithmetic.

![](attachments/从自然数到有理数（From%20natural%20numbers%20to%20rational%20numbers）_image_2.png)



![](attachments/从自然数到有理数（From%20natural%20numbers%20to%20rational%20numbers）_image_3.png)



![](attachments/从自然数到有理数（From%20natural%20numbers%20to%20rational%20numbers）_image_4.png)



![](attachments/从自然数到有理数（From%20natural%20numbers%20to%20rational%20numbers）_image_5.png)









The natural numbers are the adequate instrument for counting elements of a collection or "set." However, they do not suffice for another equally important objective: to measure quantities such as the length of a curve and the volume or weight of a body. The question "how much ?", cannot be answered immediately in terms of the natural numbers. The profound need for expressing measures of quantities in terms of what we would like to call numbers forces us to extend the

number concept so that we may describe a continuous gradation of measures. This extension is called the number continuum.

We must greatly extend the original concept of number as natural number in order to create an instrument powerful enough for the needs of practice and theory. 

In daily life we need not only to count indiindividual objects, but also to measure quantities such as length, area, weight, and time. If we want to operate freely with the measures of these quantities, which are capable of arbitrarily fine subdivision, it is necessary to extend the realm of arithmetic beyond the integers.

After all, in physical reality quantities are never given or known with absolute precision but always only with a degree of uncertainty and therefore might just as well be considered as measured

by rational numbers.



The most we can say is that it lies between two successive multiples of this unit, say between 53 and 54 pounds. Aside from the "practical" reason for the introduction of rational numbers, there is a more intrinsic and in some ways an even more compelling one, which we shall now discuss quite independently of the preceding argument. It is of an entirely arithmetical character, and is typical of a dominant tendency in mathematical procedure.

theoretical need











What is Mathematics, Really? - 第 271 页



We subtract in the natural system that is not closed under subtraction to generate the integers. The same trick was repeated with division in the integer system to obtain the rationals. Now, we possessed a system that is closed under all 4 natural operations (except for division by zero, of course) so what else can we attempt? Perhaps we are desperate enough to try defining division by zero to get a really ‘closed-division’ system, but that approach would most probably gives us only two more extra ‘infinitely large’ elements (positive and negative) and that does not really answer our dilemma with the triangle. So what else can we do?



Natural numbers were simply postulated to exist, and to obey five

axioms; the integers then came via (formal) differences of the natural

numbers; the rationals then came from (formal) quotients of the integers,

and the reals then came from (formal) limits of the rationals.



 The symbols N, Q, and R stand for “natural”, “quotient”, and “real” respec-

tively. Z stands for “Zahlen”, the German word for number. There is also the complex

numbers C, which obviously stands for “complex”.































Number is the basis of modern mathematics. 

While the Greeks chose the geometrical con-

concepts of point and line as the basis of their mathematics, it has

become the modern guiding principle that all mathematical statements

should be reducible ultimately to statements about the natural numbers,

1, 2, 3, • • • . "God created the natural numbers; everything else is

man's handiwork." In these words Leopold Kronecker A823-1891)

pointed out the safe ground on which the structure of mathematics can

be built.









自然数也要定义？无规矩不成方圆，有定义（约定好规则，讲清楚规则）才好开展工作







