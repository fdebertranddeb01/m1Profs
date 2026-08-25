"""demander un entier et s'assurer qu'il est compris entre 1 et 20 (inclus)"""
n = int(input("entrez un entier entre 1 et 20 (inclus) : "))
while n < 1 or n > 20:
    n = int(input("entrez un entier entre 1 et 20 (inclus) : "))
print(f"vous avez entré : {n}")
