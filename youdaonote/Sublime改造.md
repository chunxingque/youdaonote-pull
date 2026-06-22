1. sounds like you need a custom plugin
1. *[*<font color= "#000000">**19:37**</font>*<font color= "#000000">**]**</font>*
you could either subclass exec and substitute a few functions with your own that cache and replace cmd arguments
1. *[*<font color= "#000000">**19:38**</font>*<font color= "#000000">**]**</font>*or you could write a plugin that wraps the exec command and preexpands the 
cmd argument before forwarding it to the 
exec command, caching it in the process
1. *[*<font color= "#000000">**19:39**</font>*<font color= "#000000">**]**</font>*
though I personally don't know when you would invalidate your cache

<font color= "#dcddde">- </font>[https://www.sublimetext.com/docs/api_reference.html](https://www.sublimetext.com/docs/api_reference.html)
- Command Palette → *<font color= "#dcddde">**View Package File**</font>*<font color= "#dcddde"> → </font>*<font color= "#dcddde">**Default/exec.py**</font>*