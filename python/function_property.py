def foo():
	print "Haha"

foo.secure = 1
foo.private = 1

print foo.__dict__  # all properties are stored in __dict__

# to pass __dict__ to decorator
def wrap(func):
	def call(*args,**kwargs):
		return func(*args,**kwargs)
	call.__doc__ = func.__doc__
	call.__name__ = func.__name__
	call.__dict__ = func.__dict__
	return call

from functools import wraps
# or
def wrap2(func):
	@wraps(func)
	def call(*args,**kwargs):
		return func(*args,**kwargs)
	return call