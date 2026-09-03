""" petites classes pour gérer une liste de morceaux de musique """

class Morceau:
    def __init__(self, titre : str, duree : float):
        self._titre = titre
        if duree < 0:
            raise ValueError("La durée ne peut pas être négative.")
        self._duree = duree

    def __str__(self) -> str:
        return f"Morceau(titre='{self._titre}', duree={self._duree})"

    @property
    def titre(self) -> str:
        return self._titre

    @property
    def duree(self) -> float:
        return self._duree

    @duree.setter
    def duree(self, value : float) -> None:
        if value < 0:
            raise ValueError("La durée ne peut pas être négative.")
        self._duree = value

class Playlist:
    def __init__(self, auteur : str,morceaux : list[Morceau] = None):
        # si l'on initialise par défaut la liste des morceaux à [], 
        # cela crée une liste partagée entre toutes les instances de Playlist,
        # ce qui n'est pas souhaitable. Il vaut mieux utiliser None et créer une nouvelle liste dans le constructeur.
        # voir un petit exemple fonctionnelci-dessous pour comprendre le problème
        self._auteur = auteur
        if morceaux is None:
            self._morceaux = []
        else:
            self._morceaux = morceaux

    @property
    def auteur(self) -> str:
        return self._auteur

    @property
    def morceaux(self) -> list[Morceau]:
        return self._morceaux

    def ajouter_morceau(self, morceau : Morceau) -> None:
        self._morceaux.append(morceau)

    def trouve_par_duree(self, duree : float) -> Morceau:
        """trouve le morceau dont la durée est la plus proche de la durée donnée"""
        if not self.morceaux:
            raise ValueError("La playlist est vide.")
        morceau_proche = self.morceaux[0]
        for morceau in self.morceaux:
            if abs(morceau.duree - duree) < abs(morceau_proche.duree - duree):
                morceau_proche = morceau
        return morceau_proche

    
    def __str__(self) -> str:
        """ l'auteur en entête puis la liste des morceaux, chacun sur une ligne avec le titre et la durée """
        result = f"Playlist(auteur='{self._auteur}', morceaux=[\n"
        for m in range(len(self.morceaux)-1):
            result += f"  {self.morceaux[m]}\n"
        if self.morceaux:
            result += f"  {self.morceaux[-1]}\n"
        result += "])"
        # même chose, mais avec un join
        # result = f"Playlist(auteur='{self._auteur}', morceaux=["
        # result += ", ".join(str(m) for m in self.morceaux)
        # result += "])" 
        return result

def probleme_liste_partagee(liste : list[int] = []) -> None:
    """ montre le problème de la liste partagée entre toutes les instances de Playlist """
    liste.append(len(liste))
    print(f"Liste actuelle : {liste}")

def test_probleme_liste_partagee() -> None:
    print("Test du problème de la liste partagée entre toutes les appels de la fonction")
    probleme_liste_partagee()
    probleme_liste_partagee()
    probleme_liste_partagee()

def test1() -> None:
    # test de la classe Morceau
    m1 = Morceau("Trop super", 3.5)
    m2 = Morceau("Max bien", 4.0)
    print(m1)
    print(m2)
    # test de la classe Playlist
    p = Playlist("Toto")
    p.ajouter_morceau(m1)
    p.ajouter_morceau(m2)
    print(p)
    # test de la méthode trouve_par_duree
    duree_test = 3.8
    morceau_proche = p.trouve_par_duree(duree_test)
    print(f"Le morceau le plus proche de {duree_test} est : {morceau_proche}")

if __name__ == "__main__":
    test_probleme_liste_partagee()
    test1()