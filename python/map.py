# -*- coding:utf-8 -*-
import math
a = [1,2,3]

# 像map()函数这种能够接收函数作为参数的函数，称之为高阶函数（Higher-order function）
# it supports only one iterable argument though

# 如果你读过Google的那篇大名鼎鼎的论文“MapReduce: Simplified Data Processing on Large Clusters”，你就能大概明白map/reduce的概念。
def pow2(x):
	return math.pow(x,2)

b = map(pow2,a)
print b

for i,x in enumerate(a):
	a[i] = x*x

print a


def myMap(f,l):
	return [f(i) for i in l]

def pow2(x):
	return x*x

print myMap(pow2,[1,2,3])