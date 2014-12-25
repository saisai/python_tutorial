# -*- coding:utf-8 -*-
# 生成器是基于处理管道、流或数据流编写程序的一种极其强大的方式
import time
import sys
def tail(f):
	f.seek(0,2)
	while True:
		line = f.readline()
		if not line:
			# print "line empty"
			time.sleep(1)
			continue
		# print "get line"
		yield line

def grep(lines,searchtext):
	for line in lines:
		if searchtext in line:
			yield line

wwwlog = tail(open("../resource/int.txt"))
pylines = grep(wwwlog,"python")
for line in pylines:
	print line
