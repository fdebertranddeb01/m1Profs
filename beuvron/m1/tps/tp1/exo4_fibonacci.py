"""calcul de la suite de Fibonacci"""

n = int(input("Entrez un entier n (pour calculer Fibonacci(n)): "))
if n == 0:
    courant = 0
else:
    precedent = 0
    courant = 1
    for i in range(1, n):
        poub = precedent
        precedent = courant
        courant = courant + poub
print(f"Fibonacci({n}) = {courant}")