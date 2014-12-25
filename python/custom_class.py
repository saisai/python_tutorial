# -*- coding:utf-8  -*-

class custom(object):
	def __init__(self,name):
		self._name = name

	# str() 返回用户看到的字符串
	def __str__(self):
		return "custom name %s"%self._name

	__repr__ = __str__

	# 返回一个iterator,Python的for循环就会不断调用该迭代对象的next()方法拿到循环的下一个值
	def __iter__(self):
		return self

	# 这个next不是生成器的那个next，这个是自定义的next
	def next(self):
		print self._name
		# 最后一定要出发StopIteration()
		raise StopIteration()

	# 要表现得像list那样按照下标取出元素，需要实现__getitem__()方法
	def __getitem__(self,n):
		return "call __getitem__()"

	# 把对象视作list或dict来对集合赋值
	def __setitem__():
		print "setting object"

	# 用于删除某个元素
	def __delitem__():
		print "deleting object"

	# Python解释器会试图调用__getattr__(self, attr)
	
	# 只有 在没有找到属性的情况下 ，才调用__getattr__
	def __getattr__(self, attr):
		print "calling __getattr__"

	@property
	def name(self):
		print "property getter"
		return self._name
	@name.setter
	def name(self, value):
		print "property setter"
		self._name = value
	
	# instance(),不是class()
	def __call__(self):
		print "my name is %s"%self._name

# 对实例进行直接调用就好比对一个函数进行调用一样，所以你完全可以把对象看成函数，
# 把函数看成对象，因为这两者之间本来就没啥根本的区别。

cus = custom("laozhikun")
print cus
for i in cus:
	print i

print cus[100]

print cus.name

# __call__
cus()

print callable(cus)

class temp(object):
	def __init__(self):
		pass

print type(temp)
# class的类型是type，可以使用type()动态生成

t = temp()
print callable(t)