"""affiche une croix d'étoiles"""
taille = int(input("Entrez la taille de la croix : "))
for ligne in range(taille):
    for col in range(taille):
        if col == ligne or col == taille - ligne - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
