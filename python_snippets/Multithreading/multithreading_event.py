from threading import *
import time


def trafficpolice():
    while True:
        time.sleep(10)
        print("Traffic Police Giving GREEN Signal")
        event.set()
        time.sleep(20)
        print("Traffic Police Giving RED Signal")
        event.clear()

def driver():
    num=0
    while True:
        print("Drivers waiting for GREEN Signal")
        event.wait()
        print("Traffic Signal is GREEN...Vehicles can move")
        while event.isSet():
            num=num+1
            print("Vehicle No:",num,"Crossing the Signal")
            time.sleep(2)
        print("Traffic Signal is  RED...Drivers have to wait")

event=Event()
t1=Thread(target=trafficpolice)
t2=Thread(target=driver)
t1.start()
t2.start()