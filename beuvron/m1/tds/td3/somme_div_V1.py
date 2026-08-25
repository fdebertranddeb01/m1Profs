"""calcule la somme des diviseurs d'un entier naturel n (n exclu)
version 1 : on teste beaucoup trop de nombre : 
on teste tous les entiers de 1 à n-1, alors que les diviseurs sont au plus n/2
"""
n = int(input("entrez un entier naturel : "))
somme = 0
for i in range(1, n):
    if n % i == 0:
        somme = somme + i
print(f"la somme des diviseurs de {n} est {somme}")
