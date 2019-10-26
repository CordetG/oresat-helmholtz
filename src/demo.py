import thread6, threading, time, random
from utilities import *

@thread6.threaded()
def print_time(delay=0):
    sum = 0
    for i in range(5):
        sum += random.randrange(0, 100)
        time.sleep(delay)
        log(Mode.INFO, "[" + str(threading.current_thread().name) + "]: " + str(sum))
    return sum

try:
    thread_1 = print_time(3)
    thread_2 = print_time(1)
    value_1 = thread_1.await_output()
    value_2 = thread_2.await_output()
    log(Mode.INFO, "Thread 1: " + str(value_1))
    log(Mode.INFO, "Thread 2: " + str(value_2))

except Exception as e:
    log(Mode.INFO, "Failed to start thread: " + str(e))
