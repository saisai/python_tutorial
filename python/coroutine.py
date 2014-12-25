def print_matches(matchtext):
	print "Looking for",matchtext
	while True:
		line = (yield)
		if matchtext in line:
			print line

matcher = print_matches("python")
matcher.next()

matcher.send("python is a good thing")

matcher.send("python")

matchers = [
	print_matches("python"),
	print_matches("guido"),
	print_matches("jython")
]

for m in matchers:
	m.next()

# wwwlog = tail(open("access_log"))
# for line in wwwlog:
# 	for m in matchers:
# 		m.send(line)

# avoid forgetting to call next() at the start of coroutine

# coroutine runs endlessly until you explicitly shut it down
def coroutine(func):
	def start(*args,**kwargs):
		g = func(*args,**kwargs)
		g.next()
		return g
	return start

@coroutine
def receiver():
	print "begin receiving information"
	while True:
		name = (yield)
		print "hello %s"%name

recv = receiver()
recv.send("laozhikun")
recv.send("world")

# return value while generating it
@coroutine
def line_splitter(delimiter=None):
	print "ready to split"
	result = None
	while True:
		line = (yield result)
		result = line.split(delimiter)

splitter = line_splitter(",")
print splitter.send("a,b,c")
print splitter.send("A,B,C")
print splitter.send("asdasd,2342,dfge13")


