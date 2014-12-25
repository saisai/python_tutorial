# -*- coding:utf-8 -*-
bar = lambda x,y:x+y
print bar(1,2)

# 匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。
# Small anonymous functions can be created with the lambda keyword
# They are syntactically restricted to a single expression

def make_incrementor(n):
	return lambda x:lambda y:lambda z:n+x+y+z

print make_incrementor(1)(2)(3)(4)

