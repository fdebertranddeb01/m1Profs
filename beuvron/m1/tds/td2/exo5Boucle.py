"""créer une chaine de caractères contenant n fois le caractère A"""
n = int(input("entrez le nombre de 'A' : "))
s = ""
for i in range(n):
    s = s + "A"
print(f"la chaine de caractères est : {s}")
