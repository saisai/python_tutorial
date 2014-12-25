# -*- coding:utf-8 -*-

from multiprocessing import Process
import os
import time

def run_proc(name):
	print "run child process %s (%s)"%(name,os.getpid())
	print "sleep for 2 seconds"
	time.sleep(2.0)
	print "wake up"


if __name__ == "__main__":
	print "parent process %s."%os.getpid()
	p = Process(target=run_proc,args=("laozhikun",))
	print "child process is starting"
	p.start()
	p.join() # join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步
	print "after join"
