"""calculer la somme des entiers de 1 à n avec une boucle while"""
n = int(input("entrez un entier : "))
s = 0
i = 1
while i <= n:
    s = s + i
    i = i + 1
print(f"la somme des entiers de 1 à {n} est : {s}")
