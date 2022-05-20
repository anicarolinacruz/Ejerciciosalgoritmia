cadena1=input("digite las letras: ")
cadena2=str(input("digite los numeros: "))

for letra in cadena1:
    for numero in cadena2:
        print(f"{letra}{numero}", end=' , ')