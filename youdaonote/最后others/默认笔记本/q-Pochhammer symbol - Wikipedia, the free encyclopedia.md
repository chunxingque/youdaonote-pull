In [mathematics](http://en.wikipedia.org/wiki/Mathematics "Mathematics"), in the area of [combinatorics](http://en.wikipedia.org/wiki/Combinatorics "Combinatorics"), a **q-Pochhammer symbol**, also called a **q-shifted factorial**, is a [q-analog](http://en.wikipedia.org/wiki/Q-analog "Q-analog") of the common [Pochhammer symbol](http://en.wikipedia.org/wiki/Pochhammer_symbol "Pochhammer symbol"). It is defined as

![(a;q)_n = \prod_{k=0}^{n-1} (1-aq^k)=(1-a)(1-aq)(1-aq^2)\cdots(1-aq^{n-1})](attachments/q-Pochhammer%20symbol%20-%20Wikipedia,%20the%20free%20encyclopedia_image_0.png)with

![(a;q)_0 = 1](attachments/q-Pochhammer%20symbol%20-%20Wikipedia,%20the%20free%20encyclopedia_image_1.png)by definition. The q-Pochhammer symbol is a major building block in the construction of q-analogs; for instance, in the theory of [basic hypergeometric series](http://en.wikipedia.org/wiki/Basic_hypergeometric_series "Basic hypergeometric series"), it plays the role that the ordinary Pochhammer symbol plays in the theory of [generalized hypergeometric series](http://en.wikipedia.org/wiki/Generalized_hypergeometric_series "Generalized hypergeometric series").

Unlike the ordinary Pochhammer symbol, the q-Pochhammer symbol can be extended to an infinite product:

![(a;q)_\infty = \prod_{k=0}^{\infty} (1-aq^k).](attachments/q-Pochhammer%20symbol%20-%20Wikipedia,%20the%20free%20encyclopedia_image_2.png)This is an [analytic function](http://en.wikipedia.org/wiki/Analytic_function "Analytic function") of *q* in the interior of the [unit disk](http://en.wikipedia.org/wiki/Unit_disk "Unit disk"), and can also be considered as a [formal power series](http://en.wikipedia.org/wiki/Formal_power_series "Formal power series") in *q*. The special case

![\phi(q) = (q;q)_\infty=\prod_{k=1}^\infty (1-q^k)](attachments/q-Pochhammer%20symbol%20-%20Wikipedia,%20the%20free%20encyclopedia_image_3.png)is known as [Euler's function](http://en.wikipedia.org/wiki/Euler%27s_function "Euler's function"), and is important in [combinatorics](http://en.wikipedia.org/wiki/Combinatorics "Combinatorics"), [number theory](http://en.wikipedia.org/wiki/Number_theory "Number theory"), and the theory of [modular forms](http://en.wikipedia.org/wiki/Modular_forms "Modular forms").

A q-series is a [series](http://en.wikipedia.org/wiki/Series_(mathematics) "Series (mathematics)") in which the coefficients are functions of *q*, typically depending on *q* via q-Pochhammer symbols.



|  |
| --- |
| Contents [hide] * 1Identities
* 2Combinatorial interpretation
* 3Multiple arguments convention
* 4Relationship to other q-functions
* 5See also
* 6References
* 7External links
 |

[[edit](http://en.wikipedia.org/w/index.php?title=Q-Pochhammer_symbol&action=edit§ion=1 "Edit section: Identities")]Identities
------------------------------------------------------------------------------------------------------------------------------

The finite product can be expressed in terms of the infinite product:

![(a;q)_n = \frac{(a;q)_\infty} {(aq^n;q)_\infty}, ](attachments/q-Pochhammer%20symbol%20-%20Wikipedia,%20the%20free%20encyclopedia_image_4.png)which extends the definition to negative integers *n*. Thus, for nonnegative *n*, one has

![(a;q)_{-n} = \frac{1}{(aq^{-n};q)_n}=\prod_{k=1}^n \frac{1}{(1-a/q^k)}](attachments/q-Pochhammer%20symbol%20-%20Wikipedia,%20the%20free%20encyclopedia_image_5.png)and

![(a;q)_{-n} = \frac{(-q/a)^n q^{n(n-1)/2}} {(q/a;q)_n}.](attachments/q-Pochhammer%20symbol%20-%20Wikipedia,%20the%20free%20encyclopedia_image_6.png)The *q*-Pochhammer symbol is the subject of a number of q-series identities, particularly the infinite series expansions

![(x;q)_\infty = \sum_{n=0}^\infty \frac{(-1)^n q^{n(n-1)/2}}{(q;q)_n} x^n](attachments/q-Pochhammer%20symbol%20-%20Wikipedia,%20the%20free%20encyclopedia_image_7.png)and

![\frac{1}{(x;q)_\infty}=\sum_{n=0}^\infty \frac{x^n}{(q;q)_n}](attachments/q-Pochhammer%20symbol%20-%20Wikipedia,%20the%20free%20encyclopedia_image_8.png),which are both special cases of the [q-binomial theorem](http://en.wikipedia.org/wiki/Q-binomial_theorem "Q-binomial theorem"):

![\frac{(ax;q)_\infty}{(x;q)_\infty} = \sum_{n=0}^\infty \frac{(a;q)_n}{(q;q)_n} x^n.](attachments/q-Pochhammer%20symbol%20-%20Wikipedia,%20the%20free%20encyclopedia_image_9.png)[[edit](http://en.wikipedia.org/w/index.php?title=Q-Pochhammer_symbol&action=edit§ion=2 "Edit section: Combinatorial interpretation")]Combinatorial interpretation
------------------------------------------------------------------------------------------------------------------------------------------------------------------

The *q*-Pochhammer symbol is closely related to the enumerative combinatorics of partitions. The coefficient of ![q^m a^n](attachments/q-Pochhammer%20symbol%20-%20Wikipedia,%20the%20free%20encyclopedia_image_10.png) in

![(a;q)_\infty^{-1} = \prod_{k=0}^{\infty} (1-aq^k)^{-1}](attachments/q-Pochhammer%20symbol%20-%20Wikipedia,%20the%20free%20encyclopedia_image_11.png)is the number of partitions of *m* into at most *n* parts.

Since, by conjugation of partitions, this is the same as the number of partitions of *m* into parts of size at most *n*, by identification of generating series we obtain the identity:

![(a;q)_\infty^{-1} = \sum_{k=0}^\infty \left(\prod_{j=1}^k \frac{1}{1-q^j} \right) a^k                         = \sum_{k=0}^\infty \frac{a^k}{(q;q)_k}](attachments/q-Pochhammer%20symbol%20-%20Wikipedia,%20the%20free%20encyclopedia_image_12.png)as in the above section.

We also have that the coefficient of ![q^m a^n](attachments/q-Pochhammer%20symbol%20-%20Wikipedia,%20the%20free%20encyclopedia_image_13.png) in

![(-a;q)_\infty = \prod_{k=0}^{\infty} (1+aq^k)](attachments/q-Pochhammer%20symbol%20-%20Wikipedia,%20the%20free%20encyclopedia_image_14.png)is the number of partitions of *m* into *n* or *n*-1 distinct parts.

By removing a triangular partition with *n-1* parts from such a partition, we are left with an arbitrary partition with at most *n* parts. This gives a weight-preserving bijection between the set of partitions into *n* or *n*-1 distinct parts and the set of pairs consisting of a triangular partition having *n*-1 parts and a partition with at most *n* parts. By identifying generating series, this leads to the identity:

![(-a;q)_\infty = \prod_{k=0}^\infty (1+aq^k)                     = \sum_{k=0}^\infty \left(q^{k\choose 2} \prod_{j=1}^k \frac{1}{1-q^j}\right) a^k                     = \sum_{k=0}^\infty \frac{q^{k\choose 2}}{(q;q)_k} a^k](attachments/q-Pochhammer%20symbol%20-%20Wikipedia,%20the%20free%20encyclopedia_image_15.png)also described in the above section.

The *q*-binomial theorem itself can also be handled by a slightly more involved combinatorial argument of a similar flavour.

[[edit](http://en.wikipedia.org/w/index.php?title=Q-Pochhammer_symbol&action=edit§ion=3 "Edit section: Multiple arguments convention")]Multiple arguments convention
--------------------------------------------------------------------------------------------------------------------------------------------------------------------

Since identities involving *q*-Pochhammer symbols so frequently involve products of many symbols, the standard convention is to write a product as a single symbol of multiple arguments:

![(a_1,a_2,\ldots,a_m;q)_n = (a_1;q)_n (a_2;q)_n \ldots (a_m;q)_n.](attachments/q-Pochhammer%20symbol%20-%20Wikipedia,%20the%20free%20encyclopedia_image_16.png)[[edit](http://en.wikipedia.org/w/index.php?title=Q-Pochhammer_symbol&action=edit§ion=4 "Edit section: Relationship to other q-functions")]Relationship to other q-functions
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Noticing that

![\lim_{q\rightarrow 1}\frac{1-q^n}{1-q}=n,](attachments/q-Pochhammer%20symbol%20-%20Wikipedia,%20the%20free%20encyclopedia_image_17.png)we define the *q*-analog of *n*, also known as the ***q*-bracket** or ***q*-number** of *n* to be

![[n]_q=\frac{1-q^n}{1-q}.](attachments/q-Pochhammer%20symbol%20-%20Wikipedia,%20the%20free%20encyclopedia_image_18.png)From this one can define the *q*-analog of the [factorial](http://en.wikipedia.org/wiki/Factorial "Factorial"), the ***q*-factorial**, as



|  |  |
| --- | --- |
| \big[n]_q! | =\prod_{k=1}^n [k]_q |
| = [1]_q [2]_q \cdots [n-1]_q [n]_q |
| =\frac{1-q}{1-q} \frac{1-q^2}{1-q} \cdots \frac{1-q^{n-1}}{1-q} \frac{1-q^n}{1-q} |
| =1(1+q)\cdots (1+q+\cdots + q^{n-2})  (1+q+\cdots + q^{n-1}) |
| =\frac{(q;q)_n}{(1-q)^n}. |

Again, one recovers the usual factorial by taking the limit as *q* approaches 1. This can be interpreted as the number of [flags](http://en.wikipedia.org/wiki/Flag_(linear_algebra) "Flag (linear algebra)") in an *n*-dimensional vector space over the field with *q* elements, and taking the limit as *q* goes to 1 yields the interpretation of an ordering on a set as a flag in a vector space over the [field with one element](http://en.wikipedia.org/wiki/Field_with_one_element "Field with one element").

A product of negative integer q-brackets can be expressed in terms of the q-factorial as:

![\prod_{k=1}^n [-k]_q = \frac{(-1)^n\,[n]_q!}{q^{n(n+1)/2}}](attachments/q-Pochhammer%20symbol%20-%20Wikipedia,%20the%20free%20encyclopedia_image_19.png)From the *q*-factorials, one can move on to define the ***q*-binomial coefficients**, also known as **Gaussian coefficients**, **Gaussian polynomials**, or **[Gaussian binomial coefficients](http://en.wikipedia.org/wiki/Gaussian_binomial_coefficient "Gaussian binomial coefficient")**:

![\begin{bmatrix}n\\k\end{bmatrix}_q=\frac{[n]_q!}{[n-k]_q! [k]_q!}.](attachments/q-Pochhammer%20symbol%20-%20Wikipedia,%20the%20free%20encyclopedia_image_20.png)One can check that

![\begin{bmatrix}n+1\\k\end{bmatrix}_q=\begin{bmatrix}n\\k\end{bmatrix}_q+q^{n-k+1}\begin{bmatrix}n\\k-1\end{bmatrix}_q.](attachments/q-Pochhammer%20symbol%20-%20Wikipedia,%20the%20free%20encyclopedia_image_21.png)One also obtains a q-analog of the [Gamma function](http://en.wikipedia.org/wiki/Gamma_function "Gamma function"), called the **[q-gamma function](http://en.wikipedia.org/wiki/Q-gamma_function "Q-gamma function")**, and defined as

![\Gamma_q(x)=\frac{(1-q)^{1-x} (q;q)_\infty}{(q^x;q)_\infty}](attachments/q-Pochhammer%20symbol%20-%20Wikipedia,%20the%20free%20encyclopedia_image_22.png)This converges to the usual Gamma function as *q* approaches 1 from inside the unit disc.. Note that

![\Gamma_q(x+1)=[x]_q\Gamma_q(x)\,](attachments/q-Pochhammer%20symbol%20-%20Wikipedia,%20the%20free%20encyclopedia_image_23.png)for any *x* and

![\Gamma_q(n+1)=[n]_q!\frac{}{}.](attachments/q-Pochhammer%20symbol%20-%20Wikipedia,%20the%20free%20encyclopedia_image_24.png)for non-negative integer values of *n*. Alternatively, this may be taken as an extension of the q-factorial function to the real number system.

[[edit](http://en.wikipedia.org/w/index.php?title=Q-Pochhammer_symbol&action=edit§ion=5 "Edit section: See also")]See also
--------------------------------------------------------------------------------------------------------------------------

* [Basic hypergeometric series](http://en.wikipedia.org/wiki/Basic_hypergeometric_series "Basic hypergeometric series")
* [Pochhammer symbol](http://en.wikipedia.org/wiki/Pochhammer_symbol "Pochhammer symbol")
* [Q-derivative](http://en.wikipedia.org/wiki/Q-derivative "Q-derivative")
* [Q-theta function](http://en.wikipedia.org/wiki/Q-theta_function "Q-theta function")
* [Elliptic gamma function](http://en.wikipedia.org/wiki/Elliptic_gamma_function "Elliptic gamma function")
* [Jacobi theta function](http://en.wikipedia.org/wiki/Theta_function "Theta function")

[[edit](http://en.wikipedia.org/w/index.php?title=Q-Pochhammer_symbol&action=edit§ion=6 "Edit section: References")]References
------------------------------------------------------------------------------------------------------------------------------

* George Gasper and [Mizan Rahman](http://en.wikipedia.org/wiki/Mizan_Rahman "Mizan Rahman"), *Basic Hypergeometric Series, 2nd Edition*, (2004), Encyclopedia of Mathematics and Its Applications, **96**, Cambridge University Press, Cambridge. [ISBN 0-521-83357-4](http://en.wikipedia.org/wiki/Special:BookSources/0521833574).
* Roelof Koekoek and Rene F. Swarttouw, *[The Askey scheme of orthogonal polynomials and its q-analogues](http://fa.its.tudelft.nl/~koekoek/askey/)*, section 0.2.

[[edit](http://en.wikipedia.org/w/index.php?title=Q-Pochhammer_symbol&action=edit§ion=7 "Edit section: External links")]External links
--------------------------------------------------------------------------------------------------------------------------------------

* [Weisstein, Eric W.](http://en.wikipedia.org/wiki/Eric_W._Weisstein "Eric W. Weisstein"), "[*q*-Analog](http://mathworld.wolfram.com/q-Analog.html)" from [MathWorld](http://en.wikipedia.org/wiki/MathWorld "MathWorld").
* [Weisstein, Eric W.](http://en.wikipedia.org/wiki/Eric_W._Weisstein "Eric W. Weisstein"), "[*q*-Bracket](http://mathworld.wolfram.com/q-Bracket.html)" from [MathWorld](http://en.wikipedia.org/wiki/MathWorld "MathWorld").
* [Weisstein, Eric W.](http://en.wikipedia.org/wiki/Eric_W._Weisstein "Eric W. Weisstein"), "[*q*-Factorial](http://mathworld.wolfram.com/q-Factorial.html)" from [MathWorld](http://en.wikipedia.org/wiki/MathWorld "MathWorld").
* [Weisstein, Eric W.](http://en.wikipedia.org/wiki/Eric_W._Weisstein "Eric W. Weisstein"), "[*q*-Binomial Coefficient](http://mathworld.wolfram.com/q-BinomialCoefficient.html)" from [MathWorld](http://en.wikipedia.org/wiki/MathWorld "MathWorld").
