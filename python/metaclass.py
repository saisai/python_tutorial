# -*- coding:utf-8 -*-
# 先定义metaclass，就可以创建类，最后创建实例

# 按照默认习惯，metaclass的类名总是以Metaclass结尾

# *****************************************
# 使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass
# *****************************************

class ListMetaclass(type):
	def __new__(cls,name,bases,attrs):
		attrs["add"] = lambda self,value : self.append(value)
		return type.__new__(cls,name,bases,attrs)

# 其实可以在MyList直接加add
class MyList(list):
	__metaclass__ = ListMetaclass

l = MyList()
l.add(1)
print l

l2 = list()
try:
	l2.add(2)
except:
	print "no add"

# 但是，总会遇到需要通过metaclass修改类定义的

