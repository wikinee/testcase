#-*- coding:utf-8 -*-
import threading
import time
def fun(name, ls_name, front_thread = None):
    '''
    线程启动函数
    通过front_thread来使用线程有序的运行
    '''
    time.clock()
    time.sleep(2)
    # 如果front_thread存在，则在front_thread运行完成后，才运行当前线程
    if front_thread != None:
        front_thread.join()
    ls_name.append(name)
    print "thread %s : %s"% (name, time.clock())

if __name__ == '__main__':
    ls_result_name = []
    ls_thread = []
    time.clock()
    # 逐一启动1000个线程
    for i in range(0,10):
        if len(ls_thread) == 0:
            t = threading.Thread(target=fun, args=(i,ls_result_name,None))
        else:
            t = threading.Thread(target=fun, args=(i,ls_result_name,ls_thread[-1]))
        t.start()
        ls_thread.append(t)

    # 等待所有线程结束
    for t in ls_thread:
        t.join()

    print 'ls_result_name:', ls_result_name
    print "main thread:%s" % time.clock()