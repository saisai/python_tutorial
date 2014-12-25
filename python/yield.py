# -*- coding:utf-8 -*-
def countdown(n):
	print "Counting down from %d"%n
	while n > 0:
		yield n
		n -= 1
	return

# next():不断执行语句，直到遇到yield为止。yield在函数执行的地方生成一个结果，直到再次调用next()

c = countdown(10)

for i,u in enumerate(c):
	if i == 2:
		break
	print u

# shut down explicitly
c.close()

def countdown2(n):
	print "Counting down from %d"%n
	try:
		while n > 0:
			yield n
			n = n - 1
	except GeneratorExit:
		print "only made it to %d"%n

c2 = countdown2(10)
for i in c2:
	print i

