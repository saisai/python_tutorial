# -*- coding: utf-8 -*-
ttuple = (1,2,3,4,5)

ttuple2 = 1,2,3,4,5

# 解包
one,two,three,four,five = ttuple
print one,two,three,four,five

one,two,three,four,five = ttuple2
print one,two,three,four,five


try:
	ttuple[2] = 1
except:
	print "cant change tuple's value"

# filename = "tuple.txt"
# portfolio = []
# for line in open(filename):
# 	fields = line.split(",")
# 	name = fields[0]
# 	shares = int(fields[1])
# 	price = float(fields[2])
# 	stock = (name,shares,price)
# 	portfolio.append(stock)


# tuple的单元素写法
a = (one,)