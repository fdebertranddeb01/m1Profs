"""calculer n!"""
n = int(input("entrez un entier : "))
if n < 0:
    print("n! n'est pas défini pour les entiers négatifs")
else:
    f = 1
    for i in range(1, n + 1):
        f = f * i
    print(f"{n}! = {f}")