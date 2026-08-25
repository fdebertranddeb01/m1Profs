""" faire trouver à l'utilisateur un nombre compris entre 0 et 9 (inclus) en lui donnant des indications """
import random


a_trouver = random.randint(0, 9)
essai = -1
while essai != a_trouver:
    essai = int(input("entrez un entier entre 0 et 9 (inclus) : "))
    while essai < 0 or essai > 9:
        essai = int(input("on a dit entre 0 et 9 (inclus) !"))
    if essai < a_trouver:
        print("trop petit")
    elif essai > a_trouver:
        print("trop grand")
print(f"bravo, c'était bien {a_trouver} !")
