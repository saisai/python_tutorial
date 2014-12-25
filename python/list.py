names = ["Dave","Mark","Ann","Phil"]

print names[2]

names.append("Frank")

print names

names[0:2] = ["Frank1","Frank2","Frank3"]

print names

a = [1,2,3] + [4,5]

print a

list1 = []
list2 = list()

print list1
print list2

list3 = [1,"Dave",3.14,[5,4,2323]]

print list3[3][1]

# 
import sys

if len(sys.argv) != 2:
	print "please supply a filename"
	raise SystemExit(1)
f = open(sys.argv[1])
lines = f.readlines()
print lines
f.close()

# 列表包含
fvalues = [float(line) for line in lines]

print "The minumum value is" , min(fvalues)
print "The maximum value is" , max(fvalues)