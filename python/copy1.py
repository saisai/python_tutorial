from copy import *

#  For collections that are mutable or contain mutable items,
# a copy is sometimes needed so one can change one copy without changing the other.
a = [1,2,3,4]
b = a
# print b is a
b[2] = 100
# print a


a = [1,2,[3,4]]
b = list(a)
# print b is a
b.append(100)
# print a
# print b
b[2][0] = 100
# print a

# help(copy)
a = [1,2,3,4] 
c = a[:] # it is deepcopy already
c[0] = 5
# print a is c
# print "a",a
# b = copy.copy(a)
# print "c",c
# print b


a = {
	"a":1,
	"b":2
}

b = a.copy() # it is deepcopy already
b["a"] = 3
# print a

a = set([1,2,3])
b = a.copy()
b.add("aasd")
# print a


# for list
a = [1,2,3,4]
b = a # shallow
b = a[:] # deep
b.append(5)
# print a
# print b


# for dict
a = {
	"a":1,
	"b":2
}

b = a.copy() # deep
b = a # shallow
b["c"] = 3
# print a
# print b


# for set
a = set([1,2,3])
b = a # shallow
b = a.copy() # deep
b.add(4)
# print a
# print b

# for tuple
# it doesnt matter
a = (1,2)
b = a
b = a[:]
