# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 20:39:04 2018

Eksempler med lister og exception handling

Dette program beder brugeren lave en liste.

Derefter skal brugeren finde elementer fra listen med indeksering.

Hvis indeks ikke passer med listen, skal programmet reagere med
en exception

@author: HTH
"""

def checkint():
    run = True
    while run:
        tal = input()
        if tal == "q" or tal == "Q":
            exit()
        try:
            inttal = int(tal)
            run = False
        except ValueError:
            print("Giv mig et tal, tak :)")
    return inttal

# Beder brugeren om input om hvor mange elementer listen skal have
antalElementer = checkint("Hvor mange elementer skal listen have? ")

elementListe = []

# Brugeren skal fylde listen op med elementer
for elementIndeks in range(antalElementer):
    element = input("Indtast element nr. " + str(elementIndeks) +" som skal i listen: ")
    elementListe.append(element)

# Brugeren skal nu finde elementer frem fra listen
while True:
    elementIndeks = checkint("Vælg indeks fra listen, mellem 0 og " + str(antalElementer-1) + ". Vælg q for at stoppe. ")
    if elementIndeks == None:
        break
    try:
        element = elementListe[elementIndeks]
    except IndexError:
        print("Indeks " + str(elementIndeks) + " er ikke i listen.")
    else:
        print("Element på plads " + str(elementIndeks) + " i listen er " + str(elementListe[int(elementIndeks)]))
