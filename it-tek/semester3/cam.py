from gpiozero import LED, Motionsensor
from time import sleep
from picamera import PiCamera

# PIN SETUP
green_led = LED(17)
pir = Motionsensor(4)

# CAMERA SETUP
camera = PiCamera()
camera.resulution = (640, 480)
camera.vflip =  True


print("starting")
sleep(2)
print("STARTED")
# MAIN LOOP
while True:
    pir.wait_for_motion()
    print("Motion DETECTED")
    green_led.on()

    camera.capture(['image%i.jpg' % ra])

    pir.wait_for_no_motion()
    green_led.off()
    print("Motion STOPPED")
