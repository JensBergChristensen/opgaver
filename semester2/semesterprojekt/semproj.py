#!/usr/bin/env python
import time
import RPi.GPIO as GPIO
import mysql.connector
from mfrc522 import SimpleMFRC522
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="MaaGodt*7913",
    database="system" #adminguy pass 1234
)

cursor = db.cursor()
reader = SimpleMFRC522()


try:
  while True:
    print('Scan dit kort for at \nregistere en ny bruger')
    id, text = reader.read()
    cursor.execute("SELECT id FROM brugere WHERE rfid_uid="+str(id))
    cursor.fetchone()

    if cursor.rowcount >= 1:
      print("Vil du overskrive\neksisterende bruger?")
      overwrite = input("Overskriv (Y/N)? ")
      if overwrite[0] == 'Y' or overwrite[0] == 'y':
        print("Overskriver bruger.")
        time.sleep(1)
        sql_insert = "UPDATE users SET name = %s WHERE rfid_uid=%s"
      else:
        continue;
    else:
      sql_insert = "INSERT INTO users (name, rfid_uid) VALUES (%s, %s)"
    print('Skriv dit navn:')
    new_name = input("Navn: ")

    cursor.execute(sql_insert, (new_name, id))

    db.commit()
    print("Bruger" + new_name + "\nGemt")
    time.sleep(2)
finally:
  GPIO.cleanup()
        

























#cursor = db.cursor()

create table check(
    user_id INT UNSIGNED NOT NULL,
   clock_in TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
   PRIMARY KEY ( id )
);

#create table brugere(
  # id INT UNSIGNED NOT NULL AUTO_INCREMENT UNIQUE,#The AUTO_INCREMENT attribute can be used to generate a unique identity for new rows:
 #  rfid_uid VARCHAR(255) NOT NULL,
#  name VARCHAR(255) NOT NULL,
#   created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
#   PRIMARY KEY ( id )
#);

