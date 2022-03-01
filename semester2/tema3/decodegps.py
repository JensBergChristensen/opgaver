import serial
import time


s = serial.Serial("/dev/ttyS0", timeout=1)
print(s.name)


while True:
  data = s.readline()

  #print("DATA: ", data)

  if b"GPGGA" in data:
    gp_gga = data
    print("GP_GGA IS FOUND", gp_gga)

# $GPGGA,093634.000,5701.2381,N,00953.0488,E,1,5,1.63,102.2,M,42.5,M,,*54
    use_data = gp_gga.decode().split(",")
    latitude = use_data[2]
    latitude_degree = (use_data[2])[:2]
    latitude_decimal_minute = (use_data[2])[2:]
    #print("Latitude: ", latitude)
    #print("Degrees: ",latitude_degree,"°")
    #print("Degree minutes: ", latitude_decimal_minute)

    longitude_degree = (use_data[4])[0:3]
    longitude_decimal_minute = (use_data[4])[3:]


    print("Coordinates:")
    print(latitude_degree,"°",latitude_decimal_minute,"'",use_data[3],longitude_degree,"°",longitude_decimal_minute,"'",use_data[5])
    print("Quality: ", use_data[6])
    print("Satelittes: ", use_data[7])
    print("Precision: ", use_data[8])

s.close()
