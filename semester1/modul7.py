#import
from time import sleep

#7.1 lav en liste og sort den

print("Opgave 7.1 Sort a list\n")
navne = ["Zack", "Xeno", "abe", "Bob", "Aalborg", "Gunar", "Kevin", "Silvan"]
print("The list:", navne)
x = slice(0, 3)
z = slice(5, 8)
navne.sort()
print("3 first:", navne[x], " 3 last:", navne[z])
navne.sort(reverse=True)
print("Reverse:", navne)
# sort string length
def howlong(e):
    return len(e)
navne.sort(key=howlong)
print("String Length:", navne)

#7.2 gæt et tal
"""
print("\n\nOpgave 7.2 Guess a number\n")

number = 10
T = 3
while T > 0:
    print("Try to guess my number, you have", T, "tries left")
    guess = input()
    guess = int(guess)
    print("You guessed:", guess)

    if guess == number:
        print("Correct!")
        exit()
    elif guess < number:
        print("Higher")
    else:
        print("Lower")
    T -= 1
"""
    #7.8
print("\n\nOpgave 7.8\n")
