"""calculer la somme des entiers de 1 à n avec une boucle while,
sans utiliser de variable supplémentaire, mais en perdant le nombre entré"""
n = int(input("entrez un entier : "))
s = 0
while n > 0:
    s = s + n
    n = n - 1
print("avec cette méthode, la somme est correcte, mais le nombre entré est perdu")
print(f"la somme des entiers est : {s}")
