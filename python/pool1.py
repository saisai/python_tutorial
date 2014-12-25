from multiprocessing import Pool
import os,time,random

def work(name):
	sec = random.random()*10
	print "%s begin sleeping"%name
	time.sleep(sec)
	print "%s sleep for %f seconds"%(name,sec)

if __name__ == "__main__":
	print "parent process id => %s"%os.getpid()
	p = Pool(10)
	for i in range(10):
		p.apply_async(work,args=(str(i),))
	p.close()
	p.join()
	print "all child process runned"

