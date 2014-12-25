# -*- coding:utf-8  -*-

# 可以使用__slot__来限制class的属性
class ak48(object):
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
a.name = "aaa"
# 虽然实际调用是这个，但是不可以直接访问
a.name = "bbb"



