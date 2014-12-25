# -*-  coding:utf-8 -*-
from collections import OrderedDict

d1 = dict([("a",1),("b",2),("c",3)])
print d1
print d1.keys()

# OrderedDict的Key会按照插入的顺序排列，不是Key本身排序
d2 = OrderedDict([("a",1),("b",2),("c",3)])
print d2
print d2.keys()