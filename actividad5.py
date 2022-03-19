palabra= str(input("inserte una palabra: "))

palabra_1=len(palabra)

a=palabra.count("a")
e=palabra.count("e")
i=palabra.count("i")
o=palabra.count("o")
u=palabra.count("u")

metrica=palabra_1*(a+e+i+o+u)
print(f"total de vocales: {metrica}")