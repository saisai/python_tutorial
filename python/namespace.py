# -*- coding:utf-8 -*-

# test1
c = 3
def a():
	# python2中
	# 内嵌函数可以一层层与“访问”，但如果要修改，就要放到列表或字典中....
	# 只支持给最里面的那层和全局空间的变量重新复制
	e = [2]
	def b():
		e[0]+=1
	def d():
		b()
	b()
	print e[0]

a()

# 而在python3
# 可以使用nonlocal,动态作用域,不只是搜索最里面的那层和全局空间

# test2
c = 3
def a():
	e = 2
	def b():
		e = 3
	def d():
		b()
	b()
	print e

a()

def error():
	# c = c + 1 #UnboundLocalError
	global c
	c = c + 1

error()