"""calculer la somme des entiers de 1 à n avec une boucle for"""
n = int(input("entrez un entier : "))
s = 0
for i in range(1, n + 1):
    s = s + i
print(f"la somme des entiers de 1 à {n} est : {s}")
