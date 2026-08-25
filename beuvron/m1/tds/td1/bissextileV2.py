a = int(input("entrez une année : "))
if a % 4 != 0:
    print(f"{a} n'est pas bissextile")
else:
    if a % 400 == 0:
        print(f"{a} est bissextile")
    else:
        if a % 100 == 0:
            print(f"{a} n'est pas bissextile")
        else:
            print(f"{a} est bissextile")
