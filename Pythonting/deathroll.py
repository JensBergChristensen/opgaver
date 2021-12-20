# deathroll program
from random import randrange
from time import sleep

pc = 1
you = input("Enter a number to roll: ")
you = int(you)
you = randrange(1, you)
print("You rolled:", you)
while True:
    pc = randrange(1, you)
    print("pc rolled:", pc)
    if pc == 1:
        print("YOU WON")
        exit()
    sleep(0.5)
    you = randrange(1, pc)
    print("You rolled:", you)
    if you == 1:
        print("YOU LOST")
        exit()
    sleep(0.5)
