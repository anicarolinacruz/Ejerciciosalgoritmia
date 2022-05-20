n=int(input("digite el numero: "))
a=list(range(0,n))
b=[]
for i in a:
    cadena=str(input("Digite la palabra: "))
    mayus=cadena.upper()
    if mayus not in b:
        b.append(mayus)
        
        
print(b)