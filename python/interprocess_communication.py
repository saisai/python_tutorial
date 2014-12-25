from multiprocessing import Process,Queue,Pipe
import os,time,random

def write(q):
	for i in range(1,6):
		print "putting value %i into queue"%i
		q.put(i)
		time.sleep(random.random())

def read(q):
	while True:
		value = q.get()
		print "get value %i from queue"%value

if __name__ == "__main__":
	q = Queue()
	w = Process(target=write,args=(q,))
	r = Process(target=read,args=(q,))
	w.start()
	r.start()

	w.join()
	r.terminate()
