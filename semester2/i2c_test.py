import smbus
import time

bus = smbus.SMBus(1)
DEVICE_ADDRESS = 0x20      #7 bit address (will be left shifted to add the read write bit)
device_reg_gpio_a = 0x12
device_reg_dir_a = 0x00
device_reg_lat_a = 0x14

write_to_pin = 0b11111110
led_on = 0b00000001
led_off = 0b00000000

"""
bus.write_byte_data(DEVICE_ADDRESS, device_reg_dir_a, write_to_pin)

while True:
  bus.write_byte_data(DEVICE_ADDRESS, device_reg_lat_a, led_on)
  time.sleep(0.5)
  bus.write_byte_data(DEVICE_ADDRESS, device_reg_lat_a, led_off)
  time.sleep(0.5)

"""
while True:
  a = bus.read_byte_data(DEVICE_ADDRESS, device_reg_gpio_a)
  a = (a>>7) & 1
  print(a)


  time.sleep(1)
