def factorial(n):
	'''
	haha
	'''
	if n<=1:
		return 1
	else:
		return n*factorial(n-1)

print factorial.__doc__  # haha

def wrap(func):
	def call(*args,**kwargs):
		return func(*args,**kwargs)
	return call

@wrap
def factorial2(n):
	'''
	haha
	'''
	if n<=1:
		return 1
	else:
		return n*factorial(n-1)

print factorial2.__doc__ # None

def wrap2(func):
	def call(*args,**kwargs):
		return func(*args,**kwargs)
	call.__doc__ = func.__doc__
	call.__name__ = func.__name__
	return call

@wrap2
def factorial3(n):
	'''
	haha
	'''
	if n<=1:
		return 1
	else:
		return n*factorial(n-1)

print factorial3.__doc__  # haha


from functools import wraps

def wrap3(func):
	@wraps(func)   # copy __doc__ and __name__ automatically
	def call(*args,**kwargs):
		return func(*args,**kwargs)
	return call