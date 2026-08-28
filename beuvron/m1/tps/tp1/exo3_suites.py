"""calcul itératif de suites"""
n = int(input("Entrez un entier n : "))
un = 0.25
vn = 0.5
for i in range(1, n + 1):
    un = un + vn
    vn = un + vn
print(f"u({n}) = {un}")

