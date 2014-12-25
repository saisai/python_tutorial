# -*- coding:utf-8  -*- 

print sorted([213,45,2,35,33])

# 通常规定，对于两个元素x和y，如果认为x < y，则返回-1，如果认为x == y，则返回0，如果认为x > y，则返回1
def reverse_sort(x,y):
	if x > y:
		return -1
	elif x < y:
		return 1
	else:
		return 0

# 本身为高级函数
print sorted([213,45,2,35,33],reverse_sort)

print sorted(["Abc","asd","Zsd","rty"])

def insensitive_sort(x,y):
	x = x.upper()
	y = y.upper()
	if x > y:
		return 1
	elif x < y:
		return -1
	else:
		return 0

print sorted(["Abc","asd","Zsd","rty"],insensitive_sort)
