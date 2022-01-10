# -*- coding: ISO-8859-1 -*-
import glob
import time
import os
import sys

#  An Example Reading from /sys/bus/w1/devices/<ds18b20-id>/w1_slave
#  a6 01 4b 46 7f ff 0c 10 5c : crc=5c YES
#  a6 01 4b 46 7f ff 0c 10 5c t=26375

import RPi.GPIO as GPIO

#  Set Pullup mode on GPIO14 and GPIO15
GPIO_PIN_NUMBER1=14
GPIO_PIN_NUMBER2=15
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_PIN_NUMBER1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(GPIO_PIN_NUMBER2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# !!! VARIABLES !!!

temp1 = []
temp2 = []
percent = 0

# !!! FUNCTIONS !!!

# find and get data from sensors
def ds18b20_read_sensors():
  rtn = {}
  w1_devices = []
  w1_devices = os.listdir("/sys/bus/w1/devices/")
  for deviceid in w1_devices:
    rtn[deviceid] = {}
    rtn[deviceid]['temp_c'] = None
    device_data_file = "/sys/bus/w1/devices/" + deviceid + "/w1_slave"
    if os.path.isfile(device_data_file):
      try:
         f = open(device_data_file, "r")
         data = f.read()
         f.close()
         if "YES" in data:
           (discard, sep, reading) = data.partition(' t=')
           rtn[deviceid]['temp_c'] = float(reading) / float(1000.0)
         else:
           rtn[deviceid]['error'] = 'No YES flag: bad data.'
      except Exception as e:
         rtn[deviceid]['error'] = 'Exception during file parsing: ' + str(e)
    else:
      rtn[deviceid]['error'] = 'w1_slave file not found.'
  return rtn;

def readtempdata():
    temp1file = open("/home/pi/temp1file.txt", "r")
    temp2file = open("/home/pi/temp2file.txt", "r")

    file_lines1 = temp1file.read()[1:]
    file_lines2 = temp2file.read()[1:]

    one = file_lines1.split("\n")
    two = file_lines2.split("\n")

    return one, two

def savetempdata(input1, input2):
    temp1file = open("/home/pi/temp1file.txt", "w")
    temp2file = open("/home/pi/temp2file.txt", "w")

    file_lines1 = "\n".join(map(str, input1))
    file_lines2 = "\n".join(map(str, input2))

    temp1file.write(file_lines1)
    temp2file.write(file_lines2)

    return

# For appending temp
def getTemp(dataDict, sted):
    for k in sted: dataDict = dataDict[k]
    return dataDict

# is float
def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False


# !!! START PROGRAM !!!

getthetemps = readtempdata()
temp1 = getthetemps[0]
temp2 = getthetemps[1]
# print("EEE", temp1)

# !!! MAIN LOOP !!!

while True:

    # Run sensor read
    temp_readings = ds18b20_read_sensors()
    if '28-000798431dd0' in temp_readings:
        temp1.append(getTemp(temp_readings, ['28-000798431dd0', 'temp_c']))
        # print("TEMP1 LISTE: ", temp1)
    if '28-000798431dd0' in temp_readings:
        temp2.append(getTemp(temp_readings, ['28-000598431a78', 'temp_c']))
        # print("TEMP2 LISTE: ", temp2)
    else:
        print("fejl")
    # Save  temp data
    savetempdata(temp1, temp2)

    # debug
    for t in temp_readings:
        if not 'error' in temp_readings[t]:
            print(u"Device id '%s' reads %.3f +/- 0.5 °C" % (t, temp_readings[t]['temp_c']))

    # Remove string from lists
    temp1 = [float(x) for x in temp1 if isfloat(x)]
    temp2 = [float(x) for x in temp2 if isfloat(x)]

    # Force lists to float
    # temp1 = list(map(float, temp1))
    # temp2 = list(map(float, temp2))

    # Check temp1 list and temp2 list
    count = 0
    check = []
    if len(temp1) > 0:
        for n in temp1:
            if temp1[count] - 5.0 <= temp2[count] <= temp1[count] + 5.0:
                check.append(0)
            else:
                check.append(1)
            count += 1
    print(check)
    if len(check) > 10:
        percent = round((check.count(1) / len(check))*100)
        print("percentage", percent)
    else:
        print('list too short')
    if percent > 80:
        print("YOU ARE WASTING WATER")
    time.sleep(60)
