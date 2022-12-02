#!/usr/bin/env python
# ------------------------
# Imports:
from datetime import datetime, time
from time import sleep
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import mysql.connector

# ------------------------
# GPIO SETUP:
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
# GPIO PINS
GPIO.setup(20,GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(21,GPIO.OUT)

# ------------------------
# Connect to database
db = mysql.connector.connect(
  host="localhost",
  user="isi",
  passwd="MaaGodt*7913",
  database="testbase"
)
# database cursor creation
cursor = db.cursor()

# RFID object setup
reader = SimpleMFRC522()


# ------------------------
# Functions:

# Time check function. If time is 
def is_time_between(begin_time, end_time):
    check_time = datetime.utcnow().time() # Uses current time in utc
    if begin_time < end_time:
        return check_time >= begin_time and check_time <= end_time
    else: # crosses midnight
        return check_time >= begin_time or check_time <= end_time

# green led blink
def green_led_blink():
  GPIO.output(20,GPIO.HIGH)
  sleep(1)
  GPIO.output(20,GPIO.LOW)
# red led blink
def red_led_blink():
  GPIO.output(21,GPIO.HIGH)
  sleep(1)
  GPIO.output(21,GPIO.LOW)
# Opens the door
def open_door():
  GPIO.output(17, GPIO.HIGH)
  sleep(2)
  GPIO.output(17, GPIO.LOW)

# ------------------------
# Main Program:
try:
  while True:
    
    print("Place Card to record attendance. Press Ctrl + c to stop program")
    uid, text = reader.read() # waits for card to scan

    sleep(0.3) # Sleep to stop spamming database and casuing crash
    cursor.execute("Select id, name, sec FROM users WHERE uid="+str(uid)) # Finds user with the unique card UID
    
    result = cursor.fetchone() # if user found return as tuple, if not return none.
    
    if cursor.rowcount >= 1: # if database finds a user
      if result[2] == "2": # if sec is 2, check time.
        allow_time = is_time_between(time(6,00), time(18,00)) # returns true if time is between input
        if not allow_time:
          print("Cannot record attendance after 18:00")
          red_led_blink()
          continue # restarts loop

      print("Welcome " + result[1])
      cursor.execute("INSERT INTO entry (name) VALUES (%s)", (result[1],) ) # Create new entry with cardholder name and current timestamp
      db.commit() #commit insert to database
      green_led_blink()
      open_door()


    else: # if database does not find a user
      print("User does not exist.")
      red_led_blink()
    sleep(1)
except KeyboardInterrupt:
  print("Program has stopped")
  GPIO.cleanup()
  exit()