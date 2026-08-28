""" comparaison des temps de calcul des nombres amis suivant les 3 versions"""

# la recherche des modules hors du répertoire courant semble une vrai galère en python
# en désespoir de cause, j'ai copié le module beuvron.utils.temps_exec.py dans le répertoire courant 
# pour pouvoir l'importer

from temps_exec import temps_calcul

# je remets les diverses versions de somme_div sous forme de fonctions pour pouvoir les tester avec le temps de calcul
def somme_div_V1(n : int) -> int:
    somme = 0
    for i in range(1, n):
        if n % i == 0:
            somme = somme + i
    return somme

def somme_div_V2(n : int) -> int:
    somme = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            somme = somme + i
    return somme

def somme_div_V3(n : int) -> int:
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
    return somme

# pareil pour les nombres amis mais je ne renvoie que le nombre de couples pour ne pas avoir à afficher tous les couples
# (ce qui prend du temps)
def amis_V1(nmax : int) -> int:
    count = 0
    for a in range(1, nmax):
        for b in range(1, nmax):
            somme_a = somme_div_V1(a)
            somme_b = somme_div_V1(b)
            if somme_a == b and somme_b == a:
                count += 1
    return count

def amis_V2(nmax : int) -> int:
    count = 0
    for a in range(1, nmax):
        somme_a = somme_div_V3(a)
        for b in range(a, nmax):
            somme_b = somme_div_V3(b)
            if somme_a == b and somme_b == a:
                count += 1
    return count

def amis_V3(nmax : int) -> int:
    count = 0
    for a in range(2, nmax):
        somme_a = somme_div_V3(a)
        if somme_a <= a:
            b = somme_a
            somme_b = somme_div_V3(b)
            if somme_b == a:
                count += 1
    return count

def test_temps_amis_v3(nmax,maxTimeInSeconds = 1):
    try :
        res,duree = temps_calcul(amis_V3, (nmax,), maxTimeInSeconds)
        print(f"temps de calcul des nombres amis V3 pour nmax = {nmax} : {duree:.3f} secondes")
    except TimeoutError as e:
        print(f"calcul des nombres amis V3 pour nmax = {nmax} a échoué : {e}")

def test_temps_amis_v1(nmax,maxTimeInSeconds = 1):
    try :
        res,duree = temps_calcul(amis_V1, (nmax,), maxTimeInSeconds)
        print(f"temps de calcul des nombres amis V1 pour nmax = {nmax} : {duree:.3f} secondes")
    except TimeoutError as e:
        print(f"calcul des nombres amis pour nmax = {nmax} a échoué : {e}")

def test_temps_amis_v2(nmax,maxTimeInSeconds = 1):
    try :
        res,duree = temps_calcul(amis_V2, (nmax,), maxTimeInSeconds)
        print(f"temps de calcul des nombres amis pour nmax = {nmax} : {duree:.3f} secondes")
    except TimeoutError as e:
        print(f"calcul des nombres amis pour nmax = {nmax} a échoué : {e}")

def affiche_tableau_temps_calcul(maxTimeInSeconds = 1):
    print(f"temps de calcul des nombres amis pour divers nmax (timeout (TO) : {maxTimeInSeconds} secondes)")
    print(f"nmax : nbrAmis : --V1- --V2- --V3-")
    v1ok = True
    v2ok = True
    v3ok = True
    for nmax in [2**i for i in range(7,15)]:
        print(f"{nmax:5}", end=": ")
        print(f"{amis_V3(nmax):7}", end=" : ")
        if v1ok:
            try :
                res,duree_V1 = temps_calcul(amis_V1, (nmax,), maxTimeInSeconds)
                print(f"{duree_V1:5.3f}", end=" ")
            except TimeoutError as e:
                v1ok = False
                print("--TO-", end=" ")
        else:
            print("--TO-", end=" ")
        if v2ok:
            try :
                res,duree_V2 = temps_calcul(amis_V2, (nmax,), maxTimeInSeconds)
                print(f"{duree_V2:5.3f}", end=" ")
            except TimeoutError as e:
                v2ok = False
                print("--TO-", end=" ")
        else:
            print("--TO-", end=" ")
        if v3ok:
            try :
                res,duree_V3 = temps_calcul(amis_V3, (nmax,), maxTimeInSeconds)
                print(f"{duree_V3:5.3f}", end=" ")
            except TimeoutError as e:
                v3ok = False
                print("--TO-", end=" ")
        else:
            print("--TO-", end=" ")
        print("")

if __name__ == "__main__":
    #test_temps_calcul(1)
    # print(amis_V3(1000))
    #test_temps_amis_v1(1000,30)
    #test_temps_amis_v3(1000,30)
    affiche_tableau_temps_calcul(5)
    """ temps obtenu sur mon PC :
temps de calcul des nombres amis pour divers nmax (timeout (TO) : 5 secondes)
nmax : nbrAmis : --V1- --V2- --V3-
  128:       2 : 0.050 0.007 0.000 
  256:       2 : 0.535 0.032 0.000 
  512:       4 : 2.560 0.114 0.000 
 1024:       4 : --TO- 0.497 0.001 
 2048:       5 : --TO- 2.699 0.003 
 4096:       6 : --TO- --TO- 0.009 
 8192:       9 : --TO- --TO- 0.026 
16384:      11 : --TO- --TO- 0.063 
    """
