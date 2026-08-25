"""calcule la somme des diviseurs d'un entier naturel n (n exclu)
version 2 : on teste moins de nombre que la V1 puisque l'on s'arrete à n/2,
mais on teste encore trop de nombres (voir V3)
"""
n = int(input("entrez un entier naturel : "))
somme = 0
for i in range(1, n // 2 + 1):
    if n % i == 0:
        somme = somme + i
print(f"la somme des diviseurs de {n} est {somme}")
