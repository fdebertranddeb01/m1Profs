"""affiche un sapin d'étoiles"""
"""
    String res = "";
    // calcule la liste des triangles
    for (int triangle = 1; triangle <= taille; triangle++) {
      for (int ligne = 0; ligne < triangle; ligne++) {
        // ajoute les espaces dus au décalage du triangle dans le sapin
        for (int esp = 0; esp < taille - triangle; esp++) {
          res = res + BLANC;
        }
        // ajoute les espaces pour faire un triangle
        for (int esp = 0; esp < triangle - ligne - 1; esp++) {
          res = res + BLANC;
        }
        // ajoute les étoiles
        for (int etoiles = 0; etoiles < 2 * ligne + 1; etoiles++) {
          res = res + ETOILE;
        }
        // passe à la ligne suivante
        res = res + "\n";
      }
    }
    // calcule le tronc
    for (int tronc = 0; tronc <= taille; tronc++) {
      // ajoute les espaces
      for (int esp = 0; esp < taille - 1; esp++) {
        res = res + BLANC;
      }
      res = res + TRONC + "\n";
    }"""
taille = int(input("Entrez la taille du sapin : "))
for triangle in range(1, taille + 1):
    for ligne in range(triangle):
        for esp in range(taille - triangle):
            print(" ", end="")
        for esp in range(triangle - ligne - 1):
            print(" ", end="")
        for etoiles in range(2 * ligne + 1):
            print("*", end="")
        print()
for tronc in range(taille+1):
    for esp in range(taille - 1):
        print(" ", end="")
    print("|")