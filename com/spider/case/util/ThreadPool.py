import threading, time, os, queue

class ThreadPool(object):
    def __init__(self,maxsize):
        self.maxsize=maxsize
        self.q=queue.Queue(maxsize)
        for t in range(0,maxsize):
            print("put a thread=====")
            self.q.put(threading.Thread)

    def getThread(self):
        return self.q.get()

    def addThread(self):
        self.q.put(threading.Thread)
