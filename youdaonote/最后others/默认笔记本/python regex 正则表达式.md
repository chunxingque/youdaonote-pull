Matching Characters

Here’s a complete list of the metacharacters

. ^ $ * + ? { } [ ] \ | ( )


[ and ] re used for specifying a character class, which is a set of characters that you wish to match. Characters can be listed individually, or a range of characters can be indicated by giving two characters and separating them by a '-'. For example, [abc] will match any of the characters a, b, or c; this is the same as [a-c], which uses a range to express the same set of characters. If you wanted to match only lowercase letters, your RE would be [a-z].

Metacharacters are not active inside classes. For example, [akm$] will match any of the characters 'a', 'k', 'm', or '$'; '$' is usually a metacharacter, but inside a character class it’s stripped of its special nature.

You can match the characters not listed within the class by complementing the set. This is indicated by including a '^' as the first character of the class; '^' outside a character class will simply match the '^' character. For example, [^5] will match any character except '5'.

>>> re.compile(r'[^A-Za-z0-9_]').findall('_no class at all')

[' ', ' ', ' ']

>>> 



Perhaps the most important metacharacter is the backslash, \. As in Python string literals, the backslash can be followed by various characters to signal various special sequences. It’s also used to escape all the metacharacters so you can still match them in patterns; for example, if you need to match a [ or \, you can precede them with a backslash to remove their special meaning: \[ or \\.

Some of the special sequences beginning with '\' represent predefined sets of characters that are often



re.ASCII

Make \w, \W, \b, \B, \d, \D, \s and \S perform ASCII-only matching instead of full Unicode matching. This is only meaningful for Unicode patterns, and is ignored for byte patterns.

\w Match any alphanumeric character,  same as  [A-Za-z0-9_] ( \W is inverse of  \w ), can also match Chinese character.   

\d

Matches any decimal digit; this is equivalent to the class [0-9].

\D

Matches any non-digit character; this is equivalent to the class [^0-9].

\s

Matches any whitespace character; this is equivalent to the class [\t\n\r\f\v].

\S

Matches any non-whitespace character; this is equivalent to the class [^\t\n\r\f\v].

These sequences can be included inside a character class. For example, [\s,.] is a character class that will match any whitespace character, or ',' or '.'.

The final metacharacter in this section is .. It matches anything except a newline character, and there’s an alternate mode (re.DOTALL) where it will match even a newline.'.' is often used where you want to match “any character”.



Repeating Things

The first metacharacter for repeating things that we’ll look at is*.* doesn’t match the literal character *; instead, it specifies that the previous character can be matched zero or more times, instead of exactly once.

For example, ca*t will match ct (0 a characters), cat (1 a), caaat (3 a characters), and so forth. The RE engine has various internal limitations stemming from the size of C’s int type that will prevent it from matching over 2 billion a characters; patterns are usually not written to match that much data.

Repetitions such as * are greedy; when repeating a RE, the matching engine will try to repeat it as many times as possible. If later portions of the pattern don’t match, the matching engine will then back up and try again with few repetitions.

A step-by-step example will make this more obvious. Let’s consider the expression a[bcd]*b. This matches the letter 'a', zero or more letters from the class [bcd], and finally ends with a 'b'.

| Step | Matched | Explanation |
| - | - | - |
| 1 | a | The a in the RE matches. |
| 2 | abcbd | The engine matches [bcd]\*, going as far as it can, which is to the end of the string. |
| 3 | Failure | The engine tries to match b, but the current position is at the end of the string, so it fails. |
| 4 | abcb | Back up, so that [bcd]\* matches one less character. |
| 5 | Failure | Try b again, but the current position is at the last character, which is a 'd'. |
| 6 | abc | Back up again, so that [bcd]\* is only matching bc. |
| 6 | abcb | Try b again. This time the character at the current position is 'b', so it succeeds. |


The end of the RE has now been reached, and it has matched abcb. This demonstrates how the matching engine goes as far as it can at first, and if no match is found it will then progressively back up and retry the rest of the RE again and again. It will back up until it has tried zero matches for [bcd]*, and if that subsequently fails, the engine will conclude that the string doesn’t match the RE at all.



Another repeating metacharacter is+, which matches one or more times. Pay careful attention to the difference between * and +; * matches zero or more times, so whatever’s being repeated may not be present at all, while + requires at least one occurrence. To use a similar example, ca+t will match cat (1 a), caaat (3 a‘s), but won’t match ct.

There are two more repeating qualifiers. The question mark character, ?, matches either once or zero times; you can think of it as marking something as being optional. For example, home-?brew matches either homebrew or home-brew.

The most complicated repeated qualifier is {m,n}, where m and n are decimal integers. This qualifier means there must be at least m repetitions, and at most n. For example, a/{1,3}b will match a/b, a//b, and a///b. It won’t match ab, which has no slashes, or a////b, which has four.

You can omit either m or n; in that case, a reasonable value is assumed for the missing value. Omitting m is interpreted as a lower limit of 0, while omitting n results in an upper bound of infinity — actually, the upper bound is the 2-billion limit mentioned earlier, but that might as well be infinity.

Readers of a reductionist bent may notice that the three other qualifiers can all be expressed using this notation. {0,} is the same as *, {1,} is equivalent to +, and {0,1} is the same as ?. It’s better to use *, +, or ? when you can, simply because they’re shorter and easier to read.



re.compile() also accepts an optional flags argument, used to enable various special features and syntax variations. We’ll go over the available settings later, but for now a single example will do:

>>> p=re.compile('ab*',re.IGNORECASE)

The Backslash Plague

certain  character sequences in strings have special meanings are interpreted by Python first, then the RE engine  use the interpreted one as REs.    

 \n , for example, also means newline in the context  of a normal Python string, and Python will automatically replace the string sequence \n with a newline character before the  RE function ever sees that sequence.



\\ , which represents a single backslash to  RE s. Assume that we wish to search  some text for an occurrence of the string  "\ten" . Because we know that we have to represent a backslash as a double backslash, we might try 

regexp = re.compile("\\ten") 

This will compile without complaining, but it’s wrong. The problem is that  \\ also  means a single backslash in Python strings. Before  re.compile is invoked, Python interprets the string we typed as meaning  \ten , which is what is passed to  re.compile . In the context of regular expressions,  \t means tab, so our compiled regular expression searches for a tab character followed by the two characters en.

To fix this while using regular Python strings, we need four backslashes. Python interprets the first two backslashes as a special sequence representing a single backslash, and likewise for the second pair of backslashes, resulting in two actual backslashes in the Python string. That string is then passed in to  re.compile , which interprets the two

actual backslashes as an  RE special sequence representing a single backslash. Our code looks like this:

regexp = re.compile("\\\\ten")

That seems confusing, and it’s why Python has a way of defining strings, called raw strings.



raw string notation can be taken as an  instruction to Python saying, Don’t process special sequences in this string. 

 in

 r"""\tTo be\n\tor not to be"""

the  \t  and  \n sequences aren’t interpreted as tabs or newlines but are left as two-string character sequences beginning with a backslash.

Using raw strings with regular expressions means you don’t need to worry about Python  processes special sequences in this string, you only need to care about the regular expression special sequences. The previous  RE example then becomes

regexp = re.compile(r"\\ten")

which works as expected. The compiled  RE looks for a single backslash followed by the letters ten. You should get into the habit of using raw strings whenever defining  RE s.



| Method/Attribute | Purpose |
| - | - |
| match() | Determine if the RE matches at the beginning of the string. |
| search() | Scan through a string, looking for any location where this RE matches. |
| findall() | Find all substrings where the RE matches, and returns them as a list. |
| finditer() | Find all substrings where the RE matches, and returns them as an iterator. |


match() and search() return None if no match can be found. If they’re successful, a match object instance is returned, containing information about the match: where it starts and ends, the substring it matched, and more.



| Method/Attribute | Purpose |
| - | - |
| group() | Return the string matched by the RE |
| start() | Return the starting position of the match |
| end() | Return the ending position of the match |
| span() | Return a tuple containing the (start, end) positions of the match |


>>> m.group()'tempo'

the match() method only checks if the RE matches at the start of a string, start() will always be zero. However, the search() method of patterns scans through the string, so the match may not start at zero in that case.

In actual programs, the most common style is to store the match object in a variable, and then check if it was None. This usually looks like:

p=re.compile(...)m=p.match('string goes here')ifm:print('Match found: ',m.group())else:print('No match')

Two pattern methods return all of the matches for a pattern. findall() returns a list of matching strings:

>>> p=re.compile('\d+')>>> p.findall('12 drummers drumming, 11 pipers piping, 10 lords a-leaping')['12', '11', '10']

findall() has to create the entire list before it can be returned as the result. The finditer() method returns a sequence of match object instances as an iterator:

>>> iterator=p.finditer('12 drummers drumming, 11 ... 10 ...')>>> iterator<callable_iterator object at 0x...>>>> formatchiniterator:... print(match.span())...(0, 2)(22, 24)(29, 31)

Module-Level Functions

You don’t have to create a pattern object and call its methods; the re module also provides top-level functions called match(), search(), findall(), sub(), and so forth.

>>> print(re.match(r'From\s+','Fromage amk'))None

Should you use these module-level functions, or should you get the pattern and call its methods yourself? If you’re accessing a regex within a loop, pre-compiling it will save a few function calls. Outside of loops, there’s not much difference thanks to the internal cache.

Compilation Flags

Flags are available in the re module under two names, a long name such as IGNORECASE and a short, one-letter form such as I.

Multiple flags can be specified by bitwise OR-ing them; re.I | re.M sets both the I and M flags, for example.

Here’s a table of the available flags, followed by a more detailed explanation of each one.

| Flag | Meaning |
| - | - |
| ASCII, A | Makes several escapes like \\w, \\b, \\s and \\d match only on ASCII characters with the respective property.<br>This means the default is Unicode matching |
| DOTALL, S | Make . match any character, including newlines |
| IGNORECASE, I | Do case-insensitive matches This means the default is case-sensitive matching |
| LOCALE, L | Do a locale-aware match |
| MULTILINE, M | Multi-line matching, affecting ^ and $ |
| VERBOSE, X (for &apos;extended’) | Enable verbose REs, which can be organized more cleanly and understandably. |




More Metacharacters

|

Alternation, or the “or” operator. If A and B are regular expressions, A|B will match any string that matches either A or B. 

Crow|Servo will match either Crow or Servo, not Cro, a 'w' or an 'S', and ervo.

To match a literal '|', use \|, or enclose it inside a character class, as in [|].



^

Matches at the beginning of lines. Unless the MULTILINE flag has been set, this will only match at the beginning of the string. In MULTILINE mode, this also matches immediately after each newline within the string.

For example, if you wish to match the word From only at the beginning of a line, the RE to use is ^From.

>>> print(re.search('^From','From Here to Eternity'))<_sre.SRE_Match object; span=(0, 4), match='From'>>>> print(re.search('^From','Reciting From Memory'))None

$

Matches at the end of a line, which is defined as either the end of the string, or any location followed by a newline character.

>>> print(re.search('}$','{block}'))<_sre.SRE_Match object; span=(6, 7), match='}'>>>> print(re.search('}$','{block} '))None>>> print(re.search('}$','{block}\n'))<_sre.SRE_Match object; span=(6, 7), match='}'>

To match a literal '$', use \$ or enclose it inside a character class, as in [$].

\A

Matches only at the start of the string. When not in MULTILINE mode, \A and ^ are effectively the same. In MULTILINE mode, they’re different: \A still matches only at the beginning of the string, but ^ may match at any location inside the string that follows a newline character.

\Z

Matches only at the end of the string.



\b

Word boundary. This is a zero-width assertion that matches only at the beginning or end of a word. A word is defined as a sequence of alphanumeric characters, so the end of a word is indicated by whitespace or a non-alphanumeric character.

The following example matches class only when it’s a complete word; it won’t match when it’s contained inside another word.

>>> p=re.compile(r'\bclass\b')>>> print(p.search('no class at all'))<_sre.SRE_Match object; span=(3, 8), match='class'>>>> print(p.search('the declassified algorithm'))None>>> print(p.search('one subclass is'))None

\B

Another zero-width assertion, this is the opposite of \b, only matching when the current position is not at a word boundary.

Grouping

Groups are marked by the '(', ')' metacharacters. '(' and ')' have much the same meaning as they do in mathematical expressions; they group together the expressions contained inside them, and you can repeat the contents of a group with a repeating qualifier, such as *, +, ?, or {m,n}. For example, (ab)* will match zero or more repetitions of ab.

>>> p=re.compile('(ab)*')>>> print(p.match('ababababab').span())(0, 10)

Groups indicated with '(', ')' also capture the starting and ending index of the text that they match; this can be retrieved by passing an argument to group(), start(), end(), and span(). Groups are numbered starting with 0. Group 0 is always present; it’s the whole RE, so match object methods all have group 0 as their default argument. Later we’ll see how to express groups that don’t capture the span of text that they match.

>>> p=re.compile('(a)b')>>> m=p.match('ab')>>> m.group()'ab'>>> m.group(0)'ab'

Subgroups are numbered from left to right, from 1 upward. Groups can be nested; to determine the number, just count the opening parenthesis characters, going from left to right.

>>> p=re.compile('(a(b)c)d')>>> m=p.match('abcd')>>> m.group(0)'abcd'>>> m.group(1)'abc'>>> m.group(2)'b'

group() can be passed multiple group numbers at a time, in which case it will return a tuple containing the corresponding values for those groups.

>>> m.group(2,1,2)('b', 'abc', 'b')

The groups() method returns a tuple containing the strings for all the subgroups, from 1 up to however many there are.

>>> m.groups()('abc', 'b')

Backreferences in a pattern allow you to specify that the contents of an earlier capturing group must also be found at the current location in the string. For example, \1 will succeed if the exact contents of group 1 can be found at the current position, and fails otherwise. Remember that Python’s string literals also use a backslash followed by numbers to allow including arbitrary characters in a string, so be sure to use a raw string when incorporating backreferences in a RE.

For example, the following RE detects doubled words in a string.

>>> p=re.compile(r'(\b\w+)\s+\1')>>> p.search('Paris in the the spring').group()'the the'

Backreferences like this aren’t often useful for just searching through a string — there are few text formats which repeat data in this way — but you’ll soon find out that they’re very useful when performing string substitutions.



Non-capturing and Named Groups

Sometimes you’ll want to use a group to denote a part of a regular expression, but aren’t interested in retrieving the group’s contents. You can make this fact explicit by using a non-capturing group: (?:...), where you can replace the ... with any other regular expression.

>>> m=re.match("([abc])+","abc")>>> m.groups()('c',)>>> m=re.match("(?:[abc])+","abc")>>> m.groups()()



instead of referring to them by numbers, groups can be referenced by a name.

The syntax for a named group is one of the Python-specific extensions: (?P<name>...). name is, obviously, the name of the group. Named groups behave exactly like capturing groups, and additionally associate a name with a group. The match object methods that deal with capturing groups all accept either integers that refer to the group by number or strings that contain the desired group’s name. Named groups are still given numbers, so you can retrieve information about a group in two ways:

>>> p=re.compile(r'(?P<word>\b\w+\b)')>>> m=p.search('(((( Lots of punctuation )))')>>> m.group('word')'Lots'>>> m.group(1)'Lots'

InternalDate=re.compile(r'INTERNALDATE "'r'(?P<day>[ 123][0-9])-(?P<mon>[A-Z][a-z][a-z])-'r'(?P<year>[0-9][0-9][0-9][0-9])'r' (?P<hour>[0-9][0-9]):(?P<min>[0-9][0-9]):(?P<sec>[0-9][0-9])'r' (?P<zonen>[-+])(?P<zoneh>[0-9][0-9])(?P<zonem>[0-9][0-9])'r'"')

The syntax for backreferences in an expression such as (...)\1 refers to the number of the group. There’s naturally a variant that uses the group name instead of the number. This is another Python extension: (?P=name) indicates that the contents of the group called name should again be matched at the current point. The regular expression for finding doubled words, (\b\w+)\s+\1 can also be written as (?P<word>\b\w+)\s+(?P=word):

>>> p=re.compile(r'(?P<word>\b\w+)\s+(?P=word)')>>> p.search('Paris in the the spring').group()'the the'

Lookahead Assertions

A negative lookahead cuts through all this confusion:

.*[.](?!bat$).*$ The negative lookahead means: if the expression bat doesn’t match at this point, try the rest of the pattern; if bat$ does match, the whole pattern will fail. The trailing $ is required to ensure that something like sample.batch, where the extension only starts with bat, will be allowed.

Excluding another filename extension is now easy; simply add it as an alternative inside the assertion. The following pattern excludes filenames that end in either bat or exe:

.*[.](?!bat$|exe$).*

Modifying Strings

| Method/Attribute | Purpose |
| - | - |
| split() | Split the string into a list, splitting it wherever the RE matches |
| sub() | Find all substrings where the RE matches, and replace them with a different string |
| subn() | Does the same thing as sub(), but returns the new string and the number of replacements |




Empty matches are replaced only when they’re not adjacent to a previous match.

>>> p=re.compile('x*')>>> p.sub('-','abxd')'-a-b-d-'

>>> re.compile(r'').sub('-', 'abxd')

'-a-b-x-d-'

>>> 



Backreferences, such as \6, are replaced with the substring matched by the corresponding group in the RE. This lets you incorporate portions of the original text in the resulting replacement string.

This example matches the word section followed by a string enclosed in {, }, and changes section to subsection:

>>> p=re.compile('section{ ( [^}]* ) }',re.VERBOSE)>>> p.sub(r'subsection{\1}','section{First} section{second}')'subsection{First} subsection{second}'



There’s also a syntax for referring to named groups as defined by the (?P<name>...) syntax. \g<name> will use the substring matched by the group named name, and \g<number> uses the corresponding group number. \g<2> is therefore equivalent to \2, but isn’t ambiguous in a replacement string such as \g<2>0. (\20 would be interpreted as a reference to group 20, not a reference to group 2 followed by the literal character '0'.) The following substitutions are all equivalent, but use all three variations of the replacement string.

>>> p=re.compile('section{ (?P<name> [^}]* ) }',re.VERBOSE)>>> p.sub(r'subsection{\1}','section{First}')'subsection{First}'>>> p.sub(r'subsection{\g<1>}','section{First}')'subsection{First}'>>> p.sub(r'subsection{\g<name>}','section{First}')'subsection{First}'

>>> defhexrepl(match):... "Return the hex string for a decimal number"... value=int(match.group())... returnhex(value)...>>> p=re.compile(r'\d+')>>> p.sub(hexrepl,'Call 65490 for printing, 49152 for user code.')'Call 0xffd2 for printing, 0xc000 for user code.'

Use String Methods

If you’re matching a fixed string, or a single character class, and you’re not using any re features such as the IGNORECASE flag, then the full power of regular expressions may not be required. Strings have several methods for performing operations with fixed strings and they’re usually much faster, because the implementation is a single small C loop that’s been optimized for the purpose, instead of the large, more generalized regular expression engine.

In short, before turning to the re module, consider whether your problem can be solved with a faster and simpler string method.



match() versus search()

The match() function only checks if the RE matches at the beginning of the string while search() will scan forward through the string for a match. It’s important to keep this distinction in mind. Remember, match() will only report a successful match which will start at 0; if the match wouldn’t start at zero, match() will not report it.

>>> print(re.match('super','superstition').span())(0, 5)>>> print(re.match('super','insuperable'))None

On the other hand, search() will scan forward through the string, reporting the first match it finds.

>>> print(re.search('super','superstition').span())(0, 5)>>> print(re.search('super','insuperable').span())(2, 7)

Sometimes you’ll be tempted to keep using re.match(), and just add .* to the front of your RE. Resist this temptation and use re.search() instead. The regular expression compiler does some analysis of REs in order to speed up the process of looking for a match. One such analysis figures out what the first character of a match must be; for example, a pattern starting with Crow must match starting with a 'C'. The analysis lets the engine quickly scan through the string looking for the starting character, only trying the full match if a 'C' is found.

Adding .* defeats this optimization, requiring scanning to the end of the string and then backtracking to find a match for the rest of the RE. Use re.search() instead.





Greedy versus Non-Greedy

When repeating a regular expression, as in a*, the resulting action is to consume as much of the pattern as possible. This fact often bites you when you’re trying to match a pair of balanced delimiters, such as the angle brackets surrounding an HTML tag. The naive pattern for matching a single HTML tag doesn’t work because of the greedy nature of .*.

>>> s='<html><head><title>Title</title>'>>> len(s)32>>> print(re.match('<.*>',s).span())(0, 32)>>> print(re.match('<.*>',s).group())<html><head><title>Title</title>

The RE matches the '<' in <html>, and the .* consumes the rest of the string. There’s still more left in the RE, though, and the > can’t match at the end of the string, so the regular expression engine has to backtrack character by character until it finds a match for the >. The final match extends from the '<' in <html> to the '>' in </title>, which isn’t what you want.

In this case, the solution is to use the non-greedy qualifiers *?, +?, ??, or {m,n}?, which match as little text as possible. In the above example, the '>' is tried immediately after the first '<' matches, and when it fails, the engine advances a character at a time, retrying the '>' at every step. This produces just the right result:

>>> print(re.match('<.*?>',s).group())<html>

(Note that parsing HTML or XML with regular expressions is painful. Quick-and-dirty patterns will handle common cases, but HTML and XML have special cases that will break the obvious regular expression; by the time you’ve written a regular expression that handles all of the possible cases, the patterns will be very complicated. Use an HTML or XML parser module for such tasks.)



Using re.VERBOSE

specifying the re.VERBOSE flag when compiling the regular expression can be helpful, because it allows you to format the regular expression more clearly.

The re.VERBOSE flag has several effects. Whitespace in the regular expression that isn’t inside a character class is ignored. This means that an expression such as dog|cat is equivalent to the less readable dog|cat, but [ab] will still match the characters 'a', 'b', or a space. In addition, you can also put comments inside a RE; comments extend from a # character to the next newline. When used with triple-quoted strings, this enables REs to be formatted more neatly:

pat=re.compile(r""" \s*                 # Skip leading whitespace (?P<header>[^:]+)   # Header name \s* :               # Whitespace, and a colon (?P<value>.*?)      # The header's value -- *? used to                     # lose the following trailing whitespace \s*$                # Trailing whitespace to end-of-line""",re.VERBOSE)

This is far more readable than:

pat=re.compile(r"\s*(?P<header>[^:]+)\s*:(?P<value>.*?)\s*$")





never use match(), using search() instead 

using Non-Greedy pattern if possible for performance reason  如果目标字串的后面字串比目标字串长度大，则使用Non-Greedy pattern，反之则不然

regex必须使用raw string





>>> print(re.match('<.*?>',s).group())

In this case, the solution is to use the non-greedy qualifiers *?, +?, ??, or {m,n}?, which match as little text as possible. In the above example, the '>' is tried immediately after the first '<' matches, and when it fails, the engine advances a character at a time, retrying the '>' at every step. This produces just the right result:



Repetitions such as * are greedy; when repeating a RE, the matching engine will try to repeat it as many times as possible. If later portions of the pattern don’t match, the matching engine will then back up and try again with few repetitions.

A step-by-step example will make this more obvious. Let’s consider the expression a[bcd]*b. This matches the letter 'a', zero or more letters from the class [bcd], and finally ends with a 'b'. Now imagine matching this RE against the string abcbd.

| Step | Matched | Explanation |
| - | - | - |
| 1 | a | The a in the RE matches. |
| 2 | abcbd | The engine matches [bcd]\*, going as far as it can, which is to the end of the string. |
| 3 | Failure | The engine tries to match b, but the current position is at the end of the string, so it fails. |
| 4 | abcb | Back up, so that [bcd]\* matches one less character. |
| 5 | Failure | Try b again, but the current position is at the last character, which is a 'd'. |
| 6 | abc | Back up again, so that [bcd]\* is only matching bc. |
| 6 | abcb | Try b again. This time the character at the current position is 'b', so it succeeds. |


The end of the RE has now been reached, and it has matched abcb. This demonstrates how the matching engine goes as far as it can at first, and if no match is found it will then progressively back up and retry the rest of the RE again and again. It will back up until it has tried zero matches for [bcd]*, and if that subsequently fails, the engine will conclude that the string doesn’t match the RE at all.















re.compile('[\\]').search('6temp o')

Python escapes the  \\ to \ first , the '[\]' used as the regex escaped by RE engine, it interprets \] as an escaped right bracket  and is expecting an unescaped right bracket to close the character class

when \ used in  raw string as regex even bracketed like this r'[\]', \ is still an escaping character and not a backslash

 

 

anyone can help explain why the result  re.compile("([abc])+").search('abc').groups() --------> ('c',) ?

 <monoprotic> c was the final match

[11:21] <monoprotic> it overwrites the previous matches

[11:21] <monoprotic> since its the same capture group

http://www.regular-expressions.info/backref.html



Backreferences, such as \0, doesn't exit , tested with re.compile(r"\w\0").search('abc')==None





- [0-5][0-9] will match all the two-digits numbers from 00 to 59, and [0-9A-Fa-f] will match any hexadecimal digit. If - is escaped (e.g. [a\-z]) or if it’s placed as the first or last character (e.g. [a-]), it will match a literal '-'.

-  





- [^^] will match any character except '^'. ^ has no special meaning if it’s not the first character in the set. 

regex里也有很多条件判断，所以需要使用regex和判断语句的时候，这是一个快捷方式



6.2.5. Regular Expression Examples

Checking for a Pair

re.compile(r"^[a2-9tjqk]{5}$")





>>> pair=re.compile(r".*(.).*\1")>>> displaymatch(pair.match("717ak"))# Pair of 7s."<Match: '717', groups=('7',)>">>> displaymatch(pair.match("718ak"))# No pairs.>>> displaymatch(pair.match("354aa"))# Pair of aces."<Match: '354aa', groups=('a',)>"



Regular expressions beginning with '^' can be used with search() to restrict the match at the beginning of the string:

>>> re.match("c","abcdef")# No match>>> re.search("^c","abcdef")# No match>>> re.search("^a","abcdef")# Match<_sre.SRE_Match object; span=(0, 1), match='a'>



Note however that in MULTILINE mode match() only matches at the beginning of the string, whereas using search() with a regular expression beginning with '^' will match at the beginning of each line.

>>> re.match('X','A\nB\nX',re.MULTILINE)# No match>>> re.search('^X','A\nB\nX',re.MULTILINE)# Match<_sre.SRE_Match object; span=(4, 5), match='X'>

不轻易使用re.MULTILINE

6.2.5.7. Finding all Adverbs and their Positions

If one wants more information about all matches of a pattern than the matched text, finditer() is useful as it provides match objects instead of strings. Continuing with the previous example, if one was a writer who wanted to find all of the adverbs and their positions in some text, he or she would use finditer() in the following manner:

>>> text="He was carefully disguised but captured quickly by police.">>> forminre.finditer(r"\w+ly",text):... print('%02d-%02d: %s'%(m.start(),m.end(),m.group(0)))07-16: carefully40-47: quickly



r'[+\-*/]') match +—*/



re.search(r"([^])*", '^')

^ 在r"[^]" 里面并没有代表^，而是仍然表示排除的意思



what does "^" mean if it is not placed at the beginning of a regex ? for example , why re.search(r"a^b", 'ab') return None?

















































*?, +?, ??







