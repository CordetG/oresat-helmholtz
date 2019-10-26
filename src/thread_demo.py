import threading, random, time
from queue import Queue
from utilities import *

MAX_THREAD_COUNT = 8
MAX_CALC = 10000000
PARENT = threading.main_thread()

def proc(lower, upper, mod):
    for i in range(0, MAX_CALC):
        if(lower == 0): lower = 1
        if(mod == 0): mod = 1
        if(upper <= lower): upper = lower + 1
        num = random.randrange(lower, upper) % mod
        q.put(num)
        log(Mode.INFO, 'Added to queue: ' + str(num))
    q.task_done()

if __name__ == '__main__':
    q = Queue(128)

    for i in range(MAX_THREAD_COUNT): threading.Thread(name='T' + str(i), target=proc, args=(i, random.randint(i, 100), i)).start()

    for thread in threading.enumerate():
        if(thread.ident != PARENT.ident):
            thread.join()
            log(Mode.INFO, "Thread: " + thread.name + " finished!")

    q.join()
    sum = 0
    for i in range(q.qsize()): sum += q.get()
    log(Mode.INFO, 'Sum: ' + str(sum))
