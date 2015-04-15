s = set([3,4,5,6])
print s

t = set("hello")
print t,"only one l shown"

a = t | s
b = t & s
c = t - s
d = t ^ s

print "|" , a
print "&" , b
print "-" , c
print "^" , d

t.add("x")
print "add" , t

t.update("123","2","3")
print t

print t.remove("l")
print t

class haha(object):
	def __init__(self):
		pass

hh = haha()
aa = set()
aa.add(hh)
print aa
aa.remove(hh)
help(aa)


