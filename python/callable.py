class foo(object):
	def __init__(self):
		print "set up"
	def __call__(self):
		print "called"

# object become callable
ak = foo()
ak()