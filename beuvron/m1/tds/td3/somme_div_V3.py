"""calcule la somme des diviseurs d'un entier naturel n (n exclu)
version 3 : 
  imaginons que i divise n, alors n/i divise aussi n, donc on peut se contenter de tester les entiers de 1 à ~sqrt(n)
  pour rester dans le domaine des entiers, il vaut mieux tester i*i <= n, plutôt que i <= sqrt(n)
  En réfléchissant un peu, il faut faire attention aux carrés parfaits : 
  si n = 36, alors 6 divise 36, mais 36/6 = 6, donc on ne doit pas compter 6 deux fois.
  Dernier cas particulier : pour 1, on est dans le cas unique ou n*n = n. 
  Sans précaution on aurait sommeDiv(1) = 1 ce qui est faux puisque l'on veut les diviseurs n exclu.
"""
n = int(input("entrez un entier naturel : "))
if n == 1:
    somme = 0
else:
    somme = 1
    i = 2
    while i * i <= n:
        if n % i == 0:
            somme = somme + i
        if i * i != n:
            somme = somme + n // i
    i = i + 1
print(f"la somme des diviseurs de {n} est {somme}")
