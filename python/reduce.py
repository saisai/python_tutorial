# -*- coding:utf-8   -*-

def add(x,y):
	return x + y

# reduce把一个函数作用在一个序列[x1, x2, x3...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
def fn(x,y):
	return x*10 + y


print reduce(add,[1,2,3,4,5])
print reduce(fn,[1,2,3,4,5])

def str2int(s):
	def fn(x,y):
		return x*10 + y
	def char2num(c):
		return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[c]
	return reduce(fn,map(char2num,s))

print str2int("42536634")


def prod(l):
	def multiply(x,y):
		return x*y
	return reduce(multiply,l)

print prod([1,2,3,4])