# -*- coding:utf-8 -*-
#  上下文管理器，造出一个临时上下文


# must implement __enter__ and __exit__
class context(object):
	def __enter__(self):
		self.a = 1
		self.b = 2
		return self
	def __exit__(self,type,value,tb):
		if type:
			print "error occured exit"
		else:
			print "normal exit"

# 目的是对系统状态（如打开文件、网络连接和锁定对象等）的对象简化资源控制
# 使得能够在离开上下文时安全释放资源（对于系统类型应该有定义）

cont = context()
with cont as c:
	print c.a,c.b
	# raise ValueError("oh no")


with open("../resource/temp.txt","w") as f:
	f.write("write in context")

