import os
import fnmatch

def coroutine(func):
	def start(*args,**kwargs):
		g = func(*args,**kwargs)
		g.next()
		return g
	return start

@coroutine
def find_files(target):
	while True:
		topdir,pattern = (yield)
		for path,dirname,filelist in os.walk(topdir):
			for name in filelist:
				if fnmatch.fnmatch(name.pattern):
					target.send(os.path.join(path,name))

@coroutine
def opener(target):
	while True:
		name = (yield)
		if name.endswith(".gz"):
			f = gzip.open(name)
		elif name.endswith(".bz2"):
			f = bz2.open(name)
		else:
			f = open(name)
		target.send(f)

@coroutine
def cat(target):
	while True:
		f = (yield)
		for line in f:
			target.send(line)

@coroutine
def grep(pattern,target):
	while True:
		line = (yield)
		if pattern in line:
			target.send(line)

@coroutine
def printer():
	while True:
		line = (yield)
		sys.stdout.write(line)

# just opposite to pipe using generator
finder = find_files(opener(cat(grep("python",printer()))))

finder.send(("www","access-log"))