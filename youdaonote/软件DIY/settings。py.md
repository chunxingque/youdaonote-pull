ADMINSfile:///D:/%E6%88%91%E7%9A%84%E6%96%87%E6%A1%A3/Downloads/django-docs-1.9-en/howto/error-reporting.html  
### 404 errors

Django can also be configured to email errors about broken links (404 “page not found” errors). Django sends emails about 404 errors when:

* [`DEBUG`](../ref/settings.html#std:setting-DEBUG) is `False`;
* Your [`MIDDLEWARE_CLASSES`](../ref/settings.html#std:setting-MIDDLEWARE_CLASSES) setting includes [`django.middleware.common.BrokenLinkEmailsMiddleware`](../ref/middleware.html#django.middleware.common.BrokenLinkEmailsMiddleware "django.middleware.common.BrokenLinkEmailsMiddleware").

  
MIDDLEWARE\_CLASSES = ['django.middleware.common.BrokenLinkEmailsMiddleware',  
  
土豆  
  
<http://www.tudou.com/programs/view/86Am2sQCYEE/><http://v.ifeng.com/v/news/byzb/index.shtml#019086f1-a12b-40a9-b78f-6625edddafaf>  
新浪打开文件夹  
  
Technically, `foo.com/bar` and `foo.com/bar/`   
  
  
