import random

def terningkast(tal):
    antalkast = range(tal)
    list = []
    for n in antalkast:
        list.append(random.randint(1,6))
    return list

uinspillere = int(input("Indtast spillere: "))
uinrunder = int(input("Indtast runder: "))

for n in uinspillere:
    


print(spil)


"""
userinput = int(input())
print("antal kast: ", userinput)
kast = terningkast(userinput)
kast2 = terningkast(userinput)
print("P1:", kast, "P2:", kast2)

op = -1
for n in kast:
    op += 1
    print(op)
    if kast[op] > kast2[op]:
        print("kast")

    else:
        print("kast2")
"""
