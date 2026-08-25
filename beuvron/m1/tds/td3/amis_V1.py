"""affiche toutes les paires de nombres amis inférieurs à 1000
Version 1 : doublement inefficace : 
  . on calcule les sommes des diviseurs avec la V1 de somme_div
  . on teste tous les couples (a,b) avec a < 1000 et b < 1000 
  ==> on a les couples "en double" : (220,284) et (284,220) (voir V2 pour corriger ce petit problème)

  Note : on n'a pas vu les fonctions, donc pour calculer la somme des diviseurs, on fait du copier/coller en renommant les variables pour ne pas avoir de conflit entre les deux calculs de sommes des diviseurs.
  ==> ce sera l'occasion de voir (dans un td ultérieur) comment utiliser les fonctions rend le code beaucoup plus lisible et plus facile à maintenir.
"""
for a in range(1, 1000):
    for b in range(1, 1000):
        # comme le calcul de somme_a ne dépend pas de b, on pourrait le sortir de la boucle sur b
        # mais ici on ne l'a pas fait puisque l'on veut la version la plus inéfficace. On le fera dans la V2.
        somme_a = 0
        for i in range(1, a):
            if a % i == 0:
                somme_a = somme_a + i
        somme_b = 0
        for j in range(1, b):
            if b % j == 0:
                somme_b = somme_b + j
        if somme_a == b and somme_b == a:
            print(f"({a},{b}) sont amis")
