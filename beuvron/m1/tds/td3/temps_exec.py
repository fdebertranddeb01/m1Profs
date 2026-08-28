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

def calcul_exponentiel(n : int) -> int:
    resultat = 0
    for i in range(2 ** n):
        resultat += i
    return resultat

def fonction_sans_resultat() -> None:
    return None

def erreur_immediate() -> None:
    raise ValueError("Erreur immédiate pour tester la gestion des exceptions.")

def test_temps_calcul(maxTimeInSeconds : float = 1) -> None:
    for nmax in range(20, 30):
        try :
            res,duree = temps_calcul(calcul_exponentiel, (nmax,), maxTimeInSeconds)
            print(f"temps de calcul de l'exponentiel pour n = {nmax} : {duree:.3f} secondes : résultat = {res}")
        except TimeoutError as e:
            print(f"calcul de l'exponentiel pour n = {nmax} a échoué : {e}")
        except Exception as e:
            print(f"calcul de l'exponentiel pour n = {nmax} a échoué avec une exception : {e}")
    res,duree = temps_calcul(fonction_sans_resultat, (), maxTimeInSeconds)
    print(f"temps de calcul de la fonction sans résultat : {duree:.3f} secondes : résultat = {res}")
    try:
        res,duree = temps_calcul(erreur_immediate, (), maxTimeInSeconds)
    except Exception as e:
        print(f"calcul de la fonction avec erreur : type : {type(e)} ; message : {e}")


if __name__ == "__main__":
    test_temps_calcul()