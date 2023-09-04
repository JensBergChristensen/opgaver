import time
import RPi.GPIO as G
G.setmode(G.BOARD)
G.setup(40, G.OUT)
G.setup(33, G.OUT)

G.output(33, G.HIGH)
G.output(40, G.HIGH)


p = G.PWM(40, 50)
p.start(0)
try:
    while 1:
        a = int(input("indtast drej"))
        p.ChangeDutyCycle(a)
        time.sleep(0.5)
except KeyboardInterrupt:
    pass
p.stop()
G.cleanup()
