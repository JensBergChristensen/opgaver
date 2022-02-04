# forskellige loops og ting
#import
from time import sleep

"""
r = range(40)
for n in r:
    print(n, end=" ")

li = list(range(40))
print(li)

#printer hverty 5 tal
h = list(range(0, 100, 5))
print(h)

-----------------------------------
# er a større end b eller er de lige?
a = 11
b = 11

if a > b:
    print("a er større end b")
elif b > a:
    print("b er større end a")
else:
    print("a og b er lige")
----------------------------------
"""

karakter = -3
karakterliste = list(range(-3, 12))
for n in karakterliste:
    karakter += 1
    if karakter <= -3:
        print("F")
    elif karakter <= 0:
        print("Fx")
    elif karakter <= 2:
        print("E")
    elif karakter <= 4:
        print("D")
    elif karakter <= 7:
        print("C")
    elif karakter <= 10:
        print("B")
    elif karakter <= 12:
        print("A")
    else:
        print("ERROR")
