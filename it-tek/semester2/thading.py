import threading

def coder():
    for k in range(5000000):
        print ('t', end='', flush=True)
    return

def koder():
    for k in range(5000000):
        print ('M', end='', flush=True)
    return

t = threading.Thread(target=coder)
m = threading.Thread(target=koder)
t.start()
m.start()