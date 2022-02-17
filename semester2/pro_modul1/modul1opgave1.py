import math
import statistics

print("Opgave 1:")
opgave1 = -3
while True:
    opgave1 = opgave1 + 3
    if opgave1 != 66:
        print(opgave1)
    if opgave1 == 99:
        break

print("\nOpgave 2:")

opgave2 = list(range(0,102,3))
for n in opgave2:
    print(n)

print("\nOpgave3:")

opgave3 = [13, 20, -5, 0, 5, 1, 8, 3, 12, 2]
small = opgave3[0]
for a in opgave3:
    if a < small:
        small = a
print(small)

print("\nOpgave4:")
opgave4 = statistics.median(opgave3)
print(opgave4)

print("\nOpgave5:")
def cut10(x):
    del x[:10]
    return x
cut10(opgave2)
print(opgave2)

print("\nOpgave6:")
print("wat")

print("\nOpgave7:")
def add1(x):
    x = x + 1
    return x
tal = 77
tal2 = add1(tal)
print(tal2)

print("\nOpgave8")
di = {
"age":{
    "john":{
        "plads0":"nul",
        "plads1":"et",
        "plads2":"to",
        2:42,
        },
    "peter":{
        2:"Hej med dig"
        }
    }
}
print(di["age"]["john"][2])

print("\nOpgave9")
