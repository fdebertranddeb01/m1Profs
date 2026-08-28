"""calcule par génération de tous les cas possibles
l'espérance de gain lors d'un lancer unique au jeu 421 """
somme_gains = 0
nbr_de_lancers = 0
# je génère tous les cas possibles : pour chaque dé une valeur de 1 à 6
for d1 in range(1, 7):
    for d2 in range(1, 7):
        for d3 in range(1, 7):
            nbr_de_lancers += 1
            # il est plus facile de faire les test si les dés sont triés
            # comme on ne connait pas les listes durant ce premier tp,
            # on va trier les dés "à la main"
            # en plaçant les valeurs dans min, milieu et max
            if d1 <= d2:
                if d1 <= d3:
                    min = d1
                    if d2 <= d3:
                        milieu = d2
                        max = d3
                    else:
                        milieu = d3
                        max = d2
            else :
                if d2 <= d3:
                    min = d2
                    if d1 <= d3:
                        milieu = d1
                        max = d3
                    else:
                        milieu = d3
                        max = d1
                else:
                    min = d3
                    milieu = d2
                    max = d1
            # inutile : seulement pour vérifier
            if min > milieu or milieu > max:
                raise Exception("Erreur de tri")
            if max == 4 and milieu == 2 and min == 1:
                val = 8
            elif min == 1 and milieu == 1:
                if max == 1:
                    val= 7
                else:
                    val = max
            elif min == milieu and milieu == max:
                val = min
            elif milieu == min+1 and max == min+2:
                val = 2
            else:
                val = 1
            somme_gains += val
print("somme des gains :", somme_gains)
print("nombre de lancers :", nbr_de_lancers)
print("espérance de gain :", somme_gains / nbr_de_lancers)


           