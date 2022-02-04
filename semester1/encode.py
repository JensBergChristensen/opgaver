
# 12.1
"""
tal = input("Indtast: ")
bi = bin(tal)
hex = format(tal, "x")
print("Binary: ", bi)
print("Hex: ", hex)
"""

# 12.2
seatning = input("Indtast sætning")
kompress = seatning.encode(encoding = 'UTF-8')
print("Sætning: ", seatning)
print("Encoded: ", kompress)
