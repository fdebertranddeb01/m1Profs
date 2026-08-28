"""conversion d'un nombre entier en base 2"""
n = int(input("Entrez un entier naturel : "))
if n == 0:
    print("0")
else:
    res = ""
    while n > 0:
        res = str(n % 2) + res
        n = n // 2
    print(res)
