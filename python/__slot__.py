# -*- coding:utf-8 -*-

class ak47(object):
	def __init__(self):
		print "initializaion"

a = ak47()
a.aa = 3
a.bb = 4


# 可以使用__slot__来限制class的属性
class ak48(object):
	# 各种变量要放到__slot__,方法名不用
	__slots__ = ("_score","_name")

	def __init__(self):
		print "initializaion"
		self._name = "laozhikun"
		self._score = 60

	@property
	def score(self):
	    return self._score

	@score.setter
	def score(self, value):
	    self._score = value
	

	@property
	def name(self):
	    return self._name
	@name.setter
	def name(self, value):
	    self._name = value
	

a = ak48()

# 实际转化为 a.set_score()，又因为方法名不受__slot__影响
a.score = 100
# a.aa = 3
# a.bb = 4
print a.name

a.name = "aaa"
print a.name
print a._ak48__name  # 连这种方式也访问不了了