# -*- coding:utf-8 -*-
import urllib

def callf(func):
	return func()

print callf.__globals__

# 最精辟定义
# 将组成函数的语句和这些语句的执行环境打包在一起时，得到的对象叫做闭包
x = 37
def hello():
	print "hello",x

print hello.__globals__

# 这个时候hello带有它的执行环境，这种 语言特性 叫做闭包
# 所有函数拥有一个指向定义该函数的全局命名空间的__globals__属性

callf(hello)

# 这个特性用于惰性求值很有用
def page(url):
	def get():
		return urllib.urlopen(url).read()
	return get

python = page("http://www.python.org")
jython = page("http://www.jython.org")

pydata = python()
jydata = jython()

print python.__closure__
