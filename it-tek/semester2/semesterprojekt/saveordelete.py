#!/usr/bin/env python
# ------------------------
# Imports:
from time import sleep
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import mysql.connector

# ------------------------
# Connect to database:
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

# Register card to database function:
def register_card():
    try:
        while True:
            print("Hold a tag near the scanner to register new user. Press Ctrl + c to cancel")
            uid, text = reader.read() # waits for card to scan
            sleep(0.3)
            cursor.execute("SELECT id FROM users WHERE uid="+str(uid))
            cursor.fetchone()

            if cursor.rowcount >= 1:
                print("Overwrite\nexisting user?")
                overwrite = input("Overwrite (Y/N)? ")
                if overwrite[0] == 'Y' or overwrite[0] == 'y':
                    print("Overwriting user.")
                    sleep(1)
                    sql_insert = "UPDATE users SET name = %s, sec = %s WHERE uid=%s"
                else:
                    continue
            else:
                sql_insert = "INSERT INTO users (name, sec, uid) VALUES (%s, %s, %s)"
            print("Enter new name")
            new_name = input("Name: ")
            print("Enter new access level")
            sec = input("Enter 1 for admin, Enter 2 for user: ")

            cursor.execute(sql_insert, (new_name, sec, uid))

            db.commit()

            print("User " + new_name + "\nSaved")
            sleep(2)
        
    except KeyboardInterrupt:
        print(" Register cancel")
        sleep(1)

# Delete User Function:
def delete_user():
    print("current users:")
    cursor.execute("SELECT * FROM users")
    result = cursor.fetchall()
    for row in result:
        print("ID:", row[0], "| UID:", row[1], "| Name:", row[2], "| Sec:", row[3], "| Created:", row[4], "\n")
    
    delete_user = input("Enter id to delete(q to cancel): ")
    if delete_user == "q": # ends function
        print("No user deleted")
    else:
        try:
            cursor.execute("DELETE FROM users WHERE id="+str(delete_user))
        except Exception:
            print("User not found")

# Print list of users that have entered the server room, sorted by latest entry
def view_logs():
    print("Last person to enter was: ")
    cursor.execute("SELECT * FROM entry")
    result2 = cursor.fetchall()
    for row in result2:
        print(row[0], "| Name:", row[1], "| Time:", row[2], "\n")


# ------------------------
# Main Program:
while True:
    print("\n")
    print("select 1 for new user")
    print("select 2 to delete user")
    print("select 3 to see logs ")
    print("select 4 to exit program")
    try:
        k = int(input("\nchoose option from menu: ")) # get input from user
        if k == 1:
            register_card() # add user
        if k == 2:
            delete_user() # delete user
        if k == 3:
            view_logs() # see entry log
        if k == 4:
            exit() # exit program
    except Exception:
        print("\nPlease enter a valid input")