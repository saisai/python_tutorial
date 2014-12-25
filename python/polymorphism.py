# -*- coding:utf-8  -*-

# 调用方只管调用，不管细节。这就是著名的“开闭”原则

# 在调用类实例方法的时候，*尽量把变量视作父类类型*，这样，所有子类类型都可以正常被接收

class animal():
	def __init__(self):
		pass
	def run(self):
		print "animal is running"

class dog(animal):
	def __init__(self):
		pass
	def run(self):
		print "dog is running"

class lion(animal):
	def __init__(self):
		pass
	def run(self):
		print "lion is running"

# 这个就是接口
def run(animal):
	animal.run()


run(lion())
run(dog())
run(animal())