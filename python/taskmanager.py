# -*- coding:utf-8  -*-
import random,time,Queue
from multiprocessing.managers import BaseManager

# Python的分布式进程接口简单，封装良好，适合需要把繁重任务分布到多台机器的环境下。
# 简单但真正的分布式计算
# celery就是把这个task_queue换成了RabbitMQ、Redis甚至是数据库

task_queue = Queue.Queue()

result_queue = Queue.Queue()

class QueueManager(BaseManager):
	pass

QueueManager.register("get_task_queue",callable=lambda:task_queue)
QueueManager.register("get_result_queue",callable=lambda:result_queue)

manager = QueueManager(address=("127.0.0.1",5001), authkey="123")

manager.start()

tasks = manager.get_task_queue()
results = manager.get_result_queue()

for i in range(10):
	n = random.randint(0,10000)
	print "put task %i .."%n
	tasks.put(n)

print "start trying fetching result"
for i in range(10):
	r = results.get()
	print "result: %s"%r

manager.shutdown()
