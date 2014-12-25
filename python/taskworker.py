from multiprocessing.managers import BaseManager

class QueueManager(BaseManager):
	pass

# still need to register method
QueueManager.register("get_task_queue")
QueueManager.register("get_result_queue")

manager = QueueManager(address=("127.0.0.1",5001),authkey="123")
manager.connect()

tasks = manager.get_task_queue()
results = manager.get_result_queue()

for i in range(10):
	try:
		t = tasks.get()
		n = t * t
		print "task %i ,result %i" %(t,n)
		results.put(n)
	except Queue.Empty:
		print "jobs done"

# manager.shutdown()
