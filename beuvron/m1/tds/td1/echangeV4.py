""" pourquoi ne pas utiliser quand les variables sont des flottants ? """
a = 1E10
b = 1E-10
saveb = b
a = a + b
b = a - b
a = a - b
print("a =", a)
print("b =", b)
if a != saveb:
    print(f"erreur : a ({a}) != old b ({saveb})")
