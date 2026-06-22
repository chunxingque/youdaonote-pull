you-get -u http://v.youku.com/v_show/id_XMjUxMjczMzYyMA==.html?tpa=dW5pb25faWQ9MTAzNzUzXzEwMDAwMV8wMV8wMQ



![](attachments/url%20match%20限制_image_0.png)

# 搜寻链接，因为有了download-url:，所以必须从Real URLs:后面搜寻

![](attachments/url%20match%20限制_image_1.png)



Real URLs里可能有非链接内容，所有搜寻的是(https?://\S*)



![](attachments/url%20match%20限制_image_2.png)



没有s，有列表边框

![](attachments/url%20match%20限制_image_3.png)

split('- format'， 小写的Real urls

![](attachments/url%20match%20限制_image_4.png)

路径





re.search(r'''Real URLs?:#搜寻链接，因为有了download-url:，所以必须从Real URLs:后面搜寻，可能会没有s结尾，缺省故而s?

\s*#匹配换行和空格

[\[']*#匹配you-get解析爱课程、爱奇艺的字符化列表左边['，用括号（['）*的话findall会得出不相干的结果，也可以使用(?:\[')*来代替，(?:...)

A non-capturing version of regular parentheses. Matches whatever regular expression is inside the parentheses, but the substring matched by the group cannot be retrieved after performing a match or referenced later in the pattern.

(?P<videoUrls>.*)''', #联合后面的 re.DOTALL搜寻的是Real URL后面去掉左列表界定符的内容，之所以不在regex最后面加上['\]]*是因为.*已经是贪婪模式了，['\]]*表示可有可无，前面贪婪的情况下它无用

parseResult, re.IGNORECASE | re.DOTALL)#是为了you-get解析爱奇艺显示Real URL，解析搜狐显示Real URLs，ykdl则是Real urls