# -*- coding:utf-8  -*-


# doctest非常有用，不但可以用来测试，还可以直接作为示例代码。通过某些文档生成工具，
# 就可以自动把包含doctest的注释提取出来。用户看文档的时候，同时也看到了doctest。

class Dict(dict):
	'''
	Simple dict but also support access as x.y style.

	>>> d1 = Dict()
	>>> d1['x'] = 100
	>>> d1.x
	100
	>>> d1.y = 200
	>>> d1['y']
	200
	>>> d2 = Dict(a=1, b=2, c='3')
	>>> d2.c
	'3'
	>>> d2['empty']
	Traceback (most recent call last):
		...
	KeyError: 'empty'
	>>> d2.empty
	Traceback (most recent call last):
		...
	AttributeError: 'Dict' object has no attribute 'empty'
	'''


	# 只有测试异常的时候，可以用...表示中间一大段烦人的输出。
	def __init__(self, **kw):
		super(Dict, self).__init__(**kw)

	def __getattr__(self, key):
		try:
			return self[key]
		except KeyError:
			raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

	def __setattr__(self, key, value):
		self[key] = value

import unittest

class TestDict(unittest.TestCase):

	def setUp(self):
		print "setting up"

	def test_init(self):
		d = Dict(a=1, b='test')
		
		# 常用之一 self.assertEquals
		self.assertEquals(d.a, 1)
		self.assertEquals(d.b, 'test')
		self.assertTrue(isinstance(d, dict))

	def test_key(self):
		d = Dict()
		d['key'] = 'value'
		self.assertEquals(d.key, 'value')

	def test_attr(self):
		d = Dict()
		d.key = 'value'
		self.assertTrue('key' in d)
		self.assertEquals(d['key'], 'value')

	def test_keyerror(self):
		d = Dict()

		# 期待抛出指定类型的Error
		# with就是说，在这块临时的作用于内期待那个错误，而不是其他地方
		with self.assertRaises(KeyError):
			value = d['empty']

	def test_attrerror(self):
		d = Dict()
		with self.assertRaises(AttributeError):
			value = d.empty

	def tearDown(self):
		print "tearing down"


if __name__ == '__main__':
	# unittest.main()
	import doctest
	doctest.testmod()
