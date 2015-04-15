'''
Licensed under Kun's 
(C) Copyright A Corp. 1999, 2011 All Rights Reserved
Copyright statement and purpose

File name    : pythonic.py
Description  : some advice on improving my code style to meet PEP8
Author       : Frank
'''

a = [1,2,3,4]
print list(reversed(a))

print "{greet} from {language} !".format(greet="Hello world",language="Python")

aa = {"a":"a"}
if "a" in aa:
	print "a in aa"

print "true" if 1 +1 == 3 else "false"

x = 1
x = x + 1      # increment


def docstring_sample():
	'''
	this is a docstring sample
	'''
	pass

print docstring_sample.__doc__

