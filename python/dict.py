# -*- coding:utf-8 -*-
stock = {
	"name" : "GOOG",
	"shares" : 100,
	"price" : 490.10
}

name = stock["name"]
print name

if "name" in stock:
	print "name is in dict stock"

# 有就获取，没有就200
p = stock.get("APPLE",200)

print p

keys = list(stock)
print keys

del stock["price"]
print stock