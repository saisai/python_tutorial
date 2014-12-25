# -*- coding:utf-8 -*-
s = "hello"
d = "world"

if isinstance(s, str):
	print "s is a string"

if type(s) is str:
	print "s is a string2"

if type(s) is type(d):
	print "1"

if type(s) == type(d):
	print "2"

print id(s) - id(d)  # consistent

# if a == b:
# 	print "3"


# 通过type()函数创建的类和直接写class是完全一样的
# 因为Python解释器遇到class定义时，仅仅是扫描一下class定义的语法，
# 然后调用type()函数创建出class。

# class的类型就是type

# *****************************************
# type()可用于动态创建类
# *****************************************
def fn(self):
	print "hello"

Hello = type("temp",(object,),dict(hello=fn))

print type(Hello)

h = Hello()
h.hello()

# equals to...
class temp2(object):
	def __init__(self):
		pass
	def hello(self):
		print "hello"


