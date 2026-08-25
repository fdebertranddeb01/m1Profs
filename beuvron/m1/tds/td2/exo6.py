"""Demande un entier n puis n nombres flottants,
affiche la somme et la moyenne de ces nombres"""
n = int(input("entrez le nombre de nombres : "))
s = 0.0
for i in range(n):
    x = float(input(f"entrez le nombre {i + 1} : "))
    s = s + x
print(f"la somme des {n} nombres est : {s}")
if n > 0:
    m = s / n
    print(f"la moyenne des {n} nombres est : {m}")
else:
    print("la moyenne n'est pas définie pour n = 0")