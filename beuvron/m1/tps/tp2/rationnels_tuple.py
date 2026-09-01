""" création d'un type rationnel avec un tuple """

def pgcd(a : int, b : int) -> int:
    """ calcule le pgcd de a et b """
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a

def ppcm(a : int, b : int) -> int:
    """ calcule le ppcm de a et b """
    return a * (b // pgcd(a, b))

def normalise(r : tuple[int, int]) -> tuple[int, int]:
    """ normalise un rationnel """
    num, den = r
    if den < 0:
        num, den = -num, -den
    d = pgcd(num, den)
    return (num // d, den // d)

def cree(num : int, den : int) -> tuple[int, int]:
    """ crée un rationnel sous forme de tuple (num, den) """
    if den == 0:
        raise ValueError("Le dénominateur ne peut pas être nul.")
    r = (num, den)
    return normalise(r)

def entree(message : str = "Entrez un rationnel : ") -> tuple[int, int]:
    """ demande à l'utilisateur de saisir un rationnel """
    print(message,end="")
    num = int(input("Entrez le numérateur : "))
    den = int(input("Entrez le dénominateur : "))
    return cree(num, den)

def text(r : tuple[int, int]) -> str:
    """ retourne une représentation sous forme de chaîne du rationnel """
    return f"{r[0]}/{r[1]}"

def test1() -> None:
    """ test de la fonction cree """
    r = cree(2, 4)
    assert r == (1, 2), f"Erreur : {r} != (1, 2)"
    r = cree(-2, 4)
    assert r == (-1, 2), f"Erreur : {r} != (-1, 2)"
    r = cree(2, -4)
    assert r == (-1, 2), f"Erreur : {r} != (-1, 2)"
    r = cree(-2, -4)
    assert r == (1, 2), f"Erreur : {r} != (1, 2)"
    n = int(input("Entrez un numérateur pour le test : "))
    d = int(input("Entrez un dénominateur pour le test : "))
    r = cree(n, d)
    print(f"Le rationnel saisi (normalisé) est : {text(r)}")

def plus1(r1 : tuple[int, int], r2 : tuple[int, int]) -> tuple[int, int]:
    """ additionne deux rationnels directement sans simplification """
    num = r1[0] * r2[1] + r2[0] * r1[1]
    den = r1[1] * r2[1]
    return cree(num, den)

def plus(r1 : tuple[int, int], r2 : tuple[int, int]) -> tuple[int, int]:
    """ additionne deux rationnels avec simplification par pgcd et ppcm pour ne pas utiliser des entiers inutilement grands 
    non demandé aux éttudiants"""
    pg = pgcd(r1[1], r2[1])
    pp = r1[1] // pg * r2[1]
    num = r1[0] // pg + r2[0] // pg
    den = pp
    return cree(num, den)

def test2() -> None:
    """ test de la fonction plus """
    r1 = cree(1, 2)
    r2 = cree(1, 3)
    r3 = plus(r1, r2)
    assert r3 == (5, 6), f"Erreur : {r3} != (5, 6)"
    print("test de la fonction plus")
    r1 = entree("Entrez le premier rationnel : ")
    r2 = entree("Entrez le second rationnel : ")
    r3 = plus(r1, r2)
    print(f"{text(r1)} + {text(r2)} = {text(r3)}")

def opp(r : tuple[int, int]) -> tuple[int, int]:
    """ retourne l'opposé d'un rationnel """
    return cree(-r[0], r[1])

def moins(r1 : tuple[int, int], r2 : tuple[int, int]) -> tuple[int, int]:
    """ soustrait deux rationnels """
    return plus(r1, opp(r2))

def mult1(r1 : tuple[int, int], r2 : tuple[int, int]) -> tuple[int, int]:
    """ multiplie deux rationnels """
    num = r1[0] * r2[0]
    den = r1[1] * r2[1]
    return cree(num, den)

def mult(r1 : tuple[int, int], r2 : tuple[int, int]) -> tuple[int, int]:
    """ multiplie deux rationnels avec simplification par pgcd pour ne pas utiliser des entiers inutilement grands 
    non demandé aux éttudiants"""
    pg1 = pgcd(r1[0], r2[1])
    pg2 = pgcd(r2[0], r1[1])
    num = (r1[0] // pg1) * (r2[0] // pg2)
    den = (r1[1] // pg2) * (r2[1] // pg1)
    return cree(num, den)

def inv(r : tuple[int, int]) -> tuple[int, int]:
    """ retourne l'inverse d'un rationnel """
    if r[0] == 0:
        raise ValueError("Le numérateur ne peut pas être nul pour l'inverse.")
    return cree(r[1], r[0])

def div(r1 : tuple[int, int], r2 : tuple[int, int]) -> tuple[int, int]:
    """ divise deux rationnels """
    return mult(r1, inv(r2))

def menu() -> None:
    """ affiche le menu et demande à l'utilisateur de choisir une opération """
    choix = -1
    while choix != 0 :
        print("Menu :")
        i = 1
        print(f"{i} : Addition de deux rationnels")
        i += 1
        print(f"{i} : Opposé d'un rationnel")
        i += 1
        print(f"{i} : Soustraction de deux rationnels")
        i += 1
        print(f"{i} : Multiplication de deux rationnels")
        i += 1
        print(f"{i} : Inverse d'un rationnel")
        i += 1
        print(f"{i} : Division de deux rationnels")
        i += 1
        print(f"0 : Quitter")
        choix = int(input("Entrez votre choix : "))
        j = 1
        if choix == j:
            r1 = entree("Entrez le premier rationnel : ")
            r2 = entree("Entrez le second rationnel : ")
            r3 = plus(r1, r2)
            print(f"{text(r1)} + {text(r2)} = {text(r3)}")
        j += 1
        if choix == j:
            r = entree("Entrez un rationnel : ")
            r2 = opp(r)
            print(f"L'opposé de {text(r)} est {text(r2)}")
        j += 1
        if choix == j:
            r1 = entree("Entrez le premier rationnel : ")
            r2 = entree("Entrez le second rationnel : ")
            r3 = moins(r1, r2)
            print(f"{text(r1)} - {text(r2)} = {text(r3)}")
        j += 1
        if choix == j:
            r1 = entree("Entrez le premier rationnel : ")
            r2 = entree("Entrez le second rationnel : ")
            r3 = mult(r1, r2)
            print(f"{text(r1)} * {text(r2)} = {text(r3)}")
        j += 1
        if choix == j:
            r = entree("Entrez un rationnel : ")
            try:
                r2 = inv(r)
                print(f"L'inverse de {text(r)} est {text(r2)}")
            except ValueError as e:
                print(f"Erreur : {e}")
        j += 1
        if choix == j:
            r1 = entree("Entrez le premier rationnel : ")
            r2 = entree("Entrez le second rationnel : ")
            r3 = div(r1, r2)
            print(f"{text(r1)} / {text(r2)} = {text(r3)}")
        j += 1
        if choix == j:
            r1 = entree("Entrez le premier rationnel : ")
            r2 = entree("Entrez le second rationnel : ")
            r3 = div(r1, r2)
            print(f"{text(r1)} / {text(r2)} = {text(r3)}")
        j += 1
        if choix == j:
            r1 = entree("Entrez le premier rationnel : ")
            r2 = entree("Entrez le second rationnel : ")
            r3 = div(r1, r2)
            print(f"{text(r1)} / {text(r2)} = {text(r3)}")
        j += 1
        if choix == j:
            r1 = entree("Entrez le premier rationnel : ")
            r2 = entree("Entrez le second rationnel : ")
            r3 = div(r1, r2)
            print(f"{text(r1)} / {text(r2)} = {text(r3)}")

def determinant(a1 : tuple[int, int], a2 : tuple[int, int], b1 : tuple[int, int], b2 : tuple[int, int]) -> tuple[int, int]:
    """ calcule le déterminant d'une matrice 2x2 de rationnels """
    return moins(mult(a1, b2), mult(a2, b1))

def est_nul(r : tuple[int, int]) -> bool:
    """ teste si un rationnel est nul """
    return r[0] == 0

def resoud_système() -> None:
    """ résout un système de deux équations à deux inconnues avec des coefficients rationnels """
    print("Résolution d'un système de deux équations à deux inconnues :")
    print("Le système est de la forme :")
    print("a1 * x + b1 * y = c1")
    print("a2 * x + b2 * y = c2")
    print("Entrez les coefficients du système :")
    a1 = entree("Entrez le coefficient a1 (numérateur/denominateur) : ")
    b1 = entree("Entrez le coefficient b1 (numérateur/denominateur) : ")
    c1 = entree("Entrez le coefficient c1 (numérateur/denominateur) : ")
    a2 = entree("Entrez le coefficient a2 (numérateur/denominateur) : ")
    b2 = entree("Entrez le coefficient b2 (numérateur/denominateur) : ")
    c2 = entree("Entrez le coefficient c2 (numérateur/denominateur) : ")

    det = determinant(a1, b1, a2, b2)
    if est_nul(det):
        print("Le système n'a pas de solution unique.")
        return

    x_num = determinant(c1, b1, c2, b2)
    y_num = determinant(a1, c1, a2, c2)

    x = div(x_num, det)
    y = div(y_num, det)

    print(f"La solution du système est : x = {text(x)}, y = {text(y)}")