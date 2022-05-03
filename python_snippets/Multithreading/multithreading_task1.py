from threading import *
import time

def doubles(numbers):
    for n in numbers:
        time.sleep(1)
        print("Double:", 2*n)

def squares(numbers):
    for n in numbers:
        time.sleep(1)
        print("Square:", n*n)

numbers=[1,2,3,4,5,6]
start_time=time.time()
doubles(numbers)
squares(numbers)
print("The total time taken without threading:", time.time()-start_time)

start_time=time.time()
t1=Thread(target=doubles, args=(numbers,))
t2=Thread(target=squares, args=(numbers,))
t1.start()
t2.start()
t1.join()
t2.join()
print("The total time taken with threading:",time.time()-start_time)