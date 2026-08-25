""" faire trouver à l'utilisateur un nombre compris entre 0 et 9 (inclus) en lui donnant des indications  """
import random


a_trouver = random.randint(0, 9)
essai = -1
min = 0
max = 9
while essai != a_trouver:
    essai = int(input("entrez un entier entre 0 et 9 (inclus) : "))
    while essai < 0 or essai > 9:
        essai = int(input("on a dit entre 0 et 9 (inclus) !"))
    if essai < a_trouver:
        if essai < min:
            print(f"Ridicule : vous savez déjà que le nombre est plus grand (ou égal à) {min} !")
        else:
            print("trop petit")
            min = essai + 1
    elif essai > a_trouver:
        if essai > max:
            print(f"Ridicule : vous savez déjà que le nombre est plus petit (ou égal à) {max} !")
        else:
            print("trop grand")
            max = essai - 1
print(f"bravo, c'était bien {a_trouver} !")
