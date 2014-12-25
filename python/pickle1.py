# -*- coding:utf-8 -*-

# Python语言特定的序列化模块是pickle，但如果要把序列化搞得更通用、更符合Web标准，就可以使用json模块。

try:
	import cPickle as pickle
except ImportError:
	import pickle
# Create portable serialized representations of Python objects.

# 把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling，
# 在其他语言中也被称之为serialization，marshalling，flattening等等，都是一个意思。

# 只能用于Python，并且可能不同版本的Python彼此都不兼容，
# 因此，只能用Pickle保存那些不重要的数据，不能成功地反序列化也没关系

class a(object):
	def __init__(self):
		self.name = "laozhikun"

obj = a()
f = open("../resource/temp.txt","wb")
pickle.dump(obj,f)
f.close()

f = open("../resource/temp.txt","rb")
obj = pickle.load(f)
f.close()
print obj.name

