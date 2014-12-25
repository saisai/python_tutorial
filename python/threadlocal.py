# -*- coding:utf-8 -*-
# Lock解决的是共享资源被改乱的问题
# ThreadLocal解决的是各个线程部分变量有自己copy的问题
# 多进程是全部变量都有自己copy

# 要实现多任务，通常我们会设计Master-Worker模式，Master负责分配任务
# Worker负责执行任务，因此，多任务环境下，通常是一个Master，多个Worker。

# 我们可以把任务分为计算密集型和IO密集型
# 计算密集型任务同时进行的数量应当等于CPU的核心数。
# 对于IO密集型任务，最合适的语言就是开发效率最高（代码量最少）的语言，脚本语言是首选，C语言最差。
# 如果充分利用操作系统提供的异步IO支持，就可以用单进程单线程模型来执行多任务，这种全新的模型称为事件驱动模型
# 用异步IO编程模型来实现多任务是一个主要的趋势。

# 对应到Python语言，单进程的异步编程模型称为 协程


import threading

# 创建全局ThreadLocal对象:
local_school = threading.local()

def process_student():
    print 'Hello, %s aged %i (in %s)' % (local_school.student, local_school.age,threading.current_thread().name)

def process_thread(name):
    # 绑定ThreadLocal的student:
    local_school.student = name
    local_school.age = 20
    process_student()

t1 = threading.Thread(target= process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target= process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()