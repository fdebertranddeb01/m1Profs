"""affiche un triangle d'étoiles"""
taille = int(input("Entrez la taille du triangle : "))
for ligne in range(taille):
    for esp in range(taille - ligne - 1):
        print(" ", end="")
    for etoiles in range(2 * ligne + 1):
        print("*", end="")
    print()
