import threading
from time import sleep

ting = 0

def thad1():
    while True:
        return ting + 1

def thad2():
    while True:
        sleep(0.1)
        return 1 - ting

def pint():
    while True:
        print(ting)
        sleep(1)

t = threading.Thread(target=thad1)
m = threading.Thread(target=thad2)


t.start()
m.start()
pint()
