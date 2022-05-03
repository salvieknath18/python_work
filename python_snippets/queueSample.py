import queue

Q = queue.Queue()

'''
put(): put item in Q
get(): remove and return the item from Q

Producer-Consumer:
Producer thread use put() to insert data in Q. internally have logic to acquaire lock. after inserting release automatically
put() also check whether q full or not if full producer thread entered into wait state by calling wait() internally
Consumer thread use get() to remove and to get the data from the queue. internally have logic to acquaire lock. after removing release automatically.
if Q is empty consumer thread enter into wait state by calling wait() internally.once Q updated with data then thread notified automatically
'''