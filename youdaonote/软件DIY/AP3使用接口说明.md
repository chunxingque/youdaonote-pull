把分段了的文件按顺序POST方式发给'<http://e100.feing.com.cn/dicts/audio2text/>'，附带的json参数

*   chunk\_count代表文件被分成的分段数目，如果没有分段请复制1
*   hash代表整个录音文件的crc16.genibus值，注意并非分段文件的crc16.genibus值
*   file是编码成base64的字符串

**返回值json格式：**

如果文件没有完整上传会返回，`{'`errorMsg`':"文件未完整上传，请继续上传"}`

如果完整上传且处理成功就会返回类似于下面的内容，

```json
{"audio_text": "\u684c\u5b50"}
```

errorMsg的值有以下几种情况

1.  "File validation failed"

2.  "Please continue to upload files"

3.  百度语音识别返回的一系列请看<https://cloud.baidu.com/doc/SPEECH/s/Zlbxew2qk>

4.  “API exception:<这部分是出错信息，没有固定格式>”，这是我设计的API错误，可以报告给我

