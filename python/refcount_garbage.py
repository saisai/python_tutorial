import sys

s = "10"
print sys.getrefcount(s)


a = {}
b = {}
a["b"] = b
b["a"] = a

