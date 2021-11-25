# Import lib
import time
import pygame
import socket as S

# Make socket
#host = "10.31.132.155" #slotpi
host = "10.31.129.237"
port = 3000
skt = S.socket(S.AF_INET, S.SOCK_DGRAM)

# Py game ssetup
pygame.init()
screenSize = (800, 700)
screen = pygame.display.set_mode(screenSize)
pygame.display.set_caption("square move")
done = False
clock = pygame.time.Clock()

# Send function
def SEND(tast):
    skt.sendto(tast, (host, port))

# Send data
pakke = "hejsa"
pakke = pakke.encode("UTF-8")

W = b'W'
A = b'A'
S = b'S'
D = b'D'

WA = b'WA'
WD = b'WD'
SA = b'SA'
SD = b'SD'

nul = b'0'

# Create graphics
pygame.Rect(0, 0, 75, 75)

while not done:
        for event in pygame.event.get():
                # !!! GET EVENT !!!
                if event.type == pygame.QUIT:
                        done = True
        # !!! GET KEYS !!!
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            skt.sendto(pakke, (host, port))

        # W Frem
        if (pressed[pygame.K_w] and not pressed[pygame.K_a]) and (pressed[pygame.K_w] and not pressed[pygame.K_d]):
            SEND(W)
        elif pressed[pygame.K_w] and pressed[pygame.K_a]:
            SEND(WA)
        elif pressed[pygame.K_w] and pressed[pygame.K_d]:
            SEND(WD)
        else:
            pass

        # A Venstre
        if (pressed[pygame.K_a] and not pressed[pygame.K_w]) and (pressed[pygame.K_a] and not pressed[pygame.K_s]):
            SEND(A)
        # D Højre
        if (pressed[pygame.K_d] and not pressed[pygame.K_w]) and (pressed[pygame.K_d] and not pressed[pygame.K_s]):
            SEND(D)
        # S Tilbage
        if (pressed[pygame.K_s] and not pressed[pygame.K_a]) and (pressed[pygame.K_s] and not pressed[pygame.K_d]):
            SEND(S)
        elif pressed[pygame.K_s] and pressed[pygame.K_a]:
            SEND(SA)
        elif pressed[pygame.K_s] and pressed[pygame.K_d]:
            SEND(SD)
        else:
            pass

        # Send nul hvis ingen knap er trykket
        if pressed[pygame.K_w] or pressed[pygame.K_a] or pressed[pygame.K_s] or pressed[pygame.K_d]:
            pass
        else:
            SEND(nul)

        # Update graphic
        if pressed[pygame.K_w]:
            pass
        if pressed[pygame.K_a]:
            pass
        if pressed[pygame.K_s]:
            pass
        if pressed[pygame.K_d]:
            pass




        pygame.display.flip()
        clock.tick(60)

skt.close()
