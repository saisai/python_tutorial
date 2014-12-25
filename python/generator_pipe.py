# -*- coding:utf-8  -*-
# 生成器和协程在解决系统、网络和分布式计算方面的编程问题时特别有用

import os
import fnmatch

# full path to all files
# open file
# all lines in a file
# 
def find_files(topdir,pattern):
	for path,dirname,filelist in os.walk(topdir):
		for name in filelist:
			if fnmatch.fnmatch(name,pattern):
				yield os.path.join(path,name)

import gzip,bz2
def opener(filenames):
	for name in filenames:
		if name.endswith(".gz"):
			f = gzip.open(name)
		elif name.endswith(".bz2"):
			f = bz2.open(name)
		else:
			f = open(name)
		yield f

def cat(filelist):
	for f in filelist:
		for line in f:
			yield line

def grep(pattern,lines):
	for line in lines:
		if pattern in line:
			yield line

import sys
# wwwlogs = find_files("www","access_log")
# files = opener(wwwlogs)
# lines = cat(files)
# pylines = grep("python",lines)
pylines = grep("python",cat(opener(find_files("www","access_log"))))

for line in pylines:
	sys.stdout.write(line)
