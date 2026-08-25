"""afficher un carré de n lignes et n colonnes d'étoiles"""
n = int(input("entrez le nombre de lignes et de colonnes : "))
for i in range(n):
    for j in range(n):
        print("*", end="")
    print()
