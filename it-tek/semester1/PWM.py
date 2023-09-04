import time
import RPi.GPIO as G
G.setmode(G.BOARD)
G.setup(40, G.OUT)
G.setup(37, G.OUT)
G.setup(33, G.OUT)

G.output(33, G.HIGH)
G.output(40, G.LOW)
G.output(37, G.HIGH)


p = G.PWM(37, 50)
p.start(0)
try:
    while 1:
        for dc in range(0, 101, 5):
            p.ChangeDutyCycle(dc)
            time.sleep(0.5)
        for dc in range(100, -1, -5):
            p.ChangeDutyCycle(dc)
            time.sleep(0.5)
except KeyboardInterrupt:
    pass
p.stop()
G.cleanup()
