# -*- coding:utf-8 -*-
import base64

# Base64是一种用64个字符来表示任意二进制数据的方法。
# Base64是一种任意二进制到文本字符串的编码方法.
# 常用于在URL、Cookie、网页中传输少量二进制数据。
# Base64是一种通过查表的编码方法，不能用于加密，即使使用自定义的编码表也不行。

print base64.b64encode('binary\x00string')
print base64.b64decode("YmluYXJ5AHN0cmluZw==")
print base64.b64encode('i\xb7\x1d\xfb\xef\xff')
print base64.urlsafe_b64encode('i\xb7\x1d\xfb\xef\xff')
# print base64.urlsafe_b64decode('abcd--__')
print base64.b64decode('YWJjZA==')
try:
	base64.b64decode('YWJjZA')
except:
	print "need =="

help(base64)
# print base64.safe_b64decode('YWJjZA')

