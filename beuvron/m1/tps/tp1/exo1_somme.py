""" déjà vu en td somme des entiers de 1 à n"""
n = int(input("Entrez un entier n : "))
somme = 0
for i in range(1, n + 1):
    somme = somme + i
print("La somme des entiers de 1 à", n, "est", somme)
