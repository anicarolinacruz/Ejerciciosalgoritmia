numero1= int(input("digite el numero 1: "))
numero2= int(input("digite el numero 2: "))
numero3= int(input("digite el numero 3: "))

if numero1<numero2<numero3 or numero1<numero3<numero2:
    print(f"el numero menor es: {numero1}")
elif numero2<numero1<numero3 or numero2<numero3<numero1:
    print(f"el numero menor es: {numero2}")
elif numero3<numero2 and numero3<numero1 or numero3<numero1<numero2:
    print(f"el numero menor es: {numero3}")
elif numero1==numero2 and numero3<numero2:
    print(f"el numero menor es: {numero3}")
elif numero1<numero2 and numero2==numero3:
    print(f"el numero menoes es : {numero1}")
elif numero1<numero2 and numero2==numero3:
    print(f"hay dos numero menores iguales {numero2},{numero3}")
elif numero1==numero2 and numero2<numero3:
    print(f"hay dos numeros menores iguales: {numero1},{numero2}")
elif numero1==numero2==numero3:
    print("todos los numero son iguales")