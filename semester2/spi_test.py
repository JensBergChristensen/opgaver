import spidev

spi = spidev.SpiDev()
spi.open(0,0)

# Settings (for example)
spi.max_speed_hz = 5000


send = [0x01, 0xE0, 0x55]

a = spi.xfer2(send)

x = str(bin(a[1]))[8:10] + str(bin(a[2]))[2:]

y = int(x,2)

print("Transmit: ",a)

print("Receive: ",x)

print("Received value: ", y)
