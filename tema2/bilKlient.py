# Import lib
import time
import pygame
import socket as S
import RPi.GPIO as G

# Make socket
host = "10.31.132.155"
port = 3000

skt = S.socket(S.AF_INET, S.SOCK_DGRAM)
skt.bind((host, port))

# Set pins
G.setmode(G.BOARD)
# Motor 1 setup
G.setup(40, G.OUT)
G.setup(37, G.OUT)
G.setup(33, G.OUT)
#Motor 1 output
G.output(33, G.HIGH) # Enable
G.output(40, G.LOW)
G.output(37, G.HIGH)
# Motor 1 start
m1 = G.PWM(37, 50)
m1.start(0)

# Motor 2 setup VENSTRE
G.setup(38, G.OUT)
G.setup(36, G.OUT)
G.setup(32, G.OUT)
# Motor 2 output
G.output(32, G.HIGH) # Enable
G.output(36, G.LOW)
G.output(38, G.HIGH)
# Motor 2 start
m2 = G.PWM(38, 50)
m2.start(0)

# Variabler
speed1 = 0
speed2 = 0

# ChangeDutyCycle function
def setfart(motor1, motor2):
    global speed1
    global speed2
    if speed1 == motor1 and speed2 == motor2:
        pass
    else:
        speed1 = motor1
        speed2 = motor2
        m1.ChangeDutyCycle(motor1)
        m2.ChangeDutyCycle(motor2)

        print("Speed set", speed1, speed2)

# Main thing
while True:
    # Get & set data

    pakke, adresse = skt.recvfrom(64)
    info = pakke.decode("UTF-8")


    # DEBUG: sender hvad klient modtager
    """
    if pakke:
        print("Data modtaget: ", str(info))
    else:
        print("Ikke mere data.")
    break
    """
    # Styring:
    # Kor frem
    if info == "W":

        # Hojre
        G.output(40, G.LOW)
        G.output(37, G.HIGH)
        # Venstre
        G.output(36, G.LOW)
        G.output(38, G.HIGH)

        setfart(99, 99)
    # Kor bagud
    if info == "S":
        # Hojre
        G.output(40, G.HIGH)
        G.output(37, G.LOW)
        # Venstre
        G.output(36, G.HIGH)
        G.output(38, G.LOW)

        setfart(99, 99)
    # Drej venstre
    if info == "A":
        setfart(80, 0)
    # Drej hojre
    if info == "D":
        setfart(0, 80)
    # Kor frem og til venstre
    if info == "WA":
        setfart(80, 30)
    # Kor frem og til hojre
    if info == "WD":
        setfart(30, 80)
    # Kor bagud og venstre
    if info == "SA":
        setfart(80, 30)
    # Kor bagud og Hojre
    if info == "SD":
        setfart(30, 80)
    # STOP
    if info == "0":
        setfart(0, 0)

skt.close()
