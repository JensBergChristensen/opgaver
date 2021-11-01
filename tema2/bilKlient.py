# Import lib
import time
import pygame
import socket as S

# Make socket
host = "10.31.132.201"
port = 3500

skt = S.socket(S.AF_INET, S.SOCK_DGRAM)
skt.bind((host, port))

# get data


while True:

    pakke, adresse = skt.recvfrom(64)
    dekodet_pakke = pakke.decode("UTF-8")

    if pakke:
        print("Data modtaget: ", str(dekodet_pakke))
    else:
        print("Ikke mere data.")
        break

    if dekodet_pakke == "W":
        print("fremad")






skt.close()
