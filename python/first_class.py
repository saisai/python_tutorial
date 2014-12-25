items = {
	"number" : 42,
	"text" : "hello world"
}

# all nameable object can be treated as data

items["func"] = abs
import math
items["mod"] = math
items["error"] = ValueError
nums = [1,2,3,4]
items["append"] = nums.append

print items["func"](-45)

print items["mod"].sqrt(49)

try:
	x = int("hah")
except items["error"] as e:
	print("couldnt convert")

line = "GOOG,100,13.45"
field_types = [str,int,float]
raw_fields = line.split(",")
print "raw",raw_fields
# zip is a function to combine two list
# print zip(field_types,raw_fields)
fields = [ty(val) for ty,val in zip(field_types,raw_fields)]
print "processed",fields