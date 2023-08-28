import urllib.parse

url_str = 'http://www.example.com/path/to/file?param1=value1&~param2=value2'
encoded_str = urllib.parse.quote(url_str, safe='/&:')
print(encoded_str)