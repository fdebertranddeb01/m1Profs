""" algorithmes de tris """
import random

# reprise du TD sur les listes pour garder ce fichier auto-suffisant
def cree_alea(n : int, xmin : float = 0.0, xmax : float = 10.0) -> list[float]:
    """retourne une liste de n nombres aléatoires compris entre xmin et xmax (inclus)"""
    return [random.uniform(xmin, xmax) for i in range(n)]
    
def est_trie(tab : list[float]) -> bool:
    res = True
    i = 0
    while res and i < len(tab) - 1:
        if tab[i] > tab[i + 1]:
            res = False
        i += 1
    return res

def tri_selection(liste : list[float]) -> None:
    """ tri par sélection """
    n = len(liste)
    for i in range(n-1):
        for j in range(i + 1, n):
            if liste[j] < liste[i]:
                liste[i], liste[j] = liste[j], liste[i]

def min_position(liste : list[float], minpos : int) -> int:
    """ retourne la position du minimum de liste[i:] """
    pos_min = minpos
    for j in range(minpos + 1, len(liste)):
        if liste[j] < liste[pos_min]:
            pos_min = j
    return pos_min

def tri_selection_variante(liste : list[float]) -> None:
    """ tri par sélection en utilisant la fonction min_position """
    n = len(liste)
    for i in range(n-1):
        pos_min = min_position(liste, i)
        liste[i], liste[pos_min] = liste[pos_min], liste[i]

def tri_bulle(liste : list[float]) -> None:
    """ tri à bulle """
    encore = True
    n = len(liste)
    while encore:
        encore = False
        for i in range(n-1):
            if liste[i] > liste[i + 1]:
                liste[i], liste[i + 1] = liste[i + 1], liste[i]
                encore = True

def pos_supp(liste : list[float],x : float) -> int:
    """ retourne la position de la première valeur supérieure à x 
     retourne len(liste) si aucune valeur n'est supérieure à x """
    pos = 0
    while pos < len(liste) and liste[pos] <= x:
        pos += 1
    return pos

def tri_insertion(liste : list[float]) -> list[float]:
    """ tri par insertion"""
    n = len(liste)
    liste_triee = []
    for i in range(n):
        x = liste[i]
        pos = pos_supp(liste_triee, x)
        liste_triee.insert(pos, x)
    return liste_triee

def fusion_crea(liste1 : list[float], liste2 : list[float]) -> list[float]:
    """ fusionne deux listes triées en une nouvelle liste triée """
    res = []
    i = 0
    j = 0
    while i < len(liste1) and j < len(liste2):
        if liste1[i] <= liste2[j]:
            res.append(liste1[i])
            i += 1
        else:
            res.append(liste2[j])
            j += 1
    while i < len(liste1):
        res.append(liste1[i])
        i += 1
    while j < len(liste2):
        res.append(liste2[j])
        j += 1
    return res

def tri_fusion_crea(liste : list[float]) -> list[float]:
    """ tri par fusion avec création systématique de nouvelles listes (très coûteux en mémoire) """
    n = len(liste)
    if n <= 1:
        return liste
    else:
        mid = n // 2
        left = tri_fusion_crea(liste[:mid])
        right = tri_fusion_crea(liste[mid:])
        return fusion_crea(left, right)

def tri_rapide(liste : list[float]) -> None:
    """ tri rapide """
    tri_rapide_borne(liste, 0, len(liste))

def moyenne(liste : list[float],debut : int, fin : int) -> float:
    """ retourne la moyenne des valeurs de la liste entre début (inclus) et fin (inclus) """
    if len(liste) == 0:
        raise ValueError("la liste est vide")
    else:
        return sum(liste[debut:fin]) / (fin - debut)

def tri_rapide_borne(liste : list[float], debut : int, fin : int) -> None:
    """ tri rapide entre debut (inclus) et fin (exclus) """
    if debut < fin - 1:
        pivot = moyenne(liste, debut, fin)
        # on espère que moyenne ~= médiane pour que le pivot soit un bon pivot
        # mais on est sûr que min <= moyenne
        # dans la boucle, le i avancera d'au moins une position
        # ce qui assure que la récursion se termine
        i = debut
        j = fin - 1
        while i <= j:
            if liste[i] <= pivot:
                i += 1
            else:
                liste[i], liste[j] = liste[j], liste[i]
                j -= 1
        tri_rapide_borne(liste, debut, j+1)
        tri_rapide_borne(liste, j + 1, fin)

#-------------------------------- fin du td
#---------- ce qui suit est pour la comparaison des temps d'exécution des tris

# je commence par recopier la fonction temps_calcul de beuvron.utils.temps_exec 
# pour pouvoir l'utiliser dans ce fichier sans avoir à gérer les imports de modules hors du répertoire courant
import time
from multiprocessing import Process,Queue
from typing import Callable

def fonction_mesuree(f : Callable, args: tuple, queue: Queue):
    """ Fonction qui exécute la fonction f avec les arguments args et mesure le temps d'exécution. 
    Les résultats sont envoyés à travers la queue pour être récupérés par le processus principal. 
    On a deux cas suivant que l'exécution se passe bien ou qu'une exception soit levée :
    - Si l'exécution se passe bien, on envoie un tuple ("success", resultat, temps_execution)
    - Si une exception est levée, on envoie un tuple ("error", exception, trace) où trace est la trace de l'exception.
    """
    try:
        debut = time.perf_counter()
        resultat = f(*args)
        fin = time.perf_counter()

        queue.put(("success", resultat, fin - debut))

    except Exception as erreur:
        # On transmet l'exception et sa trace au processus principal
        queue.put(("error", erreur))

def temps_calcul(f:Callable, args:tuple, maxTimeInSeconds:float):
    """ la fonction f va être exécutée dans un processus séparé pour pouvoir imposer un temps maximum d'exécution.
    On utilise une queue pour récupérer le résultat ou l'exception levée par la fonction f
    il y a donc quatre cas possibles :
    - le calcul se passe bien et on récupère le résultat et le temps d'exécution
    - le calcul dépasse le temps maximum et on lève une exception TimeoutError
    - le calcul lève une exception et on la récupère pour la relancer dans le processus principal
    - le processus s'est terminé sans renvoyer de résultat (dans la queue): c'est une erreur interne, on lève une exception RuntimeError"""
    queue = Queue()
    proc = Process(target=fonction_mesuree, args=(f, args, queue))
    proc.start()
    proc.join(timeout=maxTimeInSeconds)
    if proc.is_alive():
        proc.terminate()
        proc.join()
        raise TimeoutError(f"le calcul a dépassé {maxTimeInSeconds} secondes")
    elif queue.empty():
        raise RuntimeError("Le processus s'est terminé sans renvoyer de résultat.")
    else:
        status, *data = queue.get()
        if status == "success":
            resultat, temps_execution = data
            return resultat, temps_execution
        else:  # status == "error"
            erreur = data[0]
            raise erreur

class Trieur:
    def __init__(self,nom : str, fonction : Callable):
        self.nom = nom
        self.fonction = fonction

#--- c'est le résultat qui est sauvegardé dans le sous-process lors du calcul du temps d'exécution,
#  il faut donc que la fonction de tri renvoie le résultat du tri
#  renvoyer la liste triée est inutile et fait "ramer" voire "bugger" le passage par la queue du sub-process
# la seule chose qui nous interresse, c'est de savoir si le trie est correct ou non
# je fais de petit wrapper qui renvoie vrai si le tri est correct false sinon
def tri_selection_wrapper(liste : list[float]) -> bool:
    tri_selection(liste)
    if est_trie(liste):
        return True
    else:
        return False

def tri_selection_variante_wrapper(liste : list[float]) -> bool:
    tri_selection_variante(liste)
    if est_trie(liste):
        return True
    else:
        return False

def tri_bulle_wrapper(liste : list[float]) -> bool:
    tri_bulle(liste)
    if est_trie(liste):
        return True
    else:
        return False

def tri_insertion_wrapper(liste : list[float]) -> bool:
    liste_triee = tri_insertion(liste)
    if est_trie(liste_triee):
        return True
    else:
        return False

def tri_fusion_crea_wrapper(liste : list[float]) -> bool:
    liste_triee = tri_fusion_crea(liste)
    if est_trie(liste_triee):
        return True
    else:
        return False

def tri_rapide_wrapper(liste : list[float]) -> bool:
    tri_rapide(liste)
    if est_trie(liste):
        return True
    else:
        return False

def test_one(trieur : Trieur, taille : int, maxTimeInSeconds : float) -> str:
    """ test un trieur sur une liste de taille donnée et retourne le temps d'exécution et si le tri est correct """ 
    liste = cree_alea(taille)
    try:
        res, duree = temps_calcul(trieur.fonction, (liste,), maxTimeInSeconds)
        if res:
            return str(duree)
        else:
            return "TI"
    except TimeoutError as e:
        return "TO"
    except RecursionError as e:
        return "TD"
    except Exception as e:
        print(f"Erreur inattendue lors du test de {trieur.nom} : {e}")
        return "EI"

def tris_disponibles() -> list[Trieur]:
    """ retourne la liste des tris disponibles """
    return [
        Trieur("tri_selection", tri_selection_wrapper),
        Trieur("tri_selection_variante", tri_selection_variante_wrapper),
        Trieur("tri_bulle", tri_bulle_wrapper),
        Trieur("tri_insertion", tri_insertion_wrapper),
        Trieur("tri_rapide", tri_rapide_wrapper),
        Trieur("tri_fusion", tri_fusion_crea_wrapper)
        ]
    

def premier_test(taille: int,maxTimeInSeconds : float = 1) -> None:
    """ test rapide de tous les tris sur une liste de taille 1000 """
    for trieur in tris_disponibles():
        res = test_one(trieur, 1000, maxTimeInSeconds)
        print(f"{trieur.nom} : {res}")

def test_taille_variable(trieurs : list[Trieur], taille_min : int, croissance : float, nbr_tailles : int, maxTimeInSeconds : float = 1) -> None:
    """ test de tous les tris sur des listes de tailles variables """
    print("val : durée d'exécution en secondes, TO : timeout, TI : tri incorrect, TD : dépassement de profondeur de récursion, EI : erreur inattendue")
    print("taille", end=" ; ")
    for trieur in trieurs:
        print(trieur.nom, end=" ; ")
    print()
    current_taille = taille_min
    tos = [False] * len(trieurs)
    for i in range(nbr_tailles):
        print(f"{current_taille}", end=" ; ")
        for t in range(len(trieurs)):
            if tos[t]:
                res = "TO"
            else:
                trieur = trieurs[t]
                res = test_one(trieur, current_taille, maxTimeInSeconds)
                if res == "TO":
                    tos[t] = True
            print(f"{res}", end=" ; ")
        print()
        current_taille = int(current_taille * croissance)

if __name__ == "__main__":
    # print(est_trie(tri_fusion_crea(cree_alea(10000))))
    # print(tri_fusion_crea_wrapper(cree_alea(10000)))
    # print(test_one(Trieur("tri_fusion", tri_fusion_crea_wrapper), 8000, 30))
    test_taille_variable(tris_disponibles(), 1000, 1.5, 22,5)
    """ vals obtenues sur mon PC
    val : durée d'exécution en secondes, TO : timeout, TI : tri incorrect, TD : dépassement de profondeur de récursion, EI : erreur inattendue
taille ; tri_selection ; tri_selection_variante ; tri_bulle ; tri_insertion ; tri_rapide ; tri_fusion ; 
1000 ; 0.013080600008834153 ; 0.007569200010038912 ; 0.028262399981031194 ; 0.006304100010311231 ; 0.0006879000284243375 ; 0.00077039998723194 ; 
1500 ; 0.028598300006706268 ; 0.016742899984819815 ; 0.068010899994988 ; 0.014289400016423315 ; 0.0011455000203568488 ; 0.0012278000067453831 ; 
2250 ; 0.06987619999563321 ; 0.03700429998571053 ; 0.16133550001541153 ; 0.032478899986017495 ; 0.0016985999827738851 ; 0.0020084999850951135 ; 
3375 ; 0.14993720001075417 ; 0.08446489999187179 ; 0.3561175000213552 ; 0.07379270001547411 ; 0.002486999990651384 ; 0.0029965000285301358 ; 
5062 ; 0.33528080000542104 ; 0.19400879999739118 ; 0.8124466000008397 ; 0.16699170001083985 ; 0.004011799988802522 ; 0.004501899995375425 ; 
7593 ; 0.7563206999911927 ; 0.4343335000157822 ; 1.8667058999999426 ; 0.4015411000000313 ; 0.006719500001054257 ; 0.007090400002198294 ; 
11389 ; 1.7607980000029784 ; 0.9992313999973703 ; 4.30324860001565 ; 0.8693761999893468 ; 0.009551600000122562 ; 0.011430000013206154 ; 
17083 ; 3.984721399989212 ; 2.213165299996035 ; TO ; 2.0423539000039455 ; 0.014877700014039874 ; 0.018549200001871213 ; 
25624 ; TO ; TO ; TO ; 4.674673500005156 ; 0.02226549998158589 ; 0.026707700017141178 ; 
38436 ; TO ; TO ; TO ; TO ; 0.03381779999472201 ; 0.04482159999315627 ; 
57654 ; TO ; TO ; TO ; TO ; 0.05417489999672398 ; 0.0716938000114169 ; 
86481 ; TO ; TO ; TO ; TO ; 0.0862384999927599 ; 0.10801139997784048 ; 
129721 ; TO ; TO ; TO ; TO ; 0.1331789999967441 ; 0.17328649997944012 ; 
194581 ; TO ; TO ; TO ; TO ; 0.20258769998326898 ; 0.2663784000033047 ; 
291871 ; TO ; TO ; TO ; TO ; 0.3172097000060603 ; 0.4045099000213668 ; 
437806 ; TO ; TO ; TO ; TO ; 0.5015251000004355 ; 0.6436386000132188 ; 
656709 ; TO ; TO ; TO ; TO ; 0.817028699995717 ; 1.1028683000185993 ; 
985063 ; TO ; TO ; TO ; TO ; 1.3628266000014264 ; 1.7516389999946114 ; 
1477594 ; TO ; TO ; TO ; TO ; 2.195754799991846 ; 2.8781097999890335 ; 
2216391 ; TO ; TO ; TO ; TO ; 3.579412599996431 ; 4.574909299990395 ; 
3324586 ; TO ; TO ; TO ; TO ; TO ; TO ; 
4986879 ; TO ; TO ; TO ; TO ; TO ; TO ; 
"""
    # pour aller plus loin
    # test_taille_variable(tris_disponibles(), 1000, 1.5, 25,30)
    """ vals obtenues sur mon PC 
    val : durée d'exécution en secondes, TO : timeout, TI : tri incorrect, TD : dépassement de profondeur de récursion, EI : erreur inattendue
taille ; tri_selection ; tri_selection_variante ; tri_bulle ; tri_insertion ; tri_rapide ; tri_fusion ; 
1000 ; 0.013334799994481727 ; 0.00769539998145774 ; 0.029237300012027845 ; 0.006851299986010417 ; 0.0007365999917965382 ; 0.00082230000407435 ; 
1500 ; 0.030046500003663823 ; 0.017095799994422123 ; 0.07268549999571405 ; 0.015540399996098131 ; 0.001135500002419576 ; 0.0013908999972045422 ; 
2250 ; 0.06587479999870993 ; 0.0393231000052765 ; 0.16433189998497255 ; 0.03451129997847602 ; 0.0016911000129766762 ; 0.002103099977830425 ; 
3375 ; 0.15659580001374707 ; 0.08929569998872466 ; 0.3683880000025965 ; 0.07744760002242401 ; 0.0026516000216361135 ; 0.0034623999963514507 ; 
5062 ; 0.34442869998747483 ; 0.19540840000263415 ; 0.838967199990293 ; 0.17558710000594147 ; 0.004056899982970208 ; 0.004674900003010407 ; 
7593 ; 0.8060630999971181 ; 0.44408399998792447 ; 1.936822600022424 ; 0.3953369000228122 ; 0.006357700010994449 ; 0.007309899985557422 ; 
11389 ; 1.8267758000001777 ; 1.008038400002988 ; 4.352478299988434 ; 0.9124015000124928 ; 0.009759100008523092 ; 0.012065799994161353 ; 
17083 ; 4.118821100011701 ; 2.282681499986211 ; 9.773647199996049 ; 2.0063155999814626 ; 0.01421749999281019 ; 0.017178599984617904 ; 
25624 ; 9.123300699982792 ; 5.022644999990007 ; 21.902047500014305 ; 4.81157869999879 ; 0.022185900015756488 ; 0.026865299994824454 ; 
38436 ; 20.887609299999895 ; 11.622542199998861 ; TO ; 10.553949099994497 ; 0.034307099995203316 ; 0.04294449998997152 ; 
57654 ; TO ; 26.136665900005028 ; TO ; 24.267971199995372 ; 0.05343420000281185 ; 0.06813540001166984 ; 
86481 ; TO ; TO ; TO ; TO ; 0.08260379999410361 ; 0.10264620001544245 ; 
129721 ; TO ; TO ; TO ; TO ; 0.13310510001610965 ; 0.16192629997385666 ; 
194581 ; TO ; TO ; TO ; TO ; 0.2020085999974981 ; 0.256048200011719 ; 
291871 ; TO ; TO ; TO ; TO ; 0.3311180000018794 ; 0.45283620001282543 ; 
437806 ; TO ; TO ; TO ; TO ; 0.5311241999734193 ; 0.6511781000008341 ; 
656709 ; TO ; TO ; TO ; TO ; 0.8173355000035372 ; 1.0475149000121746 ; 
985063 ; TO ; TO ; TO ; TO ; 1.3437167000083718 ; 1.73346620000666 ; 
1477594 ; TO ; TO ; TO ; TO ; 2.1856530999939423 ; 2.8601421000203118 ; 
2216391 ; TO ; TO ; TO ; TO ; 3.502603300003102 ; 4.541422300011618 ; 
3324586 ; TO ; TO ; TO ; TO ; 5.630092200008221 ; 7.427810399996815 ; 
4986879 ; TO ; TO ; TO ; TO ; 9.109421099972678 ; 12.161148200015305 ; 
7480318 ; TO ; TO ; TO ; TO ; 14.822357999975793 ; 19.32570690001012 ; 
11220477 ; TO ; TO ; TO ; TO ; 23.632594900002005 ; TO ; 
16830715 ; TO ; TO ; TO ; TO ; TO ; TO ; 
"""
