from gpiozero import LED
from gpiozero import MotionSensor
from picamera import PiCamera
from time import sleep
import time

green_led = LED(17)
pir = MotionSensor(4)
green_led.off()
camera = PiCamera()
camera.resolution = (1920,1080)

while True:
   pir.wait_for_motion()
   print("Bevægelse dedikteret")
   sleep(6)
   camera.capture("/home/pi/Desktop/killa" + time.strftime("%b-%d-%Y_%H:%M:%S") + ".jpg")
   green_led.on()
   pir.wait_for_no_motion()
   green_led.off()
   print ("Bevaegelse stoppet")