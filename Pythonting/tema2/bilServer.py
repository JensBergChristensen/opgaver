# Import lib
import time
import pygame
import socket as S

# Make socket
host = "10.31.132.201"
port = 3500
skt = S.socket(S.AF_INET, S.SOCK_DGRAM)

# Py game ssetup
pygame.init()
screenSize = (800, 700)
screen = pygame.display.set_mode(screenSize)
pygame.display.set_caption("square move")
done = False
clock = pygame.time.Clock()

# Send ting
pakke = "Hejsa"
pakke = pakke.encode("UTF-8")

while not done:
        for event in pygame.event.get():
                # !!! GET EVENT !!!
                if event.type == pygame.QUIT:
                        done = True
        # !!! GET KEYS !!!
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            skt.sendto(pakke, (host, port))



        clock.tick(60)

skt.close()
