""" quelques exercices sur les listes """

import random

def cree_liste1(n : int) -> list[float]:
    """renvoie une liste de n zéros
    avec append (vu en cours)"""
    l = []
    for i in range(n):
        l.append(0)
    return l

def cree_liste2(n : int) -> list[float]:
    """renvoie une liste de n zéros
    avec compréhension de liste ("survolée" en cours)"""
    return [0.0 for i in range(n)]

def cree_liste3(n : int) -> list[float]:
    """renvoie une liste de n zéros
    avec multiplication d'une liste (pas vu en cours)"""
    return [0.0] * n

def cree_liste(n : int,init : float = 0.0) -> list[float]:
    """renvoie une liste de n éléments tous égaux à init
    avec compréhension de liste"""
    return [init for i in range(n)]

def test_cree_liste() -> None:
    print("appel sans founir le paramètre init qui prend sa valeur par défaut:")
    print("n est passé en positionnel (c'est le plus courant):")
    print("cree_liste(5):", cree_liste(5))
    print("appel en fournissant n en positionnel (courant) et le paramètre init en positionnel (pas très courant, mais possible):")
    print("cree_liste(5,2.0):", cree_liste(5,2.0))
    print("appel en fournissant le paramètre n en nommé (pas courant, mais possible) et init en nommé:")
    print("cree_liste(n=4,init=3.0):", cree_liste(n=4,init=3.0))
    print("lorsque les paramètres sont nommés, on peut les fournir dans n'importe quel ordre:")
    print("cree_liste(init=4.0,n=3):", cree_liste(init=4.0,n=3))
    print("par contre, on ne peut pas fournir un paramètre positionnel après un paramètre nommé (ça ne marche pas):")
    print("cree_liste(init=4.0,3):", " Erreur")
    print("cree_liste(n=3,4.0):", " Erreur")

def cree_alea(n : int, xmin : float = 0.0, xmax : float = 10.0) -> list[float]:
    """retourne une liste de n nombres aléatoires compris entre xmin et xmax (inclus)"""
    return [random.uniform(xmin, xmax) for i in range(n)]

def entree_notes(n : int) -> list[float]:
    """retourne une liste de n nombres aléatoires compris entre 0 et 10"""
    notes = []
    for i in range(n):
        note = float(input(f"Entrez la note {i+1} (entre 0 et 10 inclus): "))
        while note < 0 or note > 10:
            print("Erreur: la note doit être comprise entre 0 et 10 inclus")
            note = float(input(f"Entrez la note {i+1} (entre 0 et 10 inclus): "))
        notes.append(note)
    return notes

def moyenne(notes : list[float]) -> float:
    """renvoie la moyenne des notes (sans utiliser de fonction de haut niveau sum...)"""
    somme = 0.0
    for note in notes:
        somme += note
    return somme / len(notes)

def max_et_posmax(notes : list[float]) -> tuple[float,int]:
    """renvoie le maximum et la position du maximum dans la liste"""
    if len(notes) == 0:
        raise ValueError("La liste est vide")
    max_note = notes[0]
    pos_max = 0
    for i in range(1, len(notes)):
        if notes[i] > max_note:
            max_note = notes[i]
            pos_max = i
    return max_note, pos_max

def test1() -> None:
    n = int(input("Entrez le nombre de notes: "))
    notes = entree_notes(n)
    print("Les notes saisies sont:", notes)
    print("La moyenne des notes est:", moyenne(notes))
    max_note, pos_max = max_et_posmax(notes)
    print(f"La note maximale est {max_note} à la position {pos_max}")

def arrondir_notes1(notes : list[float]) -> list[int]:
    """renvoie une nouvelle liste avec les notes arrondies à l'entier le plus proche"""
    notes_arrondies = []
    for note in notes:
        notes_arrondies.append(round(note))
    return notes_arrondies

def arrondir_notes(notes : list[float]) -> list[int]:
    """renvoie une nouvelle liste avec les notes arrondies à l'entier le plus proche
    avec compréhension de liste"""
    return [round(note) for note in notes]

def histogramme(notes : list[float]) -> list[int]:
    """affiche un histogramme des notes arrondies à l'entier le plus proche"""
    notes_arrondies = arrondir_notes(notes)
    res = [0] * 11
    for note in notes_arrondies:
        res[note] += 1
    return res

def afficher_histogramme_horizontal(histo : list[int]) -> str:
    """représntation textuelle  d'un histogramme en horizontal"""
    result = ""
    for i in range(len(histo)):
        result += f"{i}: {'*' * histo[i]}\n"
    return result

def afficher_histogramme_vertical(histo : list[int]) -> str:
    """représntation textuelle  d'un histogramme en vertical"""
    max_h,p = max_et_posmax(histo)
    result = ""
    for i in range(max_h, 0, -1):
        for j in range(len(histo)):
            if histo[j] >= i:
                result += "* "
            else:
                result += "  "
        result += "\n"
    result += " ".join(str(i) for i in range(len(histo))) + "\n"
    return result

if __name__ == "__main__":
    test_cree_liste()
    test1()