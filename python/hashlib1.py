# -*- coding:utf-8 -*-
# Python的hashlib提供了常见的 摘要算法 ，如MD5，SHA1等等。

# 有没有可能两个不同的数据通过某个摘要算法得到了相同的摘要？
# 完全有可能，因为任何摘要算法都是把无限多的数据集合映射到一个有限的集合中。
# 这种情况称为碰撞,这种情况也并非不可能出现，但是非常非常困难。

# ***************************************************************
# 存储MD5的好处是即使运维人员能访问数据库，也无法获知用户的明文口令
# ***************************************************************

# 要注意摘要算法不是加密算法，不能用于加密（因为无法通过摘要反推明文），只能用于防篡改，
# 但是它的单向计算特性决定了可以在不存储明文口令的情况下验证用户口令。
import random

import hashlib
md5 = hashlib.md5()
md5.update("i am laozhikun")
print md5.hexdigest()

md6 = hashlib.md5()
md6.update("i am ")
md6.update("laozhikun")
print md6.hexdigest()

sha1 = hashlib.sha1()
sha1.update("i am laozhikun")
print sha1.hexdigest()

sha2 = hashlib.sha1()
sha2.update("i am ")
sha2.update("laozhikun")
print sha2.hexdigest()

db = {}
salts = {}

def get_md5(s):
	md5 = hashlib.md5()
	md5.update(s)
	return md5.hexdigest()

def register(username, password):
	try:
		salt = str(random.randint(0,100000000000))
		salts[username] = salt
		db[username] = get_md5(password + username + salt)
		print "register success"
	except:
		print "register error"

def login(username,password):
	try:
		salt = salts[username]
		md5 = hashlib.md5()
		md5.update(password + username + salt)
		if md5.hexdigest() == db[username]:
			print "login success"
	except:
		print "login error"

def test():
	register("laozhikun","123456")
	login("laozhikun","123456")

if __name__ == "__main__":
	test()
