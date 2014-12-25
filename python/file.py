# -*- coding:utf-8 -*-
# simply speaking => use with

# 引入了with语句来自动帮我们调用close()方法：

# 最后一步是调用close()方法关闭文件。文件使用完毕后必须关闭，
# 因为文件对象会占用操作系统的资源，并且操作系统同一时间能打开的文件数量也是有限的：

# 你可以反复调用write()来写入文件，但是务必要调用f.close()来关闭文件。当我们写文件时，操作系统往往不会立刻把数据写入磁盘，而是放到内存缓存起来，空闲的时候再慢慢写入。只有调用close()方法时，操作系统才保证把没有写入的数据全部写入磁盘。忘记调用close()的后果是数据可能只写了一部分到磁盘，剩下的丢失了。
with open("../resource/temp.txt","w") as f:
	f.write("你好啊")

with open("../resource/temp.txt","r") as f:
	print f.read()


# file_like object  => object with read()

import codecs

with codecs.open("../resource/temp.txt","r","utf-8") as f:
	print f.read().encode("utf-8")

# StringIO用于临时缓存
try:
	import cStringIO as StringIO
except ImportError:
	import StringIO

a = StringIO.StringIO()
a.write("你好啊")
print a.getvalue()
a.close()