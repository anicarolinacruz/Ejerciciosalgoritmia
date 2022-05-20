from unittest import result


uno= str(input("inserte numero: "))
for i in range(1, 10):
    repetirNumero= int(uno * i)
    multiplicacion=repetirNumero*repetirNumero
    print (f'{repetirNumero} * {repetirNumero} = {multiplicacion}')