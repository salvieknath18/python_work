from threading import *
import time

print("current thread: ",current_thread().getName())

def task1():
    for i in range(1,11):
        print("task1 : ", i)
        print("****************", active_count())
        time.sleep(1)

t1 = Thread(target=task1)
t1.start()


class MyThread(Thread):
    def run(self):
        for i in range(1,11):
            print("task2 : ", i)
            print("****************", active_count())
            time.sleep(1)

t2 = MyThread()
t2.start()



for m in range(1,2):
    print("main : ", m)
    print("****************",active_count())
    time.sleep(1)

#t1.join()
#t2.join()


#active_count()   : counts number of active threads
#current_thread().getName() : Returns Name of the thread
#current_thread().setName() : Set the name for current thread
#current_thread().ident : returns Identification number for the current thread
#enumerate : return list of all active threads currently running
#isAlive() : Check whether the thread is still executing or not
#join() : if a thread wants to wait until completing some other thread then we should go for join method


'''
Daemon Thread: Thread runnung in the background eg. garbage collector to support non daemon thread like main thread


Synchronisation: Main advantage to overcome data inconsistency problem but disadvantage that increases waiting time

Lock is use for synchronisation have methods acquaire() and release()
But simple lock have problem of geting block eg. if it is used in recursive 
function
So to solve that we use RLock means thread can acquaire same lock again but 
for every acquaire call release call should be there

Semaphore:
Lock, Rlock allowed only one thread to run at a time, but what if more than one, or perticular number of thread should be allowed
eg. 10 members are allowed to access database at a time for this semaphores are used
Semaphores used to limit the access to shared the resources
s=Semaphore(2) allow to 2 threads to acuaire()  

event = threading.Event()
consumer uses event.wait(), event.isSet()
producer :- event.set(), event.clear()
event.set()

'''

'''
import queue

Q = queue.Queue()
put(): put item in Q
get(): remove and return the item from Q

Producer-Consumer:
Producer thread use put() to insert data in Q. internally have logic to acquaire lock. after inserting release automatically
put() also check whether q full or not if full producer thread entered into wait state by calling wait() internally
Consumer thread use get() to remove and to get the data from the queue. internally have logic to acquaire lock. after removing release automatically.
if Q is empty consumer thread enter into wait state by calling wait() internally.once Q updated with data then thread notified automatically
'''






