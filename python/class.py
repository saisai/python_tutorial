# -*- coding:utf-8 -*-

# 面向对象的抽象程度又比函数要高，因为一个Class既包含数据，又包含操作数据的方法。
# 约定第一个参数为self，指向自己，涉及对象属性的所有操作都要显式引用self
class Stack(object):
	def __init__(self):
		self.stack = []
	def push(self,object):
		self.stack.append(object)
	def pop(self):
		return self.stack.pop()
	def length(self):
		return len(self.stack)

s = Stack()
s.push("Dave")
s.push(42)
s.push([3,4,5])
x = s.pop()
y = s.pop()
del s

class Stack2(list):
	@staticmethod
	def sayHello():
		print "hello"
	

Stack2.sayHello()


print object.__doc__
# print help(object)


# 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__
# 变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，
# 特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名。
class withPrivate(object):
	def __init__(self):
		self.__name = "laozhikun"
		self.__lover = "zhangning"

pr = withPrivate()
try:
	print pr.__name
except:
	print "cant visit private variable"

# setter/getter可以写为一个修饰器
class withPrivate2(object):
	def __init__(self,name="laozhikun",lover= "zhangning",age=10):
		self.__name = name
		self.__lover = lover
		self.__age = age
	def getName(self):
		return self.__name
	def getLover(self):
		return self.__lover
	def setName(self,name):
		self.__name = name
	# can exam before applying
	def setAge(self,age):
		if 0 <= age <= 100:
			self.__age = age
		else:
			pass

pr2 = withPrivate2()
print "still can visit but not recommended->",pr2._withPrivate2__name
# 