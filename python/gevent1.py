# -*- coding:utf-8 -*-
from gevent import monkey
monkey.patch_socket()
# monkey.patch_all(dns=False)

# gevent是第三方库，通过greenlet实现协程

import gevent
import urllib2

def f(n):
	for i in range(n):
		print gevent.getcurrent(),i

# 10个携程
# coroutines = []
# for i in range(10):
# 	a = gevent.spawn(f,50)
# 	coroutines.append(a)

# gevent.joinall(coroutines)

def f2(url):
	print('GET: %s' % url)
	resp = urllib2.urlopen(url)
	data = resp.read()
	print('%d bytes received from %s.' % (len(data), url))

gevent.joinall([
        gevent.spawn(f2, 'http://www.weibo.com/'),
        gevent.spawn(f2, 'http://www.163.com/'),
        gevent.spawn(f2, 'http://www.qq.com/'),
])

