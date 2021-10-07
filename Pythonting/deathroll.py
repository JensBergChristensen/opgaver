# deathroll program
from random import randrange
from time import sleep

pc = 1
you = input("Enter a number to roll: ")
you = int(you)
you = randrange(0, you)
print("You rolled:", you)
while True:
    pc = randrange(0, you)
    print("pc rolled:", pc)
    if pc == 0:
        print("YOU WON")
        exit()
    sleep(0.5)
    you = randrange(0, pc)
    print("You rolled:", you)
    if you == 0:
        print("YOU LOST")
        exit()
    sleep(0.5)
