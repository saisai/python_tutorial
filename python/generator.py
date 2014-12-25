# -*- coding:utf-8 -*-
def countdown(n):
	print "counting down"
	while n>0:
		yield n
		n-=1

# 生成器生成一个序列
c = countdown(3)
print "type",type(c)

print "next",c.next()

print "for in"
for i in c:
	print i

# 没有把东西都放进内存，只知道如何按照需要生成数据的生成器


