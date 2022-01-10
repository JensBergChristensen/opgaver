# -*- coding: ISO-8859-1 -*-
import glob
import time
import os
import sys

#  An Example Reading from /sys/bus/w1/devices/<ds18b20-id>/w1_slave
#  a6 01 4b 46 7f ff 0c 10 5c : crc=5c YES
#  a6 01 4b 46 7f ff 0c 10 5c t=26375

import RPi.GPIO as GPIO

#  Set Pullup mode on GPIO14 first.
GPIO_PIN_NUMBER1=14
GPIO_PIN_NUMBER2=15
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_PIN_NUMBER1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(GPIO_PIN_NUMBER2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

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
  print("ting", w1_devices)
  return rtn;

def getTemp(dataDict, sted):
    for k in sted: dataDict = dataDict[k]
    return dataDict

temp1 = []
temp2 = []
check = []
percent = 0
count = 0

while True:
    temp_readings = ds18b20_read_sensors()
    if '28-000798431dd0' in temp_readings:
        temp1.append(getTemp(temp_readings, ['28-000798431dd0', 'temp_c']))
        print("TEMP1 LISTE: ", temp1)
    if '28-000798431dd0' in temp_readings:
        temp2.append(getTemp(temp_readings, ['28-000598431a78', 'temp_c']))
        print("TEMP2 LISTE: ", temp2)
    else:
        print("fejl")
    # debug
    for t in temp_readings:
        if not 'error' in temp_readings[t]:
            print(u"Device id '%s' reads %.3f +/- 0.5 °C" % (t, temp_readings[t]['temp_c']))
    # Check temp1 list and temp2 list
    if temp1[count] - 5.0 <= temp2[count] <= temp1[count] + 5.0:
        check.append(0)
    else:
        check.append(1)
    count += 1
    print(check)
    if len(check) > 1200:
        percent = round((check.count(1) / len(check))*100)
        print("percentage", percent)
    else:
        print('list too short')
    if percent > 80:
        print("YOU ARE WASTING WATER")
    time.sleep(60)
