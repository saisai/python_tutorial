# -*- coding:utf-8 -*-
def remainder(a,b):
	q = a // b  #截断式除法
	r = a - q*b
	return r

# 截断式除法把结果截为整数，浮点数和整数都可以使用

print remainder(100,3)


def divide(a,b):
	q = a // b
	r = a - q*b
	return q,r

quotient,remainder = divide(15,7)

print quotient,remainder

def connect(hostname,port,timeout=3000):
	pass