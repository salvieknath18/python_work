from threading import *
import time
I = Lock()
flag = 0


def even(i):
        I.acquire()
        print("even : "+str(i))
        time.sleep(1)
        I.release()
        

def odd(i):
        I.acquire()
        print("odd : "+str(i))
        time.sleep(1)
        I.release()


for i in range(0,11):
    if flag == 0:
        t1 = Thread(target=even,args=(i,))
        t1.start()
    if flag == 1:
        t2 = Thread(target=odd,args=(i,))
        t2.start()
    flag = not flag
    time.sleep(1)
    
        
