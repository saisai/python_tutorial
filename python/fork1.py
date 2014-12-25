import os

print "process (%s) start ..."%os.getpid()

# similar to system call
pid = os.fork()
if pid == 0:
	print "i am child process %s and my parent is %s"%(os.getpid(),os.getppid())
else:
	print "this is parent process %s"%os.getpid()

