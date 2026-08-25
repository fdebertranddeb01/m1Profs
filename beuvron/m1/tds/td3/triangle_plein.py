"""afficher un triangle plein de n lignes d'étoiles"""
n = int(input("entrez le nombre de lignes : "))
for i in range(n):
    for j in range(n-i-1):
        print(".", end="")
    for j in range(2*i+1):
        print("*", end="")
    print()
