# -*- coding:utf-8  -*-

from collections import namedtuple

# easily define a new data structure
# | type  | name | changeable |
# | list  |  no  |     yes    |
# | tuple |  no  |     no     |
# | dict  |  yes |     yes    |
# | nt    |  yes |     no     | 

Point = namedtuple("Point",["x","y"])
p = Point(1,2)
print "p.x =",p.x
print "p.y =",p.y

# old-fashioned
class Point2(tuple):
	def __init__(self,li):
		try:
			super(Point2,self).__init__(self)
			self._mapping = {"x":li[0],"y":li[1]}
		except:
			print "err while initing"

	def __getattr__(self,name):
		return self._mapping[name]

p2 = Point2([1,2])
print "p2.x =",p2.x
print "p2.y =",p2.y
