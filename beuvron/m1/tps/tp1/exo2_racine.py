"""calcul de la racine carrée par la méthode de Newton"""
epsilon = 1e-5
a = float(input("Entrez un nombre : "))
xn = (1+a) / 2
xn1 = (xn + a / xn) / 2
while abs(xn1 - xn) > epsilon:
    xn = xn1
    xn1 = (xn + a / xn) / 2
print("La racine carrée de", a, "est", xn1)
