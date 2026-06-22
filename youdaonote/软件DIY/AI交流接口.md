POST方式发给http\://e100.feing.com.cn/ChatBot/，附带的json参数里包含如下字段

*   question代表发给AI的文字内容
*   file是文件编码成base64的字符串，可选参数，*目前暂未实现处理文件的功能，敬请期待*



**返回值json格式：**

如果处理成功就会返回类似于下面的内容，

```json
{"answer": "\u662f\u4e00\u4e2a\u5e38\u7528\AABAAEAgD4AAAB9AAACABAATElTVBoA……"}
```

*   answer是AI返回的结果

