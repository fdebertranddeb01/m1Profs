"""affiche toutes les paires de nombres amis inférieurs à 1000
Version 2 : correction du problème des couples en double et utilisation de la V3 de somme_div
  . on calcule les sommes des diviseurs avec la V3 de somme_div
  . on teste tous les couples (a,b) avec a <= b < 1000 (voir amis_V3 pour se rendre compte que c'est inutile !)

  Note1 : on fait a <= b < 1000 considérant qu'un nombre peut être ami avec lui-même 
  (exemple : 6 est ami avec 6 puisque la somme de ses diviseurs propres est 6)

  Note : on n'a pas vu les fonctions, donc pour calculer la somme des diviseurs, on fait du copier/coller en renommant les variables pour ne pas avoir de conflit entre les deux calculs de sommes des diviseurs.
  ==> ce sera l'occasion de voir (dans un td ultérieur) comment utiliser les fonctions rend le code beaucoup plus lisible et plus facile à maintenir.
"""
for a in range(1, 1000):
    if a == 1:
        somme_a = 0
    else:
        somme_a = 1
        i = 2
        while i * i <= a:
            if a % i == 0:
                somme_a = somme_a + i
                if i * i != a:
                    somme_a = somme_a + a // i
            i = i + 1
    for b in range(a, 1000):
        if b == 1:
            somme_b = 0
        else:
            somme_b = 1
            j = 2
            while j * j <= b:
                if b % j == 0:
                    somme_b = somme_b + j
                    if j * j != b:
                        somme_b = somme_b + b // j
                j = j + 1
        if somme_a == b and somme_b == a:
            print(f"({a},{b}) sont amis")
