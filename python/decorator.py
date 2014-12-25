# -*-  coding:utf-8 -*-
import inspect

enable_tracing = True
if enable_tracing:
	debug_log = open("../resource/debug.log","w")

# customized decorator
# use decorator to add function to the method 

# 在面向对象（OOP）的设计模式中，decorator被称为装饰模式。OOP的装饰模式需要通过继承和组合来实现，
# 而Python除了能支持OOP的decorator外，直接从语法层次

# 这种在代码运行期间 动态增加功能 的方式，称之为“装饰器”（Decorator）。

# 两层包装--不需要参数的时候
def trace(func):
	if enable_tracing:
		def callf(*args,**kwargs):
			debug_log.write("Calling %s : %s,%s\n"%(func.__name__,args,kwargs))
			r = func(*args,**kwargs)
			debug_log.write("%s returned %s"%(func.__name__,r))
			return r
		return callf
	else:
		return func

# foo = trace(foo)
@trace
def foo(name):
	print "hello",name

foo("frank")

event_handlers = {}
# 有参数就要两层包装
from functools import wraps

# 三层包装--在装饰器需要参数的时候
def eventhandler(event_text):
	def decorator(func):
		@wraps(func)
		def register_function(*args, **kw):
			event_handlers[event_text] = func.__name__
			return func
		return register_function
	return decorator


# 实现兼容
def say(text):
	isfunc = inspect.isfunction(text)
	def decorator(func):
		@wraps(func)
		def wrappers(*args, **kw):
			if isfunc:
				print "default"
			else:
				print text
		return wrappers
	if isfunc:
		return decorator(text)
	return decorator

@say
def aa():
	pass

@say("abc")
def bb():
	pass

aa()
bb()

# 要兼容
# sayHello = eventhandler('hello')(sayHello)
# sayHello = eventhandler(sayHello)

@eventhandler("hello")
def sayHello():
	print "hello"

@eventhandler("goodbye")
def sayGoodbye():
	print "Goodbye"

sayHello()
sayGoodbye()

print event_handlers