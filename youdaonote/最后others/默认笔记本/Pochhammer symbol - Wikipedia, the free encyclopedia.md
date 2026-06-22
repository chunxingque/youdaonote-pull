In [mathematics](http://en.wikipedia.org/wiki/Mathematics "Mathematics"), the **Pochhammer symbol** introduced by [Leo August Pochhammer](http://en.wikipedia.org/wiki/Leo_August_Pochhammer "Leo August Pochhammer") is the notation **(*x*)*n***, where *n* is a [non-negative integer](http://en.wikipedia.org/wiki/Non-negative_integer "Non-negative integer"). Depending on the context the Pochhammer symbol may represent either the rising factorial or the falling factorial as defined below. Care needs to be taken to check which interpretation is being used in any particular article. Pochhammer himself actually used (*x*)*n* with yet another meaning, namely to denote the [binomial coefficient](http://en.wikipedia.org/wiki/Binomial_coefficient "Binomial coefficient")![\tbinom xn](attachments/Pochhammer%20symbol%20-%20Wikipedia,%20the%20free%20encyclopedia_image_0.png).[1]

In this article the Pochhammer symbol (*x*)*n* is used to represent the **falling factorial** (sometimes called the *"descending factorial"*,[2]*"falling sequential product"*, *"lower factorial"*):

![(x)_{n}=x(x-1)(x-2)\cdots(x-n+1)](attachments/Pochhammer%20symbol%20-%20Wikipedia,%20the%20free%20encyclopedia_image_1.png)In this article the symbol *x*(*n*) is used for the **rising factorial** (sometimes called the *"Pochhammer function"*, *"Pochhammer polynomial"*, *"ascending factorial"*,[2]*"rising sequential product"* or *"upper factorial"*):

![x^{(n)}=x(x+1)(x+2)\cdots(x+n-1). ](attachments/Pochhammer%20symbol%20-%20Wikipedia,%20the%20free%20encyclopedia_image_2.png)These conventions are used in [combinatorics](http://en.wikipedia.org/wiki/Combinatorics "Combinatorics") (Olver 1999, p. 101). However in the theory of [special functions](http://en.wikipedia.org/wiki/Special_functions "Special functions") (in particular the [hypergeometric function](http://en.wikipedia.org/wiki/Hypergeometric_function "Hypergeometric function")) the Pochhammer symbol (*x*)*n* is used to represent the rising factorial.

When *x* is a non-negative integer, then (*x*)*n* gives the number of [*n*-permutations](http://en.wikipedia.org/wiki/Twelvefold_way#case_i "Twelvefold way") of an *x*-element set, or equivalently the number of [injective](http://en.wikipedia.org/wiki/Injective_function "Injective function") functions from a set of size *n* to a set of size *x*. However, for these meanings other notations like *x**P**n* and *P*(*x,n*) are commonly used. The Pochhammer symbol serves mostly for more algebraic uses, for instance when *x* is an [indeterminate](http://en.wikipedia.org/wiki/Indeterminate_(variable) "Indeterminate (variable)"), in which case (*x*)*n* designates a particular [polynomial](http://en.wikipedia.org/wiki/Polynomial "Polynomial") of degree *n* in *x*.



|  |
| --- |
| Contents [hide] * 1Properties
* 2Relation to umbral calculus
* 3Connection coefficients
* 4Alternate notations
* 5Generalizations
* 6See also
* 7Notes
* 8References
 |

[[edit](http://en.wikipedia.org/w/index.php?title=Pochhammer_symbol&action=edit§ion=1 "Edit section: Properties")]Properties
----------------------------------------------------------------------------------------------------------------------------

The rising and falling factorials can be used to express a [binomial coefficient](http://en.wikipedia.org/wiki/Binomial_coefficient "Binomial coefficient"):

![\frac{x^{(n)}}{n!} = {x+n-1 \choose n} \quad\mbox{and}\quad \frac{(x)_n}{n!} = {x \choose n}.](attachments/Pochhammer%20symbol%20-%20Wikipedia,%20the%20free%20encyclopedia_image_3.png)Thus many identities on binomial coefficients carry over to the falling and rising factorials.

A rising factorial can be expressed as a falling factorial that starts from the other end:

![x^{(n)} = {(x + n - 1)}_n .](attachments/Pochhammer%20symbol%20-%20Wikipedia,%20the%20free%20encyclopedia_image_4.png)This is a special case of the fact that the rising and falling factorials are related as follows:

![{(-x)}^{(n)} = {(-1)}^n {(x)}_{{n}} .](attachments/Pochhammer%20symbol%20-%20Wikipedia,%20the%20free%20encyclopedia_image_5.png)The rising and falling factorials are well defined in any [ring](http://en.wikipedia.org/wiki/Ring_(mathematics) "Ring (mathematics)"), and therefore *x* can be taken to be, for example, a complex number, including negative integers, or a polynomial with complex coefficients, or any complex-valued function.

The rising factorial can be extended to [real](http://en.wikipedia.org/wiki/Real_number "Real number") values of *n* using the [Gamma function](http://en.wikipedia.org/wiki/Gamma_function "Gamma function") provided *x* and *x* + *n* are complex numbers that are not negative integers:

![x^{(n)}=\frac{\Gamma(x+n)}{\Gamma(x)},](attachments/Pochhammer%20symbol%20-%20Wikipedia,%20the%20free%20encyclopedia_image_6.png)and so can the falling factorial:

![(x)_n=\frac{\Gamma(x+1)}{\Gamma(x-n+1)}.](attachments/Pochhammer%20symbol%20-%20Wikipedia,%20the%20free%20encyclopedia_image_7.png)If *D* denotes [differentiation](http://en.wikipedia.org/wiki/Derivative "Derivative") with respect to *x*, one has

![D^n(x^a) = (a)_n\,\, x^{a-n}.](attachments/Pochhammer%20symbol%20-%20Wikipedia,%20the%20free%20encyclopedia_image_8.png)[[edit](http://en.wikipedia.org/w/index.php?title=Pochhammer_symbol&action=edit§ion=2 "Edit section: Relation to umbral calculus")]Relation to umbral calculus
--------------------------------------------------------------------------------------------------------------------------------------------------------------

The falling factorial occurs in a formula which represents [polynomials](http://en.wikipedia.org/wiki/Polynomial "Polynomial") using the forward [difference operator](http://en.wikipedia.org/wiki/Difference_operator "Difference operator")Δ and which is formally similar to [Taylor's theorem](http://en.wikipedia.org/wiki/Taylor%27s_theorem "Taylor's theorem") of [calculus](http://en.wikipedia.org/wiki/Calculus "Calculus"). In this formula and in many other places, the falling factorial (*x*)*k* in the calculus of [finite differences](http://en.wikipedia.org/wiki/Finite_difference "Finite difference") plays the role of *x**k* in differential calculus. Note for instance the similarity of

![\Delta (x)_{k} = k\ (x)_{k-1},](attachments/Pochhammer%20symbol%20-%20Wikipedia,%20the%20free%20encyclopedia_image_9.png)to

![D x^k = k\ x^{k-1},](attachments/Pochhammer%20symbol%20-%20Wikipedia,%20the%20free%20encyclopedia_image_10.png)A similar result holds for the rising factorial.

The study of analogies of this type is known as [umbral calculus](http://en.wikipedia.org/wiki/Umbral_calculus "Umbral calculus"). A general theory covering such relations, including the falling and rising factorial functions, is given by the theory of [polynomial sequences of binomial type](http://en.wikipedia.org/wiki/Binomial_type "Binomial type") and [Sheffer sequences](http://en.wikipedia.org/wiki/Sheffer_sequence "Sheffer sequence"). Rising and falling factorials are [Sheffer sequences](http://en.wikipedia.org/wiki/Sheffer_sequence "Sheffer sequence") of [binomial type](http://en.wikipedia.org/wiki/Binomial_type "Binomial type"):

![(a + b)^{(n)} = \sum_{{j=0}}^n {n \choose j} (a)^{(n-j)}(b)^{(j)}](attachments/Pochhammer%20symbol%20-%20Wikipedia,%20the%20free%20encyclopedia_image_11.png)![(a + b)_n = \sum_{{j=0}}^n {n \choose j} (a)_{n-j}(b)_{j}](attachments/Pochhammer%20symbol%20-%20Wikipedia,%20the%20free%20encyclopedia_image_12.png)where the coefficients are the same as the ones in the expansion of a power of a binomial ([Chu-Vandermonde identity](http://en.wikipedia.org/wiki/Chu-Vandermonde_identity#Chu-Vandermondeidentity "Chu-Vandermonde identity")).

[[edit](http://en.wikipedia.org/w/index.php?title=Pochhammer_symbol&action=edit§ion=3 "Edit section: Connection coefficients")]Connection coefficients
------------------------------------------------------------------------------------------------------------------------------------------------------

Since the falling factorials are a basis for the [polynomial ring](http://en.wikipedia.org/wiki/Polynomial_ring "Polynomial ring"), we can re-express the product of two of them as a linear combination of falling factorials:

![(x)_{m} (x)_{n} = \sum_{k=0}^{m} {m \choose k} {n \choose k} k!\, (x)_{m+n-k}.](attachments/Pochhammer%20symbol%20-%20Wikipedia,%20the%20free%20encyclopedia_image_13.png)The coefficients of the (*x*)*m+n-k*, called **connection coefficients**, have a combinatorial interpretation as the number of ways to identify (or glue together) *k* elements each from a set of size *m* and a set of size *n*.

[[edit](http://en.wikipedia.org/w/index.php?title=Pochhammer_symbol&action=edit§ion=4 "Edit section: Alternate notations")]Alternate notations
----------------------------------------------------------------------------------------------------------------------------------------------

A new notation was introduced by [Ronald L. Graham](http://en.wikipedia.org/wiki/Ronald_L._Graham "Ronald L. Graham"), [Donald E. Knuth](http://en.wikipedia.org/wiki/Donald_E._Knuth "Donald E. Knuth") and [Oren Patashnik](http://en.wikipedia.org/wiki/Oren_Patashnik "Oren Patashnik") in their book *[Concrete Mathematics](http://en.wikipedia.org/wiki/Concrete_Mathematics "Concrete Mathematics")*. They define,[3] for the rising factorial:

![x^{\overline{m}}=\overbrace{x(x+1)\ldots(x+m-1)}^{m~\mathrm{factors}}\qquad\mbox{for integer }m\ge0,](attachments/Pochhammer%20symbol%20-%20Wikipedia,%20the%20free%20encyclopedia_image_14.png)and for the falling factorial:

![x^{\underline{m}}=\overbrace{x(x-1)\ldots(x-m+1)}^{m~\mathrm{factors}}\qquad\mbox{for integer }m\ge0;](attachments/Pochhammer%20symbol%20-%20Wikipedia,%20the%20free%20encyclopedia_image_15.png)they also propose to pronounce these expressions as "*x* to the *m* rising" and "*x* to the *m* falling", respectively.

Other notations for the falling factorial include *P*(*x*, *n*), *x*P*n*, P*x*,*n*, or *x*P*n*. (See [permutation](http://en.wikipedia.org/wiki/Permutation "Permutation") and [combination](http://en.wikipedia.org/wiki/Combination "Combination").)

An alternate notation for the rising factorial *x*(*n*) is the less common (*x*)+*n*. When the notation (*x*)+*n* is used for the rising factorial, the notation (*x*)–*n* is typically used for the ordinary falling factorial to avoid confusion. [1]

[[edit](http://en.wikipedia.org/w/index.php?title=Pochhammer_symbol&action=edit§ion=5 "Edit section: Generalizations")]Generalizations
--------------------------------------------------------------------------------------------------------------------------------------

The Pochhammer symbol has a generalized version called the [generalized Pochhammer symbol](http://en.wikipedia.org/wiki/Generalized_Pochhammer_symbol "Generalized Pochhammer symbol"), used in multivariate analysis. There is also a [*q*-analogue](http://en.wikipedia.org/wiki/Q-analog "Q-analog"), the [*q*-Pochhammer symbol](http://en.wikipedia.org/wiki/Q-Pochhammer_symbol "Q-Pochhammer symbol").

A generalization of the falling factorial in which a function is evaluated on a descending arithmetic sequence of integers and the values are multiplied is:

![[f(x)]^{k/-h}=f(x)\cdot f(x-h)\cdot f(x-2h)\cdots f(x-(k-1)h),](attachments/Pochhammer%20symbol%20-%20Wikipedia,%20the%20free%20encyclopedia_image_16.png)where −*h* is the decrement and *k* is the number of factors. The corresponding generalization of the rising factorial is

![[f(x)]^{k/h}=f(x)\cdot f(x+h)\cdot f(x+2h)\cdots f(x+(k-1)h).](attachments/Pochhammer%20symbol%20-%20Wikipedia,%20the%20free%20encyclopedia_image_17.png)This notation unifies the rising and falling factorials, which are [*x*]*k*/1 and [*x*]*k*/−1, respectively.

[[edit](http://en.wikipedia.org/w/index.php?title=Pochhammer_symbol&action=edit§ion=6 "Edit section: See also")]See also
------------------------------------------------------------------------------------------------------------------------

* [Pochhammer k-symbol](http://en.wikipedia.org/wiki/Pochhammer_k-symbol "Pochhammer k-symbol")
* [Chu-Vandermonde identity](http://en.wikipedia.org/wiki/Chu-Vandermonde_identity "Chu-Vandermonde identity")

[[edit](http://en.wikipedia.org/w/index.php?title=Pochhammer_symbol&action=edit§ion=7 "Edit section: Notes")]Notes
------------------------------------------------------------------------------------------------------------------

1. ^ ***a******b***[Knuth, Donald E.](http://en.wikipedia.org/wiki/Donald_Knuth "Donald Knuth") (1992), "Two notes on notation", *American Mathematical Monthly***99** (5): 403–422, [arXiv](http://en.wikipedia.org/wiki/ArXiv "ArXiv"):[math/9205211](http://arxiv.org/abs/math/9205211), [doi](http://en.wikipedia.org/wiki/Digital_object_identifier "Digital object identifier"):[10.2307/2325085](http://dx.doi.org/10.2307%2F2325085), [JSTOR](http://en.wikipedia.org/wiki/JSTOR "JSTOR") [2325085](http://www.jstor.org/stable/2325085). The remark about the Pochhammer symbol is on page 414.
2. ^ ***a******b***[Steffensen, J. F.](http://en.wikipedia.org/wiki/Johan_Frederik_Steffensen "Johan Frederik Steffensen"), *Interpolation* (2nd ed.), Dover Publications, p. 8, [ISBN](http://en.wikipedia.org/wiki/International_Standard_Book_Number "International Standard Book Number") [0-486-45009-0](http://en.wikipedia.org/wiki/Special:BookSources/0-486-45009-0 "Special:BookSources/0-486-45009-0") (A reprint of the 1950 edition by Chelsea Publishing Co.)
3. **^**Ronald L. Graham, Donald E. Knuth, Oren Patashnik (1988) *Concrete Mathematics*, Addison-Wesley, Reading MA. [ISBN 0-201-14236-8](http://en.wikipedia.org/wiki/Special:BookSources/0201142368), pp. 47,48
[[edit](http://en.wikipedia.org/w/index.php?title=Pochhammer_symbol&action=edit§ion=8 "Edit section: References")]References
----------------------------------------------------------------------------------------------------------------------------

* Olver, Peter J. (1999), *Classical Invariant Theory*, Cambridge University Press, [ISBN](http://en.wikipedia.org/wiki/International_Standard_Book_Number "International Standard Book Number") [0-521-55821-2](http://en.wikipedia.org/wiki/Special:BookSources/0-521-55821-2 "Special:BookSources/0-521-55821-2").
